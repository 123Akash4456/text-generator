
#import openai
#import gradio

#openai.api_key="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"

#message= [{"role":"user","content":"hii what to ask?..."}]


#def CustomChatGPT():
 #   message.append({"role":"user", "content":"user_input"})
  #  response= openai.ChatCompletion.create(
   #     model="gpt-3.5-turbo",
    #    message=message
    #)


    #chatGPT_reply= response["choices"][0]["message"]["content"]
    #message.append({"role":"assistant","content":chatGPT_reply})

    #return chatGPT_reply

#demo= gradio.Interface(fn=CustomChatGPT,inputs="text",outputs="text",title="your Title")

#demo.launch()



from flask import Flask, render_template, request
import openai


app = Flask(__name__,template_folder="templates")

# Set up OpenAI API credentials
openai.api_key = "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"


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run(debug=True ,port=8080,use_reloader=False)
