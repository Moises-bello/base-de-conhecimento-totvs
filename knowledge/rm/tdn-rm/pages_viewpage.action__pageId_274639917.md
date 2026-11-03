---
content_hash: 03300c884b4320d2bf8f299a271628df8f3ed6a9f45bf1a2641f7e774802195f
fetched_at: '2026-06-29T00:08:34.046940+00:00'
page_id: '274639917'
product: rm
source: tdn-rm
title: 631236 MATESTCNTFTOF01-202 DT - VI e VO para Cálculo do Conteúdo de Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274639917
version: 116
---

# Ficha de Conteúdo de Importação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Estoque Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Produto | Cálculo de Ficha de Conteúdo de Importação* | *Cálculo de Ficha de Conteúdo de Importação* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Estoque | Produção* | *Produção* | |  |  | |
| **Cadastros Iniciais:** | *Cadastrar Atividades, Estruturas e Componentes.*  **Cadastrar Produto (insumos): Procedência/Origem.**  ***Cadastrar fórmula para o Valor Total da Operação.*** |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | 631236 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-202 |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

A partir de 01 de janeiro de 2013, nas operações **interestaduais** destinadas a **contribuintes do ICMS**, de bens e mercadorias **industrializadas**, que possuem em sua composição **insumos importados** (sejam adquiridos diretamente do exterior ou no mercador nacional) e bens e mercadorias importadas para **revenda**, terão uma alíquota de 4% para o ICMS.

A alíquota de 4% só será aplicada se, após o desembaraço aduaneiro, os produtos importados:

* Não tiverem sido submetidos a processo de industrialização; ou
* Se submetidos a processo de industrialização, resultarem em mercadorias ou bens com Conteúdo de Importação – CI superior a 40%

CI - Conteúdo de Importação:

Percentual correspondente ao quociente entre o Valor da Parcela Importada do exterior **(VI)** e o valor total da operação de saída interestadual da mercadoria ou bem submetido ao processo de industrialização **(VO)**.

**CI = (VI ÷ VO) × 100**

Consideramos:

**VI -** **Valor da Parcela Importada**

1. Quando o bem ou produto for importado diretamente do exterior

O Valor Aduaneiro, ou seja, o valor FOB da mercadoria importada, acrescidos dos valores de frete e seguro internacional.

1. Quando o bem ou produto importado for adquirido no mercado nacional:

a)       Não submetido a processo de industrialização:

Valor que consta no documento fiscal emitido pelo remetente (fornecedor), excluindo os valores do ICMS e IPI.

b)       Submetido ao processo de industrialização e que possui mais de 40% de seus componentes importados:

Valor informado no documento fiscal emitido pelo remetente (fornecedor), excluído os valores de ICMS e IPI. Nesse caso deverá também ser observado o percentual que o produto possui de componentes importados para definição do percentual a ser considerado na composição do novo produto que vai utilizar esse como parte do mesmo.

* Produtos adquiridos no mercado nacional que possuir percentual de produto importado menor que 40%, será considerado como inteiramente nacional;

* Produtos adquiridos no mercador nacional que possuir percentual de produto importado maior que 40% e menor que 70%, será considerado 50% do valor como importado;

* Produtos adquiridos do Mercado nacional que possuir percentual de produto importado maior que 70%, será considerado 100% do valor como produto importado.

Observações:

* Valor unitário da parcela importada do exterior é obtido pela média aritmética ponderada praticada no penúltimo período de apuração.

* Na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, deverá buscar nos períodos anteriores até encontrar um período que tenha ocorrido à operação.

**VO – Valor Total da Operação de Saída Interestadual**

Valor das operações de saída interestadual, obtido no penúltimo período de apuração, excluindo os valores de ICMS e IPI.

Observação:

* Caso não tenha ocorrido nenhuma saída interestadual no penúltimo período de apuração, a empresa pode considerar as operações internas do penúltimo período de apuração, excluindo os valores de ICMS e IPI.

* Na hipótese de não ter ocorrido operação de saída interna no penúltimo período de apuração, deverá buscar nos períodos anteriores até encontrar um período que tenha ocorrido a operação.

