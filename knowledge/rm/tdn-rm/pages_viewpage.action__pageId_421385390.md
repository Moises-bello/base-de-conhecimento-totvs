---
content_hash: d31b72e9fc113f834c36527afb2195de74a9aad6e244f5b4ad59ea6bcac745ae
fetched_at: '2026-06-29T00:09:15.481081+00:00'
page_id: '421385390'
product: rm
source: tdn-rm
title: Análise de Valor Agregado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385390
version: 8
---

---

É uma funcionalidade que permite ao usuário a partir de índices apresentados avaliar os resultados atingidos do projeto comparando a quantidade de capital investida.

Existem características do Projeto que são essenciais para utilizar o recurso:

1-    Deve-se ter um plano de Projeto que identifica o trabalho a ser cumprido,  
2-    Uma avaliação do trabalho planejado (Valor Planejado – VP)  
3-    Regras de ganho pré-definidas para quantificar o trabalho executado (Valor Agregado – VA).

**Versões de Avaliação do Valor Agregado:**  
No Cadastro das Versões, o usuário apenas informa a Descrição. A partir daí poderá calcular e visualizar os Índices na data do cálculo. A idéia  de se cadastrar varias versões é possibilitar ao usuário, à medida que for necessário, manter um histórico acompanhando o segmento do Projeto.

Ao Visualizar os Índices, serão exibidos:

**COTA - Custo Orçado do Trabalho Agendado - Valor Planejado (VP**)

É definido através do valor que indica a parcela do orçamento que deveria ser gasta, considerando o custo de linha da base da atividade. Ele é proveniente do Custo de cada atividade e consequentemente do custo do Projeto.

**CRTR - Custo Real do Trabalho Realizado - Custo Real (CR)**

Demonstra os custos reais decorrentes do trabalho já realizado em uma atividade, até a data de referência, ou data atual do projeto. Custo Real verifica o quanto já foi gasto no projeto.

**COTR - Custo Orçado do Trabalho Realizado - Valor Agregado (VA)**

É definido através do valor que indica a parcela do custo que deveria ser utilizada, considerando-se o trabalho realizado até o momento e o custo (linha de base) da atividade. O COTR/BCWP também é denominado Valor acumulado ou Valor Agregado.

**VC - Variação de Custo**

É obtido através da diferença entre o Custo Previsto (VP) para atingir o nível atual de conclusão (VA) e o Custo Real (CR), até a data de referência. 

**VP - Variação de Progresso**

Com a Variação de Progresso é possível verificar atrasos ou adiantamento do projeto por período.

**IDC - Índice de Desempenho de Custo**

Com o índice de desempenho de custo vamos identificar se o custo utilizado no projeto está de acordo com o valor agregado. O IDC mostra a taxa de conversão de Custo Real em Valor Agregado.

**IDP - Índice de Desempenho de Prazos**

Com o índice de desempenho de prazos vamos identificar se a velocidade em que o projeto gera valor agregado está acima ou abaixo da prevista originalmente. O IDP mostra a taxa de conversão de valor previsto em valor agregado.

**ENT - Estimativa no Término**

Uma ENT é uma previsão do valor total mais provável baseada no desempenho do projeto e na quantificação do risco. A ENT é o valor final total projetado ou antecipado de uma atividade do cronograma, um componente da EAP ou um projeto quando o trabalho definido do projeto é terminado.

**ENT - Utilizando o IDC**

ENT usando IDC. A ENT é igual aos custos reais até a data atual (CR) mais o orçamento necessário para terminar o trabalho do projeto restante, que é o OAT menos o VA, modificado por um fator de desempenho (frequentemente o IDC). Esta abordagem é mais frequentemente usada quando as variações atuais são consideradas típicas de variações futuras.

**Baseada em Variações Típicas - EPT1**

EPT baseada em variações típicas: Esta abordagem é mais frequentemente usada quando as variações atuais são consideradas típicas de variações futuras. A EPT é igual ao OAT menos o VA cumulativo (o VP restante) dividido pelo índice de desempenho de custos cumulativo (IDC). 

**Baseada em Variações Atípicas - EPT**

EPT baseada em variações atípicas: Esta abordagem é mais frequentemente usada quando as variações atuais são consideradas atípicas e as expectativas da equipe de gerenciamento de projetos são de que variações semelhantes não irão ocorrer no futuro. A EPT é igual ao OAT menos o valor agregado cumulativo até a data atual (VA).

**OAT** é utilizado apenas no cálculo para compor os demais índices. Representa o valor total planejado pra o projeto. É o orçamento final do projeto ou custo da linha de base (custo total das atividades e do Projeto).

**Origem do valor planejado**  
  
**Procedimentos para configuração**

1- É necessário configurar a origem dos dados do relatório nos parâmetros do projeto. Atualmente o relatório de Analise de valor Agregado permite que os dados sejam extraídos por origem padrão ou através de fórmula.

