---
content_hash: 0e77805c85647336fb44c0e34db496025b4960dbda752cb06c8ff275f497eef7
fetched_at: '2026-06-29T00:09:15.560434+00:00'
page_id: '421385411'
product: rm
source: tdn-rm
title: Leis / Outros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385411
version: 12
---

**Fator 1:** Informe o valor do fator da lei social 1 ou calcule-o através de uma planilha eletrônica do Corpore RM.

**Planilha para cálculo:** Selecione a planilha eletrônica Leis Sociais (Padrão) do Corpore RM ou uma de sua preferência que fará o cálculo do fator. Para que efetuar a seleção, digite parte do nome da planilha e depois pressione a tecla TAB.

**Célula de retorno:** Informe a célula da planilha eletrônica que retorna o valor do fator 1.

Visualizar Planilha:

Marque essa opção se desejar visualizar o cálculo.

Essa informação não é gravada no banco de dados, ou seja, essa opção virá sempre desmarcada.

**Fator 2:** Informe o valor do fator da lei social 2 ou calcule-o através de uma planilha eletrônica do Corpore RM.

Planilha para cálculo: Selecione a planilha eletrônica Leis Sociais (Padrão) do Corpore RM ou uma de sua preferência q

ue fará o cálculo do fator. Para que efetuar a seleção, digite parte do nome da planilha e depois pressione a tecla TAB.

Célula de retorno: Informe a célula da planilha eletrônica que retorna o valor do fator 2.

Visualizar Planilha:

Marque essa opção se desejar visualizar o cálculo.

Essa informação não é gravada no banco de dados, ou seja, essa opção virá sempre desmarcada.

Os fatores serão aplicados de acordo com a forma de aplicação das leis sociais (sobre o custo unitário do insumo ou sobre o total do grupo na composição) para o grupo de custo que tiver incidência da lei social.

Aplicar Leis Sociais sobre: Informe se a Lei Social do projeto será aplicada sobre o "Valor Total do Grupo na Composição" ou sobre o "Custo Unitário dos Insumos".

**Exemplos:**

Considere a taxa de leis sociais 134,5%, o valor unitário sem leis do insumo Servente igual a 0,47 e do insumo Pedreiro igual a 1,04.

Se a forma de aplicação das leis sociais for sobre o "Custo Unitário dos Insumos" o valor unitário do Servente será 1,10 e o do Pedreiro será 2,44, o valor parcial é o produto entre o preço unitário e a quantidade, conforme demonstrado abaixo.

| Código | Quantidade | Preço Unitário | Preço Parcial |
| --- | --- | --- | --- |
| Servente | 3,6571 | 1,10 | 4,02 |
| Pedreiro | 2,0000 | 2,44 | 4,88 |

Se a forma de aplicação das leis sociais for sobre o "Valor Total do Grupo na Composição" será calculado o valor parcial de cada insumo (quantidade x valor unitário sem leis), os valores parciais serão somados e a lei social (2,345) será aplicada sobre esse valor, conforme demonstrado abaixo.

| Código | Quantidade | Preço Unitário | Preço Parcial |
| --- | --- | --- | --- |
| Servente | 3,6571 | 0,47 | 1,72 |
| Pedreiro | 2,0000 | 1,04 | 2,08 |

Considerar Quantidade de Obras: Caso esta opção esteja habilitada, a quantidade de obras será considerada no cálculo do valor dos campos 'Valor parcial' e 'Vlr. Lei Social' das tarefas.

**Habilita Calculo das Curvas ABC:**

Esse parametro definirá se as curvas ABC serão calculadas e atualizadas durante o processo de calculo de um projeto. O default para esse parametro é marcado (sempre calcular).

**Distribuir Diferenças na Curva ABC de insumos:**

Caso este parâmetro esteja habilitado, no cálculo do projeto, é verificado tarefa a tarefa as diferenças entre a planilha de atividades x curva ABC de insumos distribuindo as diferenças na tabela da curva ABC de insumos, igualando os valores do cálculo do projeto e da curva. Durante o cálculo da curva ABC de insumos, o sistema realizará o cálculo da quantidade do recurso x valor considerando a distribuição da diferença.

**Moeda do Projeto:**

Define a moeda em que o projeto está sendo orçado. Caso essa moeda não esteja definida, será considerada a moeda default, definida no menu Opções | Parâmetros | RM Solum | Gerais, pasta Identificação, ou seja, este campo será preenchido com a moeda definida nos parâmetros gerais do sistema.

**Aceita Coeficiente Improdutivo Igual a ZERO:**

Caso esta opção esteja habilitada, na associação de insumos do grupo DNIT A (Equipamentos) à composição, o coeficiente improdutivo pode ser igual a zero. Independente da ativação/desativação do parâmetro, na associação de insumos do grupo DNIT A à composição por produção, o coeficiente improdutivo é calculado (1 – coeficiente produtivo).