*Fonte: Especificação VI e VO para Cálculo Conteúdo de Importação*

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.14.160*

## Procedimento para Utilização

 

Parametrização e Cadastros necessários para implantação do cálculo:

 

###### 1.       Cadastrar: Atividade, Estrutura e Componentes:

 

Para identificar se na composição dos Produtos Industrializados existem insumos importados, será necessário trabalhar com o conceito de **Atividade**, **Estrutura** e **Componente**.

 

*Acesse*:

 

MDI - | Estoque | Produção |

 

Delphi - | Cadastros | Tabelas de Produção |

 

Sugestão para o cadastro em clientes que não possuem o módulo TOTVS Planejamento e Controle da Produção

 

Atividade

 

Sugiro criar uma atividade exclusiva para esse cálculo: CCI – Cálculo Conteúdo de Importação

 

Estrutura

 

Deve existir uma Estrutura para cada Produto Industrializado. Sugiro inclusive, cadastrar como código da estrutura, o mesmo código do produto industrializado.

 

Componente

 

Nessa tabela será informada a composição de cada estrutura (PI). Nela deve-se informar a quantidade usada de cada componente (insumo).

 

1. *2.**Cadastro Produto (insumos): Procedência/Origem devidamente cadastrada*

 

Para que o insumo entre no cálculo do Conteúdo de Importação, o mesmo deve estar classificado, em seu cadastro com as seguintes Procedências/Origens:

 

**1 – Estrangeira – Importação direta, exceto a indicada no código 6;**

 

**2 – Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7;**

 

**3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%.**

 

**8 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%**

 

Observação: Pode acontecer de um único código de produto (componente/insumo) de procedência/origem estrangeira, ser adquirido diretamente do exterior (1) ou ser adquirido no mercado interno (2). Neste caso, deve-se informar na procedência/origem, a procedência/origem principal.

 

1. *3.**Cadastrar fórmula para o Valor Total da Operação, seja de Importação ou Saída. (Nas explicações abaixo estaremos utilizando a nomenclatura ‘**For\_VTO**’ para referenciar a esta fórmula).*

 

Essa fórmula atenderá tanto o cálculo do **VI** quanto do **VO.**

 

Como o valor a ser considerado pode variar entre importação direta e aquisições no mercado interno, e operações de saída, foi criada uma fórmula para que cada empresa defina como será o cálculo do valor unitário de suas operações.

 

Essa fórmula deve ser executada no contexto do item de movimento (utilizar variáveis e funções que retornem valores do item de movimento) e deve retornar o Valor Total do Item, ou seja, não deve retornar o valor unitário do item.

 

Observação: Se houver necessidade, essa fórmula deve possuir a condição ‘SE’ para tratar de forma diferenciada movimentação de entrada (importação) de movimentações de saída.

 

A execução do processo no RM:

 

O Cálculo do Conteúdo de Importação é um **processo** da visão de **Produtos**. O mesmo pode ser executado pelo TOTVS Gestão Fiscal ou pelo TOTVS Gestão de Estoque, Compras e Faturamento.

 

O cálculo será executado para todos os produtos selecionados na visão (sugiro fazer um filtro com os produtos industrializados que possuem em sua composição insumos importados).

 

Com os produtos selecionados, clique em: **| Processos | Cálculo Conteúdo de Importação |**.

 

Na tela de execução do processo informe:

 

**Filial** informe a filial na qual as movimentações serão pesquisadas.

 

**Fórmula VI e VO**informe a fórmula criada para calcular o Valor da Operação, seja de Importação ou Saída (**For\_VTO**).

 

**Data último período de apuração** informe o último Período de Apuração Encerrado.

 

**Gerar Log de Cálculo** à flag para indicar se deverá ser gerado um Log com as movimentações selecionadas para o cálculo do CI. Dependendo do volume de produtos selecionados, do volume de movimentações e da complexidade da fórmula, a execução desse log poderá comprometer a performance do processo.

 

Observação: Os movimentos serão filtrados de acordo com a Filial informada.

 

