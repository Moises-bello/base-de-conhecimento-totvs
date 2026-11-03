---
content_hash: e694c0139edc65dbdd0d5b5db8e50dfeea2276273b9b1eabc6a3d085c2b5de13
fetched_at: '2026-06-29T00:09:22.592131+00:00'
page_id: '422546008'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco 0 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546008
version: 43
---

Este Bloco é composto pelos registros:  
 

BLOCO0left00000000

**Abertura do arquivo Digital e Identificação da Entidade**

Será gerado para todos os arquivos e contempla dados informados pelo usuário e dados referentes à filial no qual o arquivo está sendo gerado. Este registro será gerado de acordo com os dados informados pelo usuário na tela de parametrização do Wizard.

A partir de 2021 estará disponível a versão 015 na tela de geração da rotina.

00010001

**Abertura do Bloco 0**

Informações da tela da rotina

00050005

**Dados Complementares da entidade**

Será gerado conforme dados da Filial

00150015

**Dados do Contribuinte Substituto**

Este registro deverá ser gerado quando a filial possuir Inscrições ST cadastradas para ela. (Anexo de Filial).

01000100

**Dados do Contabilista**

Registro preenchido com os dados do contador da filial, estes dados devem ser informados na tela de cadastro da filial. Cadastro de Filiais -> Anexo Dados Fiscal -> Aba Contador" .

01500150

**Tabela de Cadastro do Participante**

Este registro contempla os dados de todos os participantes de todos os lançamentos que serão inseridos no arquivo. Estes participantes podem ser Clientes/Fornecedores, Filiais e Transportadoras nos quais a Filial geradora teve alguma operação no período informado.

Informações

Foi criado um novo Tipo de Natureza no cadastro da CFOP, este tipo é referente a Devolução por Recusa.

Se na Natureza o campo Tipo Natureza(Rotinas Legais) for Devolução por Recusa, as informações geradas no registro 0150 do SPED Fiscal será considerado o Emitente/Destinatário Filial.

Veja como parametrizar Devolução por Recusa: <https://tdn.totvs.com/x/-lYrIw>

01750175

**Alteração da Tabela de Cadastro de Participante**

Este registro deve conter as informações referentes às alterações ocorreram no cadastro dos participantes no período informado pelo usuário. No sistema estes dados podem ser visualizados em anexos existentes tanto do cadastro de Filial quanto de Cliente/Fornecedor.

01900190

**Identificação das unidades de medida**

Este registro tem por objetivo descrever as unidades de medidas utilizadas no arquivo digital. Não podem ser informados dois ou mais registros com o mesmo código de unidade de medida. Somente devem constar as unidades de medidas informadas em qualquer outro registro.

02000200

**Tabela de Identificação do Item (Produtos e Serviços)**

Este registro tem por objetivo informar mercadorias, serviços, produtos ou quaisquer outros itens concernentes às transações fiscais e aos movimentos de estoques em processos produtivos, bem como os insumos. Informações exclusivas do Cadastro de  do TOTVS Gestão de Estoques, Compras e Faturamento.

