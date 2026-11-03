---
content_hash: 5b2a6bb56bcaea2dff64d3edffc1c9992862d9a5de3b6269becf7d5a469ba20c
fetched_at: '2026-06-29T00:06:01.319668+00:00'
page_id: '198937535'
product: rm
source: tdn-rm
title: TSUZQV_DT_Calculo_De_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUZQV_DT_Calculo_De_Formula
version: 3
---

# CÁLCULO DE FÓRMULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | Cálculo de Fórmula |
| **Situação/Requisito:** | Criação de serviço com a função de fórmula NDTRAB para ser utilizado no cálculo Delphi. |
| **Solução/Implementação:** | Houve uma evolução na função de fórmula NDTRAB em .Net para passar a chamar um método do RMChronus que calcula a jornada trabalhada do funcionário. Isto foi necessário porque em escalas de horário mais complexas, onde em um mesmo dia havia jornada trabalhada e jornada de descanso, o algoritmo utilizado no RMLabore não conseguia tratar corretamente. Como toda regra de cálculo de jornada é de responsabilidade do RMChronus, foi decidido que o mais coerente seria que o cálculo utilizado pela NDTRAB também fosse feito no RMChronus. Entretanto, na NDTRAB em Delphi este cálculo ainda é feito internamente no fonte do RMLabore. E como o Gerador de Relatórios na versão 11.82 continua chamando a fórmula Delphi, passou a ocorrer situações de divergências no valor da NDTRAB do cálculo (.Net) e da NDTRAB dos relatórios (Delphi). Para resolver este problema, está sendo criado um serviço com o cálculo da NDTRAB .Net para ser chamado no fonte Delphi, quando for executada a NDTRAB antiga. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TSUZQV |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39* |
