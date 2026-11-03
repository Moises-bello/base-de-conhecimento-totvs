---
article_id: 360025836551
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: b4215bbfabd3213558574a5fa304310e5f2497348fca7ea7b7a2b6c25856ee31
fetched_at: '2026-06-28T22:40:44.804650+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD REGISTRO I015 LIVRO
  R OU B
type: support-article
updated_at: '2025-05-26T15:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025836551-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-REGISTRO-I015-LIVRO-R-OU-B
---

**Dúvida**Como gerar o registro I015 para o livro R ou B  
  
**Ambiente**Protheus– Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**Na rotina central de escrituração (CTBS001) após gerar o livro R ou B, posicione sobre a revisão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024706411)

Efetue o cadastro do livro auxiliar. Em seguida clique em **Sel. Cont.** para cadastrar manualmente e/ou importar o plano de contas. Informar as contas analíticas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024706591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024706991)

**REGRA\_VALIDA\_CONTA\_RESUMIDA\_AUXILIAR**:  Verifica se o campo indicador da forma da escrituração contábil – IND\_ESC (campo 02) do registro I010 – é igual a **“R” ou “B”** e se o campo **código da conta analítica** do livro diário com escrituração resumida – COD\_CTA\_RES (Campo 02) – possui uma correspondência idêntica ao campo código da conta analítica/grupo de contas – COD\_CTA (campo 06) – do registro I050. Se a regra não for cumprida, o PGE do Sped Contábil gera um erro.

Veja mais:

[Como gerar o Livro Z](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025044871-MP-SIGACTB-ECD-COMO-GERAR-O-LIVRO-Z-Layout-parametriz%C3%A1vel-)

[Como gerar o Livro A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024645212-MP-ECD-LIVRO-A-DI%C3%81RIO-AUXILIAR)
