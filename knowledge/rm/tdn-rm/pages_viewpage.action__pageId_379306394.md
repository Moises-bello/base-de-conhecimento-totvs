---
content_hash: 1e569dac8a87391ba09c7473545bf5502a73520e6812d27575fd6ce18f85eaf3
fetched_at: '2026-06-29T00:09:02.396675+00:00'
page_id: '379306394'
product: rm
source: tdn-rm
title: DT Integração Bancária com Banco CECRED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379306394
version: 8
---

## Configurações bancárias com a integração com o banco CECRED

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Nosso Número | Geração de Nosso Número | | Geração de Código de Barras | Geração de Código de Barras | | Impressão de Boletos | Impressão de Boletos | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7016> <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7015> |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQLServer;Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este documento visa demonstrar, de acordo com a liberação do documento “Manual Técnico de Cobrança Bancária Geração de Boleto Pelo Software do Cooperado Padrão CNAB 240 Posições” versão 07 de Agosto de 2016, o tratamento de geração de nosso número e código de barra para o Banco CECRED (085).

## Definição da Regra de Negócio

### **Nosso Número**

É composto por 17 dígitos incluindo o dígito verificador da conta corrente e, deve ser gerado por meio de sequenciais diferentes, não podendo retroagir ou repetir numeração já processada, utiliza-se o número do boleto (nosso número) como critério sequencial. Sugere-se a emissão em produção pelo boleto n°1. O quadro abaixo explica como compor este campo definido como **CCCCCCCdNNNNNNNNN**:

| Posição | Conteúdo |
| --- | --- |
| 8 primeiros dígitos | Conta correte + dv do cooperado (Sempre será fixo) |
| 9 dígitos restantes | Número do boleto (Sequencial) |

## **Código de Barras**

Segundo o documento “Manual Técnico de Cobrança Bancária Geração de Boleto Pelo Software do Cooperado Padrão CNAB 240 Posições” versão 07 de Agosto de 2016, o código de barras para o Banco CECRED 085 são representados por sequências numéricas, onde no momento do pagamento serão descodificados por uma leitora de dados. No quadro abaixo está disponível com maior detalhamento, o leiaute que deverá ser respeitado pela formulação do código de barras:

|  |  |  |
| --- | --- | --- |
| **Posição** | **Tamanho** | **Conteúdo** |
| 01-03 | 3 | Identificação do Banco - 085 |
| 04-04 | 1 | Código da Moeda (9-Real) |
| 05-05 | 1 | Dígito verificador do código de barras (DV Módulo 11) |
| 06-09 | 4 | Fator de Vencimento |
| 10-19 | 10 | Valor nominal do título |
| 20-44 | 25 | Campo livre – Utilizado de acordo com as especificações internas do banco |

#### **Rotina Para Cálculo do DV do Código de barras**

Para cálculo do dígito verificador, que deverá constar na quarta posição do código de barras, deverá ser feita a seguinte montagem:

Definir uma área auxiliar de 43 posições subdivididas em dois campos. O primeiro deverá conter informações do Banco "085". O segundo campo deverá conter as 40 posições restantes;

Calcular o módulo 11, conforme acima, das 43 posições;

Montar o campo para impressão no código de barras, com as três primeiras posições (n° da instituição), o DAC já calculado, e as 40 posições restantes.

**Exemplo**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Banco** | | | **Código de Barra** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| 0 | 8 | 5 | 9 | 7 | 5 | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 5 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 | 0 | 0 | 0 | 0 | 8 | 8 | 6 | 2 | 1 | 1 | **DV: 8** |
| 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | **MOD:3** |
| 0 | 24 | 10 | 81 | 56 | 35 | 42 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 48 | 25 | 0 | 3 | 4 | 27 | 32 | 35 | 36 | 35 | 0 | 0 | 0 | 0 | 0 | 56 | 48 | 30 | 8 | 3 | 2 | **= 685** |

B B B N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N N

**Pesos:**  9 8 7 6 5 4 3 2

Ou seja: 08598757400000005000000850123456700000886211

Pesos: 4329876543298765432987654329876543298765432

Parcial:   0+24+10+81+56+35+42+20+0+0+0+0+0+0+0+25+0+0+0+0+0+0+48+25+0+3+4+27+32+35+36+35+0+0+0+0+0+56+48+30+8+3+2 = 685

TOTAL:   685 / 11 = 62 resto 3;

Divisão: 11 - 3 = 8 DV.

No caso do dígito verificador ser "1",  acontece pelo motivo em que, quando o resto da divisão for igual a 0 ou 1, deverá ser atribuído ao dígito verificador o dígito "1". Se o resultado for 10, ou 11, também atribui-se ao dígito verificar o dígito "1".

Portanto, podemos concluir que o DAC da sequência numérica principal é igual a "8".

**Subtrai-se o Mod 11 sobre o resto da divisão:** 11 - 3 obtendo DAC igual a 8.

Observação: Quando o resto da divisão for igual a 0,10 ou 11, atribui-se o dígito verificador o dígito "1".

### **Fator de Vencimento**

O fator de vencimento está localizado no campo 5, posições 34 a 37 da linha digitável e nas posições 06 até 09 do código de barras. Para obter o fator de vencimento podem ser utilizados duas fórmulas:

**Fórmula sobre data base**

