---
article_id: 7895710353559
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 25276899bc526b917d3450a581687f01ef837ba4b9669b2e23666f51179bd154
fetched_at: '2026-06-28T22:38:29.815966+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Formação do preço de venda
  e cálculo de impostos
type: support-article
updated_at: '2026-04-10T20:25:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7895710353559-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Forma%C3%A7%C3%A3o-do-pre%C3%A7o-de-venda-e-c%C3%A1lculo-de-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23021001879831) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível informar um valor base (sem impostos) e o sistema calcular automaticamente o preço de venda considerando os impostos?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

No Protheus, o cálculo de impostos no Pedido de Venda é realizado a partir das configurações fiscais do sistema.

Os impostos são determinados conforme regras definidas em:

* TES (Tipo de Entrada e Saída)
* Exceções Fiscais
* Natureza de Operação
* Cadastro de Cliente e Produto (dados fiscais)
* Configurador de Tributos

Cada imposto possui um comportamento específico:

* Alguns podem ser visualizados no Pedido de Venda (ex: IPI)
* Outros são efetivamente calculados apenas no faturamento do Documento de Saída (ex: PIS, COFINS, CSLL)

No Pedido de Venda, os valores de impostos podem ser consultados por meio da planilha financeira.

Também é possível ter a visão de alguns impostos do pedido pelo Smartview **Pré-nota (****FATSV012) como IPI, ICMS, ICMS ST e ISS** e todos os demais impostos do pedido já faturado no Smartview **Notas fiscais** (**FATSV025).**

**Observação:** A Tabela de Preço (OMSA010) não realiza cálculo ou validação de impostos. O preço informado na tabela é considerado como valor comercial, sem decomposição automática de tributos, o cálculo tributário ocorre somente na Planilha Financeira e é efetivado no Documento de Saída.
