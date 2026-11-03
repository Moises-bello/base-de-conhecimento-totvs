---
article_id: 1500004627141
category: Chão de Fábrica (SIGASFC)
content_hash: 6aa605a1466f64cb7d476c24aef23a6cf2fc162411d1f96de1d7229bffadf0f8
fetched_at: '2026-06-28T22:42:49.909524+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: 'MP - SIGASFC - Mensagem AJUDA: D3_TM'
type: support-article
updated_at: '2021-03-31T20:16:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004627141-MP-SIGASFC-Mensagem-AJUDA-D3-TM
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:39 min**  
**Ocorrência**Ao tentar encerrar a **OP - Ordem de Produção** é apresentada a mensagem **AJUDA: D3\_TM**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006196282/mceclip0.png)

**Ambiente**Microsiga Protheus - Chão de Fábrica - Versão 12  
  
**Causa**  
O parâmetro **MV\_SFRQMB - Tipo de Movimento a ser utilizado pelo módulo Chão de Fábrica ao fazer requisições e apontamentos de mão de obra** não está configurado corretamente.  
 **Solução**Informar um**TM - Tipo de Movimentação** do tipo **Requisição** no parâmetro **MV\_SFRQMB**.  
  
**Importante**  
As **TM's** são cadastradas no **MATA230 - Tipo de Movimentação.**
