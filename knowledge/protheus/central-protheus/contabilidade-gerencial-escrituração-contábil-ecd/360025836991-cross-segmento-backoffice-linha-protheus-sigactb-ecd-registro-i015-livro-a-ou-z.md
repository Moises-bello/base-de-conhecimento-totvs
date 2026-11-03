---
article_id: 360025836991
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 5880079ce26da860bf1abe4d0a62dddf372955073b184dc490a6a4ed81a0d9fc
fetched_at: '2026-06-28T22:40:44.800640+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD REGISTRO I015 LIVRO
  A ou Z
type: support-article
updated_at: '2022-05-10T15:03:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025836991-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-REGISTRO-I015-LIVRO-A-ou-Z
---

**Dúvida**Como gerar o registro I015 para o livro A ou Z?  
   
 **Ambiente**Protheus – Contabilidade Gerencial– A partir da versão 11.80  
  
   
**Solução**Na rotina central de escrituração (CTBS001) após gerar o livro A ou Z, posicione sobre a revisão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024708011/mceclip0.png)

Para livros A ou Z, clique em **Sel. Conta**. Será apresentada tela para cadastro manual e/ou importação do plano de contas a serem utilizadas no registro I015. Informar conta sintética.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024693932/mceclip1.png)

**REGRA\_VALIDA\_CONTA\_AUXILIAR\_RESUMIDA:** Verifica se o IND\_ESC (campo 02) do registro I010 se o campo indicador da forma da escrituração contábil – IND\_ESC (campo 02) do registro I010 – é igual a **“A” ou “Z”** e se o campo código da conta analítica do livro diário com escrituração resumida – COD\_CTA\_RES (Campo 02) – possui uma correspondência idêntica ao campo código da conta analítica/grupo de contas – COD\_CTA (campo 06) – do registro I050, para o campo indicador do tipo de conta – IND\_CTA (campo 04) – do registro I050 igual a **“S” (sintética)**. Se a regra não for cumprida, o PGE do Sped Contábil gera um aviso.
