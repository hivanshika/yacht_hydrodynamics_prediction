import gradio as gr

# Define a simple function
def process_data(user_input):
    return f"Processed: {user_input}"

# Create the Gradio interface
iface = gr.Interface(
    fn=process_data,     # Function to process input
    inputs="text",       # Input type
    outputs="text"       # Output type
)

# Launch the app
iface.launch()

