---
content_hash: 69ac7ed718591c03573ecea22e23ae5d8a869712a2f03d2a3e3d45d5bceaaa07
fetched_at: '2026-06-29T00:10:26.827161+00:00'
page_id: '514750126'
product: rm
source: tdn-rm
title: Taxa de Oxigênio Litros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514750126
version: 3
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Importante**
4. **Tela utilizadas**

## **01. VISÃO GERAL**

Este documento tem como objetivo especificar o requisito de utilização de cobrança de taxa de oxigênio na unidade de medida litros.

## **02. EXEMPLO DE UTILIZAÇÃO**

Vincular Taxa/Serviço a um cuidado parametrizado em Cadastros>Cuidados com Paciente>Prescrição Médica>Item de Enfermagem selecionar o cuidado e acessar a aba Itens de débito.

## **03.** **IMPORTANTE**

|  |
| --- |
| Integração RM Nucleus |
| Condições Contratuais |
| Tabela de Procedimentos e Serviços |
| Elaboração de Conta |
| Prontuário |

## **04. TABELAS UTILIZADAS**

* Acesse "**Opções/Parâmetros/Integração RM** **Nucleus**".  
  Configure a unidade de medida Litros.

* **Acesse "Cadastros/Faturamento/Condições Contratuais com** **Convênios**"  
  Na aba "Gerais", verifique a tabela de preços configuradas.

           

* Na aba "Parâmetros 3", marque "Utiliza Faturamento de Gases em Litros".

          

* Acesse"**Cadastros/Faturamento/Tabela de Procedimentos e Serviços**"**.**  
  Acesse o item e configure o fator para a unidade de medida litros parametrizada.

**PROCEDIMENTO PARA UTILIZAÇÃO**

* Acesse Lançamentos na Conta do Paciente.
* Lançar o item parametrizado, será necessário informar o inicio e fim do uso e a vazão que estava configurada no período.
* O sistema ira calcular a quantidade a ser faturada.

* Acesse Prontuário
* Na  aba "Enfermagem", selecione a aba "Equipamentos/Insumos".
* Selecione um item da lista de itens que tenha item de débito vinculado para lançamento que esteja parametrizado.
* Ao finalizar o lançamento, o sistema irá calcular a quantidade a ser faturada.
