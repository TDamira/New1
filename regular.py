import re

text_with_emails = """
Привет, john@example.com, давно не виделись! 
Алиса сказала, что её новый адрес электронной почты - alice1234@gmail.com. 
Ты можешь написать ей письмо на peter@mail.ru, если хочешь.
Анна написала мне на anna_21@outlook.com, предлагает встретиться.
Свяжись с Mike по электронной почте на mike-007@yahoo.com. 
emily99@hotmail.com ждёт ответа.
David на protonmail - david42@protonmail.com.
Ты помнишь, что у Lisa адрес lisa.smith@icloud.com?
Samantha ждёт от тебя письма на samantha87@aol.com.
Robert, напиши мне на robert.brown@example.org.
Александр недавно переехал на адрес alexander34@yandex.ru.
Сарах на rocketmail - sarah12@rocketmail.com.
Напиши мне на kate1234@inbox.lv, буду рада услышать.
Майкл, пожалуйста, ответь на michael22@mail.com.
Olivia написала мне на olivia_45@tutanota.com, у неё проблемы.
"""
matches=re.findall(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',text_with_emails)

print(matches)