Se a empresa possuir movimentações em várias filiais, antes da execução desse processo, será necessário selecionar, a filial no qual os movimentos devem ser pesquisados.

 

O Cálculo do VI no RM:

 

Para cada Produto Industrializado selecionado para o cálculo o sistema fará:

 

1. Identificar no cadastro de Estrutura/Componente, os componentes (insumos) cujo campo de Procedência/Origem da tabela de Produtos possui as opções:

 

(1)     Estrangeira – Importação direta, exceto a indiada no código 6;

 

(2)     Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7;

 

(3)     Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou menor que 70%;

 

(8)  Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%

 

1. O cálculo varia de acordo com a Procedência/Origem do componente (insumo), conforme descrito abaixo:

 

Observação: Para os produtos cadastrados com procedência/origem (1) e (2), o sistema sempre irá verificar se existe movimentação com importação direta ou adquirida no mercado interno, ou seja, serão sempre executados os processos 2.1 e 2.2 descritos abaixo. Isso, para evitar a duplicidade do cadastro de produto, uma vez que o mesmo código pode ser adquirido dentro ou fora do país.

 

**2.1.****Procedência/Origem** = **1 – Estrangeira, Importação direta exceto a indicada no código 6**

 

a)      Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de entrada selecionada.

 

*Considerar*:

 

* Movimentos de entrada por importação:

 

Código do Tipo de Movimento iniciado com **1.2.%** e

 

Emitente/Destinatário = **Empresa** / **Empresa** e

 

Código da Natureza de Operação do Item iniciado com **3.101%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      Somar a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (**QTI**).

 

c)       Calcular o Valor Unitário de Importação (**VUI**)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Final Importado do Insumo/componente (VFII)

 

O Valor Importado do Insumo/componente corresponde ao produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

**2.2. Procedência/Origem = 2 – Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7**

 

a)      Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de entrada selecionada.

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**  e

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      **SOMAR** a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (**QTI**).

 

c)       Calcular o Valor Unitário de Importação (**VUI**)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Final Importado do Insumo/componente (VFII)

 

O Valor Importado do Insumo/componente corresponde ao produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

**2.3.****Procedência/Origem =** **3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e igual ou inferior a 70%**

 

a)      Calcular o Valor Total Importado (For\_VTO) para cada nota fiscal de entrada selecionada

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação.

 

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

c)       Calcular o Valor Unitário de Importação (VUI)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Importado do Insumo/componente (VII)

 

O Valor Importado do Insumo/componente corresponde 50% do produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA) × 0,50**

 

Observação: Na procedência/origem 3 - Nacional, mercadoria ou bem com CI superior a 40% e igual ou inferior a 70%, será considerado 50% do resultado

 

**2.4.****Procedência/Origem = 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%**

 

a)      Calcular o Valor Total Importado (For\_VTO) para cada nota fiscal de entrada selecionada

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%, **2.151%****

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação.

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

c)       Calcular o Valor Unitário de Importação (VUI)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Importado do Insumo/componente (VII)

 

O Valor Importado do Insumo/componente corresponde 100% do produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

1. O Valor de Importação do Produto Industrializado (**VI**) será:

 

A SOMA de todos os valores finais de importação dos insumos/componentes do produto industrializado em questão:

 

**I = Soma (VFII)**

 

O Cálculo do VO no RM:

 

Para cada Produto Industrializado selecionado para o cálculo o sistema fará:

 

1. Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de saída selecionada:

 

*Considerar*:

 

* Movimentos de saída:

 

Código do Tipo de Movimento iniciado com **2.2%** e

 

Emitente / Destinatário = **Empresa / Cliente**  e

 

Código da Natureza de Operação do Item iniciado com:

 

**6.101.%, 6.103.%, 6.105.%, 6.109.%, 6.111.%, 6.113.%, 6.116.%, 6.118.%, 6.122.%, 6.151.%, 6.155.%, 6.401.%, 6.402.%, 6.651.%, 6.652.%, 5%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de saída interestadual no penúltimo período de apuração, buscar operações de saída internas (iniciadas com 5). Se não existir movimentação, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação (interestadual/interna). O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

1. SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

