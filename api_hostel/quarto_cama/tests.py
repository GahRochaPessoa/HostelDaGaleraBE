import datetime
import json
from django.test import TestCase
from api_hostel.quarto_cama.models import quarto
from api_hostel.quarto_cama.models import tipo_quarto
from api_hostel.quarto_cama.models import cama
from api_hostel.quarto_cama.models import tipo_cama

# Create your tests here.

class QuartoCamaTestCase(TestCase):
    
    #create object to test
    def setUp(self):

            #create tipo_quarto
            quarto_ar_condicionado = tipo_quarto.objects.create(
                nome = 'Ar Condicionado'
            )
            quarto_ventilador = tipo_quarto.objects.create(
                nome = 'Ventilador'
            )
            #create quarto
            quarto1 = quarto.objects.create(
                tipo_quarto = quarto_ar_condicionado,
                nome = 'Quarto 1',
                descricao = 'Quarto 1 para várias pessoas'
            )  
            quarto2 = quarto.objects.create(
                tipo_quarto = quarto_ventilador,
                nome = 'Quarto 2',
                descricao = 'Quarto 2 para poucas pessoas'
            )

            #create tipo_cama
            cama_solteiro = tipo_cama.objects.create(
                nome = 'Solteiro'
            )
            cama_casal = tipo_cama.objects.create(
                nome = 'Casal'
            )
            #create cama
            cama.objects.create(
                tipo_cama = cama_solteiro,
                quarto = quarto1,
                status = 'l',
                nome = 'Cama 1',
                descricao = 'Cama 1',
                valor = 30.00
            ) 
            cama.objects.create(
                tipo_cama = cama_casal,
                quarto = quarto2,
                status = 'o',
                nome = 'Cama 2',
                descricao = 'Cama 2',
                valor = 50.00
            )
            

            





    #get
    def test_get(self):
        #get all data tipo_quarto
        comparative_tipo = [
            {
                "id":1,
                "nome":"Ar Condicionado"
            },
            {
                "id":2,
                "nome":"Ventilador"
            }
        ]
        response_tipo = self.client.get('http://127.0.0.1:8000/tipoquarto/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo)

        #get all data quarto
        comparative_quarto = [
            {
                'id':1,
                'tipo_quarto': 1, 
                'nome': 'Quarto 1',
                'descricao': 'Quarto 1 para várias pessoas'
            },
            {
                'id':2,
                'tipo_quarto': 2, 
                'nome': 'Quarto 2',
                'descricao': 'Quarto 2 para poucas pessoas'
            }
        ]
        response_quarto = self.client.get('http://127.0.0.1:8000/quarto/')
        self.assertEquals(response_quarto.status_code, 200)
        self.assertEquals(json.loads(response_quarto.content), comparative_quarto)

        #get all data tipo_cama
        comparative_tipo = [
            {
                "id":1,
                "nome":"Solteiro"
            },
            {
                "id":2,
                "nome":"Casal"
            }
        ]
        response_tipo = self.client.get('http://127.0.0.1:8000/tipocama/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo)

        #get all data cama
        comparative_cama = [
            {
                'id':1,
                'tipo_cama': 1, 
                'quarto': 1, 
                'status': 'l',
                'nome': 'Cama 1',
                'descricao': 'Cama 1',
                'valor': 30.00
            },
            {
                'id':2,
                'tipo_cama': 2, 
                'quarto': 2, 
                'status': 'o',
                'nome': 'Cama 2',
                'descricao': 'Cama 2',
                'valor': 50.00
            }
        ]
        response_cama = self.client.get('http://127.0.0.1:8000/cama/')
        self.assertEquals(response_cama.status_code, 200)
        self.assertEquals(json.loads(response_cama.content), comparative_cama)

        #get by id from db - quarto
        q1 = tipo_quarto.objects.get(id = 1)
        self.assertEquals(q1.__str__(), 'Ar Condicionado')

        q2 = tipo_quarto.objects.get(id = 2)
        self.assertEquals(q2.__str__(), 'Ventilador')

        q3 = quarto.objects.get(nome = 'Quarto 1')
        self.assertEquals(q3.__str__(), (q1, 'Quarto 1', 'Quarto 1 para várias pessoas'))

        q4 = quarto.objects.get(nome = 'Quarto 2')
        self.assertEquals(q4.__str__(), (q2, 'Quarto 2', 'Quarto 2 para poucas pessoas'))

        #get by id from db - cama
        p1 = tipo_cama.objects.get(id = 1)
        self.assertEquals(p1.__str__(), 'Solteiro')

        p2 = tipo_cama.objects.get(id = 2)
        self.assertEquals(p2.__str__(), 'Casal')

        p3 = cama.objects.get(nome = 'Cama 1')
        self.assertEquals(p3.__str__(), (p1, q3, 'l', 'Cama 1', 'Cama 1', 30.00))

        p4 = cama.objects.get(nome = 'Cama 2')
        self.assertEquals(p4.__str__(), (p2, q4, 'o', 'Cama 2', 'Cama 2', 50.00))






    #post
    def test_post(self):

        #post tipo_quarto
        data_tipo = {
            'nome': 'Vista para a praia'
        }
        response_tipo2 = self.client.post('http://127.0.0.1:8000/tipoquarto/', data=data_tipo)
        self.assertEquals(response_tipo2.status_code, 201)

        p1 = tipo_quarto.objects.get(nome = 'Vista para a praia')
        self.assertEquals(p1.__str__(), 'Vista para a praia')

        #post quarto
        data_quarto = {
            'tipo_quarto': json.loads(response_tipo2.content)['id'],
            'nome': 'Quarto 3',
            'descricao': 'Quarto 3 para 3 pessoas'
        }
        
        response_quarto = self.client.post('http://127.0.0.1:8000/quarto/', data = data_quarto)
        self.assertEquals(response_quarto.status_code, 201)

        p2 = quarto.objects.get(nome = 'Quarto 3')
        self.assertEquals(p2.__str__(), (p1, 'Quarto 3', 'Quarto 3 para 3 pessoas'))


        #post tipo_cama
        data_tipo = {
            'nome': 'Cama King Size'
        }
        response_tipo3 = self.client.post('http://127.0.0.1:8000/tipocama/', data=data_tipo)
        self.assertEquals(response_tipo3.status_code, 201)

        p1 = tipo_cama.objects.get(nome = 'Cama King Size')
        self.assertEquals(p1.__str__(), 'Cama King Size')

        #post cama
        data_cama = {
            'tipo_cama': json.loads(response_tipo3.content)['id'], 
            'quarto': json.loads(response_quarto.content)['id'], 
            'status': 'o',
            'nome': 'Cama 3',
            'descricao': 'Cama 3',
            'valor': 70.00
        }
        
        response = self.client.post('http://127.0.0.1:8000/cama/', data = data_cama)
        self.assertEquals(response.status_code, 201)

        p3 = cama.objects.get(nome = 'Cama 3')
        self.assertEquals(p3.__str__(), (p1, p2, 'o', 'Cama 3', 'Cama 3', 70.00))




    # # def test_put(self):
    # #     data = {
    # #         'cpf':'12345678945',
    # #         'nome': 'vinicius',
    # #         'email': 'paulo@gmail.com',
    # #         'telefone':'3578451245',
    # #         'data_nascimento':'1990-02-27'
    # #     }

    # #     response_put = self.client.put('http://127.0.0.1:8000/cama/1', data=data)
    # #     self.assertEquals(response_put.status_code, 200)

    # #     p1 = cama.objects.get(cpf = '12345678945')
    # #     self.assertEquals(p1.__str__(), ('12345678945', 'vinicius', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))



    # # def test_patch(self):
    # #       data = {'nome': 'Maria'}
    # #       response = self.client.patch('http://127.0.0.1:8000/cama/1', data=data)
    # #       self.assertEqual(response.status_code, 200)

    # #       p1 = cama.objects.get(cpf = '12345678945')
    # #       self.assertEquals(p1.__str__(), ('12345678945', 'Maria', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))


    # # def test_delete(self):
    # #     response = self.client.delete('http://127.0.0.1:8000/cama/1')
    # #     self.assertEqual(response.status_code, 200)





    # #test view
    # def test_status_code_200(self):
    #     response = self.client.get('http://127.0.0.1:8000/cama/')
    #     self.assertEquals(response.status_code, 200)