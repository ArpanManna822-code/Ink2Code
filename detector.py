import cv2

def detect_ui(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,50,150)

    contours,_ = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    components=[]

    for c in contours:

        x,y,w,h=cv2.boundingRect(c)

        if w>120 and h>50:

            components.append((x,y,w,h))

            # Draw bounding box
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

            # Determine component type
            if w > 250:
                label = "Input Field"

            elif w > 170:
                label = "Button"

            else:
                label = "Container"

            # Draw label above box
            cv2.putText(
                image,
                label,
                (x, y-8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,255),
                2
            )

    output_path="static/detected.png"

    cv2.imwrite(output_path,image)

    components = sorted(components, key=lambda x: x[1])

    return components,output_path