1. Calcular o Valor Total Operação de Saída (VO)

 

O Valor Total das Operações de Saída corresponde ao quociente entre a SOMA de todos os Valores Total de Operação (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VO = Soma(For\_VTO) ÷ Soma(QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada praticada no penúltimo período de apuração.

 

O Log de Cálculo:

 

O Log de Cálculo lista, para cada Produto Industrializado, os movimentos selecionados para o cálculo do VI e VO. Movimentos cancelados são excluídos do cálculo.

 

Ele apresenta a SOMA das Quantidades, a SOMA do Resultado da Fórmula utilizada no cálculo e o Valor de Importação e Operação para cada produto Industrializado.

 

Os valores intermediários, como Valor Unitário de Importação – VUI e Valor Final Importação por Insumo – VFII são calculados internamente e não são apresentados no log, em função da sequencia que o mesmo é gerado.

 

Para identificação desses valores intermediários, o usuário deve efetuar os cálculos conforme demonstrado neste documento e os valores apresentados no Log.

 

**Veja modelo do log:**

 

 

 

divs

# Ficha de Conteúdo de Importação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Estoque Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Produto | Cálculo de Ficha de Conteúdo de Importação* | *Cálculo de Ficha de Conteúdo de Importação* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Estoque | Produção* | *Produção* | |  |  | |
| **Cadastros Iniciais:** | *Cadastrar Atividades, Estruturas e Componentes.*  **Cadastrar Produto (insumos): Procedência/Origem.**  ***Cadastrar fórmula para o Valor Total da Operação.*** |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | 631236;   * [548151](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22548151%22 "548151") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-202; MATESTCNTFTOF01-223 |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

A partir de 01 de janeiro de 2013, nas operações **interestaduais** destinadas a **contribuintes do ICMS**, de bens e mercadorias **industrializadas**, que possuem em sua composição **insumos importados** (sejam adquiridos diretamente do exterior ou no mercador nacional) e bens e mercadorias importadas para **revenda**, terão uma alíquota de 4% para o ICMS.

A alíquota de 4% só será aplicada se, após o desembaraço aduaneiro, os produtos importados:

* Não tiverem sido submetidos a processo de industrialização; ou
* Se submetidos a processo de industrialização, resultarem em mercadorias ou bens com Conteúdo de Importação – CI superior a 40%

CI - Conteúdo de Importação:

Percentual correspondente ao quociente entre o Valor da Parcela Importada do exterior **(VI)** e o valor total da operação de saída interestadual da mercadoria ou bem submetido ao processo de industrialização **(VO)**.

**CI = (VI ÷ VO) × 100**

Consideramos:

**VI -** **Valor da Parcela Importada**

1. Quando o bem ou produto for importado diretamente do exterior

O Valor Aduaneiro, ou seja, o valor FOB da mercadoria importada, acrescidos dos valores de frete e seguro internacional.

1. Quando o bem ou produto importado for adquirido no mercado nacional:

a)       Não submetido a processo de industrialização:

Valor que consta no documento fiscal emitido pelo remetente (fornecedor), excluindo os valores do ICMS e IPI.

b)       Submetido ao processo de industrialização e que possui mais de 40% de seus componentes importados:

Valor informado no documento fiscal emitido pelo remetente (fornecedor), excluído os valores de ICMS e IPI. Nesse caso deverá também ser observado o percentual que o produto possui de componentes importados para definição do percentual a ser considerado na composição do novo produto que vai utilizar esse como parte do mesmo.

* Produtos adquiridos no mercado nacional que possuir percentual de produto importado menor que 40%, será considerado como inteiramente nacional;

* Produtos adquiridos no mercador nacional que possuir percentual de produto importado maior que 40% e menor que 70%, será considerado 50% do valor como importado;

* Produtos adquiridos do Mercado nacional que possuir percentual de produto importado maior que 70%, será considerado 100% do valor como produto importado.

Observações:

* Valor unitário da parcela importada do exterior é obtido pela média aritmética ponderada praticada no penúltimo período de apuração.

* Na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, deverá buscar nos períodos anteriores até encontrar um período que tenha ocorrido à operação.

