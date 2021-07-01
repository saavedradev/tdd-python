import unittest
from core.cuenta import Cuenta

class TestIngresoEnCuenta(unittest.TestCase):
    
    def test_cuando_se_hace_un_ingreso_en_una_cuenta_nueva_el_saldo_sera_igual_al_dinero_ingresado(self):
        # Caso cuenta recien creada
        cuenta = Cuenta()
        cuenta.ingresar_dinero(500)
        self.assertEqual(cuenta.saldo, 500)
        
        
    def test_cuando_se_hace_un_ingreso_el_saldo_aumenta(self): 
         # Caso que ya tenia saldo
         cuenta = Cuenta()
         #Preparar
         cuenta.saldo = 1000
         #Actuar
         cuenta.ingresar_dinero(500)
         #comprobar
         self.assertEqual(cuenta.saldo, 1500)
         
         
         
         
if __name__== '__main__':
    unittest.main()