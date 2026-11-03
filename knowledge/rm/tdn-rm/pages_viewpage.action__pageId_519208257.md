---
content_hash: d9339d90084e818d60de2be0bad2e8f5b0071a4988b0e83369623bd4d072d127
fetched_at: '2026-06-29T00:10:30.201427+00:00'
page_id: '519208257'
product: rm
source: tdn-rm
title: Estrutura dos Códigos de Barras EAN13, EAN128 e DataMatrix
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519208257
version: 23
---

## **CONTEÚDO**

1. **Visão Geral**
2. **EAN13**
3. **EAN128**
4. **DataMatrix**

barratrue1Visão Geral

Vários locais no Gestão Hospitalar utilizam leitura por código de barra para pesquisar o produto desejado. Por exemplo:

* Todos os componentes de pesquisa de Produto, permitem filtrar por código de barra.

* No menu "Cadastro de Produto/ Anexos/Informações/Totvs Saúde/Produtos do Kit", para um produto que é do tipo “Kit Pré Montado”, permite pesquisar um item lendo o código de barra (previamente associado).
* Nos menus localizados em "Farmácia"  e "Cuidado com pacientes", onde existir campo para escolher um MATMED ou qualquer outro Produto.

Farmácia / Movimentação de Estoque

Farmácia / Painel de Dispensação

Farmácia / Kit Pré-Montado

Farmácia / Processos Farmacêuticos

Cuidados com Paciente / Nova Requisição

Cuidados com Paciente / Painel de Cirurgias

Cuidados com Paciente / Processos Farmacêuticos

2EAN 13

## Estrutura código de barras EAN13:

* Seis primeiras posições é o ID do Produto;
* Da sétima a décima segunda posição é o ID do Lote.
* Última posição é o dígito verificador.

## Exemplo de código EAN13:

0143820837064

**Id do produto:** 014382  
**Id do lote:** 083706  
**Dígito verificador:** 4

### **Pré Requisito para utilizar EAN13:** o produto deverá ser controlado por lote.

Marcado no menu Cadastro de Produto/Anexos/Informações-Totvs Saúde, aba “Controle de Estoque”.

A partir da versão 12.1.2406 foi implementado uma segunda opção para a estrutura do EAN13.

## **Estrutura código de barras EAN13 - Com o Lote identificado no Cadastro de Código de Barras**

Implementada opção para leitura de código de barras, cujo Lote esteja informado no menu “Cadastros/Produto/Código de Barras”.

Ao bipar o código de barras, o sistema irá pesquisar o Id do Lote no “Cadastro de Código de Barras”, somente se não encontrar este cadastro é que será utilizado o Id. lote escrito na posição 7ª a 12ª  da leitura do código de barras.

O padrão deste tipo de código de barras é o EAN13 (tamanho 13).

Exemplo deste código de barras 7896676438338

Observe que as 6 primeiras posições (789667) não correspondem ao Id.Produto e nem mesmo a 7a posição (6438338) não contém o Lote do produto.

O lote do produto é identificado no cadastro do código de barras específico:

3EAN 128

## Estrutura do código EAN128:

* Identificador do código de barras EAN128 poderá ser iniciado pelos identificadores ]C1 e [C1 .
* Código do fabricante =  "02", contendo 14 posições após o "02"
* Código do Lote = "10", contendo **até** 20 posições após o "10"
* Data de Fabricação = "11", contendo 6 posições após o "11"
* Data de validade = "15", contendo 6 posições após o "15"
* Data máxima da validade = "17", contendo 6 posições após o "17"
* Número de série = "21", contendo até 20 posições após o "21"
* Registro da Anvisa = "713", contendo 20 posições após o "713"

## Exemplo de código EAN128:

]C102076300303107131115060815220531105554587524

**Identificador EAN128:** ]C1  
**Código do Fabricante:** 02 07630030310713  
**Data de Fabricação:** 11 150608  
**Data de Validade:** 15 220531  
**Código do Lote:**  10 5554587524

4DataMatrix

## **Estrutura do código GS1 DataMatrix**

O código de barras no padrão **GS1 DataMatrix** segue uma estrutura composta por **Identificadores de Aplicação (AI)**, que definem o tipo de informação contida em cada parte do código.

O identificador do código GS1 DataMatrix pode ser iniciado pelos prefixos:  
**`]d2`**, **`]C1`** ou **`]D1`**, conforme o padrão GS1.

### **Composição dos campos:**

* **(01)** – **GTIN (Global Trade Item Number)**: Contém 14 posições após o identificador "01".
* **(10)** – **Número do lote**: Contém até 20 posições após o "10". Caso seja encontrado o delimitador FNC1, a leitura do lote deve ser finalizada.
* **(11)** – **Data de fabricação**: Contém 6 posições após o "11", no formato **AAMMDD**.
* **(15)** – **Data de validade**: Contém 6 posições após o "15", no formato **AAMMDD**.
* **(17)** – **Data máxima de validade**: Contém 6 posições após o "17", no formato **AAMMDD**.
* **(21)** – **Número de série**: Contém até 20 posições após o "21".
* **(713)** – **Registro ANVISA**: Contém até 20 posições após o "713".

O separador **FNC1 (ASCII 29)** é utilizado para delimitar campos de comprimento variável, como o lote (10) e o número de série (21).

### **Exemplo de código GS1 DataMatrix:**

`0102458724578451541115060815230531109551340219551340030`

> O caractere invisível representa o **delimitador FNC1 (ASCII 29)**.

---

### **Exemplo interpretado:**

| Identificador | Descrição | Valor |
| --- | --- | --- |
| (01) | GTIN (Código do produto) | 0245872457845154 |
| (11) | Data de fabricação | 150608 |
| (15) | Data de validade | 230531 |
| (10) | Lote | 9551340 |
| (21) | Número de série | 9551340030 |
