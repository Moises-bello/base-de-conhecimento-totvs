---
article_id: 29125485805719
category: Escrita Fiscal - Impostos - ICMS
content_hash: ff81ff2ec4b33511d01104e2f9974820762107140637cfc9fd8fb70beca1f8e3
fetched_at: '2026-06-28T22:39:24.030915+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  FIS - Como gerar tag
  Cbenef Ato DIAT Nº 35 DE 17/07/2024 de SC?
type: support-article
updated_at: '2025-02-05T13:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29125485805719-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-tag-Cbenef-Ato-DIAT-N%C2%BA-35-DE-17-07-2024-de-SC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29125528419095) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como gerar tag Cbenef Ato DIAT Nº 35 DE 17/07/2024 de SC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

MV\_ESTADO = SC

MV\_MTCLF3K = 0

Cliente = SC

Cadastro de produtos

Origem = 1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125485755799)

TES

Calcula icms = sim

L fiscal icms = tributado

CST = 90

**Tp Cred Pres.= B**

**Crd.Pres = 3**

Agreg CrdPre = não

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125528424599)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125485763863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125528430999)

Reflexo amarrado no TES

SC24000001 - reflexo 0000010

SC10000047 - reflexo 0000070

SC54000001 - reflexo 0000070

Reflexos usados neste teste padrões gerados pelo U\_IMPSPED

Fisa140

5102 - CST90 - SC850065 - Reflexo 0000070

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125485774231)

Fisa156

SC850065 - Tipo Lanc - credito presumido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125528434839)

Valor da mercadoria = 1000,00

Base de calculo icms = 1000,00 x4% = 40,00

Credito presumido = 1000,00\*3% = 30,00

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29125485778455)

Verificar o parametro MV\_CODCST

* Para uma ou mais UFs, preenchendo o código da UF acompanhada do CST para que o conteúdo da tag **cBenef seja alimentado com o literal "SEM CBENEF"**:  
  + Ex.: RS=10,90;PR=10

Para esse exemplo no estado de SC não pode estar preenchido o  CST90

Documentos

<https://tdn.totvs.com/pages/releaseview.action?pageId=841173522>

<https://tdn.totvs.com/display/public/TSS/DSERTSS1-23003+DT+TSS+-+NT+2019.001+-+v1.61+e+v1.62>
