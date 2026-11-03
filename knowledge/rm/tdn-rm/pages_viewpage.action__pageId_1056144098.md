---
content_hash: 1560213f8e9c2d583ee158b1941ce2d4e12c4616c1fec8d983751f730c9aff36
fetched_at: '2026-06-29T00:05:51.995106+00:00'
page_id: '1056144098'
product: rm
source: tdn-rm
title: Dados detalhados do tomador do serviço (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144098
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

Tomador0Campos Gerais

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **tomador** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | **G** | **1-1** | **Tag raiz para as informações sobre o tomador.** |  |  |
| inscmun | tomador | E | 0-1 | Inscrição municipal do tomador. | FCFO.INSCRMUNICIPAL | A Inscrição Municipal só deve ser preenchida para Tomadores do Município do Prestador. Quando a inscrição municipal do Tomador for diferente do Prestador ou não for utilizado a Inscrição municipal, deverá ser preenchida a TAG com 7 zeros conforme manual do TSS |
| cpfcnpj | tomador | E | 1-1 | CPF/CNPJ do tomador. | FCFO.CGCCFO |  |
| razao | tomador | E | 1-1 | Razão social do tomador. | FCFO.NOME |  |
| tipologr | tomador | E | 0-1 | Tipo de logradouro.  Os valores válidos são:  •  1 – Avenida;  •  2 – Rua;  •  3 – Rodovia;  •  4 – Ruela;  •  5 – Rio;  •  6 – Sítio;  •  7 – Sup. Quadra;  •  8 – Travessa;  •  9 – Vale;  •  10 – Via;  •  11 – Viaduto;  •  12 – Viela;  •  13 – Vila;  •  14 - Vargem. | DTIPORUA.DESCRICAO | Será verificado se DTIPORUA.DESCRICAO coincide com algum item da lista ao lado |
| logradouro | tomador | E | 1-1 | Logradouro do tomador. | FCFO.RUA | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag logradouro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| numend | tomador | E | 1-1 | Número do endereço do tomador. | FCFO.NUMERO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag numend não for informado nesta situação, o mesmo será exibido como SN |
| complend | tomador | E | 0-1 | Complemento do endereço do tomador. | FCFO.COMPLEMENTO |  |
| bairro | tomador | E | 1-1 | Bairro do tomador. | FCFO.BAIRRO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag bairro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| codmunibge | tomador | E | 0-1 | Código do município do tomador, padrão IBGE. |  | Código de Classificação definido para esta município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| cidade | tomador | E | 1-1 | Município do tomador. | GMUNICIPIO.NOMEMUNICIPIO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag cidade não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| uf | tomador | E | 1-1 | Unidade federativa do tomador. | FCFO.CODETD | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag uf não for informado nesta situação, o mesmo será exibido como SU |
| cep | tomador | E | 1-1 | CEP do tomador. | FCFO.CEP |  |
| email | tomador | E | 0-1 | Endereço de e-mail do tomador. | FCFO.EMAIL |  |
| telefone | tomador | E | 0-1 | Telefone do tomador. | FCFO.TELEFONE |  |
| codpais | tomador | E | 0-1 | Código do país do tomador. | DPAIS.CODPAIS | De acordo com a classificação de país informada nos parâmetros |
| nomepais | tomador | E | 0-1 | Nome do país do Tomador. | GPAIS.DESCRICAO |  |
| estrangeiro | tomador | E | 1-1 | Define se o tomador é estrangeiro. 1 – Sim;  2 – Não. | GETD.NACIONAL | Se estado Nacional  Então Sim Senão Não |
| notificatomador | tomador | E | 0-1 | Indicativo para notificar o tomador por e-mail:  1 – Sim;  2 – Não. |  | Fixo Não |
| csituacaoesptom | tomador | E | 0-1 | Situação Especial do Tomador . Consulte os valores na tabela 7  Utilizado no padrão de Joinville (Offline). |  | Não será gerado |
| ctomnaoidentificado | tomador | E | 0-1 | Define se o tomador é não Identificado |  | Não será gerado |
| inscricaoEstadual | tomador | E | 0-1 | Inscrição Estadual | FCFO.INCRESTADUAL |  |
| caepf | tomador | E | 0-1 | Cadastro de Atividade Econômica da Pessoa Física (CAEPF) | FCFO.CODIGOCAEPF |  |
| exSemNIF | tomador | E | 0-1 | Motivo para não informação do NIF | FCFO.SITUACAONIF | Os valores aceitos são: 0 - Não informado na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do NIF; |

Regras Específicas por MunicípioRE-1left0Rio Grande

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| inscmun | tomador | E | 0-1 | Inscrição municipal do tomador. | FCFOCOMPL.INSCMUNTEMP | Para o Município de Rio Grande (4315602) este campo pode ser preenchido com o código CCM informado pela prefeitura, neste caso, basta criar um campo complementar, no cadastro do cliente fornecedor, com o nome INSCMUNTEMP. |
