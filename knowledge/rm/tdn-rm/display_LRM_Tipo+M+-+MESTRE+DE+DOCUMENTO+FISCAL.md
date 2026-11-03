---
content_hash: 6f6452e1a0d2a816f1e417273cdefdcdef903a9b3bac1b6eb9cb9724f2450643
fetched_at: '2026-06-29T00:09:22.793647+00:00'
page_id: '422546029'
product: rm
source: tdn-rm
title: Tipo M - MESTRE DE DOCUMENTO FISCAL
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipo+M+-+MESTRE+DE+DOCUMENTO+FISCAL
version: 10
---

#f5f5f5#363636Visão Geral

O arquivo Tipo M é composto pelos dados dos Lançamentos Fiscais, que são classificados pelo número do documento fiscal.  
As informações referentes ao contribuinte serão geradas à partir dos dados cadastrais do cliente/fornecedor selecionado no Lançamento Fiscal.

Modelos de Documento que serão gerados na Rotina: 6, 21 e 22

#f5f5f5#363636Informações sobre os campos

O campo 13 - "Código de Autenticação Digital Documento Fiscal", será obtido através da aplicação do algoritmo MD5 de 128 bits, na cadeia de caracteres formada pelos campos 01, 12, 14, 15 e 16:

* 01 – CNPJ ou CPF;
* 12 -  Número do Documento Fiscal;
* 14 -  Valor Total do Documento Fiscal;
* 15 – Base de Cálculo do ICMS destacado no Documento Fiscal;
* 16 -  Valor do ICMS destacado no Documento Fiscal.

Observação

Este campo apenas é calculado automaticamente na geração da rotina quando selecionados valores nos campos "Classe de Consumo", "Tipo Assinante" e "Conta de Consumo do Lançamento Fiscal". Após ser calculado, ele pode ser visualizado na pasta "Energia/Comunicação" do Lançamento Fiscal. Isso só se aplica para lançamentos criados ou editados após a implementação da rotina.

O campo 24 - Código de Autenticação Digital também é obtido através da aplicação do algoritmo MD5 de 128 bits, na cadeia de caracteres formada pelos campos 01 a 23, gerado pela rotina.

