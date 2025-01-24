import Rhino
import Eto.Drawing as drawing
import Eto.Forms as forms
import clr
import json
import urllib
import urllib2
import clr
import re
clr.AddReference("System.Net.Http")  # Explicitly load the assembly
from System.Net.Http import HttpClient, StringContent
from System.Text import Encoding
from System.Net.Http import HttpClient, StringContent
from System.Text import Encoding

class DeepSeekChat(forms.Form):
    def __init__(self):
        self.messages = [{"role": "system", "content": "You are a helpful assistant in rhino software environment, what ever user asked you should try to be polite and create a python code which can do the user requested tasks. you can use rhino related libraries like Rhino, rhinoscriptsyntax, ghpythonlib"}]
        # Dialog setup
        self.Title = "DeepSeek Chat Designed by RTF"
        self.ClientSize = drawing.Size(400, 600)

        # Input field
        self.input_box = forms.TextBox(PlaceholderText="Type your query here...")
        self.input_box.Width = 300  # Set width to 300 pixels
        self.input_box.Height = 50  # Set height to 50 pixels
        # Output area
        self.output_area = forms.TextArea(ReadOnly=True, Wrap=True)
        self.output_area.Width = 300
        self.output_area.Height = 300
        # Send button
        self.send_button = forms.Button(Text="Send")
        self.send_button.Click += self.on_send_click

        # Layout setup
        layout = forms.StackLayout(Spacing=10, Padding=10)
        
        layout.Items.Add(forms.Label(Text="Chat with DeepSeek:"))
        layout.Items.Add(self.input_box)
        layout.Items.Add(self.send_button)
        layout.Items.Add(forms.Label(Text="Response:"))
        layout.Items.Add(self.output_area)

        self.Content = layout

    def append_output(self, message):
        """Update the output text area"""
        self.output_area.Text += "\n" + message
        self.output_area.ScrollToEnd()

    def extract_code(self, response_text):
        """New method to extract code blocks"""
        matches = re.findall(r'```python(.*?)```', response_text, re.DOTALL)
        return matches[0].strip() if matches else ""
    def on_send_click(self, sender, e):
        """Handle send button clicks"""
        try:
            user_input = self.input_box.Text
            if not user_input.strip():
                self.append_output("[Error]: Query cannot be empty.")
                return

            self.append_output("[You]: {}".format(user_input))
            
            # 1. Get API Response
            api_response = self.send_to_deepseek(user_input)
            
            # 2. Process Response
            if isinstance(api_response, dict):  # Check if it's a dictionary
                if "choices" in api_response:
                    message_content = api_response["choices"][0]["message"]["content"]
                    if "```python" in message_content:
                        code = self.extract_code(message_content)
                        result = self.execute_code(code)
                        self.append_output("[Code Result]:\n{}".format(result))
                    else:
                        self.append_output("[DeepSeek]: {}".format(message_content))
                else:
                    self.append_output("[Error]: Invalid API response format")
            else:
                self.append_output("[Error]: Unexpected API response: {}".format(api_response))

            self.input_box.Text = ""

        except Exception as ex:
            self.append_output("[Error]: {}".format(str(ex)))


    def send_to_deepseek(self, prompt):
       
        """Get response from DeepSeek API"""
        api_key = "your api key" # Replace with actual key
        endpoint = "https://api.deepseek.com/v1/chat/completions"
    
        client = HttpClient()
        client.DefaultRequestHeaders.Add("Authorization", "Bearer {}".format(api_key))
        self.messages.append({
                "role": "user", 
                "content": prompt
            })
        payload = {
            "model": "deepseek-reasoning",
            "messages": self.messages
        }
        
        content = StringContent(
            json.dumps(payload),
            Encoding.UTF8,
            "application/json"
        )
        
        response = client.PostAsync(endpoint, content).Result
        response_content = response.Content.ReadAsStringAsync().Result
        self.messages.append({
                "role": "assistant", 
                "content": response_content
        })
        if not response.IsSuccessStatusCode:
            raise Exception("API Error {}: {}".format(response.StatusCode, response_content))
        
        try:
            return json.loads(response_content)  # Returns dict
        except:
            return response_content  # Fallback to string if not JSON

    def execute_code(self, code):
        """Execute Python code received from the API"""
        try:
            exec_globals = {}
            exec(code, exec_globals)
            return exec_globals.get("result", "No result returned by the code.")
        except Exception as ex:
            return "Code Execution Error: {}".format(str(ex))


# To display the chatbox in Rhino
dialog = DeepSeekChat()
dialog.Show()
