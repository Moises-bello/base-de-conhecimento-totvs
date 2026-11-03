---
article_id: 29254452584215
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 721ac27a3cfee9022c61a866c54b06b3154b6fc65e9c31c438b894a397784b5d
fetched_at: '2026-06-28T22:38:44.048298+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help COMPARTILHAMENTO (Tabelas
  SF1, SF2, SD1 e SD2)
type: support-article
updated_at: '2025-01-15T20:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29254452584215-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-COMPARTILHAMENTO-Tabelas-SF1-SF2-SD1-e-SD2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29254466904215) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o correto compartilhamento do modo de acesso para as tabelas SD1/SD2 (itens documentos de entrada/saída)  
  
**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Para o correto funcionamento na inclusão de documentos fiscais e na integração com os diferentes módulos, o modo de compartilhamento das tabelas deve ser o mesmo na tabela de cabeçalho do documento (SF1/SF2) do que na tabela de itens do documento (SD1/SD2). O modo de compartilhamento sugerido por default para as tabelas SF1, SF2, SD1 e SD2 é totalmente exclusivo.

Se existe diferença entre o modo de compartilhamento das tabelas de itens com as tabelas do cabeçalho, dever ser ajustada a configuração, para que tenha o mesmo modo de compartilhamento para as tabelas SF1, SF2, SD1 e SD2.

**Compartilhamento sugerido por default:**

| Tabela | X2\_MODOEMP | X2\_MODOUN | X2\_MODO |
| --- | --- | --- | --- |
| SD1 | E-Exclusivo | E-Exclusivo | E-Exclusivo |
| SF1 | E-Exclusivo | E-Exclusivo | E-Exclusivo |
| SD2 | E-Exclusivo | E-Exclusivo | E-Exclusivo |
| SF2 | E-Exclusivo | E-Exclusivo | E-Exclusivo |

**Saiba mais: [DT Modo de compartilhamento das tabelas de documentos fiscais](https://tdn.totvs.com/x/DPGjLw)**
