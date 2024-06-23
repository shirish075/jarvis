from alaramf.alaram import Alarm
from functions import *

def offlinefunc(funcname, text):
    # Thinking()
    if funcname is not None:
        if "thanks" in funcname:
            pass
        elif "identity" in funcname:
            speak("i am jarvis your voice assistant tell me what can i do for you!!")
        elif "close app" in funcname:
            speak("which process you want to kill")
            process = str(test_recogniser())
            killtask(process)
        elif "time" in funcname:
            say_time()
        elif "date" in funcname:
            say_date()
        elif "screenshot" in funcname:
            say_screenshot()
        elif "sleep" in funcname:
            say_sleep()
        elif "restart" in funcname:
            say_restart()
        elif "shutdown" in funcname:
            say_shutdown()
        elif "greeting" in funcname:
            say_greetings()
        elif "introduction" in funcname:
            say_introduce()
        elif "bye" in funcname:
            speak("bye sir")
            speak("dont hesitate to call me when i needed")
            exit(0)
        elif "alarm" in funcname:
            Alarm(text).start()
        elif "read" in funcname:
            reader()
        elif "music" in funcname:
            play_random_song()
        elif "notepad automation" in funcname:
            notepad()
        elif "open" in funcname:
            if "folder" in text:
                open_folder()
            elif "app" in text:
                open_applications(text)
            elif "document" in text:
                open_documents()
            elif "notepad" in text:
                notepad()
            elif "pdf" in text:
                pdf_reader()
        elif "copy" in funcname:
            copy_files("copy")
        elif "move" in funcname:
            copy_files("move")
        elif "virtual mouse" in funcname:
            from virtual_mouse import vmouse
            vmouse()
        elif "add_user" in funcname:
            from face_recognition.Model_Trainer import Model_trainer
            from face_recognition.Sample_generator import Sample_generator
            Sample_generator()
            Model_trainer()
        elif "voice" in funcname:
            change_voice()
        elif "reminder" in funcname:
            if "say" in text or "what" in text:
                say_remember()
            elif "delete" in funcname:
                del_rem()
            else:
                remainder()
        elif "voice_change" in funcname:
            change_voice()
        elif "day" in funcname:
            day()
        elif "sleepjarvis" in funcname:
            sleepjarvis()
        elif "open_documents" in funcname:
            open_documents()
        elif "focus_mode" in funcname:
            focus_mode()
        elif "learn" in funcname:
            learn()
        elif "add_password" in funcname:
            add_password()
        elif "pdf_reader" in funcname:
            pdf_reader()
        elif "detection" in funcname:
            detection()
        # elif 'thanks' in funcname:
        #     Thankful()
        #     speak("its my pleasure sir")
        # elif 'robo_walk' in funcname:
        #     Walking()
        # elif 'robo_dance' in funcname:
        #     dance()

        # elif "on" in text or "off" in text:
        #     on(text)

    time.sleep(5)


if __name__ == "__main__":
    offlinefunc("tictactoe", "ee")
