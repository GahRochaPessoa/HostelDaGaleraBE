import datetime
import json
from django.test import TestCase
from api_hostel.funcionario.models import funcionario
from api_hostel.funcionario.models import tipo_funcionario

# Create your tests here.

class FuncionarioTestCase(TestCase):
    
    #create object to test
    def setUp(self):

            recepcionista = tipo_funcionario.objects.create(
                nome = 'Recepcionista'
            )
            gerente = tipo_funcionario.objects.create(
                nome = 'Gerente'
            )
            

            funcionario.objects.create(
                tipo_funcionario = recepcionista,
                cpf = '12345678945',
                nome = 'Paulo André da Silva',
                email = 'paulo@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )
            funcionario.objects.create(
                tipo_funcionario = gerente,
                cpf = '11111111111',
                nome = 'Luiza Santos',
                email = 'luiza@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )





    #test model
    def test_get(self):
        #get all data tipo_funcionario
        comparative_tipo = [
            {
                "id":1,
                "nome":"Recepcionista"
            },
            {
                "id":2,
                "nome":"Gerente"
            }
        ]
        response_tipo = self.client.get('http://127.0.0.1:8000/tipofuncionario/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo)

        #get all data funcionario
        comparative_funcionario = [
            {
                'id':1,
                'tipo_funcionario': 1,
                'cpf':'12345678945', 
                'nome': 'Paulo André da Silva',
                'email': 'paulo@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            },
            {
                'id':2,
                'tipo_funcionario': 2,
                'cpf':'11111111111', 
                'nome': 'Luiza Santos',
                'email': 'luiza@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            }
        ]
        response_funcionario = self.client.get('http://127.0.0.1:8000/funcionario/')
        self.assertEquals(response_funcionario.status_code, 200)
        self.assertEquals(json.loads(response_funcionario.content), comparative_funcionario)

        #get by id from db
        p1 = tipo_funcionario.objects.get(id = 1)
        self.assertEquals(p1.__str__(), 'Recepcionista')

        p2 = funcionario.objects.get(cpf = '12345678945')
        self.assertEquals(p2.__str__(), (p1, '12345678945', 'Paulo André da Silva', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))

        #get by id from client
        comparative_tipo_id = {
                "id":1,
                "nome":"Recepcionista"
            }
        response_tipo = self.client.get('http://127.0.0.1:8000/tipofuncionario/1/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo_id)

        comparative_funcionario = {
                'id':1,
                'tipo_funcionario': 1,
                'cpf':'12345678945', 
                'nome': 'Paulo André da Silva',
                'email': 'paulo@gmail.com',
                'telefone': '3578451245',
                'data_nascimento': '1990-02-27'
            }
        response_funcionario = self.client.get('http://127.0.0.1:8000/funcionario/1/')
        self.assertEquals(response_funcionario.status_code, 200)
        self.assertEquals(json.loads(response_funcionario.content), comparative_funcionario)


    def test_post(self):
        data_tipo = {
            'nome': 'Faxineiro'
        }
        response_tipo2 = self.client.post('http://127.0.0.1:8000/tipofuncionario/', data=data_tipo)
        self.assertEquals(response_tipo2.status_code, 201)

        p1 = tipo_funcionario.objects.get(nome = 'Faxineiro')
        self.assertEquals(p1.__str__(), 'Faxineiro')
        
        #normal post
        data_funcionario = {
            'tipo_funcionario': json.loads(response_tipo2.content)['id'],
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '4354346456',
            'data_nascimento': '1984-08-16'
        }
        
        response = self.client.post('http://127.0.0.1:8000/funcionario/', data = data_funcionario)
        self.assertEquals(response.status_code, 201)

        p2 = funcionario.objects.get(cpf = '41241241258')
        self.assertEquals(p2.__str__(), (p1, '41241241258', 'Antonio Marcos', 'antonio@gmail.com', '4354346456', datetime.date(1984, 8, 16)))


        #without phone post
        data_funcionario = {
            'tipo_funcionario': json.loads(response_tipo2.content)['id'],
            'cpf':'69565968596', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '',
            'data_nascimento': '1984-08-16'
        }
        
        response = self.client.post('http://127.0.0.1:8000/funcionario/', data = data_funcionario)
        self.assertEquals(response.status_code, 201)

        p2 = funcionario.objects.get(cpf = '69565968596')
        self.assertEquals(p2.__str__(), (p1, '69565968596', 'Antonio Marcos', 'antonio@gmail.com', None, datetime.date(1984, 8, 16)))

        #bad request post
        data_funcionario = {
            'tipo_funcionario': json.loads(response_tipo2.content)['id'],
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antoniogmail.com',
            'telefone': '4354645645',
            'data_nascimento': '1984-08-16'
        }
        
        response = self.client.post('http://127.0.0.1:8000/funcionario/', data = data_funcionario)
        self.assertEquals(response.status_code, 400)




    def test_put(self):
        
        p1 = tipo_funcionario.objects.get(nome = 'Recepcionista')
        self.assertEquals(p1.__str__(), 'Recepcionista')

        #normal put
        funcionario.objects.filter(cpf='12345678945').update(nome='vinicius')
        p2 = funcionario.objects.get(cpf = '12345678945')
        self.assertEquals(p2.__str__(), (p1, '12345678945', 'vinicius', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))

        #without phone
        funcionario.objects.filter(cpf = '12345678945').update(telefone=None)
        p2 = funcionario.objects.get(cpf = '12345678945')
        self.assertEquals(p2.__str__(), (p1, '12345678945', 'vinicius', 'paulo@gmail.com', None, datetime.date(1990, 2, 27)))


    # def test_delete(self):

    #     p1 = tipo_funcionario.objects.get(nome = 'Recepcionista')
    #     self.assertEquals(p1.__str__(), 'Recepcionista')

    #     funcionario.objects.filter(cpf = '12345678945').delete()
    #     p2 = funcionario.objects.get(cpf = '12345678945')
    #     self.assertEquals(p2.__str__(), (p1, '12345678945', 'vinicius', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))

    #     record = funcionario.objects.get(cpf = '12345678945')
    #     record.delete()



    #test view
    def test_status_code_200(self):
        response = self.client.get('http://127.0.0.1:8000/funcionario/')
        self.assertEquals(response.status_code, 200)