| N° | Campo | Descrição | Origem da Informação | Observações |
| --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "0200" | Não se aplica |  |
| 02 | COD\_ITEM | Código do item | TPRD.CODIGOPRD | Código do Produto |
| 03 | DESCR\_ITEM | Descrição do item | TPRD.DESCRICAO | A partir da versão 12.1.28 foi criado a Flag "Gera a Descrição do Item sem caracteres especiais" na tela de parâmetros do processo de geração do SPED Fiscal, na pasta Personalização, para indicar se a descrição do item deverá ser gerada retirando os **caracteres especiais\*.**  **\***Lista de caracteres especiais que são tratados:   | \*~´`^ªº§¢£³²¹¬°><¨\* | | --- |     **Obs.:**   Caracteres acentuados são substituídos por não acentuados;  "Ç" será substituído por "C";  "º" será substituído por "o";  "ª" será substituído por "a". |
| 04 | COD\_BARRA | Representação alfanumérico do código de barrado produto, se houver | TPRDCODIGO.CODIGO |  |
| 05 | COD\_ANT\_ITEM | Código anterior do item com relação à última informação apresentada | Não se aplica | Esse campo é gerado vazio, conforme orientação do guia prático atualizado: "Campo 05 (COD\_ANT\_ITEM) - Não preencher. Se houver a informação, esta deve ser prestada no registro 0205". |
| 06 | UNID\_INV | Unidade de medida utilizada na quantificação de estoques. | TPRD.CODUNDCONTROLE |  |
| 07 | TIPO\_ITEM | Tipo do item – Atividades Industriais, Comerciais e Serviços | TPRD.TIPO |  |
| 08 | COD\_NCM | Código da Nomenclatura Comum do Mercosul | DCLASSIFBENSSERVICO.NUMERO | A partir da versão **12.1.2506** este campo será gerado com base nas informações do novo cadastro de [Classificação Fiscal de Bens e Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=913828140). |
| 09 | EX\_IPI | Código EX, conforme a TIPI | DCLASSIFBENSSERVICO.CODIGOEX | A partir da versão **12.1.2506** este campo será gerado com base nas informações do novo cadastro de [Classificação Fiscal de Bens e Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=913828140). |
| 10 | COD\_GEN | Código do gênero do item, conforme a Tabela 4.2.1 | DCLASSIFBENSSERVICO.NUMERO | Apenas os dois primeiros dígitos. |
| 11 | COD\_LST | Código do serviço conforme lista do Anexo I da Lei Complementar Federal nº 116/03. | TPRD.CODIGOSERVICOFEDERAL | Campo referente ao código de serviço federal deve ser informado de acordo com a LC 116/2003, ou seja, SEM zeros não significativos à esquerda. |
| 12 | ALIQ\_ICMS | Alíquota de ICMS aplicável ao item nas operações internas | DLAF.ALIQICMS |  |
| 13 | CEST | Código Especificador da Substituição Tributária | TPRDFISCAL.CODIGOCEST |  |

02050205

**Alteração do Item**

Este registro tem por objetivo informar alterações ocorridas na descrição do produto ou quando ocorrer alteração na codificação do produto, desde que não o descaracterize ou haja modificação que o identifique como sendo novo produto. Caso não tenha ocorrido movimentação no período da alteração do item. Essas informações ficam gravadas no Log de [Produtos](http://tdn.totvs.com/display/LRM/Produto) (TPRDLOG).

02060206

**Código de produto conforme Tabela ANP (Combustíveis)**

Este registro tem por objetivo informar o código correspondente ao produto constante na Tabela da Agência Nacional de Petróleo (ANP) para os produtos denominados "Combustíveis". Deve ser apresentado apenas pelos contribuintes produtores, importadores, distribuidores e postos de combustíveis.  A informação deve ser inserida no cadastro do Produto- Anexos| Dados Fiscais.

02100210

**Consumo Específico Padronizado**

O Registro 0210 deve ser apresentado pelos estabelecimentos industriais ou a eles equiparados pela legislação Federal. Atacadistas obrigados à apresentação do Bloco K não estão obrigados à apresentação deste Registro. Este Registro somente deve existir quando o conteúdo do campo "7 - TIPO\_ITEM" do Registro 0200 for igual a 03 (produto em processo) ou 04 (produto acabado).  
Este registro é gerado para estabelecimentos do tipo indústria ou a eles equiparados pela legislação Federal. As informações que irão compor este registro podem ser cadastradas nos módulos TOTVS Planejamento e Controle da Produção ou TOTVS Gestão de Estoque, Compras e Faturamento.  
 No módulo TOTVS Planejamento e Controle da Produção as informações são definidas no cadastro de Estruturas/Componentes disponíveis no menu Cadastros | Engenharia | Estruturas, Pasta Componentes.  
 No módulo TOTVS Gestão de Estoque, Compras e Faturamento as informações são definidas em Estoque | Produção | Componentes.  
 São enviadas para o SPED Fiscal as seguintes informações: Código da Coligada, Código da Filial, Código da Estrutura, Identificador do Produto da Estrutura, Identificador do Produto Componente, Quantidade Usada do Componente.

***Atenção:***  
Para que os Componentes da Estrutura sejam considerados na geração do SPED, o produto associado a Estrutura em questão deve estar parametrizado da seguinte forma no TOTVS Gestão de Estoque, Compras e Faturamento:

* Cadastros | Produtos | Anexos | Dados Fiscais do Produto:
* Tipo de Tributação: Tributação do ICMS/IPI ou Tributação pelo ISS.
* Situação da Mercadoria: Produto Acabado ou Produto em Elaboração
* Cadastros | Produtos | Anexos | Dados Fiscais do Produto| Tributação:
* Marcada a opção "Produto Exige Inventário Fiscal".

**Geração do registro 0210:**

A partir de janeiro de 2018, a obrigatoriedade da apresentação deste registro ficará a critério de cada UF, caso exista  
produção e consumo nos Registros K230/K235 e K250/K255.

Foi criado um Flag na tela de geração do SPED Fiscal, quando este Flag for desmarcado, o registro não será gerado. 

O campo será visível somente se estiver marcada a geração do Bloco K (Pasta "Personalização" da tela de geração da rotina > Gerar Bloco K diferente de **Não Gerar**) e será apresentado por default como Marcado.  
  
A partir de janeiro de 2022, este registro não será mais gerado, devido ao novo Layout do SPED. Para períodos anteriores, como 2021, continuará a ser gerado normalmente.

02200220

**Fatores de Conversão de Unidades**

Será inserido dados neste registro quando o código de unidade de controle do produto for diferente do código da unidade do item de um lançamento fiscal.

Além disso, a unidade, do item do lançamento, deve conter a unidade de conversão igual ao do cadastro do produto (vide imagem à direita).

Imagem

 

Cadastro do produto                                                                                                                                                                                     Cadastro de Unidade

* **Campo 2 (UNID\_CONV):**

Unidade comercial a ser convertida na unidade de estoque, referida no item do lançamento.

* **Campo 3 (FAT\_CONV):**

Fator de conversão: fator utilizado para converter a unidade do item do lançamento para unidade do cadastro do produto.

* **Campo 4 (COD\_BARRA):**

Representação alfanumérica do código de barra da unidade comercial do produto.  
O código de barras cadastrado deve ter a mesma unidade do item do lançamento.  
OBS: Campo gerado para lançamentos com data de entrada após 31/12/2021.  
Para que o código de barras seja gerado, é necessário que seu tipo esteja preenchido como "GTIN" no cadastro, conforme imagem abaixo.

Observação

O registro 0220 não será gerado para produtos onde a situação da mercadoria seja "Material de Uso e Consumo" a partir de 2023.

02210221

**Correlação Entre Códigos De Itens Comercializados**

Será inserido dados neste registro a partir do [cadastro de produtos compostos](https://tdn.totvs.com/x/KstEGQ) feito em um produto que atenda às regras de seleção do registro 0200 e o tipo deste produto deve ser "00 – Mercadoria para Revenda". Não pode ser informado dois ou mais registros, filhos do 0200 Pai, com o mesmo conteúdo no campo COD\_ITEM\_ATOMICO.

Quando não houver itens vinculados ao registro pai, o item atômico será o próprio registro pai 0200 com quantidade igual a 1.

* **Campo 1 (REG):**

            Valor fixo contendo “0221”.

* **Campo 2 (COD\_ITEM\_ATOMICO):**

            O valor informado no campo deve existir no campo COD\_ITEM de um registro 0200.

* **Campo 3 (QTD\_CONTIDA):**

            Quantidade de itens “atômicos” contidos no item informado no registro 0200 pai.

            O valor informado deve ser maior ou igual a 1.

            Quando item atômico igual ao registro pai, quantidade deve ser igual a 1.

Durante a geração do SPED Fiscal há 4 opções para o registro do 0221:

* **Não Gerar:** não será gerado o registro para os produtos que são registrados como “00 – Mercadoria para Revenda”.
* **Todos Produtos:** será gerado o registro para todos os produtos que são registrados como “00 – Mercadoria para Revenda”, para os produtos que não tem vínculo deve ser registrado com o próprio código.
* **Próprio Produto:** será gerado o registro , para todos os produtos que são registrados como “00 – Mercadoria para Revenda”, com o código do próprio produto e quantidade igual a 1. Para os produtos que são “Produtos Compostos” não serão registrados nesta opção.
* **Produtos Com Vínculo:** será gerado o registro para os produtos que são registrados como “00 – Mercadoria para Revenda” e tem vínculo com o produto composto.

Quando a quantidade do produto composto for menor que 1, será gerado com quantidade igual a 1.

03000300

**Cadastro de bens ou componentes do Ativo Imobilizado**

Informações relativas ao bens ou componentes do Ativo Imobilizado.

03050305

**Informação sobre a Utilização do Bem**

Informações relativas a utilização do Bens.

04000400

**Tabela de Natureza da Operação/ Prestação**

Informações relativas as naturezas de Operação contidas no arquivo.

04500450

**Tabela de Informação Complementar do documento fiscal**

Informações relativas as informações complementares do lançamento Fiscal. Gerado com base no campo Complementar do Lançamento Fiscal "InfComplDocFiscal".

**Campos de Uso Livre  NF-e**

Também é possível gerar o 0450 a partir dos Campos de Uso Livre, que tem o cadastro de Informações Fiscais Adicionais vinculado.   
Gerando a partir dos Campos de Uso Livre, o 0450 irá pegar a descrição das Informações Fiscais Adicionais.

ImagemBloco B

A Geração do Registro 0450 pelos Campos de Uso Livre não afeta o o Bloco B.

Para mais informações, acesse a página de [Informações Fiscais Adicionais](https://tdn.totvs.com/pages/viewpage.action?pageId=696092112).

04600460

**Tabela de Observações do Lançamento Fiscal**

Este registro deve contemplar todas as observações referentes a um lançamento fiscal.

**Campos de Uso Livre  NF-e**

Também é possível gerar o 0460 a partir dos Campos de Uso Livre, que tem o cadastro de Informações Fiscais Adicionais vinculado.   
Gerando a partir dos Campos de Uso Livre, o 0460 irá pegar a descrição das Informações Fiscais Adicionais.

ImagemBloco B

A Geração do Registro 0460 pelos Campos de Uso Livre não afeta o o Bloco B.

Para mais informações, acesse a página de [Informações Fiscais Adicionais](https://tdn.totvs.com/pages/viewpage.action?pageId=696092112).

05000500

**Plano de contas contábeis**

Informar somente as contas referenciadas nos tipos de registros: 0300.

|  |
| --- |
| 11 |
