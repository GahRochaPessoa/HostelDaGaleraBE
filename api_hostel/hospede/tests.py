import datetime
import json
from django.test import TestCase
from api_hostel.hospede.models import hospede

# Create your tests here.

class HospedeTestCase(TestCase):
    
    #create object to test
    def setUp(self):
            hospede.objects.create(
                cpf = '12345678945',
                nome = 'Paulo André da Silva',
                email = 'paulo@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )
            hospede.objects.create(
                cpf = '11111111111',
                nome = 'Luiza Santos',
                email = 'luiza@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )

    #test model
    def test_get(self):

        #get all data hospede
        comparative_hospede = [
            {
                'id':1,
                'cpf':'12345678945', 
                'nome': 'Paulo André da Silva',
                'email': 'paulo@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            },
            {
                'id':2,
                'cpf':'11111111111', 
                'nome': 'Luiza Santos',
                'email': 'luiza@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            }
        ]
        response_hospede = self.client.get('http://127.0.0.1:8000/hospede/')
        self.assertEquals(response_hospede.status_code, 200)
        self.assertEquals(json.loads(response_hospede.content), comparative_hospede)


        p1 = hospede.objects.get(cpf = '12345678945')
        self.assertEquals(p1.__str__(), ('12345678945', 'Paulo André da Silva', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))


        #get by id from client
        comparative_hospede = {
                'id':1,
                'cpf':'12345678945', 
                'nome': 'Paulo André da Silva', 
                'email': 'paulo@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            }
        response_hospede = self.client.get('http://127.0.0.1:8000/hospede/1/')
        self.assertEquals(response_hospede.status_code, 200)
        self.assertEquals(json.loads(response_hospede.content), comparative_hospede)



    def test_post(self):
        response = self.client.post('http://127.0.0.1:8000/hospede/', {
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '35999568745',
            'data_nascimento': '1984-08-16'
        }, format='json')
        self.assertEquals(response.status_code, 201)

        p1 = hospede.objects.get(cpf = '41241241258')
        self.assertEquals(p1.__str__(), ('41241241258', 'Antonio Marcos', 'antonio@gmail.com', '35999568745', datetime.date(1984, 8, 16)))

        #without phone post
        data_hospede = {
            'cpf':'69565968596', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '',
            'data_nascimento': '1984-08-16'
        }
        
        response = self.client.post('http://127.0.0.1:8000/hospede/', data = data_hospede)
        self.assertEquals(response.status_code, 201)

        p2 = hospede.objects.get(cpf = '69565968596')
        self.assertEquals(p2.__str__(), ('69565968596', 'Antonio Marcos', 'antonio@gmail.com', None, datetime.date(1984, 8, 16)))

        #bad request post
        data_hospede = {
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antoniogmail.com',
            'telefone': '4354645645',
            'data_nascimento': '1984-08-16'
        }
        
        response = self.client.post('http://127.0.0.1:8000/hospede/', data = data_hospede)
        self.assertEquals(response.status_code, 400)




    def test_put(self):

        #normal put
        hospede.objects.filter(cpf='12345678945').update(nome='vinicius')
        p2 = hospede.objects.get(cpf = '12345678945')
        self.assertEquals(p2.__str__(), ('12345678945', 'vinicius', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))

        #without phone
        hospede.objects.filter(cpf = '12345678945').update(telefone=None)
        p2 = hospede.objects.get(cpf = '12345678945')
        self.assertEquals(p2.__str__(), ('12345678945', 'vinicius', 'paulo@gmail.com', None, datetime.date(1990, 2, 27)))








    # def test_delete(self):
    #     response = self.client.delete('http://127.0.0.1:8000/hospede/1')
    #     self.assertEqual(response.status_code, 200)

    #test view
    def test_status_code_200(self):
        response = self.client.get('http://127.0.0.1:8000/hospede/')
        self.assertEquals(response.status_code, 200)