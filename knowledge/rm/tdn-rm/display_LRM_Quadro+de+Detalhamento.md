---
content_hash: e67a0151b3348b7ba3dcede34b8a35e9d44831baa2eddd8bf9154406ecf82bb7
fetched_at: '2026-06-29T00:09:21.111341+00:00'
page_id: '422545815'
product: rm
source: tdn-rm
title: Quadro de Detalhamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Quadro+de+Detalhamento
version: 4
---

Este registro será gerado com o somatório da prestação de serviços com incidência de ICMS.   
 Neste caso, será somado o valor contábil dos lançamentos de saída emitidos para Cliente/Fornecedor do Estado do Espírito Santo, além disso, notas de prestação de serviços de Transporte, Comunicação ou Energia Elétrica.   
 Este somatório será por código de município do Lançamento Fiscal.  
 O detalhamento só será criado quando um dos campos descritos abaixo possuírem valores diferentes de zero.  
 ***Importante***: Mesmo que não exista valores a serem detalhados, será gerado o detalhamento para todos os 78 municípios existentes no estado do Espírito Santo.  
 ***Observação***: A criação dos municípios no arquivo será de acordo com a Classificação de Municípios selecionada na geração do arquivo e o cadastro correto dos mesmos.  
    
 Os campos que obrigaram a criação da TAG de <DETALHAMENTOS> serão:

**<VALR\_PROD\_RURAL\_PROPRIA>**  
 Gerados com os lançamentos Fiscais de entrada, com o CFOP do Grupo 1.XXX e que o Cliente/Fornecedor do lançamento possuir o Ramo de atividade "Produtor Rural" selecionado, no cadastro de Clientes/Fornecedores.

**<VALR\_AQZ\_PESSOA\_FISICA>**   
 Gerados com os lançamentos Fiscais de entrada, com o CFOP do Grupo 1.XXX, em que o Cliente/Fornecedor não poderá ser "Contribuinte de ICMS" ou sua Categoria deverá igual a "Pessoa Física" definido no Cadastro de Cliente/Fornecedor.

**<VALR\_ENERGIA\_ELETRICA>**  
 Serão consideradas lançamento fiscal onde o código modelo de documento seja = 06 e contenha os seguintes CFOP's 5.153.XX, 5.207.XX, 5.250.XX, 5.251.XX, 5.252.XX, 5.253.XX, 5.254.XX, 5.255.XX, 5.256.XX, 5.257.XX e 5.258.XX.

**<VALR\_TRANSPORTE>**  
 Serão considerados lançamentos fiscais onde o código modelo de documento seja = 07, 08, 8B, 09, 10, 11,13,14,15,16,17,20 e 57 e contenha os seguintes CFOP's 5.350.XX 5.351.XX, 5.352.XX, 5.353.XX, 5.354.XX, 5.355.XX, 5.356.XX e 5.357.XX.

**<VALR\_COMUNICACAO>**  
 Serão considerados lançamentos fiscais onde o código modelo de documento seja = 21 ou 22 e contenha os seguintes CFOP's 5.300.XX 5.301.XX, 5.302.XX, 5.303.XX, 5.304.XX, 5.305.XX, 5.306.XX e 5.307.XX.

**<VALR\_AGUA>**  
 Serão considerados lançamentos de água canalizada com o código modelo de documento = 29.

**<VALR\_OUTRAS\_ATIVIDADES>**  
 Serão considerados lançamentos de água canalizada com o código modelo de documento = 28.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **CAMPO** | **DESCRIÇÃO** | **ORIGEM DOS DADOS** |
| 01 | <CODG\_MUNICIPIO> | O município para o qual o valor foi informado. | Campo gerado com município informado no lançamento fiscal\Pasta Outros Dados\Prestação de Serviço |
| 02 | <CODG\_DETALHAMENTO> | Código para informa qual lista de detalhamento pertence o valor. |  |
| 03 | <VALR\_DETALHADO\_1> | Valor detalhado exceto quando for energia   elétrica, neste caso esse campo é gerado. | Campo gerado com o valor Contábil do Lançamento Fiscal |
| 04 | <VALR\_DETALHADO\_2>\* | Utilizado somente quando o valor a ser detalhado seja igual a energia elétrica (campo Distribuição). | Campo gerado com o valor Contábil do Lançamento Fiscal |