a- Atualmente o cronograma planejado é considerado no cálculo do valor planejado, mas é considerado como ideal para obtenção dos dados a partir da linha base. Por isso visando disponibilizar o correto cálculo, mas também permitir que os usuários utilizem o cronograma planejado caso desejem, será criado o parâmetro "utilizar linha base como valor planejado (COTA)", que será considerado como default.

**Origem do Custo Real**

b- Atualmente o custo real é obtido a partir do cronograma medido , sendo considerado como ideal a obtenção a partir do valor apropriado. O cálculo padrão será alterado para obter o CR a partir do valor apropriado.

2- Habilitar o parâmetro "Obter valor da linha base a partir do valor apropriado para períodos fechados anteriores". Este parâmetro informa para o processo de cópia de linha base que para os períodos anteriores com o cronograma previsto travado (considerado como já realizados ) deve -se copiar o valor do cronograma apropriado para o valor da linha base.

|  |  |  |  |
| --- | --- | --- | --- |
|  | COTA| VP | COTR| VA | CRTR| CR |
| Modelo Antigo | Valor do Cronograma Planejado | Valor do Cronograma Realizado | Valor do Cronograma Medido |
| Novo Modelo - Utilizando Cronograma Planejado | Valor do Cronograma Planejado | Valor do Cronograma Realizado | Valor Apropriado |
| Novo Modelo - Utilizando Linha Base | Valor da Linha Base | Valor Agregado considerando custo unitário da linha base \* | Valor Apropriado |

\* O cálculo obterá o valor agregado a partir da quantidade realizada e o valor unitário da Linha Base, conforme a seguinte fórmula:

COTR (VA) = Quantidade Realizada (Cronograma Realizado) \* (Valor da Linha Base / Quantidade da Linha Base).  
O cálculo do COTR deve ser realizado a cada período para que os valores estejam corretos.  
Exemplo:  
Tarefa 1 no Período 1 => 5,00 \* (60,00 / 4,00) = 75,00  
Tarefa 1 no Período 2 => 5,00 \* (40,00 / 6,00) = 33,33  
TOTAL = SOMA dos 2 Períodos => 108,33

Obs.: Caso não haja Linha Base no período será considerada a seguinte lógica de precedência:  
Caso haja Linha Base no período será obtido o valor do mesmo.

**Procedimento para utilização**

Após a correta parametrização e planejamento da forma a qual o cliente efetuará o acompanhamento do projeto com Analise de Valor Agregado, o mesmo deve seguir os passos abaixo para geração do relatório.  
1- Criação do registro para cálculo do relatório.  
2- Processar cálculo do relatório. (Deve-se marcar a opção de cálculo por centro de custo e informar o período de referência que será considerado como período atual.  
3- Visualizar relatório

**Exemplo de criação de fórmula**

Nesse caso um tipo de fórmula para COTR/VA

A fórmula utiliza a função `CAMPOCONSULTA2` para executar uma sentença SQL cadastrada e retornar o valor de um campo específico por tarefa e período.

## Pré-requisitos

### Funções de Contexto

As funções abaixo estão disponíveis e retornam os valores de IDTRF e NUMPERIODO para os cálculos de cada tarefa :

**IDTRFAVA()** = Retorna o Id da Tarefa do contexto AVA  
    **NUMPERIODOAVA() =** Retorna o Número do Período do contexto AVA

## Como Funciona a Função CAMPOCONSULTA2

**CAMPOCONSULTA2('CODIGO\_SENTENCA', 'CAMPO\_RETORNO', 'CAMPOS\_CHAVE', valor1, valor2)**

### Parâmetros

**CODIGO\_SENTENCA** = Código da Sentença SQL cadastrada no sistema     
    **CAMPO\_RETORNO** = Nome da coluna cujo valor será retornado  
    **CAMPOS\_CHAVE** = Colunas de busca separadas por `;` (além de CODCOLIGADA e IDPRJ que são automáticos)  
    **valor1, valor2** = Valores das chaves de busca, na mesma ordem dos `CAMPOS\_CHAVE`

Exemplo do modelo de sentença:

Os parâmetros `:$CODCOLIGADA` e `:$IDPRJ` são resolvidos automaticamente a partir da do contexto. O filtro é por projeto inteiro (sem filtrar IDTRF/NUMPERIODO), pois o cache precisa de todos os registros.

Usando a sentença criada na imagem acima, a fórmula criada seria:

**CAMPOCONSULTA2('AVASQLVA1', 'VALOR', 'IDTRF;NUMPERIODO', IDTRFAVA(), NUMPERIODOAVA())**

Dashboard de Indicadores

Esses índices poderão ser visualizados no  do Portal da Obra, mais especificamente na parte referente aos índices de desempenho, .

---
