import dlib

model = "38_predictor.dat"
xml = "labels_ibug_300W_test_38point.xml"

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor(xml, model)
print("[INFO] error: {}".format(error))
