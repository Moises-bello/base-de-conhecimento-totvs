---
article_id: 31720828670359
category: Faturamento - Integrações
content_hash: 8a793a64997b0017c5d0500e0effc6799535c58d407f619dde51426d048cd3cd
fetched_at: '2026-06-28T22:38:26.642962+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Premissas para o importador
  XML
type: support-article
updated_at: '2025-04-29T18:48:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31720828670359-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Premissas-para-o-importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31720828654871) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais as premissas para o importador XML?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

É necessário a configuração do parâmetro MV\_TCNEW, conforme as informações abaixo em "Saiba mais"

O ambiente obrigatoriamente precisa conter a licença 3100 ([TOTVS\_COLAB\_ONDEMAND](https://tdn.totvs.com/pages/viewpage.action?pageId=240976575))

A existência das tabelas do Totvs Colaboração é obrigatória:

* CKQ (Monitor Doc. TOTVS Colaboração)
* CKOCOL (Controle de Arq.TOTVS Colaboração, Realacionada a tabela "CKO")
* CKP (Parâmetros TOTVS Colaboração)

Com todos os itens acima, a integração será feita normalmente.

**Observação:** O parâmetro MV\_SPEDCOL não terá efeito sobre a integração.

**Saiba mais:**

[FAT0305 Integrador XML para Pedido de Vendas - módulo Faturamento](https://tdn.totvs.com/x/uQoxJw)

[Importador XML - Guia de Referência - Faturamento - P12](https://tdn.totvs.com/x/5zzuIw)
