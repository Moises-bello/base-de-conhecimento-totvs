---
article_id: 360051269913
category: Manutenção de Ativos (SIGAMNT)
content_hash: 17095b6b337ce88bf4176dc866a9b00de53720049a059d75d308b401d8e618aa
fetched_at: '2026-06-28T22:42:34.416662+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Rotina de bens padrão não altera Centro
  de Custo de bens antigos
type: support-article
updated_at: '2024-09-16T11:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051269913-Manufatura-Linha-Protheus-MNT-Rotina-de-bens-padr%C3%A3o-n%C3%A3o-altera-Centro-de-Custo-de-bens-antigos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26395770840087)***Tempo aproximado para leitura: **00:00:40 min**  
  
**Dúvida**Por que a rotina de **Bens Padrão -** **MNTA170** não altera o **Centro de Custo** dos bens já cadastrados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**A rotina de **Bens Padrão** não tem por objetivo realizar a movimentação de centro de custos para bens já cadastrados, apenas para cadastros de novos de bens ele irá receber o centro de custo alterado.   
  
Para alterar centro de custos de bens já cadastrados favor utilizar a rotina de **Movimentação de Bens - MNTA471**, pois existe várias regras a serem validadas e acarretaria uma perca de performance ao realizar esse tipo de procedimento em lote na rotina de bens padrão.
