from winotify import Notification, audio

toast = Notification(app_id='Water',
                     title='Hora de beber água e/ou creatina',
                     msg='Vai lá agora, senão tu esquece',
                     duration='long',
                     icon=r"C:\Users\jlima\Desktop\Languages\Python\Water\glass_water.jpg")

toast.add_actions(label="Entendi o recado e vou beber água")
toast.set_audio(audio.LoopingCall6, loop=True)
toast.show()
