---
content_hash: f9bb3c3d41d6d6463e6aa452892894283348dfacfbfd139ca951325d48909072
fetched_at: '2026-06-29T00:10:13.789534+00:00'
page_id: '458759474'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4566 DT Simulação de lançamentos - Possíveis causas para a
  não simulação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458759474
version: 2
---

# Composição dos valores da parcela

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Simular Cálculo | Simular Cálculo |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** |  |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |
| **Pacote:** |  |

## Descrição

Hoje existem algumas condições para a geração de lançamento que, quando não são atendidas, além de naturalmente não ser possível gerar o lançamento, o sistema apresenta via log os motivos para tal. Porém, ao utilizar a simulação de lançamento, nenhuma mensagem era apresentada ao usuário quando não era possível simular o lançamento.

A partir de agora, o sistema passará a apresentar ao usuário as possíveis causas quando o não for por possível simular lançamento.
