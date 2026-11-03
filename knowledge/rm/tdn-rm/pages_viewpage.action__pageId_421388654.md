---
content_hash: 36509e71711b14d4f363f609fed19fbfc21f4edb878f5f6fc3d6648d282bd5a6
fetched_at: '2026-06-29T00:09:18.036096+00:00'
page_id: '421388654'
product: rm
source: tdn-rm
title: Exportação e importação de Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388654
version: 52
---

# Conteúdo:

Conteúdo:

# 1. Sobre

Nesta página, encontram-se as informações sobre o layout de importação e exportação de Clientes e Fornecedores no TOTVS RM, com a descrição da estrutura dos registros e das regras para o correto preenchimento dos dados. A importação pode ser realizada por meio de arquivos nos formatos TXT (com campos de posição fixa) ou XML, utilizando codificações ANSI ou UTF-8, conforme os padrões estabelecidos na documentação.

# 2. Exportação

A exportação de registros de Clientes e Fornecedores no TOTVS RM é realizada exclusivamente no formato XML, utilizando uma estrutura compatível com olayout de referência adotado na importação. O processo permite gerar tanto o **arquivo XML de dados** quanto o **arquivo XSD (schema)** correspondente, garantindo a conformidade do conteúdo com a estrutura esperada pelo sistema.

**Passo a passo exportação .XSD**

1. Selecionar, na tela principal de clientes/fornecedores, os registros a serem exportados.
2. Acessar: Processos > Exportação XML de Clientes/Fornecedores.
3. Através do botão de LOOKUP informar um diretório, um nome para o arquivo a ser gerado e escolher a extensão .XSD que representa um SCHEMA XML.
4. Executar o processo de exportação de SCHEMA XML de Clientes/Fornecedores através do botão GERAR SCHEMA XML.
5. Será exibida uma mensagem dizendo "Arquivo de Schema Exportado com Sucesso". Confirme a mensagem.

**Passo a passo exportação .XML**

1. Selecionar, na tela principal de clientes/fornecedores, os registros a serem exportados.
2. Acessar: Processos > Exportação XML de Clientes/Fornecedores.
3. Através do botão de LOOKUP informar um diretório, um nome para o arquivo a ser gerado e escolher a extensão .XML.
4. Executar o processo de exportação de XML de Clientes/Fornecedores através do botão GERAR arquivo .XML.
5. Será exibida uma mensagem dizendo "Arquivo de Schema Exportado com Sucesso". Confirme a mensagem.

Exemplo de arquio .XML

