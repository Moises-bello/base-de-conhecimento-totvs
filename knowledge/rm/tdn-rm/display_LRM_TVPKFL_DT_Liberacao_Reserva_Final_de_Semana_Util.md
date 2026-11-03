---
content_hash: 00cca76ce6f35c7ebfeaabe6e5a93e7170b672671ee04f102644ab401bf9e212
fetched_at: '2026-06-29T00:08:16.601087+00:00'
page_id: '248580498'
product: rm
source: tdn-rm
title: TVPKFL_DT_Liberacao_Reserva_Final_de_Semana_Util
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPKFL_DT_Liberacao_Reserva_Final_de_Semana_Util
version: 115
---

# PARÂMETROS - MOVIMENTAÇÕES - RESERVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Parâmetros - movimentações - reserva* |
| **Situação/Requisito:** | *Ao fazer ser liberada uma reserva, o sistema está permitindo que a reserva fique liberada nos finais de semana, mesmo quando os parâmetros de sábado e domingo úteis para reserva não estão marcados.* |
| **Solução/Implementação:** | *Foi identificado que quando o parâmetro "Considerar finais de semana e feriados como úteis" na tela de 'Parâmetros -> Movimentações -> Geral está marcado, o sistema utiliza também este parâmetro para o cálculo da liberação da reserva, foi feito o ajuste nas telas de parâmetros para que a configuração de sábados e domingos como úteis para reserva fique agrupado com as configurações de movimentações para facilitar o entendimento, assim, se marcado o parâmetro "Considerar finais de semana e feriados como úteis" ficará claro que também será aplicado à reserva.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
