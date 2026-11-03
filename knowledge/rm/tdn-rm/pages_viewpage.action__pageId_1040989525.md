---
content_hash: 980216facd1eee758fe38c68b99fc19ff7619775bf1270150c9da17f15abb29e
fetched_at: '2026-06-29T00:05:49.656220+00:00'
page_id: '1040989525'
product: rm
source: tdn-rm
title: Lei Complementar nº 224/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040989525
version: 62
---

# Conteúdo

2Conteúdononenone

# 1. Sobre

A Lei Complementar nº 224/2025, regulamentada pela Instrução Normativa RFB nº 2.306/2026, passou a tratar o regime de Lucro Presumido como benefício fiscal para empresas com receita bruta anual superior a R$ 5 milhões. Para essas empresas, foi instituído um acréscimo de 10% nos percentuais de presunção do IRPJ e da CSLL, aplicável sobre a parcela da receita que exceder o limite. A alteração produz efeitos a partir do 1º Trimestre de 2026 para IRPJ e a partir do 2º Trimestre de 2026 para CSLL.

# 2. Versões para atualização

A solução está disponível a partir dos patches:

Biblioteca RM

* 12.1.2506.285
* 12.1.2510.205
* 12.1.2602.126

# 3. Detalhe da Alteração

Em complemento à LC 224/2025, a Instrução Normativa da RFB nº 2.306/2026 estabeleceu que o controle do limite de 5 milhões deve ser trimestral:

* **Limite Trimestral:** O limite anual de R$ 5 milhões foi fracionado em R$ 1,25 milhão por trimestre.
  + **Particularidade referente à CSLL em 2026:** A CSLL está sujeita à anterioridade nonagesimal (90 dias), conforme previsto no art. 195, § 6º da Constituição Federal de 1988. Dessa forma, considerando a data de publicação da Lei Complementar nº 224/2025, os efeitos da sua majoração passam a vigorar apenas a partir de abril de 2026 (2º trimestre). Em razão disso, **exclusivamente no ano-calendário de 2026**, o **limite** aplicável à **CSLL** **será de R$ 3.750.000,00**, correspondente a três trimestres, uma vez que o 1º trimestre permanece sem alterações nas regras de apuração. A partir de 2027, IRPJ e CSLL passam a adotar limite anual unificado de R$ 5 milhões, fracionado em R$ 1,25 milhão por trimestre.
* **Transporte de Saldo:** Se a receita de um trimestre for inferior a R$ 1,25 milhão, a diferença (saldo) é transportada para o limite do trimestre seguinte, dentro do mesmo ano calendário. O transporte desse saldo de limite é realizado de forma proporcional, avaliando o percentual de participação de cada receita do período em relação ao montante faturado.
* **Ajuste Anual** (4º Trimestre): Na hipótese de empresa ter recolhido a majoração em um ou mais trimestres, mas encerre o ano calendário com receita bruta total inferior a R$ 5 milhões, o valor recolhido a maior sobre a parcela excedente poderá ser objeto de pedido de restituição ou compensação, mediante solicitação do contribuinte, na forma da legislação aplicável.

Exemplo de Alíquotas (com e sem majoração):

| Atividade | IRPJ Alíquota Original | IRPJ Majorado (+10%) | CSLL Alíquota Original | CSLL Majorado (+10%) |
| --- | --- | --- | --- | --- |
| Revenda de Combustíveis | 1,6% | 1,76% | 12% | 13,2% |
| Comércio / Indústria | 8% | 8,8% | 12% | 13,2% |
| Transportes | 16% | 17,6% | 12% | 13,2% |
| Serviços em Geral | 32% | 35,2% | 32% | 35,2% |

O sistema faz a majoração das alíquotas das atividades automaticamente.  
Não é necessário coloca-las já majoradas nos campos do cadastro de tributo.

## 3.1 Cadastro de Tributos

