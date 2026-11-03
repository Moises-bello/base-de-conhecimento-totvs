---
article_id: 5245372051223
category: Materiais - Compras (SIGACOM)
content_hash: 473cca1cd77f3203330a39fa6de436bd0df041e4a58cb276be6b03e5ae5df02f
fetched_at: '2026-06-28T22:41:18.712766+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Gerar Documento de
  entrada automático no SIGAGFE.
type: support-article
updated_at: '2022-04-05T16:42:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5245372051223-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Gerar-Documento-de-entrada-autom%C3%A1tico-no-SIGAGFE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **6 min.****Dúvida**Como gerar a nota fiscal no SIGAGFE de forma automático.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões

**Solução**

Para o sistema gerar a nota fiscal no momento que classifica, precisa esta com as seguintes parametrizações cadastradas no modulo **(SIGAGFE)  Atualizações/ Cadastros/ Parâmetros/ Parâmetros do Módulo.**

Rotina GFEX000 na aba Integração Protheus:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5244825051159/mceclip0.png)

Parâmetros envolvido no processo:

MV\_INTGFE2: 

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5245255117335/mceclip4.png)

MV\_GFEI10:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5245227024151/mceclip5.png)

Caso ative a integração e apresente a mensagem abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5245289756695/mceclip6.png)

Precisa seguir o Passo a Passo abaixo:

O campo Nota Fiscal de Entrada com a opção: 1-Integrar;

GFE Ativo: Com o Flag preenchido;

Modo Integração: 1-Direta;

Código do Emitente: 1- Numeração Própria.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5245205152279/mceclip3.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
