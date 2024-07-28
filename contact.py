import streamlit as st


def display():
    st.markdown("<h1 style='color: red;'>Contact</h1>", unsafe_allow_html=True)

    st.write("Please fill out the form below:")

    # Input fields for name, email, and message
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    message = st.text_area("Message:")

    # Submit button
    if st.button("Submit"):
        # Process the form submission
        if name and email and message:
            # Placeholder for handling the form submission
            st.success("Form submitted successfully!")
        else:
            st.error("Please fill out all fields.")


# Run the display function to render the contact form
if __name__ == "__main__":
    display()