No [Cadastro do Tributo](https://tdn.totvs.com/display/LRM/Cadastro+de+Tributos) (IRPJ e CSLL), foram realizados ajustes para permitir a configuração da alíquota de majoração e o limite anual isento de majoração:

* Localização: **Gestão Fiscal | Cadastros | Tributos**.
* Ação: O usuário deve informar nos campos:
  + "**Percentual de Majoração**" de 10% para os casos de excedente e o
  + "**Limite Anual Isento da Majoração**" de R$ 5.000.000,00
    - **Particularidade do limite aplicado à CSLL exclusivamente em 2026:** informar Limite Anual Isento da Majoração de R$3.750.000,00, apenas a partir de 01/04/2026 (2º Trimestre). Já em 01/01/2027, informar o Limite de R$ 5.000.000,00, que será idêntico para IRPJ e CSLL.
    - **Atenção** quanto à **retificações de CSLL:** havendo necessidade deretificação de determinado período (CSLL), considerando a alteração do limite de isenção da majoração da CSLL entre o 2º trimestre de 2026 e o exercício de 2027, o valor do limite anual isento deverá corresponder àquele vigente no período objeto da retificação. Dessa forma, caso a retificação seja realizada, por exemplo, no ano de 2027, mas se refira a período de apuração do ano-calendário de 2026, o usuário deverá, previamente, ajustar o limite para R$ 3.750.000,00 no cadastro do tributo, proceder com a execução do processo de retificação e, após a sua conclusão, restabelecer o limite vigente para o ano-calendário correspondente, no período de apuração.

Cadastro do Tributo#002233dashed

Exemplo para IRPJ:

## 3.2 Simulação do Evento Tributário

A tela de [Simulação do Evento Tributário](https://tdn.totvs.com/pages/viewpage.action?pageId=422545748) foi atualizada para oferecer total transparência no que se refere à aplicação da majoração de 10% sobre os coeficientes de presunção. Agora, a memória de cálculo é dividida para mostrar o que está dentro do limite de isenção do trimestre (1,25 milhão) e o que excedeu o teto trimestral e por consequência, foi calculado com percentual majorado.

A execução deste processo ocorre através do menu ***Gestão Fiscal | Obrigações Principais | Eventos Tributários | Estrutura | Processos | Simulação - Regra de Apuração***.

Processo Simulação - Regra de Apuração#002233dashed

O que mudou na visualização da Simulação:

* **Segregação por Receita**: Cada grupo de atividade (1 a 4) agora exibe duas linhas de cálculo distintas caso o limite seja ultrapassado.
* **Rec. Isenta Majoração**: Exibe a parcela do faturamento (até R$ 1,25 milhão, considerando transportes de saldo) multiplicada pelo percentual de presunção original (ex: 1,6%, 8%, 16% ou 32%) de forma proporcional à participação de cada atividade/receita sob o montante, para casos de receitas contabilizadas em mais de uma atividade/percentual.
* **Receita Majorada**: Valor que ultrapassou o limite disponível. Sobre este montante, o sistema aplica a alíquota majorada (ex: 35,2%).
* **% Estimado Aliq. Majorado**: O sistema apresenta os dois percentuais, com e sem majoração.

Tela de Simulação  

## 3.3 Apuração

A rotina de Enceramento do [Período de Apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=422545773) do IRPJ e CSLL (Lucro Presumido) foi atualizada para realizar os cálculos, garantindo que a majoração só ocorra quando o teto disponível for efetivamente ultrapassado.

A execução deste processo ocorre através do menu ***Gestão Fiscal | Obrigações Principais | Período de Apuração | Processos | Encerramento Período***.

Detalhamento do Período de Apuração

Campos referente a apuração do IRPJ e CSLL (Lucro Presumido).

#002233dashed

Exemplo em que a receita do 1º Trimestre foi equivalente à R$ 1 milhão, e o saldo de R$ 250 mil foi armazenado para utilização no 2º Trimestre:

### 3.3.1 Gestão de Saldos e Transporte de Limite

O sistema monitora a Receita Bruta acumulada para definir a aplicação da majoração de 10% sobre os coeficientes:

* **Trimestre com Receita Menor R$ 1,25M:** O sistema apura o imposto com as alíquotas base e gera um **Saldo de Limite** (Ex: Receita de R$ 900 mil gera saldo de R$ 350 mil para o próximo trimestre  (memória de cálculo: R$1.250.000,00 - R$900.000,00 = R$350.000,00), logo, no próximo trimestre, o limite disponível será de R$1.600.000,00 neste exemplo (R$1.250.000,00 (padrão) + R$350.000,00 do trimestre anterior).
* **Trimestre com Receita Maior R$ 1,25M:** O sistema consome, primeiramente, o limite do trimestre corrente e, em seguida, eventual saldo remanescente transferido do período anterior. A majoração, correspondente ao acréscimo de 10% sobre a alíquota, incide exclusivamente sob o valor que exceder o consumo integral desses limites.

### 3.3.2 Regra de Proporcionalidade entre Atividades

Conforme a **IN 2.306/2026**, quando a empresa aufere receitas de atividades sujeitas a diferentes percentuais de presunção, o sistema considera o limite trimestral global e, para fins operacionais, realiza sua distribuição proporcional entre essas receitas.

* **Cálculo Automático:** O sistema aplica uma regra de três para distribuir o limite de R$ 1,25M proporcionalmente ao peso de cada receita no faturamento total. A mesma regra de proporção se aplica aos transportes de saldos de um trimestre para outro, na hipótese do Trimestre posterior também contar com mais de uma atividade.
* **Exemplo:** Em um faturamento total de R$ 1,9 milhão, sendo R$ 500.000,00 correspondentes à atividade de serviços (26,315789% do total), o limite atribuído a essa atividade será de R$ 328.947,37. O valor que exceder esse montante ficará sujeito ao percentual majorado de 35,2%.

### 3.3.3 Ajuste de Fechamento Anual (4º Trimestre)

* **Validação Anual:** se a Receita Bruta Total acumulada no ano calendário for **menor ou igual** a **R$ 5.000.000,00**, mas a empresa tiver sofrido incidência de majoração em um ou mais trimestres isolados, o sistema não realizará a compensação automaticamente no **4º trimestre**.
* **Ação:** nessa hipótese, será apresentado um **log** na apuração do **4º trimestre** (desde que os períodos anteriores estejam encerrados) na Simulação do Evento Tributário, demonstrando o valor da majoração recolhido ao longo do ano que, ao final do período anual, não ultrapassou o limite de **R$ 5.000.000,00**. Com base nessa informação, o usuário poderá informar o valor correspondente à parcela do IRPJ/CSLL decorrente da majoração no campo de **Compensação**, na aba de **Lançamento Manual**, para fins de redução/compensação do IRPJ/CSLL devido no último trimestre.

  + **Observação**: o sistema considera também nesta etapa, até 31/12/2026, o limite de R$3.750.000,00 para CSLL, conforme a legislação.

Após encerrar os períodos anteriores ao 4º Trimestre e gerar a simulação para o 4º Trimestre, se houver ajuste com valor possível para compensação, o sistema exibirá o LOG:

Para CSLL, em 2026, o limite retornado será conforme a legislação:

A mesma mensagem também pode ser visualizada no encerramento do 4º Trimestre através do menu **Progresso da execução do(s) processo(s) l Exibir informações do processo l Logs**

Se houver valor a compensar no último Trimestre, no Evento Tributário, com o tributo correspondente já selecionado, o lançamento é efetuado via menu **Anexos l Lançamento manual l Ícone l Grupo Compensações l Data do último Trimestre l Valor: equivalente ao total à compensar l Operação = Soma**

Após o lançamento de compensação, o valor à compensar é subtraído do Débito devido no período:
