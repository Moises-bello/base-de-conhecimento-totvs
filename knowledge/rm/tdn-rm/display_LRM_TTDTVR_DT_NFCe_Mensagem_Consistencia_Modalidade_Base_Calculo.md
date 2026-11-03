---
content_hash: 8a6e0fe270782870f7c49eb9ba67301a21fbb6cd3a81cc89ad8086b824d34be8
fetched_at: '2026-06-29T00:06:09.530368+00:00'
page_id: '203755609'
product: rm
source: tdn-rm
title: TTDTVR_DT_NFCe_Mensagem_Consistencia_Modalidade_Base_Calculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDTVR_DT_NFCe_Mensagem_Consistencia_Modalidade_Base_Calculo
version: 1
---

NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| RM | *Informe a linha de produto.* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PAR.008 | PARAMETRIZACAO - INTEGRACOES | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | TTDTVR |
| **Requisito (ISSUE):** | MOV000003 - Movimento |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas utilizadas:** | TPARFILIAL, TTMVEXT e TMOV |
| **Sistema(s) operacional(is):** |  |
| **Versões/Release:** | *12.1.7* |

## Descrição

Para a  emissão da NFC-e, a falta de preenchimento do campo Modalidade Base de Cálculo na linha do tributo ICMS deve gerar uma mensagem de consistência igual à que ocorre para NF-e.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações **12.1.7** deste chamado

## Procedimento para Utilização

* + Acesse o Tipo de Movimento configurado para Emitir NFC-e
  + Salve esse movimento com campo de Modalidade da base de Cálculo do Tributo ICMS sem preencher e verifique que a mensagem estará preenchida.
