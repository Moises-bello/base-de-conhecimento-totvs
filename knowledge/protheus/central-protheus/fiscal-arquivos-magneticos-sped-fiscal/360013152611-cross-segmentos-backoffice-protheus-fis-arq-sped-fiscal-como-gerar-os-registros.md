---
article_id: 360013152611
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9ce70c957c00edc6fcc5ee7f44ed4c7820d871c7f13c680cdf68e2f7097ac2e6
fetched_at: '2026-06-28T22:42:00.887566+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. - SPED FISCAL Como gerar
  os Registros 1700 e 1710
type: support-article
updated_at: '2023-04-19T17:38:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013152611-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-SPED-FISCAL-Como-gerar-os-Registros-1700-e-1710
---

#### 

#### **Dúvida** Como gerar o registro 1700 e 1710? **Ambiente** Protheus – Livros Fiscais – A partir da versão 11.80

#### **Solução**

**Registro 1700: Documentos Fiscais utilizados**

Este registro é gerado com base nos documentos fiscais emitidos no período e composto pelas informações de **AIDF** cadastrados na **tabela SFS**

Wizard Sped Fiscal:

Gera Registro 1700 - Documentos Fiscais = 1- Sim

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A27%3A45.png?version=1&modificationDate=1465158112000&api=v2)

#### **Registro 1710: Documentos Fiscais Cancelados/inutilizados**

Este registro é composto pelos documentos cancelados/inutilizados constantes no intervalo do registro 1700.

Campos abaixo preenchidos

Tabela SF3

F3\_DTCANC = ? – Data do cancelamento da nota

F3\_OBSERV= ? Preenchimento padrão NF Cancelada

F3\_CODRSEF = 101 – Código do retorno da SEFAZ referente a nota cancelada/102 - Numeração Inutilizada

F3\_CHVNFE = 44 posições

Tabela SFT

FT\_OBSERV = ? Preenchimento padrão NF Cancelada

FT\_DTCANC=? -> Data do cancelamento da nota

FT\_CHVNFE = 44 posições

Wizard SPEDFISCAL

Gera Registro 1700 - Documentos Fiscais = 1- Sim

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A27%3A45.png?version=1&modificationDate=1465158112000&api=v2)

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
