---
content_hash: d0bb5e638118a0e9d1378f8db7e199859baeea576b473d3593edd38a321675b5
fetched_at: '2026-06-29T00:09:20.037505+00:00'
page_id: '422545637'
product: rm
source: tdn-rm
title: Tipo I - ITEM DE DOCUMENTO FISCAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545637
version: 3
---

O arquivo será composto pelos itens dos Lançamentos Fiscais seguindo as Regras Gerais de seleção dos documentos fiscais.  
 Todos os dados relativos ao contribuinte serão gerados à partir dos dados do Cliente/Fornecedor informados nos Lançamentos Fiscais.  
O campo 14-Código de Classificação do Item, consiste o preenchimento do campo "Código Fiscal" no cadastro do produto em  Anexos | Dados Fiscais por UF.  
O campo 29-Código de Autenticação Digital do registro, obtido através da aplicação do algoritmoMD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de caracteres formada pelos campos 01, 02, 03, 04, 05, 06, 07, 08, 09, 10,11, 12, 13, 14, 15, 16, 17, 18,19, 20, 21, 22, 23, 24, 25, 26, 27 e 28 gerado automaticamente na geração da rotina.  
***Observação***: Para que o campo Código Autenticação Digital Doc. Fiscal seja recalculado sempre que houver alguma alteração no Lançamento Fiscal, o mesmo deve ser limpado(apagado) e posteriormente gerada a rotina novamente.  
     
 **Detalhamento do registro e origem dos dados**

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **ORIGEM DOS DADOS** |
| 1 | CNPJ ou CPF | Informar o CNPJ ou CPF | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 2 | UF | Informar a sigla da UF da localização do consumidor da energia elétrica ou tomador dos serviços de   comunicação/telecomunicação | Informação do cadastro do Cliente\Fornecedor informado no lançamento fiscal |
| 3 | Classe do Consumo ou Tipo de Assinante | Informar o código da classe de consumo da energia elétrica ou tipo de assinante de serviço de   comunicação/telecomunicação | Campo gerado conforme informação do campo classe de consumo informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação |
| 4 | Fase ou Tipo de Utilização | Informar o código do tipo de ligação (Mono/Bi/Trifásico) ou tipo de utilização | Campo gerado conforme informação do campo Tipo de Utilização informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação |
| 5 | Grupo de Tensão | Informar o código do Grupo de Tensão | Campo gerado conforme informação do campo Tipo de Tensão informado no Lançamento Fiscal\Sub Pasta Energia\Comunicação |
| 6 | Data de Emissão | Informar a data de emissão do documento fiscal | Data de Emissão do Lançamento Fiscal no formato AAAAMMDD |
| 7 | Modelo | Informar o modelo do documento fiscal |  |
| 8 | Série | Informar a série do documento fiscal | Serie do Lançamento Fiscal |
| 9 | Número | Informar a data de emissão do documento fiscal | Data de Emissão do Lançamento Fiscal no formato AAAAMMDD |
| 10 | CFOP | Informar o CFOP do item do documento fiscal | Informar a Natureza Fiscal do lançamentos Fiscal |
| 11 | Item | Informar o número de ordem do item do documento fiscal |  |
| 12 | Código do serviço ou fornecimento | Informar o código do fornecimento ou serviço do item utilizado pelo contribuinte |  |
| 13 | Descrição do serviço ou fornecimento | Informar a descrição do fornecimento ou serviço do item |  |
| 14 | Código de classificação do item | Informar o código da classificação do item do documento fiscal | Código terá origem no Cadastro de Produto – Anexo Dados Fiscais por UF – Campo "Código Fiscal", Lembrando que o mesmo deve ser preenchido conforme tabela 11.5 do Manual |
| 15 | Unidade | Informar a unidade de medida da quantidade do fornecimento ou serviço do item | Unidade do Item do lançamento Fiscal |
| 16 | Quantidade contratada (com 3 decimais) | informar a quantidade contratada de fornecimento ou serviço do item | Gerado Conforme informação do Campo Quantidade Contratada informada no Item do Lançamentos Fiscal\Sub Pasta Energia\Comunicação |
| 17 | Quantidade prestada ou fornecida (com 3 decimais) | Informar a quantidade de fornecimento ou serviço do item | Quantidade informada no Item do lançamento Fiscal |
| 18 | Total (com 2 decimais) | Informar o valor total do item | Gerar com o Campo Valor da Mercadoria da Pasta Item do lançamento Fiscal |
| 19 | Desconto (com 2 decimais) | Informar o valor do desconto concedido no item | Gerar com o valor do  campo de Desconto da Pasta de Item do Lançamento Fiscal |
| 20 | Acréscimos e Despesas Acessórias (com 2 decimais) | Informar o valor dos acréscimos e outras despesas acessórias do item | Gerar com o Valor do Campo de Acréscimo da Pasta Item do Lançamento Fiscal |
| 21 | BC ICMS (com 2 decimais) | Informar a Base de Cálculo do ICMS do item | Gerar com o valor do campo Base de Calculo do ICMS da Sub Pasta valores de ICMS do Item do Lançamento |
| 22 | ICMS (com 2 decimais) | informar o valor do ICMS destacado no item, | Gerar  com  o valor do ICMS informado na Sub Pata Valores do ICMS do Item do Lançamento Fiscal |
| 23 | Operações Isentas ou não tributadas (com 2 decimais) | Informar o valor de fornecimento ou serviço isento ou não tributados pelo ICMS, | Gerar com Valor de Isenta da Sub Pasta Valores de ICMS do Item do Lançamento Fiscal. |
| 24 | Outros valores que não compõe a BC do ICMS (com 2decimais) | Informar os outros valores do item que não compõe a Base de Cálculo do ICMS, | Campo gerado com o valores de Outros da Sub Pasta Valores de ICMS do Item do Lançamento Fiscal. |
| 25 | Alíquota do ICMS (com 2 decimais) | Informar a alíquota do ICMS do item | Campo gerado conforme informação da Alíquota do ICMS do Lançamento Fiscal |
| 26 | Situação | Informar a situação do item de fornecimento de energia elétrica ou de prestação de serviços de comunicação/ telecomunicação |  |
| 27 | Ano e Mês de referência de apuração | Informar o mês e ano de referência de apuração do documento fiscal, utilizando o formato "AAMM" | Gerar somente o Mês e Ano, conforme a Data de Emissão do Lançamento Fiscal no formato AAMM |
| 28 | Brancos - reservado para uso futuro | Brancos, reservado para uso futuro |  |
| 29 | Código de Autenticação Digital do registro | Informar o código de autenticação digital obtido através da aplicação do algoritmoMD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de caracteres formada pelos campos 01, 02, 03, 04, 05, 06, 07, 08, 09, 10,11, 12, 13, 14, 15, 16, 17, 18,19, 20, 21, 22, 23, 24, 25, 26, 27 e 28. | Esse campo será preenchido pela rotina fiscal. |
