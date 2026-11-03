---
content_hash: 83ae173a61af4afe4445e36b11221cf16895dc671eb7fe5418b9443ce7cbe80f
fetched_at: '2026-06-29T00:12:02.785265+00:00'
page_id: '904064630'
product: rm
source: tdn-rm
title: Preparar Ambiente NF-e (RM x TSS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904064630
version: 22
---

A etapa preparar Ambiente realiza as devidas configurações com no TSS conforme abaixo.

falsePreparar Ambiente RM x TSSfalseautohiddentrue8167

Fluxo Preparar AmbienteleftCFGCONNECT

Neste momento o RM irá acionar o serviço CFGCONNECT para avaliar se a conexão com o TSS esta ativa

ADMEMPRESAS

Neste momento o RM irá acionar o serviço ADMEMPRESAS com os dados da Filial Emitente do documento para que o TSS retorno o código da entidade desta Filial

GETALLMVTSS

Neste momento o RM irá acionar o serviço GETALLMVTSS para recuperar os parâmetros configurados no TSS para esta Filial

O processo irá identificar a necessidade de reconfigurar os parâmetros no TSS nas seguintes condições:

**1ª Algum dos parâmetros abaixo for retornado pelo TSS com um valor diferente das parametrizações do RM**

Modelo de Documento NF-e (55)

* MV\_MODALID
* MV\_AMBIENT
* MV\_VERSAO
* MV\_VERDPEC
* MV\_NFECAEV (for diferente de 1)

Modelo de Documento NFC-e

* MV\_AMBNFCE
* MV\_MODNFCE
* MV\_VERNFCE

**2º Quando houver falha no retorno do webservice do TSS (soapFault)**

CFGVERSAOCTE

Neste momento o RM irá acionar o serviço CFGVERSAOCTE para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGVERSAO

Neste momento o RM irá acionar o serviço CFGVERSAO para configurar a versão no TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGVERSAODPEC

Neste momento o RM irá acionar o serviço CFGVERSAODEPC para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGMODALIDGRV

Neste momento o RM irá acionar o serviço CFGMODALIDGRV para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGMODALIDADE

Neste momento o RM irá acionar o serviço CFGMODALIDADE para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGAMBIENTE

Neste momento o RM irá acionar o serviço CFGAMBIENTE para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

CFGTEMPOESPERA

Neste momento o RM irá acionar o serviço CFGAMBIENTE para configurar o TSS.

CFGMDFE

Neste momento o RM irá acionar o serviço CFGMDFE para configurar o TSS.

CFGCCE

Neste momento o RM irá acionar o serviço CFGCCE para configurar os eventos no TSS.

Configurar CertificadoCFGREADYEX

Neste momento o RM irá acionar o serviço CFGREADYEX para verificar as configurações de Certificado Digital no TSS.