**VO – Valor Total da Operação de Saída Interestadual**

Valor das operações de saída interestadual, obtido no penúltimo período de apuração, excluindo os valores de ICMS e IPI.

Observação:

* Caso não tenha ocorrido nenhuma saída interestadual no penúltimo período de apuração, a empresa pode considerar as operações internas do penúltimo período de apuração, excluindo os valores de ICMS e IPI.

* Na hipótese de não ter ocorrido operação de saída interna no penúltimo período de apuração, deverá buscar nos períodos anteriores até encontrar um período que tenha ocorrido a operação.

*Fonte: Especificação VI e VO para Cálculo Conteúdo de Importação*

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.14.160*

## Procedimento para Utilização

 

Parametrização e Cadastros necessários para implantação do cálculo:

 

###### 1.       Cadastrar: Atividade, Estrutura e Componentes:

 

Para identificar se na composição dos Produtos Industrializados existem insumos importados, será necessário trabalhar com o conceito de **Atividade**, **Estrutura** e **Componente**.

 

*Acesse*:

 

MDI - | Estoque | Produção |

 

Delphi - | Cadastros | Tabelas de Produção |

 

Sugestão para o cadastro em clientes que não possuem o módulo TOTVS Planejamento e Controle da Produção

 

Atividade

 

Sugiro criar uma atividade exclusiva para esse cálculo: CCI – Cálculo Conteúdo de Importação

 

Estrutura

 

Deve existir uma Estrutura para cada Produto Industrializado. Sugiro inclusive, cadastrar como código da estrutura, o mesmo código do produto industrializado.

 

Componente

 

Nessa tabela será informada a composição de cada estrutura (PI). Nela deve-se informar a quantidade usada de cada componente (insumo).

 

1. *2.**Cadastro Produto (insumos): Procedência/Origem devidamente cadastrada*

 

Para que o insumo entre no cálculo do Conteúdo de Importação, o mesmo deve estar classificado, em seu cadastro com as seguintes Procedências/Origens:

 

**1 – Estrangeira – Importação direta, exceto a indicada no código 6;**

 

**2 – Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7;**

 

**3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%.**

 

**8 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%**

 

Observação: Pode acontecer de um único código de produto (componente/insumo) de procedência/origem estrangeira, ser adquirido diretamente do exterior (1) ou ser adquirido no mercado interno (2). Neste caso, deve-se informar na procedência/origem, a procedência/origem principal.

 

1. *3.**Cadastrar fórmula para o Valor Total da Operação, seja de Importação ou Saída. (Nas explicações abaixo estaremos utilizando a nomenclatura ‘**For\_VTO**’ para referenciar a esta fórmula).*

 

Essa fórmula atenderá tanto o cálculo do **VI** quanto do **VO.**

 

Como o valor a ser considerado pode variar entre importação direta e aquisições no mercado interno, e operações de saída, foi criada uma fórmula para que cada empresa defina como será o cálculo do valor unitário de suas operações.

 

Essa fórmula deve ser executada no contexto do item de movimento (utilizar variáveis e funções que retornem valores do item de movimento) e deve retornar o Valor Total do Item, ou seja, não deve retornar o valor unitário do item.

 

Observação: Se houver necessidade, essa fórmula deve possuir a condição ‘SE’ para tratar de forma diferenciada movimentação de entrada (importação) de movimentações de saída.

 

A execução do processo no RM:

 

O Cálculo do Conteúdo de Importação é um **processo** da visão de **Produtos**. O mesmo pode ser executado pelo TOTVS Gestão Fiscal ou pelo TOTVS Gestão de Estoque, Compras e Faturamento.

 

O cálculo será executado para todos os produtos selecionados na visão (sugiro fazer um filtro com os produtos industrializados que possuem em sua composição insumos importados).

 

Com os produtos selecionados, clique em: **| Processos | Cálculo Conteúdo de Importação |**.

 

Na tela de execução do processo informe:

 

**Filial** informe a filial na qual as movimentações serão pesquisadas.

 