<?xml version="1.0" standalone="yes"?>  
<FinCFOImportacao xmlns="<http://tempuri.org/FinCFOImportacao.xsd>">  
  <FCFO>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCFO>E00001</CODCFO>  
    <NOMEFANTASIA>CLIENTE/FORNECEDOR</NOMEFANTASIA>  
    <NOME>CLIENTE/FORNECEDOR LTDA</NOME>  
    <CGCCFO>333.333.333-33</CGCCFO>  
    <PAGREC>3</PAGREC>  
    <RUA>RUA DO CLIENTE/FORNECEDOR</RUA>  
    <NUMERO>10</NUMERO>  
    <BAIRRO>BAIRRO DO CLIENTE/FORNECEDOR</BAIRRO>  
    <CIDADE>Belo Horizonte</CIDADE>  
    <CODETD>MG</CODETD>  
    <CEP>30570590</CEP>  
    <TELEFONE>33333333</TELEFONE>  
    <CIDADEPGTO>Belo Horizonte</CIDADEPGTO>  
    <CIDADEENTREGA>Belo Horizonte</CIDADEENTREGA>  
    <TELEX>33333333</TELEX>  
    <EMAIL>email@[email.com.br](http://email.com.br)</EMAIL>  
    <CODTCF>000004</CODTCF>  
    <ATIVO>1</ATIVO>  
    <LIMITECREDITO>0</LIMITECREDITO>  
    <VALOROP1>0</VALOROP1>  
    <VALOROP2>0</VALOROP2>  
    <VALOROP3>0</VALOROP3>  
    <PATRIMONIO>0</PATRIMONIO>  
    <NUMFUNCIONARIOS>0</NUMFUNCIONARIOS>  
    <CODCOLTCF>0</CODCOLTCF>  
    <CODMUNICIPIO>06200</CODMUNICIPIO>  
    <PESSOAFISOUJUR>F</PESSOAFISOUJUR>  
    <PAIS>Brasil</PAIS>  
    <PAISPAGTO>Brasil</PAISPAGTO>  
    <PAISENTREGA>Brasil</PAISENTREGA>  
    <CONTRIBUINTE>0</CONTRIBUINTE>  
    <CFOIMOB>0</CFOIMOB>  
    <VALFRETE>0</VALFRETE>  
    <TPTOMADOR>0</TPTOMADOR>  
    <CONTRIBUINTEISS>0</CONTRIBUINTEISS>  
    <NUMDEPENDENTES>0</NUMDEPENDENTES>  
    <ORGAOPUBLICO>0</ORGAOPUBLICO>  
    <VROUTRASDEDUCOESIRRF>0</VROUTRASDEDUCOESIRRF>  
    <OPTANTEPELOSIMPLES>0</OPTANTEPELOSIMPLES>  
    <TIPORUA>1</TIPORUA>  
    <TIPOBAIRRO>1</TIPOBAIRRO>  
    <REGIMEISS>N</REGIMEISS>  
    <RETENCAOISS>0</RETENCAOISS>  
    <RAMOATIV>0</RAMOATIV>  
    <IDPAIS>1</IDPAIS>  
    <NACIONALIDADE>0</NACIONALIDADE>  
    <TIPORUAPGTO>1</TIPORUAPGTO>  
    <TIPOBAIRROPGTO>1</TIPOBAIRROPGTO>  
    <TIPORUAENTREGA>1</TIPORUAENTREGA>  
    <TIPOBAIRROENTREGA>1</TIPOBAIRROENTREGA>  
  </FCFO>  
  <FCFOCOMPL>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCFO>E00001</CODCFO>  
  </FCFOCOMPL>  
  <FDADOSPGTO>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCOLCFO>1</CODCOLCFO>  
    <CODCFO>E00001</CODCFO>  
    <IDPGTO>-1</IDPGTO>  
    <DESCRICAO>BANCO XXX</DESCRICAO>  
    <FORMAPAGAMENTO>Z</FORMAPAGAMENTO>  
    <NUMEROBANCO>999</NUMEROBANCO>  
    <CODIGOAGENCIA>9999</CODIGOAGENCIA>  
    <DIGITOAGENCIA></DIGITOAGENCIA>  
    <CONTACORRENTE>99999999</CONTACORRENTE>  
    <DIGITOCONTA>9</DIGITOCONTA>  
    <CAMARACOMPENSACAO>1</CAMARACOMPENSACAO>  
    <TIPOCONTA>1</TIPOCONTA>  
    <TIPODOC>D</TIPODOC>  
    <FAVORECIDO>JOAO SLVA</FAVORECIDO>  
    <CODFILIAL>1</CODFILIAL>  
    <CGCFAVORECIDO>00000000000</CGCFAVORECIDO>  
  </FDADOSPGTO>  
  <FDADOSPGTODEF>  
    <IDPGTODEF>1</IDPGTODEF>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCOLCFO>1</CODCOLCFO>  
    <CODCFO>E00001</CODCFO>  
    <CODFILIAL>1</CODFILIAL>  
    <PAGREC>2</PAGREC>  
    <IDPGTO>-1</IDPGTO>  
  </FDADOSPGTODEF>  
</FinCFOImportacao>

**Observação**A partir da aplicação dos respectivos patches, os campos 'TIPOPIX' e 'CHAVE' passaram a ser devidamente tratados nos processos de exportação e importação:

* 12.1.2502.173
* 12.1.2506.117

# 3. Importação

Estão disponíveis diferentes opções de importação, que podem ser selecionadas de acordo com a necessidade e o modelo de importação a ser utilizado. Segue as três opções: 

**Atualiza os dados do Cliente/Fornecedor, quando o Código já estiver cadastrado**

A atualização de dados cadastrais pode ser realizada por meio da importação de arquivos que utilizem um código já existente no sistema. Nessa modalidade, as informações fornecidas no arquivo substituem os dados atualmente registrados no cadastro principal do cliente ou fornecedor. Essa opção deve ser utilizada sempre que for necessário atualizar ou complementar informações já existentes, como endereço, razão social, contatos principais, entre outros.

É importante observar que não é permitida a importação de um novo cliente ou fornecedor utilizando um código já cadastrado, a menos que a funcionalidade de atualização esteja explicitamente ativada.

No caso de tabelas filhas — como contatos, números de CEI ou redes sociais — os registros existentes não são substituídos automaticamente durante o processo de importação, justamente para evitar a perda de dados previamente cadastrados.

**Utilizar Código Reduzido para Contas Contábeis**

Ao habilitar esta opção, é possível informar o Código Reduzido das contas contábeis no processo de importação das informações de Contabilização Default dos cadastros de Cliente/Fornecedor, em substituição ao Código completo da conta contábil.

A informação deve ser posicionada entre as posições 347 a 386 da linha T do arquivo de importação.

Exemplo:

Conta contábil cadastrada no sistema:

* Código: 1.1.1.1.001
* Código Reduzido: 55
* Descrição: Caixa

Importação utilizando o Código completo:

* Posição 347 a 386 = `1.1.1.1.001`

Importação utilizando o Código Reduzido:

* Posição 347 a 386 = `55`

**Utilizar CNPJ/CEI/CPF ao invés de código de Cliente/Fornecedor**

Essa funcionalidade permite que a importação de registros de Cliente/Fornecedor seja realizada utilizando o CNPJ, CEI ou CPF como identificador principal, em vez do código interno do cliente/fornecedor (campo correspondente às posições 007 a 031 da linha C no arquivo de importação).

A opção estará disponível quando os seguintes parâmetros estiverem configurados nos Parâmetros Gerais do Cliente/Fornecedor:

* Usar código sequencial
* Máscara do Código (deve ser numérica)
* CPF Único
* CNPJ Único

Com essa configuração ativa, o sistema aceitará que os campos de identificação do cliente/fornecedor no arquivo de importação sejam preenchidos com o número de CNPJ, CEI ou CPF, nos formatos com ou sem pontuação.

Exemplo:

* CPF do Cliente/Fornecedor: `000.000.000-00`
* Preenchimento válido no arquivo (posições 007 a 031 da linha C):

  + `000.000.000-00` ou `00000000000`

## 3.1. Tipo de importação

Abaixo segue as regras para realizar a importação de acordo com o tipo de arquivo:

tipos\_arquivosImportação arquivo .TXT

**Estrutura do Arquivo TXT para Importação de Cliente/Fornecedor**

Para que a inclusão ou atualização de registros de Clientes e Fornecedores ocorra corretamente, é necessário gerar um arquivo com extensão `.TXT`. O arquivo deve ser composto por linhas sequenciais, em que cada linha representa um bloco específico de informações do cadastro, a estrutura deve respeitar a seguinte ordem:

| Ordem em linha | Descrição | Conteúdo principal | Prefixo da linha |
| --- | --- | --- | --- |
| 1 | [Dados do Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados--1226054438) | Identificação do Cliente/Fornecedor, Endereço principal, Endereço de pagamento, Endereço de entrega, Parâmetros do cadastro, Dados opcionais | Linha tipo "C" |
| 2 | [Campos complementares](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados--1226054438) | Informações adicionais específicas do Cliente/Fornecedor. | Linha tipo "M" |
| 3 | [Dados Defaults](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados--1089622957) | Informações sobre os Dados Defaults | Linha tipo "D" |
| 4 | [Defaults contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados-160674559) | Informações sobre dados da conta contábil | Linha tipo "T" |
| 5 | Linha subsequente com informações respectivo rateio gerencial | Linha tipo "R" |
| 6 | [Dados Contatos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados-380687518) | Informações do contato com uma linha para cada contato cadastrado | Linha tipo "O" |
| 7 | Linha seguinte com os campos complementares do contato (se houver) | Linha tipo "L" |
| 8 | [Dados bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados--1586929450) | Informações com os dados bancários com uma linha para cada conta bancária associada ao cadastro | Linha tipo "P" |
| 9 | [Dados da CEI](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados-742174226) | Informações sobre o CEI do Cliente/Fornecedor | Linha tipo "E" |
| 10 | [Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados-1563551098) | Informações sobre o tributo com uma linha para cada tributo relacionado ao Cliente/Fornecedor | Linha tipo "B" |
| 11 | [Inscrição Estadual ST](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados-839445820) | Uma linha contendo a informação da inscrição estadual de substituição tributária, se aplicável | Linha tipo "I" |
| 12 | [Redes Sociais](https://tdn.totvs.com/pages/viewpage.action?pageId=421388654#dados--2141114349) | Informações sobre as redes sociais do Cliente/Fornecedor | Linha tipo "S" |

**Observações**

* Quando o arquivo possuir mais de um Cliente/Fornecedor, esse conjunto de linhas deverá existir para cada um, ou seja, devem constar todas as linhas para um cliente/fornecedor e logo após a última linha começam as linhas para o próximo cliente/fornecedor.
* Quando o cliente/fornecedor está inativo não será possível atualizar o mesmo através da importação, será emitida uma mensagem de erro de chave primária pois o sistema entende que a operação é de inclusão e não de alteração.
* Para Campos Complementares na linha **M,** a data deve estar no formato DD/MM/AAAA.
* O separador dos campos que possuem casas decimais pode ser um ponto (.) ou uma vírgula (,).
* Para qualquer campo nulo, mesmo sendo Numérico ou Valor Financeiro, deverá ser preenchido com espaços.

**Importante**

Não deixe linhas em branco no arquivo

## 3.2. Legenda dos layout dos dados

50%

**Formato dos campos nos layout:**

* **F** = Fixo, identificador da linha.
* **N** = Campo numérico, alinhado à direita com zeros à esquerda.
* **A** = Campo alfanumérico, alinhado à esquerda com espaços à direita.
* **VF** = Valor Financeiro, campo numérico, alinhado à direita com zeros à esquerda e com um ponto (.) ou vírgula (,) como separador decimal.
* **Data** = Campo alfanumérico, no formato DD/MM/AAAA ou DDMMAAAA.
* **NU** = Não Utilizado, preencher com espaços.
50%

**Descrição dos títulos do layout:**

* **Tam.** = Tamanho do Campo
* **Form.** = Formato do Campo
* **Nº Dec.** = Número de decimais
* **Obs.** = Observação

## 3.3. Layout dos dados de cada linha

Abaixo segue as informações sobre o preenchimento de cada linha de acordo com a sua posição, tamanho e obrigatoriedade:

**Dica:** Para visualizar rapidamente as informações de uma nota sem precisar acessá-la diretamente pelo menu, basta **posicionar o cursor sobre a nota desejada**. Ao fazer isso, um resumo com os principais dados será exibido automaticamente na tela, facilitando a consulta rápida, conforme ilustrado na imagem abaixo.

dadosCliente/Fornecedor

**Linha de Dados dos Clientes/Fornecedores**

| Posição | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra C |
| 002 | 006 | 005 | N |  | Coligada | X |  |
| 007 | 031 | 025 | A |  | Código de Cliente/Fornecedor | X | Kein IconSpaceBeforeTooltipNota 12INLINE **Nota 12:**  Caso seja escolhida a importação utilizando CNPJ/CEI/CPF, na posição onde deveria estar o Código do Cli/For, deve estar o CNPJ/CEI/CPF. Lembrar que está opção de importação só estará disponível quando o parâmetro usar código sequencial para código de Cli/For estiver marcado e a mascará do Cli/For for numérica. |
| 032 | 091 | 060 | A |  | Nome Fantasia | X |  |
| 092 | 151 | 060 | A |  | Nome |  |  |
| 152 | 171 | 020 | A |  | CNPJ/CPF |  |  |
| 172 | 191 | 020 | A |  | Inscrição Estadual |  |  |
| 192 | 196 | 005 | N |  | Cliente ou Fornecedor | X | No IconNota 4INLINE **Nota 4:**   |  |  | | --- | --- | | 1 | Cliente | | 2 | Fornecedor | | 3 | Cliente e Fornecedor | |
| 197 | 236 | 040 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 237 | 244 | 008 | A |  | Número |  |  |
| 245 | 264 | 020 | A |  | Complemento |  |  |
| 265 | 284 | 020 | A |  | Não Utilizado (Espaços) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros(posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 285 | 316 | 032 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 20INLINE **Nota 20:** Para o país Brasil, o nome da "Cidade" que era informado na posição 285 a 316 passa a ser informado de acordo com a informação do campo "Código do Município", posição 1598 a 1617. Informando o "código do município" (cidade) o nome do município é incluído automaticamente. Para país estrangeiro usar as posições de 285 a 316. |
| 317 | 318 | 002 | A |  | Estado |  |  |
| 319 | 327 | 009 | A |  | CEP |  |  |
| 328 | 342 | 015 | A |  | Telefone |  |  |
| 343 | 382 | 040 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 383 | 390 | 008 | A |  | Número de Pagamento |  |  |
| 391 | 410 | 020 | A |  | Complemento de Pagamento |  |  |
| 411 | 430 | 020 | A |  | Não Utilizado (Espaços) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros(posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 431 | 462 | 032 | A |  | Cidade de Pagamento |  |  |
| 463 | 464 | 002 | A |  | Estado de Pagamento |  |  |
| 465 | 473 | 009 | A |  | CEP de Pagamento |  |  |
| 474 | 488 | 015 | A |  | Telefone de Pagamento |  |  |
| 489 | 528 | 040 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 529 | 536 | 008 | A |  | Número de Entrega |  |  |
| 537 | 556 | 020 | A |  | Complemento de Entrega |  |  |
| 557 | 576 | 020 | A |  | Não Utilizado (Espaços) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros (posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 577 | 608 | 032 | A |  | Cidade de Entrega |  |  |
| 609 | 610 | 002 | A |  | Estado de Entrega |  |  |
| 611 | 619 | 009 | A |  | CEP de Entrega |  |  |
| 620 | 634 | 015 | A |  | Telefone de Entrega |  |  |
| 635 | 649 | 015 | A |  | Fax |  |  |
| 650 | 664 | 015 | A |  | Celular |  |  |
| 665 | 724 | 060 | A |  | E-Mail |  |  |
| 725 | 764 | 040 | A |  | Contato |  |  |
| 765 | 789 | 025 | A |  | Tipo de Cliente/Fornecedor |  | Kein IconNota 21INLINE **Nota 21:** É possível controlar os cadastros dos clientes/fornecedores agrupando-os por "tipos", ou seja, "Serviços", "Comércio", "Agroindústria" e etc. Para isso, o sistema oferece um cadastro com o nome de "Tipos de Cliente/Fornecedor", neste cadastro é possível incluir vários registros para definirem diversos tipos de cliente/fornecedor.  Nesta posição você deve informar o "Código" do tipo deste cliente/fornecedor. |
| 790 | 794 | 005 | N |  | Ativo |  | Kein IconNota 13INLINE **Nota 13:**   |  |  | | --- | --- | | 00000 | Não | | 00001 | Sim | |
| 795 | 804 | 010 | VF | 02 | Limite de Crédito |  |  |
| 805 | 814 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 815 | 824 | 010 | VF | 02 | Valor do Último Lançamento |  |  |
| 825 | 829 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 830 | 839 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 840 | 849 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 850 | 859 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 860 | 869 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 870 | 879 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 880 | 919 | 040 | A |  | Campo Livre |  |  |
| 920 | 959 | 040 | A |  | Campo Alfa 1 |  |  |
| 960 | 999 | 040 | A |  | Campo Alfa 2 |  |  |
| 1000 | 1039 | 040 | A |  | Campo Alfa 3 |  |  |
| 1040 | 1049 | 010 | VF | 02 | Valor Opcional 1 |  |  |
| 1050 | 1059 | 010 | VF | 02 | Valor Opcional 2 |  |  |
| 1060 | 1069 | 010 | VF | 02 | Valor Opcional 3 |  |  |
| 1070 | 1079 | 010 | Data |  | Data Opcional 1 |  |  |
| 1080 | 1089 | 010 | Data |  | Data Opcional 2 |  |  |
| 1090 | 1099 | 010 | Data |  | Data Opcional 3 |  |  |
| 1100 | 1114 | 015 | NU |  | Não Utilizado (Espaços) |  |  |
| 1115 | 1115 | 001 | NU |  | Não Utilizado (Espaços) |  |  |
| 1116 | 1125 | 010 | Data |  | Data de Início das Atividades |  |  |
| 1126 | 1135 | 010 | VF | 02 | Patrimônio |  |  |
| 1136 | 1145 | 010 | N |  | Número de Funcionários |  |  |
| 1146 | 1239 | 94 | NU |  | Não Utilizado (Espaços) |  |  |
| 1240 | 1244 | 005 | N |  | Coligada do Tipo de Cliente/Fornecedor |  |  |
| 1245 | 1249 | 005 | N |  | Fax Dedicado |  |  |
| 1250 | 1254 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 1255 | 1274 | 020 | A |  | Inscrição Municipal |  |  |
| 1275 | 1275 | 001 | A |  | Pessoa Física ou Jurídica |  | Kein IconNota 7INLINE **Nota 7:**   |  |  | | --- | --- | | F | Pessoa Física | | J | Pessoa Jurídica | |
| 1276 | 1315 | 040 | A |  | Contato de Pagamento |  |  |
| 1316 | 1355 | 040 | A |  | Contato de Entrega |  |  |
| 1356 | 1375 | 020 | A |  | País |  |  |
| 1376 | 1395 | 020 | A |  | País de Pagamento |  |  |
| 1396 | 1415 | 020 | A |  | País de Entrega |  |  |
| 1416 | 1430 | 015 | A |  | Fax do Endereço de Entrega |  |  |
| 1431 | 1490 | 060 | A |  | E-Mail do Endereço de Entrega |  |  |
| 1491 | 1505 | 015 | A |  | Fax do Endereço de Pagamento |  |  |
| 1506 | 1565 | 060 | A |  | E-Mail do Endereço de Pagamento |  |  |
| 1566 | 1585 | 020 | A |  | Carteira de Identidade |  |  |
| 1586 | 1595 | 010 | A |  | Órgão Emissor da Carteira de Identidade |  |  |
| 1596 | 1597 | 002 | A |  | Estado Emissor da Carteira de Identidade |  |  |
| 1598 | 1617 | 020 | A |  | Código do Município |  | Kein IconNota 20INLINE **Nota 20:** Para o país Brasil, o nome da "Cidade" que era informado na posição 285 a 316 passa a ser informado de acordo com a informação do campo "Código do Município", posição 1598 a 1617. Informando o "código do município" (cidade) o nome do município é incluído automaticamente. Para país estrangeiro usar as posições de 285 a 316. |
| 1618 | 1622 | 005 | N |  | Não Utilizado (Zeros) |  |  |
| 1623 | 1623 | 001 | NU |  | Não Utilizado (Espaços) |  |  |
| 1624 | 1626 | 003 | A |  | Código do Cargo |  |  |
| 1627 | 1627 | 001 | A |  | Vínculo Empregatício |  |  |
| 1628 | 1637 | 010 | VF | 04 | Valor do Frete por Fornecedor |  |  |
| 1638 | 1642 | 005 | N |  | Tipo de Tomador |  | Kein IconNota 22INLINE **Nota 22:** Tipo Tomador   |  |  | | --- | --- | | 0 | Não se aplica | | 1 | Cessão de Mão de Obra | | 2 | Construção Civil | |
| 1643 | 1647 | 005 | N |  | Contribuinte ISS |  | Kein IconNota 23INLINE **Nota 23:** Contribuinte ISS   |  |  | | --- | --- | | 00000 | Não | | 00001 | Sim | |
| 1648 | 1657 | 010 | N |  | Número de Dependentes |  |  |
| 1658 | 1717 | 060 | A |  | Empresa que a pessoa trabalha |  |  |
| 1718 | 1718 | 001 | A |  | Estado Civil |  | Kein IconNota 24INLINE **Nota 24:** Estado Civil   |  |  | | --- | --- | | C | Casado | | D | Desquitado | | I | Divorciado | | O | Outros | | S | Solteiro | | V | Viúvo | |
| 1719 | 1719 | 001 | A |  | Produtor Rural |  |  |
| 1720 | 1733 | 014 | A |  | Inscrição no SUFRAMA |  |  |
| 1734 | 1734 | 001 | N |  | Contribuinte ICMS |  | Kein IconNota 31INLINE **Nota 31:** Contribuinte ICMS   |  |  | | --- | --- | | 0 | Não é contribuinte | | 1 | É contribuinte | | 2 | Contribuinte isento de ICMS | |
| 1735 | 1739 | 005 | N |  | Órgão Público |  | Kein IconNota 25INLINE **Nota 25:** Órgão Público   |  |  | | --- | --- | | 00000 | Não Se Aplica | | 00001 | Federal | | 00002 | Estadual | | 00003 | Municipal | |
| 1740 | 1754 | 015 | A |  | Telefone Comercial |  | Kein IconNota 10INLINE **Nota 10:**  Telefone Comercial estão disponível só para pessoa física. |
| 1755 | 1764 | 010 | A |  | Caixa Postal |  |  |
| 1765 | 1774 | 010 | A |  | Caixa Postal de Pagamento |  |  |
| 1775 | 1784 | 010 | A |  | Caixa Postal de Entrega |  |  |
| 1785 | 1789 | 005 | N |  | Categoria do Autônomo |  |  |
| 1790 | 1799 | 010 | A |  | Código Brasileiro de Ocupação do Autônomo |  |  |
| 1800 | 1810 | 011 | A |  | Número Contribuinte Individual do Autônomo |  |  |
| 1811 | 1820 | 010 | NU |  | Não Utilizado (Espaços) |  |  |
| 1821 | 1830 | 010 | VF |  | Valor de outras deduções para cálculo de IRRF |  |  |
| 1831 | 1840 | 010 | A |  | Código da Receita |  |  |
| 1841 | 1841 | 001 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 11INLINE **Nota 11:** A posição 1841 não é mais utilizada para o campo  "Ramo Atividade", o campo agora é informado na posição 2004.   |  |  | | --- | --- | | 1 | Comércio | | 2 | Indústria | | 4 | Serviços | | 8 | Associação | | 16 | Produtor Rural | |
| 1842 | 1861 | 020 | A |  | CEI |  |  |
| 1862 | 1866 | 005 | N |  | Optante pelo Simples |  | Kein IconNota 13INLINE **Nota 13:**   |  |  | | --- | --- | | 00000 | Não | | 00001 | Sim | |
| 1867 | 1871 | 005 | N |  | Tipo de Rua |  |  |
| 1872 | 1876 | 005 | N |  | Tipo de Bairro |  |  |
| 1877 | 1877 | 001 | A |  | Regime de ISS |  | Kein IconNota 14INLINE **Nota 14:** Regime de ISS   |  |  | | --- | --- | | N | Nenhum | | G | Construção Civil | | K | Depósito Judicial | | H | Estimativa | | F | Imune | | C | Isenta ISSQN | | I | Sociedade Profissional | | L | Incentivo a Cultura | | J | Micro Empresa | |
| 1878 | 1882 | 005 | N |  | Retenção de ISS |  | Kein IconNota 26INLINE **Nota 26:** Retenção de ISS   |  |  | | --- | --- | | 00000 | Não Se Aplica | | 00001 | Saída | | 00002 | Entrada | | 00003 | Ambas | |
| 1883 | 1892 | 010 | Data |  | Data de Nascimento |  |  |
| 1893 | 1893 | 001 | N |  | Desativar Dados Bancários do Cli/For |  | Kein IconNota 16INLINE **Nota 16:**  Valores válidos para o campo:  0 =  Falso e 1 =  Verdadeiro . Se o campo for verdadeiro os Dados Bancários serão colocados como inativos e adicionados os Dados Bancários do arquivo de importação. Caso contrário permanece o comportamento atual, os Dados Bancários são excluídos e adicionados os Dados Bancários do arquivo de importação. |
| 1894 | 1913 | 020 | A |  | Inscrição Estadual ST do Fornecedor em MG |  |  |
| 1914 | 1943 | 030 | A |  | Bairro (30 posições) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros(posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 1944 | 1973 | 030 | A |  | Bairro de Entrega (30 posições) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros(posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 1974 | 2003 | 030 | A |  | Bairro de Pagamento (30 posições) |  | Kein IconNota 17INLINE **Nota 17:** Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros(posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente. |
| 2004 | 2005 | 002 | N |  | Ramo de Atividade |  | Kein IconNota 11INLINE **Nota 11:** A posição 1841 não é mais utilizada para o campo  "Ramo Atividade", o campo agora é informado na posição 2004.   |  |  | | --- | --- | | 1 | Comércio | | 2 | Indústria | | 4 | Serviços | | 8 | Associação | | 16 | Produtor Rural | |
| 2006 | 2105 | 100 | A |  | Rua |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 2106 | 2205 | 100 | A |  | Rua de Pagamento |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 2206 | 2305 | 100 | A |  | Rua de Entrega |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 2306 | 2310 | 005 | A |  | Código de Pagamento GPS |  |  |
| 2311 | 2311 | 001 | N |  | Nacionalidade |  | Kein IconNota 30INLINE **Nota 30:** Nacionalidade   |  |  | | --- | --- | | 0 | Brasileira | | 1 | Estrangeira | |
| 2312 | 2331 | 020 | A |  | Código do Município de Pagamento |  | Kein IconNota 20INLINE **Nota 20:** Para o país Brasil, o nome da "Cidade" que era informado na posição 285 a 316 passa a ser informado de acordo com a informação do campo "Código do Município", posição 1598 a 1617. Informando o "código do município" (cidade) o nome do município é incluído automaticamente. Para país estrangeiro usar as posições de 285 a 316. |
| 2332 | 2351 | 020 | A |  | Código do Município de Entrega |  | Kein IconNota 20INLINE **Nota 20:** Para o país Brasil, o nome da "Cidade" que era informado na posição 285 a 316 passa a ser informado de acordo com a informação do campo "Código do Município", posição 1598 a 1617. Informando o "código do município" (cidade) o nome do município é incluído automaticamente. Para país estrangeiro usar as posições de 285 a 316. |
| 2352 | 2354 | 003 | N |  | Id. do País |  |  |
| 2355 | 2357 | 003 | N |  | Id. do País (Pagamento) |  |  |
| 2358 | 2360 | 003 | N |  | Id. do País (Entrega) |  |  |
| 2361 | 2365 | 005 | N |  | Tipo de Rua (Pagamento) |  |  |
| 2366 | 2370 | 005 | N |  | Tipo de Bairro (Pagamento) |  |  |
| 2371 | 2375 | 005 | N |  | Tipo de Rua (Entrega) |  |  |
| 2376 | 2380 | 005 | N |  | Tipo de Bairro (Entrega) |  |  |
| 2381 | 2385 | 005 | N |  | Indicador de Natureza da Retenção na Fonte |  |  |

Complementares Cliente/Fornecedor

**Linha de Campos Complementares dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra M |

**Observação**

Informe os campos complementares em sequência, a partir da posição "002".  
**Exemplo**

Você possui os campos complementares:

* Vendedor – tamanho 20;

* Comprador – tamanho 20.

O preenchimento do layout deve ser:

Posição: 002 a 021  
Tamanho: 020  
Formato: A  
Nº Decimal:  
Descrição: Vendedor

Posição: 022 a 041  
Tamanho: 020  
Formato: A  
Nº Decimal:  
Descrição: Comprador

**Atenção**

Não é possível importar Campos Complementares do "TIPO" "Texto".  
Os Campos Complementares do tipo data, devem estar no formato DD/MM/AAAA.

Valores Default

**Linha de Valores Default dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra D |
| 002 | 026 | 025 | A |  | Tabela Opcional 1 |  |  |
| 027 | 051 | 025 | A |  | Tabela Opcional 2 |  |  |
| 052 | 076 | 025 | A |  | Tabela Opcional 3 |  |  |
| 077 | 101 | 025 | A |  | Tabela Opcional 4 |  |  |
| 102 | 126 | 025 | A |  | Tabela Opcional 5 |  |  |
| 127 | 151 | 025 | A |  | Departamento |  | Kein IconNota 27INLINE **Nota 27:** Para incluir a informação de Departamento é necessária a informação de "Filial". |
| 152 | 176 | 025 | A |  | Centro de Custo |  |  |
| 177 | 181 | 005 | N |  | Filial |  |  |
| 182 | 186 | 005 | N |  | Cód. da Coligada do Cli/For | X | Kein IconNota 1INLINE **Nota 1:**   |  |  | | --- | --- | | Zeros | Coligada global | |
| 187 | 189 | 003 | A |  | Cód. do Banco de Cobrança |  |  |
| 190 | 194 | 005 | N |  | Cód. da Carteira de Cobrança |  |  |
| 195 | 199 | 005 | A |  | Não Utilizado (Espaços) |  |  |
| 200 | 215 | 016 | A |  | Cód. do Vendedor |  |  |
| 216 | 227 | 012 | VF | 4 | Percentual de Desconto por Cli/For |  |  |
| 228 | 242 | 015 | A |  | Representante por Cliente/Fornecedor |  |  |
| 243 | 252 | 010 | A |  | Default para Tipo de Documento |  |  |
| 253 | 257 | 005 | N |  | Coligada da Conta/Caixa |  |  |
| 258 | 267 | 010 | A |  | Conta/Caixa |  |  |
| 268 | 272 | 005 | A |  | Transportador |  |  |
| 273 | 282 | 010 | A |  | Código de Receita do INSS |  |  |
| 283 | 287 | 005 | A |  | Não Utilizado (Espaços) |  |  |
| 288 | 288 | 001 | A |  | Tipo Contábil |  | Kein IconNota 18INLINE **Nota 18:**   |  |  | | --- | --- | | 0 | Não Contábil | | 1 | Contábil | | 2 | Baixa Contábil | | 3 | A Contabilizar | |

**Observações**

Para a importação de informações de Default é obrigatório a existência do "Código de Cliente/Fornecedor" na linha de Dados de Cliente/Fornecedor. Se a importação for realizada em Coligada que utilize o "Código de Cliente/fornecedor" sequencial, na posição do Código de Cliente/Fornecedor deve ser informado o próximo código sequencial.

**Exemplo**  
Ao abrir a janela de edição de um novo Cliente/Fornecedor é verificado que o Código do último Cliente cadastrado foi "0000001491".  
No arquivo de importação deve ser informado o Código "0000001492".  
As informações "Condição de Pagamento para Fornecedores" e "Condição de Pagamento para Clientes" foram retiradas do Default de Cliente/Fornecedor.

Defaults contábeis

**Linha de Contabilizações Default dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra T |
| 002 | 006 | 005 | N |  | Débito/Crédito | X | Kein IconNota 3INLINE **Nota 3:**   |  |  | | --- | --- | | 1 | Débito | | 2 | Crédito | |
| 007 | 011 | 005 | N |  | Cliente ou Fornecedor | X | Kein IconNota 2INLINE **Nota 2:**   |  |  | | --- | --- | | 1 | Cliente | | 2 | Fornecedor | |
| 012 | 021 | 010 | VF | 4 | Percentual | X |  |
| 022 | 026 | 005 | N |  | Código da Filial |  |  |
| 027 | 051 | 025 | A |  | Código do Departamento |  |  |
| 052 | 076 | 025 | A |  | Código do Centro de Custos |  |  |
| 077 | 086 | 010 | A |  | Código do Histórico Padrão |  |  |
| 087 | 336 | 250 | A |  | Complemento do Histórico |  |  |
| 337 | 341 | 005 | N |  | Código da Coligada do Cli/For | X | Kein IconNota 1INLINE **Nota 1:**   |  |  | | --- | --- | | Zeros | Coligada global | |
| 342 | 346 | 005 | N |  | Código da Coligada. da Conta Contábil | X | Kein IconNota 1INLINE **Nota 1:**   |  |  | | --- | --- | | Zeros | Coligada global | |
| 347 | 386 | 040 | A |  | Código da Conta Contábil | X |  |
| 387 | 396 | 010 | A |  | Classificação Contábil da Conta |  |  |
| 397 | 406 | 010 | NU |  | Não Utilizado (Espaços) |  |  |

Defaults contábeis - Rateios Gerenciais

**Linha de Rateios Gerenciais das Contabilizações Default dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra R |
| 002 | 006 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 007 | 011 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 012 | 016 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 017 | 021 | 005 | NU |  | Não Utilizado (Espaços) |  |  |
| 022 | 061 | 040 | NU |  | Não Utilizado (Espaços) |  |  |
| 062 | 066 | 005 | N |  | Código da Coligada da Conta Gerencial | X |  |
| 067 | 106 | 040 | A |  | Código da Conta Gerencial | X |  |
| 107 | 116 | 010 | VF | 4 | Percentual |  |  |
| 117 | 126 | 010 | NU |  | Não Utilizado (Espaços) |  |  |

Dados Contatos

**Linha de Contatos dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra O |
| 002 | 051 | 050 | A |  | Nome do Contato | X |  |
| 052 | 131 | 080 | A |  | e-mail do contato |  |  |
| 132 | 146 | 015 | A |  | Telefone do contato |  |  |
| 147 | 152 | 006 | A |  | Ramal do Contato |  |  |
| 153 | 167 | 015 | A |  | Fax do Contato |  |  |
| 168 | 217 | 050 | A |  | Função |  |  |
| 218 | 297 | 080 | A |  | Observação |  |  |
| 298 | 337 | 040 | NU |  | Não Utilizado (Espaços) |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |
| 338 | 345 | 008 | A |  | Número (Endereço) |  |  |
| 346 | 375 | 030 | A |  | Complemento (Endereço) |  |  |
| 376 | 405 | 030 | A |  | Bairro (Endereço) |  |  |
| 406 | 437 | 032 | A |  | Cidade (Endereço) |  |  |
| 438 | 439 | 002 | A |  | UF (Endereço) |  | Sigla do Estado |
| 440 | 448 | 009 | A |  | CEP (Endereço) |  |  |
| 449 | 468 | 020 | A |  | País (Endereço) |  |  |
| 469 | 469 | 001 | N |  | Ativo |  | Kein IconNota 13INLINE **Nota 13:**   |  |  | | --- | --- | | 00000 | Não | | 00001 | Sim | |
| 470 | 479 | 010 | DATA |  | Data de Nascimento |  |  |
| 480 | 480 | 001 | N |  | É Default para e-mail de compras  (Gestão de Estoque, Compras e Faturamento) |  | Kein IconNota 13INLINE **Nota 13:**   |  |  | | --- | --- | | 00000 | Não | | 00001 | Sim | |
| 481 | 482 | 002 | NU |  | Não Utilizado (Espaços) |  |  |
| 483 | 582 | 100 | A |  | Rua (Endereço) |  | Kein IconNota 19INLINE **Nota 19:** Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente. |

Complementares dos Contatos

**Linha de Campos Complementares dos Contatos dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra L |

**Observação**  
Informe os campos complementares em sequência, a partir da posição "002".  
**Exemplo**

Você possui os campos complementares:

* Celular – tamanho 20;

* Departamento – tamanho 20.

O preenchimento do layout deve ser:

Posição: 002 a 021  
Tamanho: 020  
Formato: A  
Nº Decimal:  
Descrição: Celular

Posição: 022 a 041  
Tamanho: 020  
Formato: A  
Nº Decimal:  
Descrição: Departamento

Para facilitar a criação da linha de dados dos Campos Complementares, o TOTVS Gestão Financeira gera um layout dos registros de campos complementares cadastrados na base. Para gerar este layout você deve clicar sobre o ícone "Gera layout do registro de campos complementares" localizado na janela de "Importação de Arquivo Texto" (menu Utilitários | opção Conversões). O ícone é apresentado quando a opção "Tipo da Importação – Clientes/Fornecedores" é marcada.

Dados Bancários

**Linha de Dados Bancários dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra P |
| 002 | 041 | 40 | A |  | Descrição dos Dados Bancários |  |  |
| 042 | 042 | 1 | A |  | Forma de Pagamento/Débito | X | Kein IconNota 28INLINE **Nota 28:** Forma de Pagamento/Débito   | Sigla | Descrição | | --- | --- | | D | DOC (compe) | | T | Crédito em Conta Corrente no Mesmo Banco | | C | Cheque Administrativo | | I | Título de Cobrança (Boleto) | | N | Pagamento Eletrônico a Concessionários | | P | Crédito em Conta de Poupança | | R | Ordem de Pagamento à disposição | | X | Crédito em Conta Real Time | | Y | TED CIP | | Z | TED STR | | A | DARF | | G | GPS | | E | Débito Automático | | M | Crédito em Conta Corrente de Mesma Titularidade | | B | IPTU | | F | DARJ | | J | GARE | | L | FGTS | | O | GNRE | | S | PIX Transferência | | Q | PIX QR-Code | |
| 043 | 045 | 3 | N |  | Número do Banco (Dados Bancários) |  |  |
| 046 | 051 | 6 | N |  | Código da Agência (Dados Bancários) |  |  |
| 052 | 052 | 1 | A |  | Dígito da Agência (Dados Bancários) |  |  |
| 053 | 067 | 15 | A |  | Conta Corrente (Dados Bancários) |  |  |
| 068 | 069 | 2 | A |  | Dígito da Conta (Dados Bancários) |  |  |
| 070 | 099 | 30 | A |  | Nome da Agência (Dados Bancários) |  |  |
| 100 | 103 | 4 | NU |  | Não Utilizado (Espaços) |  |  |
| 104 | 107 | 4 | N |  | Câmara Compensação |  |  |
| 108 | 109 | 2 | N |  | Tipo da Conta (Dados Bancários) |  | Kein IconNota 8INLINE **Nota 8:**   |  |  | | --- | --- | | 1 | Conta Corrente Individual | | 2 | Conta Poupança Individual | | 3 | Conta Depósito Judicial/Em Consignação Individual | | 11 | Conta Corrente Conjunta | | 12 | Conta Poupança Conjunta | | 13 | Conta Depósito Judicial/Em Consignação Conjunta | |
| 110 | 110 | 1 | A |  | Tipo do D.O.C. (Dados Bancários) |  | Kein IconSpaceBeforeAndAfterTooltipNota 9INLINE **Nota 9:** Os campos  "Tipo do D.O.C." e "Código da Finalidade do D.O.C." devem ser preenchidos somente se o campo "Forma de Pagamento"  for 'D', 'Y' ou 'Z'. |
| 111 | 112 | 2 | N |  | Código da Finalidade do D.O.C.(Dados Bancários) |  | Kein IconSpaceAfterTooltipNota 9INLINE **Nota 9:** Os campos  "Tipo do D.O.C." e "Código da Finalidade do D.O.C." devem ser preenchidos somente se o campo "Forma de Pagamento"  for 'D', 'Y' ou 'Z'. |
| 113 | 172 | 60 | A |  | Favorecido (Dados Bancários) |  |  |
| 173 | 192 | 20 | A |  | CNPJ/CPF do Favorecido |  |  |
| 193 | 197 | 5 | N |  | Código da Filial |  |  |
| 198 | 199 | 2 | N |  | Tipo chave PIX |  | Kein IconSpaceAfterTooltipNota 33INLINE **Nota 33:**  Tipo Chave PIX   |  |  | | --- | --- | | 1 | Telefone | | 2 | E-mail | | 3 | CPF | | 4 | CNPJ | | 5 | Chave aleatória | |
| 200 | 299 | 100 | A |  | Chave PIX |  | Kein IconSpaceAfterTooltipNota 34BLOCK **Nota 34:**  O valor informado para a chave PIX será validado conforme o tipo da chave.  Para exportação e importação, os campos são devidamente informados a partir do patchs:    * 12.1.2502.173 * 12.1.2506.117 |

**Observação**A partir da aplicação dos respectivos patches, os campos 'Tipo Chave Pix' e 'Chave Pix' passaram a ser devidamente tratados nos processos de exportação e importação:

* 12.1.2502.173
* 12.1.2506.117
Dados CEI

**Linha de CEI do Cliente/Fornecedor**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo de Linha | X | Letra E |
| 002 | 021 | 020 | A |  | CEI | X |  |
| 022 | 061 | 040 | A |  | Descrição do CEI |  |  |
| 062 | 076 | 015 | A |  | Telefone |  |  |
| 077 | 176 | 100 | A |  | Rua |  |  |
| 177 | 184 | 008 | A |  | Número |  |  |
| 185 | 214 | 030 | A |  | Complemento |  |  |
| 215 | 244 | 030 | A |  | Bairro |  |  |
| 245 | 253 | 009 | A |  | CEP |  |  |
| 254 | 273 | 020 | A |  | Código do Município |  |  |
| 274 | 275 | 002 | A |  | Código do Estado |  |  |
| 276 | 280 | 005 | N |  | Código do País |  |  |

Tributos

**Linha de Tributos dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra B |
| 002 | 011 | 010 | A |  | Código do Tributo | X |  |

Inscrição Estadual ST

**Linha de Inscrição Estadual ST dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | F |  | Tipo da linha | X | Letra I |
| 002 | 003 | 002 | A |  | Estado da Inscrição Estadual | X |  |
| 004 | 023 | 020 | A |  | Inscrição Estadual | X |  |

Dados Redes Sociais

**Linha de Redes Sociais dos Clientes/Fornecedores**

| **Posição** | | **Tam.** | **Form.** | **Nº Dec.** | **Descrição** | **Obrigatório** | **Obs.** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **De** | **Até** |
| 001 | 001 | 001 | S |  | Tipo da linha | X | Letra S |
| 002 | 004 | 003 | N |  | Rede Social | X | Kein IconNota 32INLINE **Nota 32:** Redes Sociais   |  |  | | --- | --- | | 1 | Facebook | | 2 | Instagram | | 3 | Twitter | | 4 | LinkedIn | | 5 | Whatsapp | | 6 | Telegram | |
| 005 | 164 | 160 | A |  | Identificação | X |  |

Notas

**NOTAS EXPLICATIVAS**

**Nota 1:**

|  |  |
| --- | --- |
| Zeros | Coligada global |

**Nota 2:**

|  |  |
| --- | --- |
| 1 | Cliente |
| 2 | Fornecedor |

**Nota 3:**

|  |  |
| --- | --- |
| 1 | Débito |
| 2 | Crédito |

**Nota 4:**

|  |  |
| --- | --- |
| 1 | Cliente |
| 2 | Fornecedor |
| 3 | Cliente e Fornecedor |

**Nota 5:**

|  |  |
| --- | --- |
| D | DOC (Compe) |
| T | Crédito em Conta Corrente no mesmo Banco |
| C | Cheque Administrativo |
| I | Título de Cobrança (Boleto) |
| N | Pagamento Eletrônico a Concessionários |
| P | Crédito em Conta de Poupança |
| R | Ordem de Pagamento à disposição |
| X | Crédito em Conta real time |
| Y | TED CIP |
| Z | TED STR |

**Nota 6:**

|  |  |
| --- | --- |
| 1 | Conta Corrente |
| 2 | Poupança |

**Nota 7:**

|  |  |
| --- | --- |
| F | Pessoa Física |
| J | Pessoa Jurídica |

**Nota 8:**

|  |  |
| --- | --- |
| 1 | Conta Corrente Individual |
| 2 | Conta Poupança Individual |
| 3 | Conta Depósito Judicial/Em Consignação Individual |
| 11 | Conta Corrente Conjunta |
| 12 | Conta Poupança Conjunta |
| 13 | Conta Depósito Judicial/Em Consignação Conjunta |

**Nota 9:**  
Os campos  "Tipo do D.O.C." e "Código da Finalidade do D.O.C." devem ser preenchidos somente se o campo "Forma de Pagamento"  for 'D', 'Y' ou 'Z'.

**Nota 10:** Telefone Comercial estão disponível só para pessoa física.

**Nota 11:**  
A posição 1841 não é mais utilizada para o campo "Ramo Atividade", o campo agora é informado na posição 2004.

|  |  |
| --- | --- |
| 1 | Comércio |
| 2 | Indústria |
| 4 | Serviços |
| 8 | Associação |
| 16 | Produtor Rural |

**Nota 12:**

Caso seja escolhida a importação utilizando CNPJ/CEI/CPF, na posição onde deveria estar o Código do Cli/For, deve estar o CNPJ/CEI/CPF. Lembrar que está opção de importação só estará disponível quando o parâmetro usar código sequencial para código de Cli/For estiver marcado e a mascará do Cli/For for numérica.

**Nota 13:**

|  |  |
| --- | --- |
| 00000 | Não |
| 00001 | Sim |

**Nota 14:** Regime de ISS

|  |  |
| --- | --- |
| N | Nenhum |
| G | Construção Civil |
| K | Depósito Judicial |
| H | Estimativa |
| F | Imune |
| C | Isenta ISSQN |
| I | Sociedade Profissional |
| L | Incentivo a Cultura |
| J | Micro Empresa |

**Nota 15:** Na importação de um cli/for que tenha a forma de pagamento preenchida e que para este também tenha lançamento(s) na base, o sistema irá atualizar o(s) campo(s) do cadastro e na pasta Pagamento Eletrônico o sistema irá inserir um novo registro.

**Nota 16:** Valores válidos para o campo: 0 =  Falso e 1 =  Verdadeiro . Se o campo for verdadeiro os Dados Bancários serão colocados como inativos e adicionados os Dados Bancários do arquivo de importação. Caso contrário permanece o comportamento atual, os Dados Bancários são excluídos e adicionados os Dados Bancários do arquivo de importação.

**Nota 17:**  
Em substituição aos campos de 20 posições para o preenchimento dos nomes dos bairros (posições 265 a 284, 411 a 430 e 557 a 576) devem ser preenchidos os campos de 30 posições (posições 1914 a 1943, 1944 a 1973 e 1974 a 2003).  
Esta alteração foi feita para permitir que bairros com nome maior que vinte posições sejam importados normalmente.

**Nota 18:**

|  |  |
| --- | --- |
| 0 | Não Contábil |
| 1 | Contábil |
| 2 | Baixa Contábil |
| 3 | A Contabilizar |

**Nota 19:**  
Em substituição aos campos de 40 posições para o preenchimento do nome das ruas (posições 197 a 236, 343 a 382 e 489 a 528) devem ser preenchidos os campos de 100 posições (posições 2006 a 2105, 2106 a 2205 e 2206 a 2305).  
Esta alteração foi feita para permitir que ruas com nome maior que quarenta posições sejam importadas normalmente.

**Nota 20:**  
Para o país Brasil, o nome da "Cidade" que era informado na posição 285 a 316 passa a ser informado de acordo com a informação do campo "Código do Município", posição 1598 a 1617. Informando o "código do município" (cidade) o nome do município é incluído automaticamente.  
Para país estrangeiro usar as posições de 285 a 316.

**Nota 21:**  
É possível controlar os cadastros dos clientes/fornecedores agrupando-os por "tipos", ou seja, "Serviços", "Comércio", "Agroindústria" e etc. Para isso, o sistema oferece um cadastro com o nome de "Tipos de Cliente/Fornecedor", neste cadastro é possível incluir vários registros para definirem diversos tipos de cliente/fornecedor.  
Nesta posição você deve informar o "Código" do tipo deste cliente/fornecedor.

**Nota 22:**  
Tipo Tomador

|  |  |
| --- | --- |
| 0 | Não se aplica |
| 1 | Cessão de Mão de Obra |
| 2 | Construção Civil |

**Nota 23:**  
Contribuinte ISS

|  |  |
| --- | --- |
| 00000 | Não |
| 00001 | Sim |

**Nota 24:**  
Estado Civil

|  |  |
| --- | --- |
| C | Casado |
| D | Desquitado |
| I | Divorciado |
| O | Outros |
| S | Solteiro |
| V | Viúvo |

**Nota 25:**  
Órgão Público

|  |  |
| --- | --- |
| 00000 | Não Se Aplica |
| 00001 | Federal |
| 00002 | Estadual |
| 00003 | Municipal |
| 00004 | Distrito Federal |

**Nota 26:**  
Retenção de ISS

|  |  |
| --- | --- |
| 00000 | Não Se Aplica |
| 00001 | Saída |
| 00002 | Entrada |
| 00003 | Ambas |

**Nota 27:**  
Para incluir a informação de Departamento é necessária a informação de "Filial".

**Nota 28:**  
Forma de Pagamento/Débito

| Sigla | Descrição |
| --- | --- |
| D | DOC (compe) |
| T | Crédito em Conta Corrente no Mesmo Banco |
| C | Cheque Administrativo |
| I | Título de Cobrança (Boleto) |
| N | Pagamento Eletrônico a Concessionários |
| P | Crédito em Conta de Poupança |
| R | Ordem de Pagamento à disposição |
| X | Crédito em Conta Real Time |
| Y | TED CIP |
| Z | TED STR |
| A | DARF |
| G | GPS |
| E | Débito Automático |
| M | Crédito em Conta Corrente de Mesma Titularidade |
| B | IPTU |
| F | DARJ |
| J | GARE |
| L | FGTS |
| O | GNRE |
| S | PIX Transferência |
| Q | PIX QR-Code |

**Nota 29:**  
CEI de Cliente/Fornecedor

|  |  |
| --- | --- |
| Código do Município | Código existente na tabela de municípios |
| Código do Estado | Código existente na tabela de estados |
| Código do País | Código existente na tabela de países |

**Nota 30:**  
Nacionalidade

|  |  |
| --- | --- |
| 0 | Brasileira |
| 1 | Estrangeira |

**Nota 31:**  
Contribuinte ICMS

|  |  |
| --- | --- |
| 0 | Não é contribuinte |
| 1 | É contribuinte |
| 2 | Contribuinte isento de ICMS |

**Nota 32:**  
Redes Sociais

|  |  |
| --- | --- |
| 1 | Facebook |
| 2 | Instagram |
| 3 | Twitter |
| 4 | LinkedIn |
| 5 | Whatsapp |
| 6 | Telegram |

**Nota 33:**

Tipo Chave PIX

|  |  |
| --- | --- |
| 1 | Telefone |
| 2 | E-mail |
| 3 | CPF |
| 4 | CNPJ |
| 5 | Chave aleatória |

**Nota 34:**

O valor informado para a chave PIX será validado conforme o tipo da chave.

Importação arquivo .XML

**Importação de Clientes/Fornecedores via arquivo .XML**  
  
XML (*e**X**tensible **M**arkup **L**anguage*) é uma linguagem de marcação que é capaz de descrever diversos tipos de dados. Possui estrutura única e separa o dado da formatação do arquivo. Cria o arquivo de forma hierárquica na disposição dos dados, tornando-o mais legível.

**Observação**  
A importação via arquivo .TXT (texto) continua funcionando segundo o layout de importação de clientes/fornecedores. A utilização do arquivo .XML não substitui o o .TXT, apenas torna esse processo mais fácil. É possível gerar um SCHEMA XML que exibe o tipo e a estrutura do arquivo a ser gerado, facilitando o entendimento do usuário.

**Importação de Clientes/Fornecedores via arquivo.XML**

Passo a Passo

1. Acessar: Processos > Importação de Clientes/Fornecedores.
2. Através do botão de LOOKUP selecionar o arquivo XML a ser importado.
3. Serão exibidos todos os registros em forma de tabela.
4. Executar o processo de importação de Clientes/Fornecedores através do botão IMPORTAR.
5. Será exibida uma mensagem dizendo "Clientes/Fornecedores importados com Sucesso!". Confirme a mensagem e feche a tela, caso não queira importar outros arquivos.

**Observação**  
Ao executar o item 3 do passo a passo acima, o sistema exibe ao lado do botão de LOOKUP uma caixa com a opção de selecionar tabelas que compôem o registro do cliente/fornecedor para a exibição das mesmas em forma de tabela.

**Atenção**  
Dados Bancários  
Através da importação via XML é necessário informar a "Coligada" e o "Código do Cliente/Fornecedor" junto as informações de Dados Bancários, caso não seja informado os Dados Bancários não serão importados.

Exemplo de arquio .XML

<?xml version="1.0" standalone="yes"?>  
<FinCFOImportacao xmlns="<http://tempuri.org/FinCFOImportacao.xsd>">  
  <FCFO>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCFO>E00001</CODCFO>  
    <NOMEFANTASIA>CLIENTE/FORNECEDOR</NOMEFANTASIA>  
    <NOME>CLIENTE/FORNECEDOR LTDA</NOME>  
    <CGCCFO>333.333.333-33</CGCCFO>  
    <PAGREC>3</PAGREC>  
    <RUA>RUA DO CLIENTE/FORNECEDOR</RUA>  
    <NUMERO>10</NUMERO>  
    <BAIRRO>BAIRRO DO CLIENTE/FORNECEDOR</BAIRRO>  
    <CIDADE>Belo Horizonte</CIDADE>  
    <CODETD>MG</CODETD>  
    <CEP>30570590</CEP>  
    <TELEFONE>33333333</TELEFONE>  
    <CIDADEPGTO>Belo Horizonte</CIDADEPGTO>  
    <CIDADEENTREGA>Belo Horizonte</CIDADEENTREGA>  
    <TELEX>33333333</TELEX>  
    <EMAIL>email@[email.com.br](http://email.com.br)</EMAIL>  
    <CODTCF>000004</CODTCF>  
    <ATIVO>1</ATIVO>  
    <LIMITECREDITO>0</LIMITECREDITO>  
    <VALOROP1>0</VALOROP1>  
    <VALOROP2>0</VALOROP2>  
    <VALOROP3>0</VALOROP3>  
    <PATRIMONIO>0</PATRIMONIO>  
    <NUMFUNCIONARIOS>0</NUMFUNCIONARIOS>  
    <CODCOLTCF>0</CODCOLTCF>  
    <CODMUNICIPIO>06200</CODMUNICIPIO>  
    <PESSOAFISOUJUR>F</PESSOAFISOUJUR>  
    <PAIS>Brasil</PAIS>  
    <PAISPAGTO>Brasil</PAISPAGTO>  
    <PAISENTREGA>Brasil</PAISENTREGA>  
    <CONTRIBUINTE>0</CONTRIBUINTE>  
    <CFOIMOB>0</CFOIMOB>  
    <VALFRETE>0</VALFRETE>  
    <TPTOMADOR>0</TPTOMADOR>  
    <CONTRIBUINTEISS>0</CONTRIBUINTEISS>  
    <NUMDEPENDENTES>0</NUMDEPENDENTES>  
    <ORGAOPUBLICO>0</ORGAOPUBLICO>  
    <VROUTRASDEDUCOESIRRF>0</VROUTRASDEDUCOESIRRF>  
    <OPTANTEPELOSIMPLES>0</OPTANTEPELOSIMPLES>  
    <TIPORUA>1</TIPORUA>  
    <TIPOBAIRRO>1</TIPOBAIRRO>  
    <REGIMEISS>N</REGIMEISS>  
    <RETENCAOISS>0</RETENCAOISS>  
    <RAMOATIV>0</RAMOATIV>  
    <IDPAIS>1</IDPAIS>  
    <NACIONALIDADE>0</NACIONALIDADE>  
    <TIPORUAPGTO>1</TIPORUAPGTO>  
    <TIPOBAIRROPGTO>1</TIPOBAIRROPGTO>  
    <TIPORUAENTREGA>1</TIPORUAENTREGA>  
    <TIPOBAIRROENTREGA>1</TIPOBAIRROENTREGA>  
  </FCFO>  
  <FCFOCOMPL>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCFO>E00001</CODCFO>  
  </FCFOCOMPL>  
  <FDADOSPGTO>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCOLCFO>1</CODCOLCFO>  
    <CODCFO>E00001</CODCFO>  
    <IDPGTO>-1</IDPGTO>  
    <DESCRICAO>BANCO XXX</DESCRICAO>  
    <FORMAPAGAMENTO>Z</FORMAPAGAMENTO>  
    <NUMEROBANCO>999</NUMEROBANCO>  
    <CODIGOAGENCIA>9999</CODIGOAGENCIA>  
    <DIGITOAGENCIA></DIGITOAGENCIA>  
    <CONTACORRENTE>99999999</CONTACORRENTE>  
    <DIGITOCONTA>9</DIGITOCONTA>  
    <CAMARACOMPENSACAO>1</CAMARACOMPENSACAO>  
    <TIPOCONTA>1</TIPOCONTA>  
    <TIPODOC>D</TIPODOC>  
    <FAVORECIDO>JOAO SLVA</FAVORECIDO>  
    <CODFILIAL>1</CODFILIAL>  
    <CGCFAVORECIDO>00000000000</CGCFAVORECIDO>  
  </FDADOSPGTO>  
  <FDADOSPGTODEF>  
    <IDPGTODEF>1</IDPGTODEF>  
    <CODCOLIGADA>1</CODCOLIGADA>  
    <CODCOLCFO>1</CODCOLCFO>  
    <CODCFO>E00001</CODCFO>  
    <CODFILIAL>1</CODFILIAL>  
    <PAGREC>2</PAGREC>  
    <IDPGTO>-1</IDPGTO>  
  </FDADOSPGTODEF>  
</FinCFOImportacao>

**Observação**A partir da aplicação dos respectivos patches, os campos 'TIPOPIX' e 'CHAVE' passaram a ser devidamente tratados nos processos de exportação e importação:

* 12.1.2502.173
* 12.1.2506.117
