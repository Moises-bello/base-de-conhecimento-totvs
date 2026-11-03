---
article_id: 360010381631
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 0c4ea1af9eb002d7206b82ea5c4fb622f773fd02ee28225a334269115a88d2b8
fetched_at: '2026-06-28T22:42:02.542462+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registro C101 e C105
type: support-article
updated_at: '2025-02-11T21:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010381631-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registro-C101-e-C105
---

**Dúvida**

Como gerar o registro C101 e C105?

**Ambiente**

Protheus - Livros Fiscais - A partir de 12.1.17

**Solução**

#### **REGISTRO C101: Informação Complementar dos Documentos Fiscais para Operações Interestaduais Destinadas a Consumidor Final Não Contribuinte EC 87/15 (Código55)**

Para geração do registro C101 deve ser realizado a seguinte configuração na TES.

**Cliente**

Para Cliente consumidor final não Contribuinte é necessário que cadastro de cliente campo **Insc. Estadual (A1\_INSCR)** deve estar em **BRANCO** e o campo Contribuinte (A1\_CONTRIB) com conteúdo **NÃO.**

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-43-34.png?version=1&modificationDate=1525459415000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-44-16.png?version=1&modificationDate=1525459456000&api=v2)

**TES**

Para que seja realizado **Cálculo de Diferencial de Alíquota para Consumidor Final Não Contribuinte** é necessário configurar no cadastro de TES os campos:

* **Calcula ICMS (F4\_ICM)**= SIM
* **Calc. Difal (F4\_DIFAL)**= SIM
* **Calc.Dif.ICM (F4\_COMPL)**= SIM

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-45-9.png?version=1&modificationDate=1525459510000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-46-38.png?version=1&modificationDate=1525459599000&api=v2)

**Importante:**Após processo, serão gravados os campos **F3\_DIFAL**, **F3\_ICMSCOM** da Tabela **SF3** e **FT\_DIFAL**, **FT\_ICMSCOM** da tabela **SFT** para correta geração do registro C101.

**Gerar um pedido de venda usando o produto e a TES e verificar se calculou o DIFAL:**

**Pedido de vendas/outras ações/planilha:**

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-47-28.png?version=1&modificationDate=1525459649000&api=v2)

**Gerar apuração de ICMS e verificar se levou as informações do DIFAL na apuração:**

**Livros Fiscais/Miscelânea/Apurações/Apuração ICMS – ABA DIFAL/FECP – Confirmar!**

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-49-16.png?version=1&modificationDate=1525459757000&api=v2)

**GERAR SPED FISCAL**

**Livros Fiscais/Miscelânea/Arquivos Magnéticos/Sped Fiscal**

**Marcar campo “Gerar Registros DIFAL” =  SIM**

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-50-18.png?version=1&modificationDate=1525459818000&api=v2)

**Geração concluída com o registro gerado corretamente:**

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-51-6.png?version=1&modificationDate=1525459867000&api=v2)

#### **REGISTRO C105: Operações com ICMS ST Recolhido para UF Diversa do Destinatário do Documento Fiscal (Código55)**

Este registro não é gerado, pois a informação não é tratada pelo Microsiga Protheus.

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
