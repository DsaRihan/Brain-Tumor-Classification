from flask import Flask, render_template, request, jsonify
import os,pickle,cv2,numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('./predict.html')

@app.route('/train')
def result():
    return render_template('./train.html')

@app.route('/comparision')
def result2():
    return render_template('./comparision.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        image_path = './static/'+ 'uploaded_image.jpg'
        image.save(image_path)
        print(image)

        # Call your IPython Notebook code or machine learning model here
        # For demonstration, let's assume the model returns a prediction
        
        dec = {0:'No Tumor', 1:'Positive Tumor'}
        # plt.figure(figsize=(12,8))
        # p = os.listdir('./Testing/')
        # c=1
        # for i in os.listdir('./Testing/no_tumor/')[:9]:
        #         plt.subplot(3,3,c)
    
        img = cv2.imread(image_path,0)
        print(np.array(img).shape)
        img1 = cv2.resize(img, (200,200))
        print(np.array(img1).shape)
        img1 = img1.reshape(1,-1)/255
        X=np.array(img1)
        print(X.shape)
        p = model.predict(X)
        print(p)

        # plt.title(dec[p[0]])
        # plt.imshow(img, cmap='gray')
        # plt.axis('off')
                # c+=1    
        

        # return jsonify({'prediction': dec[p[0]]})
        return render_template('./eg.html' , image_path=image_path, predictions=dec[p[0]])

    return jsonify({'error': 'No image provided'})

if __name__ == '__main__':
    app.run(debug=True)
