from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import os
import threading

class TaggerApp(App):
    def build(self):
        self.title = "Music Tagger"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="🎵 Music Tagger App", font_size=22, size_hint_y=None, height=40))
        
        layout.add_widget(Label(text="Enter Folder Path on SD Card:", size_hint_y=None, height=30))
        self.path_input = TextInput(
            text='/storage/71DC-FC8B/Download/AAA/',
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.path_input)
        
        self.run_btn = Button(
            text="Run Tagger",
            size_hint_y=None,
            height=60,
            background_color=(0.73, 0.53, 0.98, 1)
        )
        self.run_btn.bind(on_press=self.start_tagging)
        layout.add_widget(self.run_btn)
        
        scroll = ScrollView()
        self.log_label = Label(
            text="Ready to tag...\n",
            size_hint_y=None,
            valign='top',
            halign='left'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        scroll.add_widget(self.log_label)
        layout.add_widget(scroll)
        
        return layout

    def start_tagging(self, instance):
        target = self.path_input.text.strip()
        if not os.path.exists(target):
            self.log_label.text = f"Error: Path does not exist:\n{target}"
            return
            
        self.run_btn.disabled = True
        self.log_label.text = f"Processing folder:\n{target}\n\n(Note: This app version logs actions locally)\n"
        
        # Run in background thread so app doesn't freeze
        threading.Thread(target=self.run_logic, args=(target,)).start()

    def run_logic(self, target):
        # Your core tagging execution loop goes here
        try:
            count = 0
            for root, _, files in os.walk(target):
                for file in files:
                    if file.lower().endswith(('.opus', '.ogg', '.mp3', '.flac', '.m4a', '.aac')):
                        count += 1
            self.log_label.text += f"\nSuccess! Found and queued {count} audio files."
        except Exception as e:
            self.log_label.text += f"\nError: {e}"
        finally:
            self.run_btn.disabled = False

if __name__ == '__main__':
    TaggerApp().run()
