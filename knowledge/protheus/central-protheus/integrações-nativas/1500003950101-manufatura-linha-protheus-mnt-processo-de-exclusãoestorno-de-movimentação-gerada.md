---
article_id: 1500003950101
category: Integrações Nativas
content_hash: e404b7345895362a1c02bae3bd3455cacaa80a1b43b46f22cc9a7da3030adf34
fetched_at: '2026-06-28T22:42:35.515535+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Processo de Exclusão/Estorno de movimentação
  gerada por insumo
type: support-article
updated_at: '2021-09-08T13:53:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003950101-Manufatura-Linha-Protheus-MNT-Processo-de-Exclus%C3%A3o-Estorno-de-movimenta%C3%A7%C3%A3o-gerada-por-insumo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como é o comportamento dos processos de estorno e exclusão de movimentos que tiveram origem em um insumo previsto?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Versão 12  
  
**Solução**Segue abaixo os processos de estorno e exclusão de movimentações geradas por insumos:  
  
**Estorno**Com a baixa de uma **Pré-requisição** efetivada totalmente ou parcialmente por meio da rotina **Baixa Pré-Requisição - MATA185**. Desta forma estes itens não podem mais sofrer alterações, tanto no módulo **Estoque/Custos - SIGAEST**como diretamente no insumo que originou a solicitação de armazém.  
Se houver a necessidade de modificar esta requisição, pode-se por meio da rotina **MATA185**realizar o processo de estorno da mesma, assim retornando esta para o *status* em que apenas a **Pré-requisição** encontra-se gerada, em seguida deve-se realizar o processo de exclusão da **Pré-requisição**. Feito estes procedimentos, permitirá tanto a alteração do insumo como a sua exclusão, caso seja necessária.  
 **Exclusão**Após gerar a **Pré-Requisição - MATA106** para um ou mais itens da solicitação de armazém, estes itens ficam disponíveis para efetivação da baixa. Estes mesmos itens não podem ser modificados, tanto no módulo **Estoque/Custos - SIGAEST**como diretamente no insumo que originou a solicitação de armazém.  
Caso seja necessário modificar esta requisição, é possível por meio da rotina **MATA185**, realizar o processo de exclusão da mesma, assim retornando esta para o *status* em que aguarda a geração da **Pré-requisição**. Este *status* permitirá tanto a alteração do insumo como a sua exclusão caso seja necessária.
