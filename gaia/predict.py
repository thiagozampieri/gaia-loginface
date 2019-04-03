import gaia.recognition as recognition
import gaia.draw as draw
import gaia.resize as resize
import gaia.utils as cfg
import gaia.people as model

recognizer = recognition.face_recognizer()
recognizer.read('data/trainer.yml')

people = model.all()

def predict(frame):
    global recognizer
    print("Predicting...")
    (gray, faces) = recognition.recognition(frame)
    draw.faces(gray, faces)
    
    for rect in faces:
        image_temp = resize.compare(gray, rect)
        (id, confidence) = recognizer.predict(image_temp)  
        
        if len(people) >= id:
            label_text = people[id].fullname
            if id > 0:
                draw.face(frame, rect, label_text)
        
    return frame
    