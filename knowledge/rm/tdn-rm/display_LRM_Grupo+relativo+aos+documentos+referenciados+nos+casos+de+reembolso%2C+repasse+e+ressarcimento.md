---
content_hash: 3667883e55489c8940b6c25461b0bf2f170d5d8775f2042f5efd8da03216dcc7
fetched_at: '2026-06-29T00:05:52.153577+00:00'
page_id: '1056935125'
product: rm
source: tdn-rm
title: Grupo relativo aos documentos referenciados nos casos de reembolso, repasse
  e ressarcimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+relativo+aos+documentos+referenciados+nos+casos+de+reembolso%2C+repasse+e+ressarcimento
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| documentos | [deducoes](https://tdn.totvs.com/pages/viewpage.action?pageId=560653861) | G | 0-1 | Grupo relativo aos documentos referenciados nos casos de reembolso, repasse e ressarcimento que serão considerados na base de cálculo do ISSQN, do IBS e da CBS. | Não será gerado |  |
| dFeNacional | documentos | G | 0-1 | Grupo de informações de documentos fiscais eletrônicos que se encontram no repositório nacional. | Não será gerado |  |
| tipoChaveDFe | dFeNacional | E | 0-1 | Tipo Chave:  1 = NFS-e; 2 = NF-e; 3 = CT-e; 9 = Outro; | Não será gerado |  |
| xTipoChaveDFe | dFeNacional | E | 0-1 | Descrição Tipo Chave. | Não será gerado |  |
| chaveDFe | dFeNacional | E | 0-1 | Chave DFe. | Não será gerado |  |
| docFiscalOutro | documentos | G | 0-1 | Grupo de informações de documento fiscais, eletrônicos ou não, que não se encontram no repositório nacional. | Não será gerado |  |
| cMunDocFiscal | docFiscalOutro | E | 0-1 | Código Município Documento | Não será gerado |  |
| nDocFiscal | docFiscalOutro | E | 0-1 | Número Documento | Não será gerado |  |
| xDocFiscal | docFiscalOutro | E | 0-1 | Descrição Documento | Não será gerado |  |
| docOutro | documentos | G | 0-1 | Grupo de informações de documento não fiscal. | Não será gerado |  |
| nDoc | docOutro | E | 0-1 | Número Documento | Não será gerado |  |
| xDoc | docOutro | E | 0-1 | Descrição Documento | Não será gerado |  |
| fornec | documentos | G | 0-1 | Grupo de informações do fornecedor do documento referenciado. | Não será gerado |  |
| cpfcnpj | fornec | E | 0-1 | CNPJ/CPF Fornec. | Não será gerado |  |
| NIF | fornec | E | 0-1 | NIF | Não será gerado |  |
| cNaoNIF | fornec | E | 0-1 | Motivo sem NIF. | Não será gerado |  |
| CAEPF | fornec | E | 0-1 | CAEPF | Não será gerado |  |
| IM | fornec | E | 0-1 | Inscrição Municipal. | Não será gerado |  |
| nome | fornec | E | 0-1 | Nome. | Não será gerado |  |
| logradouro | fornec | E | 0-1 | Logradouro. | Não será gerado |  |
| numend | fornec | E | 0-1 | Número. | Não será gerado |  |
| complend | fornec | E | 0-1 | Complemento | Não será gerado |  |
| bairro | fornec | E | 0-1 | Bairro | Não será gerado |  |
| cep | fornec | E | 0-1 | CEP | Não será gerado |  |
| codmunibge | fornec | E | 0-1 | Código Município | Não será gerado |  |
| cidade | fornec | E | 0-1 | Cidade | Não será gerado |  |
| estado | fornec | E | 0-1 | Estado | Não será gerado |  |
| codpais | fornec | E | 0-1 | Código País. | Não será gerado |  |
| ddd | fornec | E | 0-1 | DDD | Não será gerado |  |
| telefone | fornec | E | 0-1 | Telefone | Não será gerado |  |
| email | fornec | E | 0-1 | Email | Não será gerado |  |
| -x- Sequencia do grupo documentos | | | | | | |
| dtEmiDoc | documentos | E | 0-1 | Data Emissão. | Não será gerado |  |
| dtCompDoc | documentos | E | 0-1 | Data Competência. | Não será gerado |  |
| tpReeRepRes | documentos | E | 0-1 | Tipo Reembolso. | Não será gerado |  |
| xTpReeRepRes | documentos | E | 0-1 | Descrição Tipo Reembolso. | Não será gerado |  |
| vlrReeRepRes | documentos | E | 0-1 | Valor Reembolso. | Não será gerado |  |
