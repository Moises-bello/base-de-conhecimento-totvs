---
content_hash: d1ee75410f9eb3cd7e1b5af52b5f876356bee92df4ac3cee10db5839e85d3ef4
fetched_at: '2026-06-29T00:08:30.864165+00:00'
page_id: '272698530'
product: rm
source: tdn-rm
title: MEDU-2754 DT Melhoria na parametrização do texto do contrato financeiro exibido
  na matricula pelo portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272698530
version: 114
---

# Parâmetro - Portal Contrato Financeiro (Texto Contrato Financeiro)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetro - Portal Contrato Financeiro* | *Parâmetro - Portal Contrato Financeiro* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Plano de pagamento* | *Plano de pagamento* | | *Matricula Online* | *Matricula Online* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Realizado uma melhoria na parametrização do texto do contrato financeiro que é apresentado na confirmação da matricula no portal do aluno.

Foi disponibilizado através desta melhoria novas TAG relacionadas a plano de pagamento e fórmula.

**1º Mudança – TAG relacionadas ao plano de pagamento**

* Disponibilizada nova tag [VALOR LIQUIDO P] que representa o valor líquido do plano de pagamento selecionado para a matricula.  
  É considerado como valor líquido, o valor do plano de pagamento menos os descontos das parcelas do plano e o desconto do plano.

* A tag [VALOR LIQ P] será substituída pela tag [VALOR P]  
  A tag [VALOR P] representa o valor do plano de pagamento considerado na matricula.  
    
  Observação:  
  O sistema ajustará automaticamente a parametrização que estiver utilizando a tag [VALOR LIQ P] para considera a nova tag [VALOR P]

**2º Mudança – TAG relacionadas a fórmula**

* Disponibilizada nova tag [FORMULAMATRICPL({FORMULA})] que permite identificar uma fórmula que será executada e o seu resultado seja mostrado no comprovante de matricula.   
  Ao selecionar a tag [FORMULAMATRICPL({FORMULA})] o sistema apresentara uma tela para que seja selecionada a fórmula a ser executada.  
    
  Observação:  
  A fórmula selecionada será executada no contexto da matricula do aluno (SMATRICPL).

## Procedimento para Utilização

Parâmetros [Educacional >> RM Portal >> RM Portal – Matricula >> Texto do Contrato Financeiro]

divs
