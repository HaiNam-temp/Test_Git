from fastapi import FastAPI
from asyncio import log
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.response_schema import APIResponse
from app.db.database import get_db
from app.services import micro_learning_service
from app.apis.deps import get_current_user, oauth2_scheme

router = APIRouter(prefix="/api/v1", tags=["micro-learning"])

@router.get("/topics/all", response_model=APIResponse)
def getAllTopic(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    log.logger.info("Get all topics")
    data = {"topics": micro_learning_service.get_all_topics_process_by_user(db,token)}
    return APIResponse(status_code=200, success=True, data=data, message="successful")

@router.get("/units/detail/{unit_id}", response_model=APIResponse)
def getDetailUnit(db: Session = Depends(get_db), unit_id: str = None, token: str = Depends(oauth2_scheme)):
    log.logger.info("Get detail unit for : "+str(unit_id))
    if not unit_id:
        raise HTTPException(status_code=400, detail="unit_id is required")
    data = micro_learning_service.get_detail_unit_process_by_user(db, token, unit_id)
    return APIResponse(status_code=200, success=True, data=data, message="successful")


@router.get("/lessons/items/{lesson_id}", response_model=APIResponse)
def get_lesson_items(db: Session = Depends(get_db), lesson_id: str = None, token: str = Depends(oauth2_scheme)):
    if not lesson_id:
        raise HTTPException(status_code=400, detail="lesson_id is required")
    data = micro_learning_service.get_lesson_items_by_lesson_id(db, token, lesson_id)
    return APIResponse(status_code=200, success=True, data={"lessonId": lesson_id, "items": data}, message="successful")


@router.post("/lessons/complete", response_model=APIResponse)
def post_complete_lesson(db: Session = Depends(get_db), payload: dict = None, token: str = Depends(oauth2_scheme)):
    if not payload:
        raise HTTPException(status_code=400, detail="payload required")
    lesson_id = payload.get("lessonId")
    if not lesson_id:
        raise HTTPException(status_code=400, detail="lessonId required")
    data = micro_learning_service.complete_lesson(db, token, lesson_id)
    return APIResponse(status_code=200, success=True, data=data, message="lesson completed")

@router.get("/topics/detail/{topic_id}", response_model=APIResponse)
def get_units_by_topic(db: Session = Depends(get_db), topic_id: str = None, token: str = Depends(oauth2_scheme)):
    if not topic_id:
        raise HTTPException(status_code=400, detail="topic_id is required")
    data = micro_learning_service.get_units_by_topic_id(db, token, topic_id)
    return APIResponse(status_code=200, success=True, data={"topicId": topic_id, "units": data}, message="successful")

@router.get("/topics/detail/{topic_id}", response_model=APIResponse)
def get_units_by_topic(db: Session = Depends(get_db), topic_id: str = None, token: str = Depends(oauth2_scheme)):
    if not topic_id:
        raise HTTPException(status_code=400, detail="topic_id is required")
    data = micro_learning_service.get_units_by_topic_id(db, token, topic_id)
    return APIResponse(status_code=200, success=True, data={"topicId": topic_id, "units": data}, message="successful")

@router.get("/topics/detail/{topic_id}", response_model=APIResponse)
def get_units_by_topic(db: Session = Depends(get_db), topic_id: str = None, token: str = Depends(oauth2_scheme)):
    if not topic_id:
        raise HTTPException(status_code=400, detail="topic_id is required")
    data = micro_learning_service.get_units_by_topic_id(db, token, topic_id)
    return APIResponse(status_code=200, success=True, data={"topicId": topic_id, "units": data}, message="successful")