**Repetir Código Auxiliar de Planilha:**

Caso esta opção esteja habilitada, será permitido que itens de planilha com códigos diferentes tenham o mesmo código auxiliar de tarefa.

**Exemplo:**

A tarefa 001.01.02 pode ter o campo "Cod.Tarefa Aux." com o conteúdo 001. A tarefa 002.01.01 pode ter o campo "Cod. Tarefa Aux." com o conteúdo 001.

Considerar Cmp Aux. no Cálculo de Insumos %:

Caso esta opção esteja habilitada, o sistema irá considerar as composições auxiliares no cálculo dos insumos percentuais.

**Conversão / Indexação:**

É feita a conversão e a indexação de preços, dependendo da moeda do preço do insumo, moeda indexadora do preço do insumo e da moeda do projeto. Situações possíveis:

1) O preço do insumo que está na moeda do projeto e tem uma moeda indexadora (diferente da moeda do projeto) será indexado (preço do insumo / valor da moeda na data de atualização \* valor da moeda na data base para indexação), durante o cálculo do projeto. O valor indexado não ficará visível.

2) O preço do insumo que está numa moeda diferente da moeda do projeto será convertido (preço do insumo x valor da moeda na data base para conversão), durante o cálculo do projeto. O valor convertido não ficará visível.

3) O preço do insumo que está numa moeda diferente da moeda do projeto e tem uma moeda indexadora (diferente da moeda do projeto), é feita a indexação e depois a conversão, durante o cálculo do projeto. Para insumos globais vale a mesma regra dos insumos locais.

Data Base para Indexação: Informe a data base a ser utilizada quando o preço do insumo está na moeda do projeto e está indexado a outra moeda. Caso não exista uma cotação para a moeda na data indicada, a cotação utilizada será a última anterior à data base para indexação.

Data Base para Conversão: Informe a data base a ser utilizada quando o preço do insumo tiver uma moeda diferente da moeda do projeto. Caso não exista uma cotação para a moeda na data indicada, a cotação utilizada será a última anterior à data base para conversão.

**Exemplos:**

Considere a moeda do projeto como R$.

O insumo que tem um preço ativo de US$ 0,50 será convertido somente no cálculo do projeto. Considerando que a cotação atual do US$ é de R$ 2,00, o preço do insumo será de R$ 1,00.

O insumo que custa R$ 3,50, mas está indexado ao US$, terá o seu preço calculado da seguinte maneira, considerando que a cotação na data de atualização do preço é de R$ 1,50 e a cotação atual é de R$ 2,00: 3,50/1,50\*2,00 = 4,67.

O insumo que custa US$ 3,50, mas está indexado ao CUB terá o seu preço calculado da seguinte maneira, considerando que a cotação do CUB na data de atualização do preço é de 1,50 e na data atual é de 4,00, será feita a indexação: 3,50/1,50\*4,00=9,333333333 e depois, considerando que a cotação atual do US$ é de 6,00 será de R$ 56,00.

**Calcular Projeto Vinculados a Tarefas:**

Criado o campo "Projeto vinculado" na tela de planilha de atividade. Aba recurso.

Parâmetro se encontra em Parâmetros do Projeto – Outros - Calcular Projetos Vinculados a Tarefas.

A tarefa que receber o projeto vinculado será uma tarefa de valor cotado.

Ao clicar no lookup para escolher o projeto a ser vinculado será exibido os projetos da coligada em questão. Projeto revisado, no momento se vincular só apresentará a ultima revisão.

Com o parâmetro setado "Calcular Projetos Vinculados a Tarefas" o valor atualizado do projeto vinculado será considerado no calculo do projeto. Caso contrário, não será considerado.

Exemplo:

Projeto A contém 2 tarefas no valor de R$2,50 cada. Total do projeto A →5,00

Projeto B contém 4 tarefas no valor de R$2,50 cada. Total do projeto B →10,00

No projeto A vinculo o projeto B.

Ao calcular o projeto A o resultado será R$15,00

Edito o projeto B, incluindo mais uma tarefa no valor de R$5,00.

No projeto A realizo o calculo do projeto, porém o parâmetro "Calcular Projetos Vinculados a Tarefas" não esta setado.

O valor do projeto continua R$15,00

Com o parâmetro Setado o valor do projeto será R$20,00.

**Considerar Tarefas de Custo Indireto na Curva S**Na curva S as tarefas de custo indireto não são consideradas, Para que as tarefas de Custo Indireto sejam consideradas no cálculo da curva o parâmetro deve estar marcado.

**% Curva ABC**

