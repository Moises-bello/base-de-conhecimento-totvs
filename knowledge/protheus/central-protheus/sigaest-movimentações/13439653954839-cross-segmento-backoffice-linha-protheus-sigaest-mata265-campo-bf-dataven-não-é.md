---
article_id: 13439653954839
category: SIGAEST - MOVIMENTAÇÕES
content_hash: bf6f14ea14e46a43d18ad8cbb29345c25b5d7f8fcde0a481e525594a9eb2dcd6
fetched_at: '2026-06-28T22:38:57.054334+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Campo BF_DATAVEN
  não é exibido na rotina
type: support-article
updated_at: '2023-03-29T11:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13439653954839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-Campo-BF-DATAVEN-n%C3%A3o-%C3%A9-exibido-na-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível informar a data de vencimento pela rotina ***ENDEREÇAMENTO DE PRODUTOS (MATA265)***, existe o campo ***BF\_DATAVEN*** que não é exibido para informações do Lote, como proceder?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Sobre o campo ***BF\_DATAVEN***: É utilizado no fonte de integração EAI, o mesmo ***não é utilizado para controle de validade de Lotes***, ele está configurado para **"não"** ser marcado como **"usado"** no Configurador. O [conceito de data de vencimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus) é tratado nos lotes do produto e não no endereçamento.  
   
Pode-se utilizar o relatório de ***Saldos por Lotes (MATR425)*** para revisar os registros da tabela SB8,  com a data de vencimento do lote.

Ou mesmo utilizar a consulta ***Saldos por Lote (MATC060)*** para verificar os lotes do produto e a data de vencimento deles.

Veja também a FAQ sobre conceito de Rastro e Endereçamento no Protheus. [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus).

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
