---
content_hash: 652d01c8fe79e1701210370827ac5742091f35ad43a7b9457d55e370fbe0a9c2
fetched_at: '2026-06-29T00:09:00.381102+00:00'
page_id: '367238703'
product: rm
source: tdn-rm
title: DT Geração de Nosso Número e de Código de Barra Banco CREFISA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=367238703
version: 6
---

## Geração de Nosso Número e de Código de Barras CREFISA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Nosso Número | Geração de Nosso Número | | Geração de Código de Barras | Geração de Código de Barras | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7043><http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7042> |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQLServer;Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este documento visa demonstrar, de acordo com a liberação do documento “Especificações Técnicas para Confecção de Boletos de Cobrança do Nosso Banco – Versão 1 - Autbank” de 14/10/2013, o tratamento de geração de nosso número e código de barra para o Banco CREFISA (069).

## Definição da Regra de Negócio

### **Nosso Número**

A montagem para cálculo do DV do nosso número para o banco Crefisa (cod. febraban 069) é definido como  **AAAACCCNNNNNNNNNN**, onde

* **AAAA** é o código da agência do título, sem dv.
* **CCC** é o código da carteira (por exemplo, 121).
* **NNNNNNNNNN** é o nosso número, sem DV.

Para o cliente numerar seus títulos, o Banco deverá fornecer-lhe uma faixa de NOSSO NÚMERO, utilizando a faixa destinada à carteira escolhida.

* Para isso, acessar o Menu de Cobrança ® Operação ® Cedentes ® Nosso Número.
* Proceder à inserção de um registro para o cliente, na carteira escolhida, informando a quantidade e, quando se tratar da carteira 121, informar também a operação para a qual os títulos se destinam. Esta operação poderá ser de qualquer dos produtos das espécies de COBRANÇA (não de DESCONTO).

#### **Rotina Para Cálculo do DV do Nosso Número**

Sejam eles:

1. Multiplica-se cada algarismo do número formado pela composição dos campos acima pela sequência de multiplicadores 2,1,2,1,2,1,2 (posicionados da direita para a esquerda).
2. Se a multiplicação resultar > 9 (por exemplo = 12), somar os dígitos (1 + 2).
3. A seguir, somam-se os algarismos dos produtos e o total obtido é dividido por 10. O DV é a diferença entre o divisor (10) e o resto da divisão: 10 - (RESTO DA DIVISAO) = DV. Se o resto da divisão for zero, o DV é zero.

**Exemplo**

Agência: 0001.9 / Carteira: 121 / Nosso Número: 0004309540

A A A A C C C N N N N N N N N N N

**Pesos:**  2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2

Ou seja: 00011210004309540

Pesos: 21212121212121212

Parcial:   0 + 0 + 0 + 1 + 2 + 2 + 2 + 0 + 0 + 0 + 8 + 3 + 0 + 9 + (10) + 4 + 0

Final:      0 + 0 + 0 + 1 + 2 + 2 + 2 + 0 + 0 + 0 + 8 + 3 + 0 + 9 + (1 + 0) + 4 + 0

TOTAL:   32 / 10  RESTO ==> 2, então o DV = 8

O nosso número será a concatenação do nosso número e do DV do nosso número. No exemplo: 00043095408.

## **Código de Barras**

Segundo o documento “Especificações Técnicas para Confecção de Boletos de Cobrança do Nosso Banco – Versão 1 - Autbank” de 14/10/2013, o código de barras para o Banco CREFISA são representados por sequências numéricas, onde no momento do pagamento serão descodificados por uma leitora de dados. A seguir está disponível com maior detalhamento o layout que deverá ser respeitado para formulação do código de barras composto por 44 posições: 

|  |  |  |
| --- | --- | --- |
| **Posição** | **Tamanho** | **Conteúdo** |
| 01-03 | 3 | Identificação do Banco (Sem DV) |
| 04-04 | 1 | Moeda (9-Real, 0-Variável) |
| 05-05 | 1 | Dígito verificador do código de barras (Módulo 11) |
| 06-09 | 4 | Fator de Vencimento |
| 10-19 | 10 | Valor nominal do título. Quando moeda variável, preencher zerado |
| 20-44 | 25 | Campo livre – Utilizado de acordo com as especificações internas do banco |

