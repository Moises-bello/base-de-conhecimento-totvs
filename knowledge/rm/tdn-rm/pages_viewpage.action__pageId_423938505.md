---
content_hash: e9facfffcef067602060b6e699afd04d050ec24459a4a806f8627aee85ceefc9
fetched_at: '2026-06-29T00:09:27.346801+00:00'
page_id: '423938505'
product: rm
source: tdn-rm
title: Layout de Importação de Lançamento Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938505
version: 13
---

**Importante**

Atualmente no TOTVS Gestão Contábil a importação de lançamento contábil é a única que faz uso do novo modelo de conceito, este modelo se diferencia do modelo anterior no momento de informar o arquivo texto para a importação, esta etapa agora está disponível diretamente no momento da importação (Processamento do conceito) do processo.

Outra novidade, é que também foi disponibilizado um conceito (Importação Lançamentos Contábeis (Arquivo Delimitado).concept), que permite ao usuário montar um arquivo delimitando os campos. Utilizando este conceito, o usuário pode utilizar um ";" para delimitar o fim de cada campo, respeitando sempre o seu tamanho máximo.

**Observação**

O novo modelo de conceito utilizado na importação de lançamentos contábeis se aplica somente a versão 12. Outro detalhe é que mesmo no novo modelo de conceito não é possível fazer a importação de forma parcial, ou seja, caso algum erro ocorra será necessário corrigir e importar novamente pois nenhuma linha será gravada no caso de erro. Apesar de no novo modelo de conceito disponibilizar a opção de "Continuar a execução mesmo com erros (opção presente em todos os conceitos do novo modelo)" a mesma não é considerada para o conceito em questão por questões de limitação da arquitetura utilizada para gravação dos dados.

As informações do layout relatado abaixo deverão ser disponibilizadas em um único arquivo, ou seja, os dados referentes a Capa do lançamento, Partidas do lançamento, Distribuição gerencial (Rateio) e campo complementar, devem ser inseridas no mesmo arquivo, pois no momento da importação o sistema irá distinguir a informação através do identificador de Linha. Cada informação deve ser preenchida em linhas diferentes, pois para cada uma existe um identificador de linha que deve estar na primeira posição da linha.

**Observações**

A coluna "Obrigatório" consiste na obrigatoriedade ou não do preenchimento do campo. Quando informado com "X", o mesmo tem s do campo. Quando vazio, não é necessário o preenchimento do mesmo.

Para realizar a importação dos lançamentos contábeis, é necessário que o lote para onde os mesmos serão importados já existam no cadastro de lotes da contabilidade. Exemplo: Se desejo importar para o lote 1012, obrigatoriamente o lote 1012 deve constar no cadastro de lotes.

**1 - Lançamento**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| # | **Descrição** | **Tipo** | **Tamanho** | **Posição Inicial** | **Posição Final** | **Obrigatório** | **Observação** |
| **0** | Indicador de Linha | Alfa | 1 | 1 | 1 | X | "M" → Indica registro Mestre |
| **1** | Código do lote | Numérico | 10 | 2 | 11 | X |  |
| **2** | Descrição | Alfanumérico | 100 | 12 | 111 | X |  |
| **3** | Data da inclusão | Alfanumérico | 10 | 112 | 121 | X |  |

**1.1 - Partidas do Lançamento**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| # | **Descrição** | **Tipo** | **Tamanho** | **Posição Inicial** | **Posição Final** | **Obrigatório** | **Observação** |
| **1** | Identificador da Linha | \*P | 2 | 1 | 2 | X | \*P → Indicador Linha Partida |
| **2** | Nº Documento | Alfanumérico | 20 | 3 | 22 |  |  |
| **3** | Conta de Débito | Alfanumérico | 40 | 23 | 62 |  |  |
| **4** | Conta de Crédito | Alfanumérico | 40 | 63 | 102 |  |  |
| **5** | Conta de Contra Partida | Alfanumérico | 40 | 103 | 142 |  |  |
| **6** | Valor | Numérico com 2 decimais | 15 | 143 | 157 | X |  |
| **7** | Código do Histórico | Alfanumérico | 10 | 158 | 167 |  |  |
| **8** | Complemento do Histórico | Alfanumérico | 250 | 168 | 417 |  |  |
| **9** | Filial | Numérico | 3 | 418 | 420 | X |  |
| **10** | Centro de Custo | Alfanumérico | 25 | 421 | 445 |  |  |
| **11** | Departamento | Alfanumérico | 25 | 446 | 470 |  | As partidas podem conter departamentos ativos ou inativos. |
| **12** | 2º Data | Alfanumérico | 10 | 471 | 480 |  |  |
| **13** | 2º Valor | Numérico com 2 decimais | 15 | 481 | 495 |  |  |
| **14** | Código do Participante | Numérico | 4 | 496 | 499 |  |  |
| **15** | Código do Lote de Origem | Numérico | 10 | 500 | 509 |  |  |
| **16** | Coligada da Eliminação | Numérico | 2 | 510 | 511 |  |  |
| **17** | Coligada da conta de Eliminação | Numérico | 2 | 512 | 513 |  |  |
| **18** | Conta de Eliminação | Alfanumérico | 40 | 514 | 554 |  |  |

**1.2 - Distribuição Gerencial (Rateio)**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| # | **Descrição** | **Tipo** | **Tamanho** | **Posição Inicial** | **Posição Final** | **Obrigatório** | **Observação** |
| **1** | Identificador da Linha | \*RD ou  \*RC | 3 | 1 | 3 | X | \*RC Rateio a Credito  \*RD Rateio a Debito |
| **2** | Conta Gerencial | Alfanumérico | 40 | 4 | 43 | X |  |
| **3** | Valor do Rateio | Numérico com 2 decimais | 15 | 44 | 58 | X |  |

**1.3 - Campos Complementares da Partida**

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **Descrição** | **Tipo** | **Tamanho** | **Posição Inicial** | **Posição Final** | **Obrigatório** | **Observação** |
| **1** | Identificador da Linha | \*CP | 3 | 1 | 3 | X | Identificador de linha Complementar de Lançamentos |
| **2** | Nome do Campo Complementar | Alfanumérico | 20 | 4 | 23 | X |  |
| **3** | Valor do Campo Complementar | Sem restrições | 255 | 24 | 278 | X |  |

**Observações**

* Quando a conta exigir rateio e não foi informado o rateio, será considerado o rateio default cadastrado no plano de contas.
* Todos os campos referentes a valor devem ser inseridos no arquivo da esquerda para a direita, respeitando o limite de seu tamanho.

Atenção

Serão realizadas as seguintes consistências com relação aos Valores da Partida:

* Com o Parâmetro "*Usa 2º Valor*" **Marcado** o arquivo não será importado se o Valor Principal e 2º Valor estiverem **Zerados** ou se algum dos dois valores estiver **Negativo;**
* Com o Parâmetro "*Usa 2º Valor*" **Desarcado** o arquivo não será importado se o Valor Principal estiver **Zerado** ou se algum dos dois valores estiver **Negativo.**