**Fórmula VI e VO**informe a fórmula criada para calcular o Valor da Operação, seja de Importação ou Saída (**For\_VTO**).

 

**Data último período de apuração** informe o último Período de Apuração Encerrado.

 

**Gerar Log de Cálculo** à flag para indicar se deverá ser gerado um Log com as movimentações selecionadas para o cálculo do CI. Dependendo do volume de produtos selecionados, do volume de movimentações e da complexidade da fórmula, a execução desse log poderá comprometer a performance do processo.

 

Observação: Os movimentos serão filtrados de acordo com a Filial informada.

 

Se a empresa possuir movimentações em várias filiais, antes da execução desse processo, será necessário selecionar, a filial no qual os movimentos devem ser pesquisados.

 

O Cálculo do VI no RM:

 

Para cada Produto Industrializado selecionado para o cálculo o sistema fará:

 

1. Identificar no cadastro de Estrutura/Componente, os componentes (insumos) cujo campo de Procedência/Origem da tabela de Produtos possui as opções:

 

(1)     Estrangeira – Importação direta, exceto a indiada no código 6;

 

(2)     Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7;

 

(3)     Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou menor que 70%;

 

(8)  Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%

 

1. O cálculo varia de acordo com a Procedência/Origem do componente (insumo), conforme descrito abaixo:

 

Observação: Para os produtos cadastrados com procedência/origem (1) e (2), o sistema sempre irá verificar se existe movimentação com importação direta ou adquirida no mercado interno, ou seja, serão sempre executados os processos 2.1 e 2.2 descritos abaixo. Isso, para evitar a duplicidade do cadastro de produto, uma vez que o mesmo código pode ser adquirido dentro ou fora do país.

 

**2.1.****Procedência/Origem** = **1 – Estrangeira, Importação direta exceto a indicada no código 6**

 

a)      Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de entrada selecionada.

 

*Considerar*:

 

* Movimentos de entrada por importação:

 

Código do Tipo de Movimento iniciado com **1.2.%** e

 

Emitente/Destinatário = **Empresa** / **Empresa** e

 

Código da Natureza de Operação do Item iniciado com **3.101%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      Somar a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (**QTI**).

 

c)       Calcular o Valor Unitário de Importação (**VUI**)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Final Importado do Insumo/componente (VFII)

 

O Valor Importado do Insumo/componente corresponde ao produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

**2.2. Procedência/Origem = 2 – Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7**

 

a)      Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de entrada selecionada.

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**  e

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      **SOMAR** a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (**QTI**).

 

c)       Calcular o Valor Unitário de Importação (**VUI**)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Final Importado do Insumo/componente (VFII)

 

O Valor Importado do Insumo/componente corresponde ao produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

**2.3.****Procedência/Origem =** **3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e igual ou inferior a 70%**

 

a)      Calcular o Valor Total Importado (For\_VTO) para cada nota fiscal de entrada selecionada

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação.

 

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

c)       Calcular o Valor Unitário de Importação (VUI)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Importado do Insumo/componente (VII)

 

O Valor Importado do Insumo/componente corresponde 50% do produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA) × 0,50**

 

Observação: Na procedência/origem 3 - Nacional, mercadoria ou bem com CI superior a 40% e igual ou inferior a 70%, será considerado 50% do resultado

 

**2.4.****Procedência/Origem = 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%**

 

a)      Calcular o Valor Total Importado (For\_VTO) para cada nota fiscal de entrada selecionada

 

*Considerar*:

 

* Movimentos de entrada:

 

Código do Tipo de Movimento iniciado com **1.2%** e

 

Emitente/Destinatário = **Fornecedor** / **Empresa**

 

Código da Natureza de Operação do Item iniciado com:

 

**1.101.% / 2.101.%, 1.116.% / 2.116.%, 1.120.% / 2.120.%, 1.122.% / 2.122.%, 1.401.% / 2.401.%, 1.651.% / 2.651.%, 1.901.% / 2.901.%, **2.151%****

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação.

 

Observação: na hipótese de não ter ocorrido operação de importação no penúltimo período de apuração, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação. O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

b)      SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

c)       Calcular o Valor Unitário de Importação (VUI)

 

