---
article_id: 4859111350551
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 514b016b05a553610fc7dcfdd0e6e490b939e59c7910cc5f7ce42ec5c17d4902
fetched_at: '2026-06-28T22:39:48.831309+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Comportamento
  do frete da tabela Pré-Cálculo na fase de PO x Embarque/Desembaraço
type: support-article
updated_at: '2022-05-02T20:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4859111350551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Comportamento-do-frete-da-tabela-Pr%C3%A9-C%C3%A1lculo-na-fase-de-PO-x-Embarque-Desembara%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Qual a diferença de comportamento do frete na tabela Pré-Cálculo entre a fase de Purchase Order (PO) e a fase de Embarque/Desembaraço?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**Para entender a diferença de comportamento do Pré-Cálculo entre as fases de Purchase Order (PO) e Embarque é necessário compreender a diferença conceitual da solução que cada fase de propõe.  
  
Na **fase de Purchase Order** temos o papel da Proforma Invoice, ou seja, nele temos os dados de negociação, tais como: fornecedor, itens, moeda, valores e incoterms, dentre outros. Nesta entidade, o Incoterm utilizado determina as obrigações entre as partes e quando temos a tabela de Pré-Cálculo associada ao PO, o sistema é capaz de compreender se o Frete ou o Seguro estão embutidos no valor negociado: no valor do item ou destacados para serem somados ao total dos itens (quando a responsabilidade é do exportador) ou quando será um custo adicional por parte do Importador (quando a responsabilidade é do importador) determinando assim se haverá a necessidade de gerar um título provisório para esta despesa (frete e/ou seguro).  
  
Na **fase de Embarque/Desembaraço** temos a analogia à um "Container de Processos", onde podemos ter mercadorias de diversos purchases orders, de um ou mais fornecedor, com uma ou mais condição de negociação, ou seja, nesta fase nem os dados dos fornecedores e nem os dados da negociação (como moeda, condição de pagamento e Incoterms) da mercadoria fazem parte da capa do processo. Nestas condições, o sistema entenderá que a despesa que constar na tabela de Pré-Cálculo é a que deve ser gerada como previsão de desembolso (título provisório) no financeiro e que só deixarão de existir quando forem substituídos por um título efetivo da mesma despesa.  
  
O frete, caso conste na tabela de Pré-Cálculo, resultará na geração do título provisório com base nos valores e dados existentes no processo (como containers e cubagem - mais informações podem ser consultadas em: <https://tdn.totvs.com/pages/releaseview.action?pageId=286016575>), no entanto, o Incoterm é uma informação que não há na capa do Embarque/Desembaraço e sim nas Invoices vinculadas ao processo, podendo ainda possuir Invoices de fornecedores distintos, com moedas e incoterms diferentes.  
**Reforçando: na fase de embarque é levado em consideração as despesas que constam na tabela de Pré-Cálculo.**  
  
Neste caso, pode-se fazer uso das opções do cadastro de despesas, condicionando quais despesas gerarão títulos no **SIGAFIN** e quais tipos serão gerados: PR para a fase de PO, PRE para fase de Embarque/ Desembaraço.  
E ainda para o contexto em que temos a despesa **AFRMM** (e que comumente é aplicado à outras despesas) é possível tirar proveito dos recursos da própria tabela de Pré-Cálculo juntamente com os cadastros de despesas, definindo uma outra despesa base para apuração despesa (AFRMM) e que esteja configurada para não gerar títulos provisórios (por exemplo) e ter esta despesa informada no seu processo de Embarque/Desembaraço. Desta forma, existirá uma outra referência para a apuração da despesa, sem a necessidade de que na Tabela de Pré-Cálculo tenhamos a despesa de frete (102).  
  
**Saiba mais**[Pré-cálculo - EICTP25A](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=554660153)
