import datetime
import json
from django.test import TestCase
from api_hostel.reserva.models import reserva
from api_hostel.reserva.models import reserva_cama
from api_hostel.reserva.models import status_reserva
from api_hostel.hospede.models import hospede
from api_hostel.funcionario.models import funcionario
from api_hostel.funcionario.models import tipo_funcionario
from api_hostel.quarto_cama.models import cama
from api_hostel.quarto_cama.models import tipo_cama
from api_hostel.quarto_cama.models import quarto
from api_hostel.quarto_cama.models import tipo_quarto


class ReservaTestCase(TestCase):
    
    #create object to test
    def setUp(self):

            #hospede
            hospede1 = hospede.objects.create(
                cpf = '12345678945',
                nome = 'Paulo André da Silva',
                email = 'paulo@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )
            hospede2 = hospede.objects.create(
                cpf = '11111111111',
                nome = 'Luiza Santos',
                email = 'luiza@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )




            #funcionario
            recepcionista = tipo_funcionario.objects.create(
                nome = 'Recepcionista'
            )
            gerente = tipo_funcionario.objects.create(
                nome = 'Gerente'
            )
            funcionario1 = funcionario.objects.create(
                tipo_funcionario = recepcionista,
                cpf = '12345678945',
                nome = 'Paulo André da Silva',
                email = 'paulo@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )
            funcionario2 = funcionario.objects.create(
                tipo_funcionario = gerente,
                cpf = '11111111111',
                nome = 'Luiza Santos',
                email = 'luiza@gmail.com',
                telefone = '3578451245',
                data_nascimento = '1990-02-27'
            )




            #quarto e cama
            quarto_ar_condicionado = tipo_quarto.objects.create(
                nome = 'Ar Condicionado'
            )
            quarto_ventilador = tipo_quarto.objects.create(
                nome = 'Ventilador'
            )
            
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

            cama_solteiro = tipo_cama.objects.create(
                nome = 'Solteiro'
            )
            cama_casal = tipo_cama.objects.create(
                nome = 'Casal'
            )
            
            cama1 = cama.objects.create(
                tipo_cama = cama_solteiro,
                quarto = quarto1,
                status = 'l',
                nome = 'Cama 1',
                descricao = 'Cama 1',
                valor = 30.00
            ) 
            cama2 = cama.objects.create(
                tipo_cama = cama_casal,
                quarto = quarto2,
                status = 'o',
                nome = 'Cama 2',
                descricao = 'Cama 2',
                valor = 50.00
            )




            #reserva
            ativa = status_reserva.objects.create(
                descricao = 'Ativa'
            )

            inativa = status_reserva.objects.create(
                descricao = 'Inativa'
            )

            reserva1 = reserva.objects.create(
                hospede = hospede1,
                funcionario = funcionario1
            )

            reserva2 = reserva.objects.create(
                hospede = hospede2,
                funcionario = funcionario2
            )

            reserva_cama.objects.create(
                cama = cama1,
                reserva = reserva1,
                status_reserva = ativa,
                inicio = '2021-08-05',
                fim = '2021-08-10'
            )

            reserva_cama.objects.create(
                cama = cama2,
                reserva = reserva2,
                status_reserva = inativa,
                inicio = '2021-08-03',
                fim = '2021-08-05'
            )




    #test model
    def test_get(self):

        #get all data status_reserva
        comparative_status = [
            {
                "id":1,
                "descricao":"Ativa"
            },
            {
                "id":2,
                "descricao":"Inativa"
            }
        ]
        response_tipo = self.client.get('http://127.0.0.1:8000/statusreserva/')
        self.assertEquals(response_tipo.status_code, 200)
        self.assertEquals(json.loads(response_tipo.content), comparative_status)

        #get all data reserva
        comparative_reserva = [
            {
                'id':1,
                'hospede': 1, 
                'funcionario': 1
            },
            {
                'id':2,
                'hospede': 2, 
                'funcionario': 2
            }
        ]
        response_quarto = self.client.get('http://127.0.0.1:8000/reserva/')
        self.assertEquals(response_quarto.status_code, 200)
        self.assertEquals(json.loads(response_quarto.content), comparative_reserva)

        #get all data reserva_cama
        comparative_cama = [
            {
                'id':1,
                'cama': 1, 
                'reserva': 1, 
                'status_reserva': 1,
                'inicio': '2021-08-05',
                'fim': '2021-08-10'
            },
            {
                'id':2,
                'cama': 2, 
                'reserva': 2, 
                'status_reserva': 2,
                'inicio': '2021-08-03',
                'fim': '2021-08-05'
            }
        ]
        response_cama = self.client.get('http://127.0.0.1:8000/reservacama/')
        self.assertEquals(response_cama.status_code, 200)
        self.assertEquals(json.loads(response_cama.content), comparative_cama)



    def test_post(self):
        ##############################################################################################
        #post hospede
        hospede1 = self.client.post('http://127.0.0.1:8000/hospede/', {
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '35999568745',
            'data_nascimento': '1984-08-16'
        }, format='json')

        self.assertEquals(hospede1.status_code, 201)

        hospede_p1 = hospede.objects.get(cpf = '41241241258')
        self.assertEquals(hospede_p1.__str__(), ('41241241258', 'Antonio Marcos', 'antonio@gmail.com', '35999568745', datetime.date(1984, 8, 16)))

        #post funcionario
        data_tipo = {
            'nome': 'Faxineiro'
        }
        response_tipo2 = self.client.post('http://127.0.0.1:8000/tipofuncionario/', data=data_tipo)
        self.assertEquals(response_tipo2.status_code, 201)

        tipo_funcionario_p1 = tipo_funcionario.objects.get(nome = 'Faxineiro')
        self.assertEquals(tipo_funcionario_p1.__str__(), 'Faxineiro')

        data_funcionario = {
            'tipo_funcionario': json.loads(response_tipo2.content)['id'],
            'cpf':'41241241258', 
            'nome': 'Antonio Marcos',
            'email': 'antonio@gmail.com',
            'telefone': '4354346456',
            'data_nascimento': '1984-08-16'
        }
        
        response_funcionario = self.client.post('http://127.0.0.1:8000/funcionario/', data = data_funcionario)
        self.assertEquals(response_funcionario.status_code, 201)

        funcionario_p2 = funcionario.objects.get(cpf = '41241241258')
        self.assertEquals(funcionario_p2.__str__(), (tipo_funcionario_p1, '41241241258', 'Antonio Marcos', 'antonio@gmail.com', '4354346456', datetime.date(1984, 8, 16)))
        

        



        ##############################################################################################
        #cama
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
        
        response_cama = self.client.post('http://127.0.0.1:8000/cama/', data = data_cama)
        self.assertEquals(response_cama.status_code, 201)

        cama_p4 = cama.objects.get(nome = 'Cama 3')
        self.assertEquals(cama_p4.__str__(), (p1, p2, 'o', 'Cama 3', 'Cama 3', 70.00))


        
        ##############################################################################################
        #status reserva
        data_status = {
            'descricao': 'Outros'
        }
        
        response_status = self.client.post('http://127.0.0.1:8000/statusreserva/', data = data_status)
        self.assertEquals(response_status.status_code, 201)

        status_p2 = status_reserva.objects.get(descricao = 'Outros')
        self.assertEquals(status_p2.__str__(), ('Outros'))

        #reserva
        data_reserva = {
            'hospede': json.loads(hospede1.content)['id'], 
            'funcionario': json.loads(response_funcionario.content)['id']
        }
        
        response_reserva = self.client.post('http://127.0.0.1:8000/reserva/', data = data_reserva)
        self.assertEquals(response_reserva.status_code, 201)

        reserva_p2 = reserva.objects.get(hospede = hospede_p1)
        self.assertEquals(reserva_p2.__str__(), (hospede_p1, funcionario_p2))


        #post reserva_cama
        data_reserva_cama = {
            'cama': json.loads(response_cama.content)['id'], 
            'reserva': json.loads(response_reserva.content)['id'], 
            'status_reserva': json.loads(response_status.content)['id'],
            'inicio': '2021-08-03',
            'fim': '2021-08-05'
        }
        
        response_reserva_cama = self.client.post('http://127.0.0.1:8000/reservacama/', data = data_reserva_cama)
        self.assertEquals(response_reserva_cama.status_code, 201)

        reserva_cama_p3 = reserva_cama.objects.get(reserva = reserva_p2)
        self.assertEquals(reserva_cama_p3.__str__(), (cama_p4, reserva_p2, status_p2, datetime.date(2021, 8, 3), datetime.date(2021, 8, 5)))

    




    # def test_put(self):

    #     #normal put
    #     reserva.objects.filter(cpf='12345678945').update(nome='vinicius')
    #     p2 = reserva.objects.get(cpf = '12345678945')
    #     self.assertEquals(p2.__str__(), ('12345678945', 'vinicius', 'paulo@gmail.com', '3578451245', datetime.date(1990, 2, 27)))

    #     #without phone
    #     reserva.objects.filter(cpf = '12345678945').update(telefone=None)
    #     p2 = reserva.objects.get(cpf = '12345678945')
    #     self.assertEquals(p2.__str__(), ('12345678945', 'vinicius', 'paulo@gmail.com', None, datetime.date(1990, 2, 27)))








    # def test_delete(self):
    #     response = self.client.delete('http://127.0.0.1:8000/reserva/1')
    #     self.assertEqual(response.status_code, 200)

    #test view
    # def test_status_code_200(self):
    #     response = self.client.get('http://127.0.0.1:8000/reserva/')
    #     self.assertEquals(response.status_code, 200)