O Valor Unitário de Importação corresponde ao quociente entre a SOMA de todos os Valores Totais de Operações (VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VUI = Soma(For\_VTO) ÷ Soma (QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada.

 

d)      Calcular o Valor Importado do Insumo/componente (VII)

 

O Valor Importado do Insumo/componente corresponde 100% do produto entre o Valor Unitário de Importação e a quantidade usada do componente.

 

**VFII = VUI × (KCOMPONENTE.QTDUSADA)**

 

1. O Valor de Importação do Produto Industrializado (**VI**) será:

 

A SOMA de todos os valores finais de importação dos insumos/componentes do produto industrializado em questão:

 

**I = Soma (VFII)**

 

O Cálculo do VO no RM:

 

Para cada Produto Industrializado selecionado para o cálculo o sistema fará:

 

1. Calcular o Valor Total Operação (For\_VTO) para cada nota fiscal de saída selecionada:

 

*Considerar*:

 

* Movimentos de saída:

 

Código do Tipo de Movimento iniciado com **2.2%** e

 

Emitente / Destinatário = **Empresa / Cliente**  e

 

Código da Natureza de Operação do Item iniciado com:

 

**6.101.%, 6.103.%, 6.105.%, 6.109.%, 6.111.%, 6.113.%, 6.116.%, 6.118.%, 6.122.%, 6.151.%, 6.155.%, 6.401.%, 6.402.%, 6.651.%, 6.652.%, 5%**

 

* Penúltimo período de apuração: (**Mês Referência – 1**) buscar pela data de movimentação

 

Observação: na hipótese de não ter ocorrido operação de saída interestadual no penúltimo período de apuração, buscar operações de saída internas (iniciadas com 5). Se não existir movimentação, buscar nos períodos anteriores até encontrar um período que tenha ocorrido operação (interestadual/interna). O padrão é a pesquisa em 48 meses mas pode ser ajustado para até 999 meses. Não encontrando movimentações nesse período, verificar no último período de apuração, que corresponde ao mês de referencia.

 

1. SOMAR a quantidade, do componente/insumo pesquisado, em todas as notas selecionadas acima (QTI)

 

1. Calcular o Valor Total Operação de Saída (VO)

 

O Valor Total das Operações de Saída corresponde ao quociente entre a SOMA de todos os Valores Total de Operação (For\_VTO) e a SOMA de todas as quantidades do item pesquisado

 

**VO = Soma(For\_VTO) ÷ Soma(QTI)**

 

Observação: Aqui estamos tratando a média aritmética ponderada praticada no penúltimo período de apuração.

 

O Log de Cálculo:

 

O Log de Cálculo lista, para cada Produto Industrializado, os movimentos selecionados para o cálculo do VI e VO. Movimentos cancelados são excluídos do cálculo.

 

Ele apresenta a SOMA das Quantidades, a SOMA do Resultado da Fórmula utilizada no cálculo e o Valor de Importação e Operação para cada produto Industrializado.

 

Os valores intermediários, como Valor Unitário de Importação – VUI e Valor Final Importação por Insumo – VFII são calculados internamente e não são apresentados no log, em função da sequencia que o mesmo é gerado.

 

Para identificação desses valores intermediários, o usuário deve efetuar os cálculos conforme demonstrado neste documento e os valores apresentados no Log.

 

**Veja modelo do log:**

 

 

 

Atenção

* Para que o cálculo seja feito corretamente deve-se ter os movimentos de compra e venda corretamente configurados
  + Atenção no movimento para o correto preenchimento do:
    - Tipo de Movimento
    - Natureza do Movimento
    - Emitente | Destinatário
    - E demais configurações indicadas nesse documento
  + Atenção em relação ao produto para sua correta classificação e parametrização.
* O cálculo do FCI só identifica insumos que possuem movimento de compra realizada seguindo as configurações indicadas nesta documentação, outras movimentações são desconsideradas.
* O cálculo do FCI só identifica produção  que possuem movimento de venda realizada seguindo as configurações indicadas nesta documentação, outras movimentações são desconsideradas.

divs
