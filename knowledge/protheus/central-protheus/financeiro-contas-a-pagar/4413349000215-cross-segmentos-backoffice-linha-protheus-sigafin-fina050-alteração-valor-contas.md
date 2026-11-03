---
article_id: 4413349000215
category: Financeiro - Contas a Pagar
content_hash: 9c7b772af0cf2aceebc2f2fb448e07af50d5297480ec1cf97731167b39cd781b
fetched_at: '2026-06-28T22:38:08.523726+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Alteração
  valor contas a pagar
type: support-article
updated_at: '2023-01-25T23:24:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413349000215-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Altera%C3%A7%C3%A3o-valor-contas-a-pagar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min** **Dúvida**Como alterar valor **E2\_VALOR** de um título no contas a pagar  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.17  
  
**Solução**

Para que seja possível alterar valor **E2\_VALOR** o sistema faz a seguintes validações no titulo

-Não ter titulo filhos (Imposto)  
-Não ter sofrido baixa  
-Não ter sido contabilizado  
-Não ser de origem de outro módulo ( Compras, Faturamento e etc ) nesse caso verificar **E2\_ORIGEM**   
-Não ser de origem de outras rotinas   
-Não ter sido aglutinado   
-Não ter sido Compensado (nesse caso entra no critério baixa )  
  
**Importante**

Um ambiente desatualizado ( LIB, pacotes periódicos do Financeiro, DBACESS, SMARTCLIENT E APPSERVER )  
  
**Saiba mais**[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 – Alterar valor Desdobramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050555314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Alterar-valor-Desdobramento?source=search)
