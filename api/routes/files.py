from fastapi import APIRouter, Depends, UploadFile, File
from core.security import get_current_user

from models.audio_file import AudioFile

router = APIRouter()


@router.post("/files")
async def upload_file(
        file: UploadFile = File(...),
        current_user=Depends(get_current_user)
):
    # Save the file to storage (e.g., local disk, S3, etc.)
    path = f"uploads/{file.filename}"
    with open(path, "wb") as out_file:
        content = await file.read()
        out_file.write(content)

    # Just for case
    db_file = AudioFile(
        user_id=current_user.id,
        filename=file.filename,
        path=path
    )
    # Add to database here

    return {"filename": file.filename, "path": path}