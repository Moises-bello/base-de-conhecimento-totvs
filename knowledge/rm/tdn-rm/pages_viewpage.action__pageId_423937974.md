---
content_hash: 2a01ec255895c2c202a9a2168ef6e6412600250b33632953335e53e8cf44e158
fetched_at: '2026-06-29T00:09:24.630811+00:00'
page_id: '423937974'
product: rm
source: tdn-rm
title: Integração TOTVS Colaboração (TSS x NeoGrid x SEFAZ)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937974
version: 2
---

A integração TOTVS Colaboração contempla o TSS (servidor de aplicação da TOTVS) e a solução NeoGrid.   
Ela irá validar a autenticidade de um arquivo XML junto à SEFAZ. Este arquivo pode ser uma Nota Fiscal Eletrônica (NF-e), um Conhecimento de Transporte Eletrônico (CT-e), ou uma Nota Fiscal de Serviços (NFS-e).   
Ela irá garantir que o arquivo recebido seja o mesmo emitido pelo fornecedor e armazenado na SEFAZ.   
A integração também possibilita incluir movimentos baseados em NF-e que foram validadas pela SEFAZ.  
O fornecedor envia o arquivo XML para o ERP. Este cadastra o arquivo e o envia ao TSS, que realiza o gerenciamento dos arquivos XML recebidos e os envia ao NeoGrid. Por sua vez, o NeoGrid valida a informação contida no arquivo e o envia a SEFAZ.  
Após este fluxo, o ERP pode realizar a consulta e busca do arquivo XML.   
A consulta tem o objetivo de verificar o status do arquivo junto a SEFAZ.   
A busca consiste em receber um arquivo XML que não tenha passado pelo ERP.   
No caso da busca, o arquivo XML autorizado foi enviado do fornecedor diretamente a NeoGrid, e segue o mesmo fluxo para a SEFAZ.   
Neste cenário, os arquivos serão recebidos pela NeoGrid através da integração EDI ou do Portal WEB.
