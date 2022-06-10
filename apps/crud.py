from sqlalchemy.orm import Session

from . import model, schemas

def upload(db: Session, user: schemas.Base,file):
    # print(user.title,user.Message,"opppp")
    db_upload = model.FileUpload(title=user.title, message=user.Message, link=file)
    print(db_upload,"++++")
    db.add(db_upload)
    db.commit()
    db.refresh(db_upload)
    return db_upload