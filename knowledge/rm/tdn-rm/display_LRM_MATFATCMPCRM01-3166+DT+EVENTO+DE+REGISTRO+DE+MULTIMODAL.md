---
content_hash: 5b40b74c3b9973c43fb966c3b678a01af6cc5ffb9856a587f4059126c1a5a154
fetched_at: '2026-06-29T00:09:00.226790+00:00'
page_id: '364925878'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-3166 DT EVENTO DE REGISTRO DE MULTIMODAL
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-3166+DT+EVENTO+DE+REGISTRO+DE+MULTIMODAL
version: 2
---

# EVENTO DE REGISTRO DE MULTIMODAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento*. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CT-e* | **CONHECIMENTO DE TRANSPORTE ELETRÔNICO** | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-3166 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-3166 |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQLServer e Oracle.* |
| **Tabelas Utilizadas:** | - |
|  |  |

## Descrição

Implementação do evento de Regitro do Multimodal para CT-e.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações de uma das seguintes versões:

* *12.1.21 ou superiores*

## Procedimento para Utilização

* Para utilização do evento é necessário possuir um CT-e Multimodal autorizado.
* Selecionar o CT-e Multimodal e clicarem **Processos → Enviar Evento**
* Na tela de Processos, selecione a opção **Registro de Multimodal**e cliquei em Avançar.
* Preencha o campo **Registro do Multimoda**l e, caso seja necessário, o **Número do Documento** e clique em Executar  
  Obs: O Botão executar somente habilitará após serem preenchidos 15 caracteres no campo **Registro do Multimoda**l.
* Após o envio o registro ficará com o Status de Evento Pendente
* Selecione o registro e clique em **Processos → Consultar Evento.**
* Após a consulta, o registro retornará ao Status de Autorizado.
