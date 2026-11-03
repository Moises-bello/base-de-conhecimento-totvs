---
content_hash: ba7cb9ea7155cda14a8b6f02203579ff9442976865923bd282f176ae7859ec3a
fetched_at: '2026-06-29T00:10:47.730228+00:00'
page_id: '560653794'
product: rm
source: tdn-rm
title: Dados detalhados do tomador do serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653794
version: 23
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

Tomador0Campos Gerais

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **tomador** | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227)** | **G** | **1-1** | **Tag raiz para as informações sobre o tomador.** |  |  |
| inscmun | tomador | E | 0-1 | Inscrição municipal do tomador. | FCFO.INSCRMUNICIPAL | A Inscrição Municipal só deve ser preenchida para Tomadores do Município do Prestador. Quando a inscrição municipal do Tomador for diferente do Prestador ou não for utilizado a Inscrição municipal, deverá ser preenchida a TAG com 7 zeros conforme manual do TSS |
| cpfcnpj | tomador | E | 1-1 | CPF/CNPJ do tomador. | FCFO.CGCCFO |  |
| NIF | tomador | E | 0-1 | NIF (Exterior) (Número de Identificação Fiscal (alternativa ao CPF/CNPJ)) | FCFO.NIF |  |
| cNaoNIF | tomador | E | 0-1 | Motivo sem NIF | FCFO.SITUACAONIF | 0 - Não informado na nota de origem 1 - Dispensado do NIF 2 - Não exigência do NIF |
| CAEPF | tomador | E | 0-1 | Cadastro de Atividade Econômica da Pessoa Física | FCFO.CODIGOCAEPF | Cadastro do Cliente Fornecedor | Dados Adicionais | Cadastro de Atividade Econômica da Pessoa Física |
| identificador | tomador | E | 0-20 | Número do Cartão de Identificação Fiscal - NIF ou documento estrangeiro (Passaporte). | Quando for PJ: FCFO.SITUACAONIF  Quando for PF: FCFO.DOCUMENTOESTRANGEIRO | O número identificador NIF é exigido quando o tomador é estrangeiro.  Origem do campo quando PJ: Cadastro do Cliente Fornecedor | Tributos | Número de Identificação Fiscal  Origem do campo quando PF: Cadastro do Cliente Fornecedor | Identificação | Documentos Estrangeiros |
| razao | tomador | E | 1-1 | Razão social do tomador. | FCFO.NOME |  |
| doctomestra | tomador | E | 0-1 | Documento tomador estrangeiro. | FCFO.DOCUMENTOESTRANGEIRO |  |
| tipologr | tomador | E | 0-1 | Tipo de logradouro.  Os valores válidos são:  •  1 – Avenida;  •  2 – Rua;  •  3 – Rodovia;  •  4 – Ruela;  •  5 – Rio;  •  6 – Sítio;  •  7 – Sup. Quadra;  •  8 – Travessa;  •  9 – Vale;  •  10 – Via;  •  11 – Viaduto;  •  12 – Viela;  •  13 – Vila;  •  14 - Vargem. | DTIPORUA.DESCRICAO | Será verificado se DTIPORUA.DESCRICAO coincide com algum item da lista ao lado |
| logradouro | tomador | E | 1-1 | Logradouro do tomador. | FCFO.RUA | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag logradouro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| numend | tomador | E | 1-1 | Número do endereço do tomador. | FCFO.NUMERO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag numend não for informado nesta situação, o mesmo será exibido como SN |
| complend | tomador | E | 0-1 | Complemento do endereço do tomador. | FCFO.COMPLEMENTO |  |
| tipobairro | tomador | E | 0-1 | Tipo de bairro do tomador. (Padrão: “Bairro”) | DTIPOBAIRRO.DESCRICAO | Será verificado se DTIPOBAIRRO.DESCRICAO coincide com algum item da lista ao lado |
| bairro | tomador | E | 1-1 | Bairro do tomador. | FCFO.BAIRRO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag bairro não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| codmunibge | tomador | E | 0-1 | Código do município do tomador, padrão IBGE. |  | Código de Classificação definido para esta município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| codmunsiafi | tomador | E | 0-1 | Código do município do tomador, padrão SIAFI. |  | Código de Classificação definido para esta município conforme a tabela de classificação parametrizada (ex: IBGE, SIAFI) |
| cidade | tomador | E | 1-1 | Município do tomador. | GMUNICIPIO.NOMEMUNICIPIO | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag cidade não for informado nesta situação, o mesmo será exibido como SEM ENDERECO |
| estado | tomador | E | 0-1 | Estado | FCFO.CODETD |  |
| uf | tomador | E | 1-1 | Unidade federativa do tomador. | FCFO.CODETD | A prefeitura de Curitiba permite a emissão de NFS sem os dados do endereço do tomador do serviço. Caso a tag uf não for informado nesta situação, o mesmo será exibido como SU |
| cep | tomador | E | 1-1 | CEP do tomador. | FCFO.CEP |  |
| email | tomador | E | 0-1 | Endereço de e-mail do tomador. | FCFO.EMAIL |  |
| ddd | tomador | E | 0-1 | DDD do telefone do tomador. | FCFO.TELEFONE | Se o telefone preenchido com mais de 9 dígitos Então Será levado os 2 primeiros dígitos como DDD |
| telefone | tomador | E | 0-1 | Telefone do tomador. | FCFO.TELEFONE |  |
| codpais | tomador | E | 0-1 | Código do país do tomador. | DPAIS.CODPAIS | De acordo com a classificação de país informada nos parâmetros |
| nomepais | tomador | E | 0-1 | Nome do país do Tomador. | GPAIS.DESCRICAO |  |
| estrangeiro | tomador | E | 1-1 | Define se o tomador é estrangeiro. 1 – Sim;  2 – Não. | GETD.NACIONAL | Se estado Nacional  Então Sim Senão Não |
| notificatomador | tomador | E | 0-1 | Indicativo para notificar o tomador por e-mail:  1 – Sim;  2 – Não. |  | Fixo Não |
| inscest | tomador | E | 0-1 | Inscrição Estadual. | FCFO.INSCRESTADUAL |  |
| situacaoespecial | tomador | E | 0-1 |  |  | Não será gerado |
| tipopessoa | tomador | E | 0-1 |  | CAMPO CONDICIONAL | Se “Pessoa Física”     Então 2 – Pessoa Física Senão Se “Órgão Publico” <> Não se aplica     Então 4 – Empresa publica Senão Se “Ramo de Atividade” está marcado “Comércio” ou “Indústria”     Então 1 – Comercio/Industria Senão Se “Ramo de Atividade” está marcado “Serviços”     Então 3 – Prestação de Serviço Senão Se “Ramo de Atividade” está marcado “Serviços”     Então 3 – Prestação de Serviço Senão Se “Ramo de Atividade” está marcado “Associação”     Então 5 – Cooperado Senão     Então Null |
| VincNegoc | tomador | E | 0-1 | Vínculo de Negócio. |  | Não será gerado  0 - Sem vínculo com o Tomador Prestador 1 - Controlada 2 - Controladora 3 - Coligada 4 - Matriz  5 - Filial ou sucursal 6 - Outro víncul |

Regras Específicas por MunicípioRE-1left0Rio Grande

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| inscmun | tomador | E | 0-1 | Inscrição municipal do tomador. | FCFOCOMPL.INSCMUNTEMP | Para o Município de Rio Grande (4315602) este campo pode ser preenchido com o código CCM informado pela prefeitura, neste caso, basta criar um campo complementar, no cadastro do cliente fornecedor, com o nome INSCMUNTEMP. |