A Curva ABC agora pode ser classificada e separada em Curva A, B e C. A Classificação do Item é realizada em relação à Curva ABC. Para cada item da curva é definido uma classificação, baseada nos percentuais do item "% Curva ABC" nos parâmetros do projeto: Menu | Opções | Parâmetros | Totvs Obras e Projetos | Projetos, pasta Cálculo | Outros.

O campo % Curva ABC vem por default com os valores iniciais A = 65%, B = 25% e C = 10% e a classificação é definida em relação à importância do item no valor total da curva como no exemplo:

Valor Total Curva = R$ 1000,00

Classificação: A = 65%, B = 25% e C = 10%

Classe A = 650,00, Classe B = 250,00 e Classe C = 100,00

| Insumo | Valor | Valor Improdutivo | Total Item | Classificação Item |
| --- | --- | --- | --- | --- |
| Pedreiro | 580,00 | 100,00 | 680,00 | A |
| Carpinteiro | 170,00 | 50,00 | 220,00 | B |
| Servente | 80,00 | 20,00 | 100,00 | C |

**Observação:**

Todos os tipos de Curvas ABC deverão ter essa coluna de classificação, porém, apenas a de Insumo deverá possibilitar a utilização desse opção na confecção de relatórios.

**Considerar Tarefas de Custo Indireto**  
No cálculo do avanço físico as tarefas de custo indireto não são consideradas, Para que as tarefas de Custo Indireto sejam consideradas no cálculo o parâmetro deve estar marcado.

**Forma de cálculo do projeto**

Possibilita o cálculo do projeto de uma outra perspectiva. Além da forma **Padrão** default, considerando a quantidade total da tarefa; também será possível efetuar o cálculo pelo **Saldo da tarefa**, dessa maneira o  será exibido na barra de cálculo e nos , e não mais o valor total da tarefa e do total do projeto que é exibido atualmente na forma padrão.

* **Padrão**
  + O resultado é o valor total consolidado do projeto com base nas quantidades previstas e nos preços configurados.  
    Esse é o cálculo “base” que normalmente você executa após montar a planilha de serviços/insumos.

**Valor da Tarefa =** 100,00 (Quantidade da Tarefa) \* 10,00 (Custo Unitário) **= R$ 1.000,00**

* **Saldo da Tarefa**

* + Em vez de usar o total previsto da tarefa, o cálculo considera **o que falta realizar** conforme o saldo financeiro pendente.
  + Essa forma é útil quando você já realiza apontamentos e quer refletir apenas o valor ainda por executar no projeto.

Saldo da Tarefa = 100,00 (Quantidade da Tarefa) - 30,00 (Quantidade Cronograma Realizado) = 70,00

**Valor da Tarefa** = **70,00 (Saldo da Tarefa)** \* 10,00 (Custo Unitário) = **R$ 700,00**

* **Saldo da Tarefa + Apropriado**
  + Essa forma é usada quando o projeto já está em andamento e se deseja:

    - manter o custo real do que já foi executado,
    - recalcular apenas o restante,
    - atualizar orçamento após mudança de preços,
    - projetar custo final da obra,
    - acompanhar desvios de custo.
  + Permite visualizar:

    - custo realizado,
    - custo previsto restante,
    - custo total projetado atualizado do projeto.

    Isso evita recalcular tarefas já executadas e impede distorção do custo histórico.

Saldo da Tarefa = 100,00 (Quantidade da Tarefa) - 30,00 (Quantidade Cronograma Realizado) = 70,00

**Valor da Tarefa** = 70,00 (Saldo da Tarefa) \* 30,01 (Custo Unitário) + **60,02 (Valor Apropriado)** = **R$ 2.160,72**

* **Saldo da Tarefa + Apropriado (com indexador do projeto)**

Saldo da Tarefa = 100,00 (Quantidade da Tarefa) - 30,00 (Quantidade Cronograma Realizado) = 70,00

Indice acumulado IGPM = 1,00 + 0,01 (jan/2026) + 0,02 (fev/2026) = 1,03

Custo Unitário corrigido = 30,01 (Custo Unitário)  \* 1,03 (Indice acumulado IGPM) % = 30,9103

**Valor da Tarefa** = 70,00 (Saldo da Tarefa) \* **30,9103 (Custo Unitário Corrigido)** + **60,02 (Valor Apropriado)** = **R$ 2.223,74**

* **Saldo da Tarefa + Apropriado (Saldo calculado apenas em períodos fechados e permissão de alteração do cronograma realizado em determinado período)**

Saldo da Tarefa = 100,00 (Quantidade da Tarefa) - **10,00 (Quantidade Cronograma Realizado dos períodos fechados)** = 90,00

**Valor da Tarefa** = 90,00 (Saldo da Tarefa) \* 30,01 (Custo Unitário) + **30,01 (Valor Apropriado dos períodos que permitem alteração)** = **R$ 2.730,91**

---
