---
content_hash: 53561e04e604d6331aaf8c4e5ff27ec03850af513db6d76f709d926b0a220535
fetched_at: '2026-06-29T00:08:30.972110+00:00'
page_id: '272709506'
product: rm
source: tdn-rm
title: 645614 MATFATCMPCRM01-20 Geração da Tag AUTXML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272709506
version: 112
---

# Conhecimento de Transporte Eletrônico  CT-e

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *Totvs Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CTE006.* | *CT-E - ENVIO DE EVENTO.* | |
| **Cadastros Iniciais:** | *Movimento, Campos Complementares e dados de CT-e* |
| **Parâmetro(s):** | *Parametrização* *por tipo de movimento "Envio CT-e"*  *Parametrização por tipo de movimento "Campos Complementares"* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *645614* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | *TMOV, TMOVCOMPL, TCTE, TCTEMOV* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Implementação para gerar a tag autXML no XML de envio para a SEFAZ de acordo com as informações advindas dos campos complementares do CT-e.

Conforme exigência da ANTT (Agencia nacional de transportes terrestres) transportadoras rodoviária de cargas devem inserir no campo “CNPJ do autorizado” , do CT-e e do MDF-e - o CNPJ da sede da ANTT 04.898.488/0001-77.  
Resolução nº 4799 de 2017 – Capitulo IV §1º (anexa)

1 - Cadastrar um novo campo complementar CNPJ/CPF

2- Parametrizar para que o campo complementar criado fique visível.

3 - Adicionar os CNPJ's ou CPF's no Movimento

4 - Enviar o CT-e

5 - Campos Complementares CT-e adicionados no XML

divs
