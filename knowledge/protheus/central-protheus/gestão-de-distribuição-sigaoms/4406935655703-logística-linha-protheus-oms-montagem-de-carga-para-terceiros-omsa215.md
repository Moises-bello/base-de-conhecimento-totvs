---
article_id: 4406935655703
category: Gestão de Distribuição (SIGAOMS)
content_hash: 07120650108f7ed218667eb65645385ff132c674569da9837770b01960a75977
fetched_at: '2026-06-28T22:45:49.928202+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Montagem de Carga para Terceiros - OMSA215
type: support-article
updated_at: '2021-08-26T18:49:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406935655703-Log%C3%ADstica-Linha-Protheus-OMS-Montagem-de-Carga-para-Terceiros-OMSA215
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:12 min** **Dúvida**Como utilizar a **Montagem de Carga para Terceiros - OMSA215**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**A rotina **Montagem de Carga para Terceiros - OMSA215**, permite selecionar somente os **Pedidos de Venda - MATA410** que serão transportados por terceiros. O Sistema faz a distinção de **Pedidos de Venda** entregues por terceiros considerando os campos:

* **Transp - C5\_TRANSP**: que deve estar preenchido.
* **Carga - C5\_TPCARGA**: que deve estar configurado como **Utiliza, sempre que o pedido for entregue por terceiros**.

Para utilizar essa rotina são necessárias as configurações abaixo:

* A integração com o ambiente **TOTVS WMS - Gestão de Armazenagem** deve estar ativa, ou seja, parâmetro**MV\_INTDL** = **S - Sim.**
* Os campos **Endereço Padrão - A4\_ENDPAD,** **Estrutura Física - A4\_ESTFIS** e **Local - A4\_LOCAL** devem estar preenchidos no **Cadastro da Transportadora - MATA050**,  sendo que o campo referente à estrutura física deve ser do tipo **Doca,**pois o Sistema ordena os pedidos de venda e **gera uma carga para cada transportadora** e seus endereçamentos - docas.

O estorno de uma carga gerada pela rotina **Montagem de Carga para Terceiros - OMSA215,** deverá ocorrer pela rotina **Montagem de Carga - OMSA200.** Se desejar que a rotina **Montagem de Carga para Terceiros - OMSA215** tenha a opção de estorno, poderá utilizar o **Ponto de Entrada OM215MNU - Inclusão de novas opções.** Logo abaixo no **Saiba mais**, consta o *link* com a documentação do Ponto de Entrada.   
 **Importante**Nesse cenário, ao realizar o estorno da carga pela rotina **Montagem de Carga - OMSA200,** o Sistema irá limpar a informação da Transportadora no **Pedido de Vendas**. Devido ao conceito de geração de carga ocorrer por Transportadora.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga para Terceiros - OMSA215](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407000099607-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-para-Terceiros-OMSA215)  
[Montagem de Carga Para Terceiros - OMSA215](https://tdn.totvs.com/pages/releaseview.action?pageId=570392333#MontagemdeCargaParaTerceiros)
