from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.category import Category
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


def get_category_or_404(category_id: int, db: Session) -> Category:
    db_category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not db_category:
        raise HTTPException(status_code=404, detail="カテゴリが見つかりません")

    return db_category


def ensure_category_name_is_available(
    name: str,
    db: Session,
    exclude_category_id: int | None = None,
) -> None:
    query = db.query(Category).filter(Category.name == name)

    if exclude_category_id is not None:
        query = query.filter(Category.id != exclude_category_id)

    if query.first():
        raise HTTPException(
            status_code=409,
            detail="同じ名前のカテゴリが既に存在します",
        )


def commit_category(db: Session) -> None:
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="同じ名前のカテゴリが既に存在します",
        ) from exc


@router.post("", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    ensure_category_name_is_available(category.name, db)

    db_category = Category(name=category.name)

    db.add(db_category)
    commit_category(db)
    db.refresh(db_category)

    return db_category


@router.get("", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    db_category = get_category_or_404(category_id, db)
    ensure_category_name_is_available(
        category.name,
        db,
        exclude_category_id=category_id,
    )

    db_category.name = category.name

    commit_category(db)
    db.refresh(db_category)

    return db_category
