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


        #get by id from client - quarto
        comparative_tipo_id = {
                "id":1,
                "nome":"Ar Condicionado"
            }
        response_tipo = self.client.get('http://127.0.0.1:8000/tipoquarto/1/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo_id)

        comparative_quarto = {
                'id':1,
                'tipo_quarto': 1, 
                'nome': 'Quarto 1',
                'descricao': 'Quarto 1 para várias pessoas'
            }
        response_quarto = self.client.get('http://127.0.0.1:8000/quarto/1/')
        self.assertEquals(response_quarto.status_code, 200)
        self.assertEquals(json.loads(response_quarto.content), comparative_quarto)

        #get by id from client - cama
        comparative_tipo_id = {
                "id":1,
                "nome":"Solteiro"
            }
        response_tipo = self.client.get('http://127.0.0.1:8000/tipocama/1/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_tipo_id)

        comparative_cama = {
                'id':1,
                'tipo_cama': 1, 
                'quarto': 1, 
                'status': 'l',
                'nome': 'Cama 1',
                'descricao': 'Cama 1',
                'valor': 30.00
            }
        response_cama = self.client.get('http://127.0.0.1:8000/cama/1/')
        self.assertEquals(response_cama.status_code, 200)
        self.assertEquals(json.loads(response_cama.content), comparative_cama)






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




    def test_put(self):
        
        #quarto
        tipo_quarto.objects.filter(nome='Ar Condicionado').update(nome='Misto')
        p2 = tipo_quarto.objects.get(nome='Misto')
        self.assertEquals(p2.__str__(), 'Misto')

        quarto.objects.filter(nome='Quarto 1').update(nome='Quarto Novo')
        p3 = quarto.objects.get(nome='Quarto Novo')
        self.assertEquals(p3.__str__(), (p2, 'Quarto Novo', 'Quarto 1 para várias pessoas'))

        #cama
        tipo_cama.objects.filter(nome='Solteiro').update(nome='Queen Size')
        p4 = tipo_cama.objects.get(nome='Queen Size')
        self.assertEquals(p4.__str__(), 'Queen Size')

        cama.objects.filter(nome='Cama 1').update(nome='Cama Nova')
        p5 = cama.objects.get(nome='Cama Nova')
        self.assertEquals(p5.__str__(), (p4, p3, 'l', 'Cama Nova', 'Cama 1', 30.00))



    # # def test_delete(self):
    # #     response = self.client.delete('http://127.0.0.1:8000/cama/1')
    # #     self.assertEqual(response.status_code, 200)





    #test view
    def test_status_code_200(self):
        response = self.client.get('http://127.0.0.1:8000/cama/')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('http://127.0.0.1:8000/tipocama/')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('http://127.0.0.1:8000/quarto/')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('http://127.0.0.1:8000/tipoquarto/')
        self.assertEquals(response.status_code, 200)