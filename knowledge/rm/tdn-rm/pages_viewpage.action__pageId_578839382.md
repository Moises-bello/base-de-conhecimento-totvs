---
content_hash: bf7022a681e7537f0226254d1517b91fdc32219a5558b344915ae8c45d0c2899
fetched_at: '2026-06-29T00:10:53.713831+00:00'
page_id: '578839382'
product: rm
source: tdn-rm
title: Configuração do certificado Digital no TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578839382
version: 2
---

Para correta emissão da NFS-e é necessário que os dados do Certificado Digital configurados no processo de envio da NFS-e sejam enviados para o TSS assinar digitalmente o XML do RPS e para conectar-se ao WebService da prefeitura.

Os dados são enviados conforme o layout do serviço definido na página do TSS.

Certificado do tipo PFX: 

Certificado do tipo Apache: 

Certificado do tipo HSM: 

Contudo alguns municípios não utilizam assinatura por certificado Digital e neste caso a configuração do método cfgnfsecertpfx não é realizada. São eles:

* Ouro Preto - MG
* São Gonçalo - RJ
* Qualquer município com Layout TXT
* Qualquer município com Layout SIGISS
* Qualquer município integrado com o TOTVS Colaboração 2.0
