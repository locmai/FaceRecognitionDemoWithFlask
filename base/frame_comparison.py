import face_recognition
import cv2
import data

class FrameComparison:

    obama_image = face_recognition.load_image_file(data.get_path("obama.jpg"))
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    biden_image = face_recognition.load_image_file(data.get_path("biden.jpg"))
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding
    ]

    known_face_names = [
        "Barack Obama",
        "Joe Biden"
    ]

    def check(self, frame_to_check, known_face_encoding_frame=known_face_encodings):
        small_frame = cv2.resize(frame_to_check, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encoding_frame, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
            face_names.append(name)
        return face_locations, face_names
