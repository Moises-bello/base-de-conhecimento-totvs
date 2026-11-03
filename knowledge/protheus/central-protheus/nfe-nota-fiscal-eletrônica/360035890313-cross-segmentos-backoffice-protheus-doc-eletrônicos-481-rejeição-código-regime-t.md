---
article_id: 360035890313
category: NFe - Nota Fiscal Eletrônica
content_hash: e32a855880068d97d751a23172cb245a3ef4d2c77dc4ac795d1536fc7b15af4c
fetched_at: '2026-06-28T22:40:01.429034+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 481 Rejeição :
  Código Regime Tributário do emitente diverge do cadastro na SEFAZ'
type: support-article
updated_at: '2023-04-18T13:21:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035890313--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-481-Rejei%C3%A7%C3%A3o-C%C3%B3digo-Regime-Tribut%C3%A1rio-do-emitente-diverge-do-cadastro-na-SEFAZ
---

**Dúvida**481 Rejeição : Código Regime Tributário do emitente diverge do cadastro na SEFAZ  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Rejeição ocorre devido o **regime tributário** no XML ter sido informado **diferente do cadastrado** na SEFAZ com relação ao **emitente.**

1- Para resolver a rejeição deve ser informado o código correto do **regime tributário** no parâmetro **MV\_CODREG.** Parâmetro utilizado para informar a forma de **regime tributário** do emitente da **Nota Fiscal Eletrônica**:

**MV\_CODREG:**1 - Simples Nacional;  
2 - Simples Nacional - excesso de receita bruta;  
3 - Regime Nacional.

Parâmetro utilizado para informar a forma de **regime tributário** do emitente da **Nota Fiscal Eletrônica**:

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_CODREG**

1. Simples Nacional;

![MV_CODREG.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12204804915223)

2. Simples Nacional - excesso de receita bruta;

![MV_CODREG_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12204843703063)

3. Regime Nacional.

![MV_CODREG_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12204866974487)

4. Caso a SEFAZ **solicite que o CRT=1** será necessário preencher além do parâmetro o campo **Cod Sit SN** (F4\_CSOSN) no TES para que seja levado o CSOSN e deixar o campo **Sit. trib. ICM (F4\_SITTRIB)** em branco. 

![CRT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13959744323735)

3- Caso a SEFAZ **solicite que o CRT=2 ou 3** será necessário preencher além do parâmetro o campo **Sit. trib. ICM (F4\_SITTRIB)** no TES para que seja levado o CST

![F4_SITTRIB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13959915767831)

 4 - Após isso, exclua a nota e gere novamente.

* **Importante:**

Caso o seu fiscal informe que o regime tributário da empresa está correto, será necessário entrar em contato com a Sefaz e verificar junto a mesma o motivo da rejeição.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038360314/mceclip0.png)**
