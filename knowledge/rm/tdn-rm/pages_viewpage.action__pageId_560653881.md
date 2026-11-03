---
content_hash: 2337029d9d75b5e0762b3f2e2cfd7e952acf3fd8f0fd080329f377b4f2576634
fetched_at: '2026-06-29T00:10:47.802342+00:00'
page_id: '560653881'
product: rm
source: tdn-rm
title: Informações complementares do documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653881
version: 7
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| infcompl | [rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227) | G | 0-1 | Tag raiz que agrupará as informações complementares do documento. |  |  |
| descricao | infcompl | E | 1-1 | Descrição/Dados complementares do documento. |  |  |
| observacao | infcompl | E | 0-1 | Observações referentes ao documento. | infcompl.descricao |  |
| ativport | infcompl | G | 0-N | Tag raiz que conterá as informações sobre atividade portuária do documento. |  | Não será Gerado |
| nomraz | ativport | E | 1-1 | Nome/Razão social do proprietário/representante da atividade portuária. |  | Não será Gerado |
| cpfcnpj | ativport | E | 1-1 | CPF/CNPJ do proprietário/representante da atividade portuária. |  | Não será Gerado |
| endereco | ativport | E | 1-1 | Endereço da atividade portuária. |  | Não será Gerado |
| numero | ativport | E | 1-1 | Número do endereço da atividade portuária. |  | Não será Gerado |
| compl | ativport | E | 1-1 | Complemento do endereço da atividade portuária. |  | Não será Gerado |
| bairro | ativport | E | 1-1 | Bairro do endereço da atividade portuária. |  | Não será Gerado |
| codmunibge | ativport | E | 1-1 | Código do município do endereço da atividade portuária. |  | Não será Gerado |
| uf | ativport | E | 1-1 | Unidade federativa do endereço da atividade portuária. |  | Não será Gerado |
| cep | ativport | E | 1-1 | CEP do endereço da atividade portuária. |  | Não será Gerado |
| stpropr | ativport | E | 1-1 | O proprietário realizou substituição tributária. Os valores possíveis são: •  1 – Sim; •  2 – Não. |  | Não será Gerado |
| nomeemb | ativport | E | 1-1 | Nome da embarcação da atividade portuária. |  | Não será Gerado |
| bandemb | ativport | E | 1-1 | Bandeira da embarcação da atividade portuária. |  | Não será Gerado |
| nomeport | ativport | E | 1-1 | Nome do porto da atividade portuária. |  | Não será Gerado |
| dthrent | ativport | E | 1-1 | Data e hora da entrada da atividade portuária. Formato AAAA-MM-DDTHH:mm:ss |  | Não será Gerado |
| dthrsai | ativport | E | 1-1 | Data e hora da saída da atividade portuária. Formato AAAA-MM-DDTHH:mm:ss |  | Não será Gerado |
