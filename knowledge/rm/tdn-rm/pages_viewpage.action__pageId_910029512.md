---
content_hash: 73aa82b2a92b538c91443f10b07221ccfe0b2218f2524379c8c5bf66155e98fb
fetched_at: '2026-06-29T00:12:03.459462+00:00'
page_id: '910029512'
product: rm
source: tdn-rm
title: Preparar Ambiente NFS-e (RM x TSS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=910029512
version: 10
---

A etapa preparar Ambiente realiza as devidas configurações com no TSS conforme abaixo.

falsePreparar Ambiente NFS-efalseautohiddentrue4515

Fluxo Preparar AmbienteleftCFGCONNECT

Neste momento o RM irá acionar o serviço CFGCONNECT para avaliar se a conexão com o TSS esta ativa

ADMEMPRESAS

Neste momento o RM irá acionar o serviço ADMEMPRESAS com os dados da Filial Emitente do documento para que o TSS retorno o código da entidade desta Filial

GETALLMVTSS

Neste momento o RM irá acionar o serviço GETALLMVTSS para recuperar os parâmetros configurados no TSS para esta Filial

O processo irá identificar a necessidade de reconfigurar os parâmetros no TSS nas seguintes condições:

**1ª Algum dos parâmetros abaixo for retornado pelo TSS com um valor diferente das parametrizações do RM**

* MV\_NFSEAMB: Diferente da configuração do RM
* MV\_NFSEMOD: Diferente de 0
* MV\_NFSEVER: Diferente da configuração do RM
* MV\_NFSEMUN: Diferente do código IBGE configurado para o município da Filial
* MV\_SIAFI: Diferente do código SIAF configurado para o município da Filial
* MV\_USOCERT: Diferente de "NFSE"
* MV\_MAXLOTE: Diferente do Parâmetro quantidade de notas por lote
* MV\_CNPJAUT: O CNPJ for diferente do CNPJ do certificado Digital
* MV\_ENVSINC: Diferente de "N"
* MV\_NFSUSER: Diferente do parâmetro "login" da NFS-e
* MV\_NFSPASS: Diferente da senha do login da NFS-e
* MV\_AUTORIZ: Diferente do parâmetro "Autorização da NFS-e"
* MV\_CHVAUTE: Diferente do parâmetro "chave de autenticação" da NFS-e
* MV\_CLIENID e MV\_CLIENSC: Diferente da autenticação do TSS configurado no RM
* Caso o TSS não retorne a parametrização MV\_NFSEAMB

**2º Quando houver falha no retorno do webservice do TSS (soapFault)**

 CFGAMBNFSE001

Neste momento o RM irá acionar o serviço CFGAMBNFSE001 para configurar o TSS.

Este serviço será acionado somente se for identificada a necessidade de reconfiguração do TSS conforme definido no item GETALLMVTSS

Configurar CertificadoCFGREADYEX

Neste momento o RM irá acionar o serviço CFGREADYEX para verificar as configurações de Certificado Digital no TSS.
