---
article_id: 360028913611
category: NFe - Nota Fiscal Eletrônica
content_hash: 448bf80c0e94c3afc396f6743193f7cea65220b0df1cbef50ca14ea307e14ee0
fetched_at: '2026-06-28T22:40:01.445454+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 521 Rejeição :
  Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte
  do ICMS'
type: support-article
updated_at: '2021-07-05T15:58:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028913611--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-521-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-Interna-e-UF-do-emitente-difere-da-UF-do-destinat%C3%A1rio-remetente-contribuinte-do-ICMS
---

**Dúvida**Como solucionar a rejeição

521 Rejeição : Operação Interna e UF do emitente difere da UF do destinatário/remetente contribuinte do ICMS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Nota de saída:**

Quando operação é interna e a UF do emitente difere da UF do destinatário com o CFOP iniciado por 5 e o destinatário é contribuinte do ICMS, a nota só é autorizada caso a operação seja presencial e sem frete.

1- No pedido de vendas preencher o campo **Presença Com** "**C5\_INDPRES = 1"**

**![venda_presencial.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101196234/venda_presencial.gif)**

2 - No pedido de venda preencher o campo **Tipo frete "C5\_TPFRETE= S"**

![sem_frete.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103357353/sem_frete.gif)

3- Após isso, **excluir a nota e gerar novamente.**

**Importante:**

Caso o destinatário **não seja contribuinte do ICMS** basta alterar para isento ou não contribuinte conforme o cadastro junto a Sefaz.

* **Quando for 2 (Isento):**

**Isento**  
​  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972074/mceclip3.png)

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972034/mceclip2.png)

* **Quando for 9 (não contribuinte):**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059971394/mceclip0.png)

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059973634/mceclip5.png)

* **Referente a nota técnica 2015.002\_v\_1.40 página 18:**

Operação Interna (idDest=1) e UF emitente diferente da UF do destinatário/remetente e destinatário/remetente contribuinte do ICMS (indIEDest=1)

Exceção 1: A regra de validação não se aplica se a tag UFCons (id:LA06) foi informada com a mesma UF do emitente. (NT 2010/007) Exceção 2: A regra de validação não se aplica se a operação é presencial (tag: indPres=1 -Operação presencial) e não possui frete (tag: modFrete=9 -Sem frete). (NT 2011/004)  
Observação: No caso da NFC-e, a informação do endereço do destinatário é opcional. Considerar a UF do destinatário como sendo a mesma UF do emitente (operação interna).

Para nota de devolução de venda, será considerado o conteúdo do campo da TES **F4\_VENPRES=1** na montagem da tag **indPres=1 – Operação Presencial**.

* **Validação da Sefaz:**

![rejei__o_521_validacao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101189254/rejei__o_521_validacao.JPG)
