---
article_id: 4411767075095
category: Materiais - Compras (SIGACOM)
content_hash: e6ee6c113cc278847dc1fbdba49d3fea2865f14bfb71177333e05387cd7d66e8
fetched_at: '2026-06-28T22:41:14.170119+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao Inserir Documento
  de entrada com campo D1_LOTEFOR vazio ocorre error.log
type: support-article
updated_at: '2021-10-29T20:05:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411767075095-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-Inserir-Documento-de-entrada-com-campo-D1-LOTEFOR-vazio-ocorre-error-log
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao Inserir Documento de entrada com campo D1\_LOTEFOR vazio ocorre error.log

SD1010: DB error (Insert): -27 File: SD1010 - Error : 515 (23000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Não é possível inserir o valor NULL na coluna 'D1\_LOTEFOR', tabela 'dbMezzani.dbo.SD1010'; a coluna não permite nulos. Falha em INSERT.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão COmpras- Todas as versões

**Solução**"Normalmente esse erro é relacionado com

- campo D1\_LOTEFOR  na tabela SD1 não estar conforme o padrão do sistema:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411772427671/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411767036695/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411767039511/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411772446999/mceclip3.png)

- Haver alguma customização no ambiente que influencie (desabilitar todas as customizações e gatilhos customizados) 

- artefatos de framework (lib, binarios, dbacess) e fontes desatualizados

- Para atualizar os artefatos e fontes verificar o artigo abaixo: 

[MP - SIGACOM - Principais Atualizações do Módulo de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028041232-MP-SIGACOM-Principais-Atualiza%C3%A7%C3%B5es-do-M%C3%B3dulo-de-Compras?source=search)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
