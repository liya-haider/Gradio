import gradio as gr

gr.close_all()

def details(name, age, preference, hobbies, profile_pic):
    # Join hobbies list into a readable comma-separated string
    hobbies_str = ", ".join(hobbies)
    
    return profile_pic, f"Name: {name}\nAge: {age}\nSubject Preference: {preference}\nHobbies: {hobbies_str}"

demo = gr.Interface(
    fn=details,
    inputs=[
        gr.Textbox(label="Name:"),
        gr.Slider(label="Age:"),
        gr.Radio(label="Subject Preference: ", choices=['C', 'C#', 'Java', 'Python']),
        gr.Checkboxgroup(label="Hobbies: ", choices=['Painting', 'Singing', 'Reading', 'Gaming']),
        gr.Image(label="Profile pic"),
    ],
    outputs=[gr.Image(), gr.Textbox()],
)

demo.launch()
