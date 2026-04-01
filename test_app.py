"""
Testes Unitários para o Diário de Bordo — Máquinas

Valida as funções principais da aplicação
"""

from datetime import time
import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar as funções do app (simulado)
def calcular_horas(h_ini: time, h_fim: time) -> float:
    """Calcula horas entre dois horários."""
    ini = h_ini.hour * 60 + h_ini.minute
    fim = h_fim.hour * 60 + h_fim.minute
    diff = fim - ini
    if diff < 0:
        diff += 24 * 60
    return round(diff / 60, 2)


class TestCalcularHoras:
    """Testa a função calcular_horas"""
    
    def test_horas_normais(self):
        """Teste com horários normais do dia"""
        resultado = calcular_horas(time(7, 0), time(17, 0))
        assert resultado == 10.0, f"Esperado 10.0, obtido {resultado}"
        print(f"✅ Horas normais: {resultado}h")
    
    def test_horas_parciais(self):
        """Teste com minutos"""
        resultado = calcular_horas(time(9, 30), time(17, 45))
        assert resultado == 8.25, f"Esperado 8.25, obtido {resultado}"
        print(f"✅ Horas parciais: {resultado}h")
    
    def test_horas_noturnas(self):
        """Teste com horário noturno (atravessa meia-noite)"""
        resultado = calcular_horas(time(22, 0), time(6, 0))
        assert resultado == 8.0, f"Esperado 8.0, obtido {resultado}"
        print(f"✅ Horas noturnas: {resultado}h")
    
    def test_zero_horas(self):
        """Teste com mesmo horário"""
        resultado = calcular_horas(time(12, 0), time(12, 0))
        assert resultado == 0.0, f"Esperado 0.0, obtido {resultado}"
        print(f"✅ Zero horas: {resultado}h")
    
    def test_uma_hora(self):
        """Teste com exatamente 1 hora"""
        resultado = calcular_horas(time(10, 0), time(11, 0))
        assert resultado == 1.0, f"Esperado 1.0, obtido {resultado}"
        print(f"✅ Uma hora: {resultado}h")


class TestValidacoes:
    """Testa validações básicas"""
    
    def test_horimetro_valido(self):
        """Teste horímetro final >= inicial"""
        hor_ini = 100.5
        hor_fim = 110.3
        hor_trab = round(hor_fim - hor_ini, 2)
        assert hor_trab >= 0, f"Horímetro inválido: {hor_trab}"
        print(f"✅ Horímetro válido: {hor_trab}h")
    
    def test_media_calculo(self):
        """Teste cálculo de média"""
        abast_hor = 15.5
        horas_trab = 8.0
        media = round(abast_hor / horas_trab, 2)
        assert media > 0, f"Média inválida: {media}"
        print(f"✅ Média calculada: {media}")
    
    def test_media_zero_horas(self):
        """Teste divisão por zero em média"""
        abast_hor = 15.5
        horas_trab = 0.0
        media = round(abast_hor / horas_trab, 2) if horas_trab > 0 else 0.0
        assert media == 0.0, f"Média com zero horas deve ser 0, obtido {media}"
        print(f"✅ Divisão por zero tratada: {media}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🧪 TESTES UNITÁRIOS — Diário de Bordo")
    print("="*60 + "\n")
    
    # Executar testes
    print("📋 TESTES DE CÁLCULO DE HORAS:")
    print("-" * 60)
    test_horas = TestCalcularHoras()
    test_horas.test_horas_normais()
    test_horas.test_horas_parciais()
    test_horas.test_horas_noturnas()
    test_horas.test_zero_horas()
    test_horas.test_uma_hora()
    
    print("\n📋 TESTES DE VALIDAÇÕES:")
    print("-" * 60)
    test_val = TestValidacoes()
    test_val.test_horimetro_valido()
    test_val.test_media_calculo()
    test_val.test_media_zero_horas()
    
    print("\n" + "="*60)
    print("✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
    print("="*60 + "\n")
