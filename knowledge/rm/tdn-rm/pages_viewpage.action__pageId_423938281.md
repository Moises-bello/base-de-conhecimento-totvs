---
content_hash: d46ef2786bf23e8217dc88157b714c4446672a37ae3e7ea937d94271b61f4f67
fetched_at: '2026-06-29T00:09:26.146442+00:00'
page_id: '423938281'
product: rm
source: tdn-rm
title: Importação de Avaliação Patrimonial 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938281
version: 6
---

O Totvs Gestão Patrimonial disponibiliza através do menu Operações Patrimoniais | Avaliação Patrimonial | Importar Avaliação Patrimonial a funcionalidade que permite realizar avaliações patrimoniais em patrimônios já cadastrados no sistema. A importação é realizada via arquivo texto. Todos os campos deverão ser separados por barra vertical (|).

**Cenário de cálculo**

Deverá ser informado o cenário que será atualizado para avaliação.

**Arquivo**

Deverá ser informado o caminho do arquivo texto, contendo as informações para atualização.

**Esta importação é para implantação?  (SIM)**

Essa opção poderá ser marcada quando se tratar de um processo de implantação, ou seja, a avaliação não será realizada para o período de cálculo. O sistema irá apenas inserir o valor de avaliação nos patrimônios envolvidos e marca-los como avaliado, porém esses patrimônios não poderão ter cálculo de depreciação anterior ao período de cálculo, apenas depreciação acumulada.

**Observação importante:**Não é permitido utilizar esta opção **marcada** para patrimônios adquiridos dentro ou superior ao período atual de cálculo, porque marcando essa opção não é gerada a ocorrência de avaliação.

Layout:

|  |  |
| --- | --- |
| 1 | Código do patrimônio |
| 2 | Valor de mercado ou valor absoluto da avaliação |
| 3 | Depreciação acumulada corrigida ou Valor realizado da avaliação |
| 4 | Valor residual do patrimônio |

**Coluna 1: Código do Patrimônio de acordo com a máscara definida no sistema.**

**Coluna 2: Valor de mercado ou valor absoluto da avaliação** (valor decimal separado por ponto (.) Exemplo: 1000.00).

Exemplo - Na data da avaliação o bem possuía os seguintes valores:

Valor Base = 10.000,00

Depreciação acumulada = 5.000,00

Valor contábil = 5.000,00

O valor de Mercado do bem foi avaliado em 7.000,00. Se optar por valor de mercado na importação deve-se informar no arquivo 7000.00, se optar pelo valor da avaliação deve-se informar no arquivo 2000.00.

**Coluna 3: Depreciação acumulada corrigida ou Valor realizado da avaliação** (valor decimal separado por ponto (.) Exemplo: 1000.00). No caso de utilizar o valor absoluto da avaliação na coluna 2, a coluna 3 deve ser preenchida com o valor realizado da avaliação patrimonial.

Exemplo - Se na coluna 2 foi informado o valor de mercado do bem (7000.00), deve-se informar a depreciação acumulada total do bem na coluna 3. Se foi informado o valor de (2000.00) na coluna 2 (valor absoluto) deve informar a realização acumulada deste valor, ou seja, dos 2000.00 de avaliação quanto já foi realizado.

**Coluna 4: Valor residual do patrimônio** (valor contábil limite para depreciação).

Exemplo de uma linha do arquivo para implantação: 01.01.001|10000.00|5000.00|1000.00

**Esta importação é para implantação? (NÃO)**

O sistema também permite que seja realizada a importação da avaliação para o período de cálculo, substituindo assim, o processo de avaliação patrimonial. Basta **não** marcar a opção "Esta importação é para implantação?". O sistema irá gerar uma ocorrência para cada patrimônio avaliado, que poderá ser validada e posteriormente contabilizada no menu Operações Patrimoniais | Consulta/Cancela | Ver Avaliação Patrimonial.

Layout:

|  |  |
| --- | --- |
| 1 | Código do patrimônio |
| 2 | Valor de mercado ou valor absoluto da avaliação |
| 3 | Depreciação acumulada corrigida ou Valor realizado da avaliação |
| 4 | Valor residual do patrimônio |
| 5 | Vida útil restante em meses |
| 6 | Data da avaliação |
| 7 | Data do laudo |
| 8 | Número do laudo |
| 9 | Responsável |

**Coluna 1: Código do Patrimônio de acordo com a máscara definida no sistema.**

**Coluna 2: Valor de mercado ou valor absoluto da avaliação** (valor decimal separado por ponto (.) Exemplo: 1000.00).

Exemplo - Na data da avaliação o bem possuía os seguintes valores:

Valor Base = 10.000,00

Depreciação Acumulada = 5.000,00

Valor contábil = 5.000,00

O valor de Mercado do bem foi avaliado em 7.000,00. Se optar por valor de mercado na importação deve-se informar no arquivo 7000.00, se optar pelo valor da avaliação deve-se informar no arquivo 2000.00.

**Coluna 3: Depreciação acumulada corrigida ou Valor realizado da avaliação** (valor decimal separado por ponto (.) Exemplo: 1000.00). No caso de utilizar o valor absoluto da avaliação na coluna 2, a coluna 3 deve ser preenchida com o valor realizado da avaliação patrimonial.

Exemplo - Se na coluna 2 foi informado o valor de mercado do bem (7000.00), deve-se informar a depreciação acumulada total do bem na coluna 3. Se foi informado o valor de (2000.00) na coluna 2 (valor absoluto) deve informar a realização acumulada deste valor, ou seja, dos 2000.00 de avaliação quanto já foi realizado.

**Coluna 4: Valor residual do patrimônio** (valor contábil limite para depreciação)

**Coluna 5: Vida útil restante em meses** (somente o número. Exemplo: para 1 ano, inserir o número 12).

**Coluna 6: Data da avaliação** (data no formado dd/mm/aaaa).

**Coluna 7: Data do laudo** (data no formado dd/mm/aaaa).

**Coluna 8: Número do laudo** (até 20 caracteres não podendo conter o caractere "|")

**Coluna 9: Responsável pelo laudo** (o nome do responsável deve conter até 40 caracteres não podendo conter o caractere "|").

Exemplo de uma linha do arquivo: 01.01.001|10000.00|5000.00|1000.00|30|01/03/2016|01/03/2016|1234567890|JOSÉ DA SILVA

**O arquivo contém somente valores absolutos de Avaliação/Realização?**

Essa opção deverá ser marcada quando o campo 2 utilizar o valor absoluto da avaliação. Quando utilizar o valor de mercado está opção deverá ser desmarcada.

**Contabilizar?**

Com esta opção marcada o sistema irá gerar a ocorrência com contabilização pendente. Estando desmarcada a ocorrência será gerada como "não contabilizar".