#f5f5f5#363636Detalhamento do registro e origem das informações 

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem dos Dados** |
| 1 | CNPJ ou CPF | Informar o CNPJ ou CPF | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 2 | IE | Informar a Inscrição Estadual | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 3 | Razão Social | Informar a razão social, denominação ou nome | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 4 | UF | Informar a sigla da UF da localização do consumidor. | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 5 | Classe de Consumo ou Tipo de Assinante | Informar o código da classe de consumo da energia elétrica ou tipo de assinante de serviço de comunicação/telecomunicação | Campo gerado conforme informação do campo Classe de Consumo informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação - Gerado apenas para o Modelo 06 |
| 6 | Fase ou Tipo de Utilização | Informar o código do tipo de ligação (Mono/Bi/Trifásico) ou tipo de utilização | Campo gerado conforme informação do campo Tipo de Utilização informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação |
| 7 | Grupo de Tensão | Informar o código do Grupo de Tensão | Campo gerado conforme informação do campo Tipo de Tensão informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação |
| 8 | Código de Identificação do consumidor ou assinante | Informar o código de identificação do consumidor ou assinante | Informação do cadastro do Cliente/Fornecedor informado no Lançamento |
| 9 | Data de emissão | Informar a data de emissão do documento fiscal | Data de Emissão do Lançamento Fiscal no formato AAAAMMDD |
| 10 | Modelo | Informar o modelo do documento fiscal |  |
| 11 | Série | Informar a série do documento fiscal | Serie do Lançamento Fiscal – utilizar a letra "U" para indicar série única |
| 12 | Número | Informar o número sequencial atribuído pelo sistema eletrônico de processamento de dados ao documento fiscal |  |
| 13 | Código de Autenticação Digital documento fiscal | Informar o código de autenticação digital obtido através da aplicação do algoritmoMD5 (Message Digest 5, vide item  11.7) de 128 bits na cadeia de caracteres formada pelos campos 01, 12, 14, 15 e 16, respeitando o tamanho previsto do campo, assim como os brancos e zeros de preenchimento. | Gerado com a informação do campo CODAUTENTDIGITALDOC, informado no lançamento fiscal\sub pasta Energia\Comunicação  Observação.: Na tela de geração existe a opção de recalcular este campo, porem a mesma só será realizada para os Lançamentos onde o mesmo não esteja preenchido (Lançamentos antigos).     Caso seja alterado algum valor que componha este campo o mesmo deve ser recalculado no Lançamento Fiscal (Este só e calculado quando não esta preenchido). |
| 14 | Valor Total (com 2 decimais) | Informar o Valor Total do documento fiscal | Valor Contábil do Laçamento Fiscal |
| 15 | BC ICMS (com 2 decimais) | Informar a Base de Cálculo do ICMS destacado no documento fiscal | Base de Calculo do Lançamento Fiscal |
| 16 | ICMS destacado (com 2 decimais) | Informar o valor do ICMS destacado no documento fiscal | Valor do ICMS do Lançamento Fiscal |
| 17 | Operações Isentas ou não tributadas (com 2 decimais) | nformar o valor das operações ou serviços isentos ou não tributados pelo ICMS | Valor do Campo Isento do lançamento Fisal |
| 18 | Outros valores (com 2 decimais) | Informar os outros valores constantes do documento fiscal, com 2 decimais | Valor do Campo de Outros do Lançamento Fiscal |
| 19 | Situação do documento | Informar a situação do documento |  |
| 20 | Ano e Mês de referência de apuração | Informar o ano e mês de referência de apuração do ICMS do documento fiscal | Informar o Ano e Mês conforme a Data de Emissão do Lançamento Fiscal |
| 21 | Referência ao item da NF |  | Referencia física do primeiro item do Lançamento Fiscal no arquivo de Itens |
| 22 | Número do terminal telefônico ou Número da conta de consumo | Informar a localidade de registro e o número do terminal/aparelho telefônico no formato "LLNNNNNNNN", onde "LL" é  o código da localidade e "NNNNNNNN", o número de identificação do terminal/aparelho telefônico | Campo gerado conforme informação do lançamento Fiscal > Energia\ Comunicação > Numero da Conta de Consumo |
| 23 | Indicação do tipo de informação contida no campo 1 | Preenchendo com o dígito “1” se o conteúdo for um CNPJ ou com o dígito “2” se o conteúdo for um CPF. No caso de pessoa jurídica não obrigada à inscrição no CNPJ, preencher com o dígito “3”; se for pessoa física não obrigada ao CPF, preencher com o dígito “4”; | Gerado conforme o Cadastro do Cliente\Fornecedor informado no Lançamento Fiscal |
| 24 | Tipo de cliente | Em se tratando de nota fiscal modelo 6, informar o tipo de cliente, conforme a tabela 11.7.1. Em se tratando de Nota Fiscal de Serviço de Comunicação, modelo 21, ou Nota Fiscal de Serviço de Telecomunicação, modelo 22, informar o tipo de cliente, conforme a tabela 11.7.2. | Esse campo será preenchido pela rotina fiscal. |
| 25 | Subclasse de consumo | Em se tratando de nota fiscal modelo 6, informar a subclasse de consumo, conforme a tabela 11.8. Em se tratando de Nota Fiscal de Serviço de Comunicação, modelo 21, ou Nota Fiscal de Serviço de Telecomunicação, modelo 22, preencher com zeros. | Campo gerado conforme informação do lançamento Fiscal > Energia\ Comunicação > SubClasse de Cosnsumo |
| 26 | Número do terminal telefônico principal | Em se tratando de plano de prestação de serviço telefônico corporativo, familiar ou similares, informar o número do terminal telefônico principal do plano. Informar a localidade de registro e o número no formato “LLNNNNNNNN” |  |
| 27 | CNPJ do emitente |  |  |
| 28 | Número ou código da fatura comercial | Informar o número ou o código da fatura comercial, atribuído pelo sistema de faturamento do emitente. | Campo gerado conforme informação do lançamento Fiscal > Energia\ Comunicação > Numero Fatura Comercial |
| 29 | Valor total da fatura comercial | Valor total da fatura comercial, com duas casas decimais | Campo gerado conforme informação do lançamento Fiscal > Energia\ Comunicação > Valor Fatura Comercial |
| 30 | Data de leitura anterior | Em se tratando de nota fiscal modelo 6, informar a data da leitura anterior, no formato AAAAMMDD. Em se tratando de Nota Fiscal de Serviço de Comunicação, modelo 21, ou Nota Fiscal de Serviço de Telecomunicação, modelo 22, informar a data de início da prestação (ou do período mensal, no caso de prestação continuada) do serviço de comunicação/telecomunicação; no caso de prestações pré-pagas de serviços de comunicação/telecomunicação disponibilizados por meios físicos ou eletrônicos, em suas diversas modalidades, informar a data em que o crédito foi disponibilizado ao usuário. Nos demais casos, preencher com zeros;. | Campo gerado conforme informação do lançamento Fiscal >Sub pasta Energia/Comunicação > Data Leitura Anterior/Data Início Prestação |
| 31 | Data de leitura atual | Em se tratando de nota fiscal modelo 6, informar a data de leitura atual, no formato AAAAMMDD. Em se tratando de Nota Fiscal de Serviço de Comunicação, modelo 21, ou Nota Fiscal de Serviço de Telecomunicação, modelo 22, informar a data de término da prestação (ou do período mensal, no caso de prestação continuada) do serviço de comunicação/ telecomunicação; no caso de prestações pré-pagas de serviços de comunicação/telecomunicação disponibilizados por meios físicos ou eletrônicos, em suas diversas modalidades, informar a data em que o crédito foi disponibilizado ao usuário. Nos demais casos, preencher com zeros. | Campo gerado conforme informação do lançamento Fiscal >Sub pasta Energia/Comunicação > Data Leitura/Data Término Prestação |
| 32 | Brancos - reservado para uso futuro | Campo reservado para uso futuro. Preencher com espaços em branco |  |
| 33 | Brancos - reservado para uso futuro | Campo reservado para uso futuro. Preencher com espaços em branco |  |
| 34 | Informações adicionais |  |  |
| 35 | Brancos - reservado para uso futuro | Campo reservado para uso futuro. Preencher com espaços em branco |  |
| 36 | Código de Autenticação Digital do registro | Informar o código de autenticação digital obtido através da aplicação do algoritmoMD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de caracteres formada pelos campos 01 a 23 | Esse campo será preenchido pela rotina fiscal. |
