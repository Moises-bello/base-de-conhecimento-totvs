---
content_hash: 971a9cf57d5898e60719679cf59d629ef76835d80fb48e426cb670c040d03ff3
fetched_at: '2026-06-29T00:11:16.554120+00:00'
page_id: '673790714'
product: rm
source: tdn-rm
title: NFTS - São Paulo SP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=673790714
version: 45
---

#f5f5f5#363636Nota Fiscal Eletrônica do Tomador/Intermediário de Serviços – NFTS

**DEFINIÇÃO:**

A Nota Fiscal Eletrônica do Tomador/Intermediário de Serviços – NFTS foi instituída pela Lei Nº 15.406, de 8 de julho de 2011, e se destina à declaração dos serviços tomados ou intermediados pelas pessoas jurídicas e pelos condomínios edilícios residenciais ou comerciais por ocasião da contratação de serviços. 

A emissão da Nota Fiscal do Tomador/Intermediário - NFTS (emissão em lote) está integrada ao Sistema da Nota Fiscal de Serviços Eletrônica – NFS-e, permitindo que sejam transferidas informações dos contribuintes para a Prefeitura em arquivos no formato texto. Tais arquivos devem atender a um layout pré-definido, apresentado neste documento.

Ferramenta de Geração da NFTS

Esta rotina encontra-se disponível no [Gerador de Saídas](https://tdn.totvs.com/pages/viewpage.action?pageId=237383341) e para utilizá-la basta baixar seu layout mais recente disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816).

**FISLAY0027 - SaoPaulo\_NFTS**

InformaçõesPara utilização do processo é necessário seguir as parametrizações da FAQ:  [NFS-e - Parametrizar o sistema para emissão de NFS-e](https://tdn.totvs.com/pages/viewpage.action?pageId=66126311) porém utilizando movimento de entrada. #f5f5f5#363636RegistrosSão selecionados os Lançamentos Fiscais de Entrada associado a CFOP do tipo Não Fiscal, que possua pelo menos um item de serviço e o Tributo ISS informado no item. 

Além disso, o campo Chave de Acesso (Pasta Outros Dados) NÃO deve estar preenchido, OU, preenchido quando o Cliente/Fornecedor do Lançamento não for contribuinte do Município de São Paulo.

Para os casos onde não possui retenção do ISS o sistema possui o seguinte comportamento:  
Se o tributo ISS **não for informado**, o lançamento **não será** considerado na rotina;  
Se o tributo ISS **for informado** com valor de ISS **zerado** o lançamento **será** considerado no registro detalhe Tipo 4. No registro Tipo 9, de totalizadores, não será somado valor para este lançamento uma vez que não há valor de ISS para totalizar.

12lefttrue1Registro 1Campos

| REGISTRO | **CAMPOS** | **DESCRIÇÃO** | **ORIGEM DA INFORMAÇÃO** | REGRAS |
| --- | --- | --- | --- | --- |
| Campo - 1 | Tipo de registro | Tipo de Registro | Valor Fixo "1" |  |
| Campo - 2 | Versão do Arquivo | Indica a versão do layout a ser utilizada. Deve ser preenchido com o número da versão atual. A versão atual é a 001. | Gerado conforme informado na tela de Geração da Rotina |  |
| Campo - 3 | Inscrição Municipal do Sujeito Passivo (Tomador ou Intermediário) | Inscrição municipal do Tomador ou Intermediário a que se refere o arquivo. | Campo gerado conforme a Inscrição Municipal informado no cadastro da Filial GFILIAL.INSCMUN |  |
| Campo - 4 | Data de Início do Período Transferido no Arquivo | O arquivo de transferência deverá conter todos os documentos referentes a um período. Informe neste campo a Data INICIAL desse período no formato AAAAMMDD. | Gerado conforme o campo Data de Início informado na tela de Geração da Rotina |  |
| Campo - 5 | Data de Fim do Período Transferido no Arquivo | O arquivo de transferência deverá conter todos os documentos referentes a um período. Informe neste campo a Data FINAL desse período no formato AAAAMMDD. | Gerado conforme o campo Data de Fim informado na tela de Geração da Rotina |  |

true4Registro 4

Registro gerado quando o campo **Emiti Livros de Construção Civil** estiver desabilitado.

03.01 - Identificação da Regras de Apuração

03.01.03 - ISS  - Parâmetros Filial - Construção Civil e Deduções

Campos

| REGISTRO | **CAMPOS** | **DESCRIÇÃO** | **ORIGEM DA INFORMAÇÃO** | REGRAS |
| --- | --- | --- | --- | --- |
| Campo - 1 | TIPO\_REGISTRO | Tipo de Registro | Valor Fixo "4" |  |
| Campo - 2 | TIPO\_DOCTO | Tipo de Documento. Opções: 01 - Dispensa emissão / 02 - Com emissão / 03 - Sem emissão com obrigação. | Gerar com o Modelo ISS informado nos parâmetros modelo de ISS DMODELOISS.MODELOISS |  |
| Campo - 3 | SERIE\_DOCTO | Série do Documento | Gerado conforme a Série do Lançamento Fiscal DLAFSERIEDOC |  |
| Campo - 4 | NUM\_DOCTO | Número do Documento | Gerado conforme o Número do Documento Fiscal informado no Lançamento Fiscal DLAF.DOCINI |  |
| Campo - 5 | DATA\_PREST\_SERV | Data da Prestação dos serviços. | Informação gerada com a Data Entrada/Saída do Lançamento DLAF.DATAES |  |
| Campo - 6 | SITUACAO\_NFTS | Situação da NFTS - Opções: N - Normal / C - Cancelado. | Esse campo será gerado com valor fixo "N" uma vez que não é possível cancelar Lançamento de Entrada |  |
| Campo - 7 | TRIBUT\_SERV | Tributação do serviço - Opções: I - Imune, se não existir o Tributo ISS no Item do Lançamento Fiscal. T - Op. Normal, para demais operações. O Tipo "J - ISS Suspenso" não será gerado.  Nenhum - T  Devido - T  RetidoFonte - T  RetidoFonte\_Deduzido - T  Deposito\_Juizo - T  Isento - T  Imune - I | Tipo de Recolhimento ISS do tributo no item.  DTRBITEM.TIPOTRIBUTACAO | Busca o Tipo de Recolhimento do ISS quando existe ISS no item. Aviso campo\_7\_inicio  Não é considerado Regime de ISS nos dados fiscais da Filial. |
| Campo - 8 | VALOR\_SERV | Valor dos serviços | Será gerado com o Valor da Mercadoria informado no Item do Lançamento Fiscal |  |
| Campo - 9 | VALOR\_DED | Valor das deduções | Será gerado com o valor da dedução informado no Item do Lançamento Fiscal subpasta outros tributos ISS Campo Dedução do Tributo DTRBITEM.DEDUCAOTRB |  |
| Campo - 10 | COD\_SERVICO | Código do serviço prestado | Gerado conforme o código do serviço informado no Lançamento Fiscal subpasta Prestação de Serviço Campo Código de Serviço DLAF.CODIGOSERVICO |  |
| Campo - 11 | COD\_SUBITEM | Código do subitem da lista |  |  |
| Campo - 12 | ALIQUOTA | Alíquota | Gerado com o conforme o item do Lançamento Fiscal subpasta Outros Tributos DTRBLAF.ALIQTRB |  |
| Campo - 13 | ISS\_RETIDO | ISS Retido. Opções: 1 - ISS Retido / 2 - NFTS sem retenção do ISS | Tipo de Recolhimento ISS do tributo no item.  DTRBITEM.TIPOTRIBUTACAO | Se o prestador de serviço for do município de São Paulo e o Tipo Recolhimento for "Retido Fonte" ou "Retido Fonte Deduzido" o **valor será 1**. Caso contrário o **valor será 2**. |
| Campo - 14 | IND\_CPFCNPJ | Indicador de CPF/CNPJ do prestador: 1 - CPF / 2 - CNPJ / 3 - Prestador do exterior | Gerado conforme o Cadastro do Cliente Fornecedor informado no Lançamento Fiscal Campo Categoria FCFOPESSOAFISOUJUR | Se a Categoria  do Cliente Fornecedor for pessoa jurídica, ele recebe 2 - CNPJ.  Se a Categoria do Cliente Fornecedor for Pessoa Física, ele recebe 1 - CPF.  Se o País do Cliente Fornecedor for exterior, ele recebe 3. |
| Campo - 15 | CPF\_CNPJ | CPF ou CNPJ do prestador | Gerado conforme o Cadastro do Cliente Fornecedor informado no Lançamento Fiscal Campo FCFO.CGCCFO |  |
| Campo - 16 | INSCR\_MUN\_PREST | Inscrição Municipal do prestador | Recebe a Inscrição Municipal Gerado conforme a Inscrição Municipal informado no Cadastro do Cliente Fornecedor FCFO.INSCRMUNICIPAL |  |
| Campo - 17 | NOME\_PREST | Nome/Razão Social do prestador | Gerado com Campo Nome do Cadastro do Cliente Fornecedor FCFO.NOME |  |
| Campo - 18 | TIPO\_ENDER | Tipo do endereço do prestador | Gerado com o Campo tipo de rua do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.TIPORUA |  |
| Campo - 19 | ENDERECO | Endereço do prestador | Gerado com o Campo rua do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.RUA |  |
| Campo - 20 | NUMERO | Número do endereço do prestador | Gerado com o Campo numero do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.NUMERO |  |
| Campo - 21 | COMPLEMENTO | Complemento do endereço do prestador | Gerado com o Campo Complemento do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.COMPLEMENTO |  |
| Campo - 22 | BAIRRO | Bairro do prestador | Gerado com o Campo Bairro do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.BAIRRO |  |
| Campo - 23 | CIDADE | Cidade do Prestador | Gerado com o Campo Cidade do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CODMUNICIPIO |  |
| Campo - 24 | UF | UF do Prestador | Gerado com o Campo UF do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CODETD |  |
| Campo - 25 | CEP | CEP do Prestado | Gerado com o Campo CEP do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CEP |  |
| Campo - 26 | E-mail | E-mail do Prestado | Gerado com o Campo E-mail do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CEP |  |
| Campo - 27 | Tipo de NFTS | Tipo de NFTS | Fixo  1 - Nota Fiscal do Tomador; |  |
| Campo - 28 | Regime de Tributação | Regime de Tributação | Gerado com o Campo Porte da Empresa do Cadastro do Cliente Fornecedor subpasta - Tributos FCFO.PORTE | Regime de tributação: 0 – Normal ou Simples Nacional (DAMSP); 4 – Simples Nacional (DAS); 5 – Microempreendedor Individual - MEI |
| Campo - 29 | Data de Pagamento da | Data de Pagamento da Nota | Não Gerado |  |
| Campo - 30 | Discriminação dos Serviços | Discriminação dos Serviços | Gerado com o Campo Descrição do Cadastro do Produto  TPRODUTO.DESCRICAO |  |

true4Registro 4 Construção Civil

Registro gerado quando o campo **Emiti Livros de Construção Civil** estiver habilitado.

03.01 - Identificação da Regras de Apuração

03.01.03 - ISS  - Parâmetros Filial - Construção Civil e Deduções

Campos

| REGISTRO | **CAMPOS** | **DESCRIÇÃO** | **ORIGEM DA INFORMAÇÃO** | REGRAS |
| --- | --- | --- | --- | --- |
| Campo - 1 | TIPO\_REGISTRO | Tipo de Registro | Valor Fixo "4" |  |
| Campo - 2 | TIPO\_DOCTO | Tipo de Documento. Opções: 01 - Dispensa emissão / 02 - Com emissão / 03 - Sem emissão com obrigação. | Gerar com o Modelo ISS informado nos parâmetros modelo de ISS DMODELOISS.MODELOISS |  |
| Campo - 3 | SERIE\_DOCTO | Série do Documento | Gerado conforme a Série do Lançamento Fiscal DLAFSERIEDOC |  |
| Campo - 4 | NUM\_DOCTO | Número do Documento | Gerado conforme o Número do Documento Fiscal informado no Lançamento Fiscal DLAF.DOCINI |  |
| Campo - 5 | DATA\_PREST\_SERV | Data da Prestação dos serviços. | Informação gerada com a Data Entrada/Saída do Lançamento DLAF.DATAES |  |
| Campo - 6 | SITUACAO\_NFTS | Situação da NFTS - Opções: N - Normal / C - Cancelado. | Esse campo será gerado com valor fixo "N" uma vez que não é possível cancelar Lançamento de Entrada |  |
| Campo - 7 | TRIBUT\_SERV | Tributação do serviço - Opções: I - Imune, se não existir o Tributo ISS no Item do Lançamento Fiscal. T - Op. Normal, para demais operações. O Tipo "J - ISS Suspenso" não será gerado.  Nenhum - T  Devido - T  RetidoFonte - T  RetidoFonte\_Deduzido - T  Deposito\_Juizo - T  Isento - T  Imune - I | Tipo de Recolhimento ISS do tributo no item.  DTRBITEM.TIPOTRIBUTACAO | Busca o Tipo de Recolhimento do ISS quando existe ISS no item. Aviso campo\_7\_inicio  Não é considerado Regime de ISS nos dados fiscais da Filial. |
| Campo - 8 | VALOR\_SERV | Valor dos serviços | Será gerado com o Valor da Mercadoria informado no Item do Lançamento Fiscal |  |
| Campo - 9 | VALOR\_DED | Valor das deduções | Será gerado com o valor da dedução informado no Item do Lançamento Fiscal subpasta outros tributos ISS Campo Dedução do Tributo DTRBITEM.DEDUCAOTRB |  |
| Campo - 10 | COD\_SERVICO | Código do serviço prestado | Gerado conforme o código do serviço informado no Lançamento Fiscal subpasta Prestação de Serviço Campo Código de Serviço DLAF.CODIGOSERVICO |  |
| Campo - 11 | COD\_SUBITEM | Código do subitem da lista |  |  |
| Campo - 12 | ALIQUOTA | Alíquota | Gerado com o conforme o item do Lançamento Fiscal subpasta Outros Tributos DTRBLAF.ALIQTRB |  |
| Campo - 13 | ISS\_RETIDO | ISS Retido. Opções: 1 - ISS Retido / 2 - NFTS sem retenção do ISS | Tipo de Recolhimento ISS do tributo no item.  DTRBITEM.TIPOTRIBUTACAO | Se o prestador de serviço for do município de São Paulo e o Tipo Recolhimento for "Retido Fonte" ou "Retido Fonte Deduzido" o **valor será 1**. Caso contrário o **valor será 2**. |
| Campo - 14 | IND\_CPFCNPJ | Indicador de CPF/CNPJ do prestador: 1 - CPF / 2 - CNPJ / 3 - Prestador do exterior | Gerado conforme o Cadastro do Cliente Fornecedor informado no Lançamento Fiscal Campo Categoria FCFOPESSOAFISOUJUR | Se a Categoria  do Cliente Fornecedor for pessoa jurídica, ele recebe 2 - CNPJ.  Se a Categoria do Cliente Fornecedor for Pessoa Física, ele recebe 1 - CPF.  Se o País do Cliente Fornecedor for exterior, ele recebe 3. |
| Campo - 15 | CPF\_CNPJ | CPF ou CNPJ do prestador | Gerado conforme o Cadastro do Cliente Fornecedor informado no Lançamento Fiscal Campo FCFO.CGCCFO |  |
| Campo - 16 | INSCR\_MUN\_PREST | Inscrição Municipal do prestador | Recebe a Inscrição Municipal Gerado conforme a Inscrição Municipal informado no Cadastro do Cliente Fornecedor FCFO.INSCRMUNICIPAL |  |
| Campo - 17 | NOME\_PREST | Nome/Razão Social do prestador | Gerado com Campo Nome do Cadastro do Cliente Fornecedor FCFO.NOME |  |
| Campo - 18 | TIPO\_ENDER | Tipo do endereço do prestador | Gerado com o Campo tipo de rua do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.TIPORUA |  |
| Campo - 19 | ENDERECO | Endereço do prestador | Gerado com o Campo rua do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.RUA |  |
| Campo - 20 | NUMERO | Número do endereço do prestador | Gerado com o Campo numero do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.NUMERO |  |
| Campo - 21 | COMPLEMENTO | Complemento do endereço do prestador | Gerado com o Campo Complemento do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.COMPLEMENTO |  |
| Campo - 22 | BAIRRO | Bairro do prestador | Gerado com o Campo Bairro do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.BAIRRO |  |
| Campo - 23 | CIDADE | Cidade do Prestador | Gerado com o Campo Cidade do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CODMUNICIPIO |  |
| Campo - 24 | UF | UF do Prestador | Gerado com o Campo UF do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CODETD |  |
| Campo - 25 | CEP | CEP do Prestado | Gerado com o Campo CEP do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CEP |  |
| Campo - 26 | E-mail | E-mail do Prestado | Gerado com o Campo E-mail do Cadastro do Cliente Fornecedor subpasta Endereço principal FCFO.CEP |  |
| Campo - 27 | Tipo de NFTS | Tipo de NFTS | Fixo  1 - Nota Fiscal do Tomador; |  |
| Campo - 28 | Regime de Tributação | Regime de Tributação | Gerado com o Campo Porte da Empresa do Cadastro do Cliente Fornecedor subpasta - Tributos FCFO.PORTE | Regime de tributação: 0 – Normal ou Simples Nacional (DAMSP); 4 – Simples Nacional (DAS); 5 – Microempreendedor Individual - MEI |
| Campo - 29 | Data de Pagamento da | Data de Pagamento da Nota | Não Gerado |  |
| Campo - 30 | Cadastro Específico do INSS | Cadastro Específico do INSS | Gerado com o Campo CNPJ do Cadastro do Projeto que foi associado ao Lançamento Fiscal   MPRJ.CGC | Neste campo deve ser informado o CNPJ da Obra ou CEI |
| Campo - 31 | Número de inscrição da obra | Número de inscrição da obra | Gerado com o Campo Complementar, informado no Cadastro do Projeto associado ao Lançamento Fiscal - Sub Pasta Campo Complementar | Criar no Aplicativo Construção - Obra e Projeto um Campo complementar  **"NUMINSCOBRA"** Coluna - **"NUMINSCOBRA"** .  Descrição - Numero Inscrição da Obra  Tipo - Alfanumérico |
| Campo - 32 | Reservado |  |  |  |
| Campo - 33 | Discriminação dos Serviços | Discriminação dos Serviços | Gerado com o Campo Descrição do Cadastro do Produto  TPRODUTO.DESCRICAO |  |

true1Registro 9

Rodapé, contém a quantidade de registros, o somatório de todos os serviços do arquivo e suas deduções.

Campos

| REGISTRO | **CAMPOS** | **DESCRIÇÃO** | **ORIGEM DA INFORMAÇÃO** | REGRAS |
| --- | --- | --- | --- | --- |
| Campo - 1 | Tipo de registro | Tipo de Registro | Valor Fixo "9" |  |
| Campo - 2 | Número de linhas de detalhe do arquivo | Número de linhas de detalhe contidas no arquivo. |  |  |
| Campo - 3 | Valor total dos serviços contido no arquivo | Contém a soma dos valores dos serviços. |  |  |
| Campo - 4 | Valor total das deduções contidas no arquivo | Contém a soma dos valores das deduções |  |  |

Mais Informações

* Baixar o layout mais recente do [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816).
