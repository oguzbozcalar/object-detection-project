# %%
import cv2
from yolo_predictions import YOLO_Pred

# %%
yolo = YOLO_Pred('./Model7/weights/runs/best.onnx','data.yaml')

# %%
img = cv2.imread('./street_image.jpg')



# %%
#predictions
img_pred = yolo.predictions(img)

# %%
cv2.imshow('Prediction Image',img_pred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
# Real Time Object Detection

# %%


# %%
