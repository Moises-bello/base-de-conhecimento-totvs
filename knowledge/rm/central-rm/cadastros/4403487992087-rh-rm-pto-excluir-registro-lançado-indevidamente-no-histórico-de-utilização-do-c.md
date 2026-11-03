---
article_id: 4403487992087
category: Cadastros
content_hash: f08ac6494b43048f43cb37c480f522de3bcf588f4ebb7431648bcdf869b77f7f
fetched_at: '2026-06-28T22:46:28.468430+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Excluir registro lançado indevidamente no histórico de utilização
  do cartão de ponto
type: support-article
updated_at: '2024-06-12T20:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403487992087-RH-RM-PTO-Excluir-registro-lan%C3%A7ado-indevidamente-no-hist%C3%B3rico-de-utiliza%C3%A7%C3%A3o-do-cart%C3%A3o-de-ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981716036375)**Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Ao executar a rotina **Utilizar cartão de ponto**/**Deixar de utilizar cartão de ponto**, não foi selecionado o funcionário desejado e a alteração foi aplicada para todos os funcionários da visão. Como ajustar tal cenário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões.  
  
**Solução**Para ajustar este cenário é necessário excluir o registro inserido indevidamente do histórico de Utilização do Cartão de Ponto do funcionário.  
  
Apenas inserir outro registro executando processo inverso do anterior, fará com que sejam gerados dois registros indevidos no histórico e você poderá perder um dia no período de ponto do funcionário.  
  
Isso porque mesmo que execute o processo inverso do anterior para o mesmo dia, o produto não esta preparado para acatar dois registros: **Utilizar cartão de ponto**, **Deixar de utilizar cartão de ponto** e vice e versa, para um mesmo dia. Sendo assim, ele irá considerar o segundo registro para o dia posterior.  
  
**Importante:**  
O processo de exclusão do registro no histórico de Utilização do Cartão de Ponto é individual, sendo necessário executá-lo funcionário por funcionário.  
  
**Saiba mais:**  
Para orientação passo a passo da exclusão do registro, acesse:

[RH - RM - PTO - Utilizar cartão de ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024457232-RM-PTO-Excluir-Hist%C3%B3rico-de-Utiliza%C3%A7%C3%A3o-do-cart%C3%A3o-de-Ponto)