### **Fator de Vencimento**

Trata-se de um referencial numérico de 4 dígitos, situado nas quatro primeiras posições do campo “valor”, que representa a quantidade de dias corridos da data base à data de vencimento do título. Cada data entre 03/07/2000 e 21/02/2025 possui um fator de vencimento específico.

Exemplos:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Fator** | **1000** | **1001** | **1002** | **5316** | **9998** | **9999** |
| Vencimento | 03/07/2000 | 04/07/2000 | 05/07/2000 | 27/04/2012 | 20/02/2025 | 21/02/2025 |
|  | Início |  |  |  |  | Limite |

A data 21/02/2025 é a data limite para a utilização da data base 07/10/1997, pois nesta data, o fator de vencimento atingirá “9999”, finalizando o seu ciclo de utilização.

Em 12/03/2014, um novo modelo estará valendo para o cálculo do fator de vencimento do código de barra/linha digitável. Este novo modelo, considera que não existe um fator de término, reiniciando o ciclo automaticamente ao atingir o fator “9999” (Comunicado FB-082/2012).

Definições:

* Processo contínuo: O modelo considera que não existe um fator de término, o ciclo reinicia automaticamente ao atingir o fator “9999”.
* O ciclo reiniciará em 22/02/2025, com o fator “1000”.

### **Preenchimento do Campo Livre**

Composto por 25 dígitos. Cada banco define o formato do seu campo livre, com o intuito de identificação do mesmo em seus sistemas. Para os boletos do banco CREFISA, a definição do campo livre é composta dos seguintes dados:

|  |  |  |
| --- | --- | --- |
| **Posição** | **Tamanho** | **Conteúdo** |
| 01 – 04 | 4 | Código da Agência (Sem DV) |
| 05 – 07 | 3 | Número da Carteira do Título |
| 08-14 | 7 | Número da Operação |
| 15-25 | 11 | Nosso Número (Com DV) |

**Linha digitável**

Composição

|  |  |  |  |
| --- | --- | --- | --- |
| Posição | Tamanho | \*\* | Conteúdo |
| 01-03 | 3 | Campo 1 | Identificação do banco (Sem DV) |
| 04-04 | 1 | Código de moeda (9 – Real, 0 - Dólar) |
| 05-09 | 5 | Cinco primeiras posições do campo livre (posições 20 a 24 do código de barras) |
| 10-10 | 1 | Dígito verificador do primeiro campo. |
| 11-20 | 10 | Campo 2 | 6ª a 15ª posições do campo livre (posições 25 a 34 do código de barras) |
| 21-21 | 1 | Dígito verificador do segundo campo. |
| 22-31 | 10 | Campo 3 | 16ª a 25ª posições do campo livre (posições 35 a 44 do código de barras) |
| 32-32 | 1 | Dígito verificador do terceiro campo |
| 33-33 | 1 | Campo 4 | Dígito verificador geral (posição 5 do código de barras) |
| 34 a 37 | 4 | Campo 5 | Posições 34 a 37 – fator de vencimento (posições 6 a 9 do código de barras) |
| 38 a 47 | 10 | Posições 38 a 47 – valor nominal do título(posições 10 a 19 do código de barras) |

**Exemplo:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **99997.77213** | **30530.150082** | **18975.000003** | **1** | **10010000035000** |
| 1º campo | 2º campo | 3º campo | 4º campo (DV) | 5º campo (Fator de Vencimento / Valor |

**Relatório para impressão de boletos do banco Crefisa.**

O relatório está disponível na pasta Objetos Gerenciais: **FINREL0040 - Boleto Crefisa.**

Após importação do relatório via RM Reports, o mesmo estará disponível na visão de boletos possibilitando a impressão dos títulos conforme padrões Crefisa.