* Para vencimento até 21/02/2025 deverá ser utilizada a data base de 07.10.1997, calculando o número de dias entre essa data e a do vencimento (data de vencimento menos data base = fator)

|  |  |
| --- | --- |
| Vencimento | 03.07.2000 |
| Data Base | -07.10.1997 |
| Fator de Vencimento | 1000 |

* A partir do dia 22/02/2025 deverá ser considerado a sequência de um novo fator com numeração 1000.

|  |  |
| --- | --- |
| Vencimento | 22.02.2025 |
| Data Base | -22.02.2025 |
| Fator de Vencimento | 1000 |

**Tabela de correlação data/fator**

Iniciando pelo fator 1000, que corresponde à data de vencimento 03.07.2000, e assim sucessivamente.

| FATOR | VENCIMENTO |
| --- | --- |
| 1000 | 03.07.2000 |
| 1002 | 05.07.2000 |
| 1667 | 01.05.2002 |
| 4789 | 17.11.2010 |
| 9999 | 21.02.2025 |

**Observações:**

* Quando a primeira posição do campo "valor" (fator de vencimento + valor) for zero, significa que no código de barras / linha digitável desse titulo, não consta o fator de vencimento;
* Boletos com vencimento "à vista" ou "na apresentação" - somam-se 15 dias corridos à "data do processamento". O resultado desta operação representa a data do vencimento, cujo fator correspondente deve constar no código de barras (posições 6 a 9) e na linha digitável (posições 34 a 37).

**Preenchimento do Campo Livre**

Composto por 25 dígitos. Cada banco define o formato do seu campo livre, com o intuito de identificação do mesmo em seus sistemas. Para os boletos do banco CECRED, a definição do campo livre é composta dos seguintes dados:

|  |  |  |
| --- | --- | --- |
| **Posição** | **Tamanho** | **Conteúdo** |
| 01 – 06 | 6 | Número do Convênio da Cooperativa |
| 06 – 14 | 8 | Número da Conta Corrente + dv |
| 14-23 | 9 | Número do Boleto (Nosso Número) |
| 23-25 | 2 | Código da Carteira |

**Linha digitável**

A linha digitável de um boleto 085 é composta por cinco campos.

Alguns valores sempre serão fixos e sem variação. Segue abaixo, tabela que demonstra com maiores detalhes os valores que sempre serão fixos:

| CAMPO 1 | CAMPO 2 | CAMPO 3 |
| --- | --- | --- |
| Banco 085 | Número do Convênio | Número da Carteira |
| Moeda Real | Número da Conta Corrente | - |
| Número do Convênio | - | - |
| Dígito Verificador | - | - |

**Nota:**O número do convênio, conta corrente e carteira devem ser solicitados à Cooperativa filiada que está fornecendo o serviço CECRED Cobrança.

Cálculo do dígito verificador para Linha Digitável

As colunas que serão utilizadas para identificação DAC correspondem aos campos 1, 2 e 3, calculando cada um deles separadamente.

Para a linha digitável utilizaremos o DAC (Dígito de Auto - Conferência) do módulo 10, no qual é calculado multiplicando cada algarismo, pela sequência de multiplicadores 2,1,2,1 posicionados da direita para a esquerda. A soma dos algarismos do produto é dividida por 10, com isso o DAC será a diferença entre o divisor (10) da divisão: DAC = 10 menos (-) o resto da divisão.

**Observação:** Se o resto da subtração for igual a 10 (dez), o dígito verificador será igual a 0 (zero).

**Método de Cálculo**

Segue um exemplo simples e objetivo do método para cálculo do DAC 10. Utilizaremos o campo 1 da figura anterior como demonstração.  Segue abaixo o método para calcular:

Multiplique a numeração principal pela sequência 2,1,2,1 (da direita para a esquerda).

**Pesos:**  2, 1, 2, 1

Ou seja: 0 8 5 9 0 0 0 0 0

Pesos: 2 1 2 1 2 1 2 1 2

Resultado: 0 8 10 9 0 0 0 0 0

Observação: Todos os resultados com 2 números, como por exemplo "10", deve-se somar 1 + 0. Com resultado obtido, soma-se a sequência numérica: 0+8+1+0+9+0+0+0+0+0 = 18

Na próxima etapa divide-se o resultado por 10: 18 / 10 = 1,8 resto = 8.

DAC = 10 - (resto da divisão), portanto 10 - 8 = 2;

O DAC da sequência numérica é igual a "2" desta forma o campo 1 da linha digitável será representado pela sequência 0 8 5 9 0 0 0 0 0 2.

**Relatório para impressão de boletos do banco Cecred.**

O relatório está disponível na pasta Objetos Gerenciais: **FINREL0041 - Boleto Cecred.**

Após importação do relatório via RM Reports, o mesmo estará disponível na visão de boletos possibilitando a impressão dos títulos conforme padrões Cecred.

**Remessa de cobrança eletrônica - Layout do gerador de saídas**

Para realizar a remessa para o banco CECRED, será necessário importar o layout do gerador de saídas FINLAY0001 - Cob. FEBRABAN CNAB240.TotvsGen disponível na pasta de instalação do sistema e parametrizá-lo no convênio.

C:\totvs\CorporeRM\ObjetosGerenciais\Layout
