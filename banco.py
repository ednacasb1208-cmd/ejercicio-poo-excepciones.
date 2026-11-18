from abc import ABC, abstractmethod

# 1. Excepciones Personalizadas
class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando se intenta retirar más del saldo disponible."""
    pass

class MontoInvalidoError(Exception):
    """Excepción lanzada cuando el monto es negativo o cero."""
    pass

# 2. Clase Abstracta (Abstracción)
class CuentaBancaria(ABC):
    def __init__(self, titular: str, saldo_inicial: float):
        self._titular = titular  # Encapsulamiento
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    def depositar(self, monto: float):
        if monto <= 0:
            raise MontoInvalidoError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto
        print(f"Depósito exitoso de ${monto:.2f}. Saldo actual: ${self._saldo:.2f}")

    @abstractmethod
    def retirar(self, monto: float):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

# 3. Herencia y Polimorfismo
class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular: str, saldo_inicial: float, comision_retiro: float):
        super().__init__(titular, saldo_inicial)
        self._comision_retiro = comision_retiro

    def retirar(self, monto: float):
        if monto <= 0:
            raise MontoInvalidoError("El monto a retirar debe ser mayor a cero.")
        
        total_a_retirar = monto + self._comision_retiro
        if total_a_retirar > self._saldo:
            raise SaldoInsuficienteError(f"Fondos insuficientes. Intenta retirar ${total_a_retirar:.2f} (incluyendo comisión), pero el saldo es ${self._saldo:.2f}.")
        
        self._saldo -= total_a_retirar
        print(f"Retiro exitoso de ${monto:.2f} (Comisión: ${self._comision_retiro:.2f}). Saldo actual: ${self._saldo:.2f}")

# 4. Bloque Principal y Manejo de Excepciones
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA BANCARIO ---")
    
    try:
        # Crear objeto de la clase hija
        mi_cuenta = CuentaAhorros("Carlos Pérez", 500.0, 5.0)
        
        print(f"\nTitular: {mi_cuenta.titular} | Saldo inicial: ${mi_cuenta.saldo:.2f}")
        
        # Prueba 1: Depósito válido
        print("\nPrueba 1: Depósito válido")
        mi_cuenta.depositar(200.0)
        
        # Prueba 2: Retiro válido
        print("\nPrueba 2: Retiro válido")
        mi_cuenta.retirar(150.0)
        
        # Prueba 3: Lanzar excepción por monto inválido
        print("\nPrueba 3: Intentando depositar monto negativo")
        mi_cuenta.depositar(-50.0)
        
    except SaldoInsuficienteError as e:
        print(f"[ERROR FINANCIERO]: {e}")
    except MontoInvalidoError as e:
        print(f"[ERROR DE VALIDACIÓN]: {e}")
    except Exception as e:
        print(f"[ERROR INESPERADO]: {e}")
    finally:
        print("\n--- OPERACIÓN FINALIZADA ---")
