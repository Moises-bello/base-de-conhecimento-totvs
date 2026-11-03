---
content_hash: 993792d00361f76e9aff813c2810009bca61ced7ceead497749dcc9c01ee60d2
fetched_at: '2026-06-29T00:09:16.718629+00:00'
page_id: '421385540'
product: rm
source: tdn-rm
title: Relatórios Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385540
version: 49
---

---

Através desta funcionalidade é possível gerar os Relatórios Periódicos de Cronograma, Histograma e/ou Planilha de acordo com os filtros escolhidos:

Relatório PeriódicoCronograma

**Relatório Periódico - Cronograma**

**1- Informações de Tarefas:**

* **Subprojeto:** Aparecerá somente informações da obra. Ex: 001 - Fundação prédio; - O nome "subprojetos" será semelhante ao da tabela de parâmetros. Caso esteja vazio, o nome aparecerá como "Obra";
* **Etapa:** Aparecerá somente informações de etapa. Ex: 001.01 - Serviços iniciais;
* **Serviço:** Aparecerá somente informações de serviços. Ex: 001.01.01 - Escavação de Tubulões;
  + **Incluir Serviços de Custo Indireto:** Marque essa opção se desejar incluir os serviços de custo indireto no relatório de cronograma.
  + **Incluir Serviços de Receita:**Marque essa opção se desejar incluir os serviços de Receita no relatório de cronograma.

**2- Visualizar:**

Ao configurar essas opções, as informações de Grandeza selecionada do cronograma aparecerão na linha do relatório:

* **Percentual;**
* **Quantidade;**
* **Valor;**

Etapa - Quantidade 

Caso em Informações de Tarefas seja selecionado a Opção Etapa, o sistema desabilita a Visualização por Quantidade, uma vez que Etapas não possuem Quantidade.

**3- Campos Disponíveis:** 

Campos a serem visualizados no cabeçalho de Relatório (informações de Tarefas):

* **Código;**
* **Nome;**
* **Descrição;**
* **Unidade;**
* **Código Auxiliar;**
* **Código Recurso Associado;**

**4- Tipo:** 

Essas colunas aparecerão ou não de acordo com a opção de seleção. Opções disponíveis:

* **Previsto;**
* **Realizado;**
* **Medido;**
* **Linha Base;**

**Apropriado:**

De acordo com as opções selecionadas, serão exibidos dados de:

* **Apropriação do Backoffice:**Para o cronograma apropriado do Backoffice, são considerados os movimentos que têm o parâmetro "Gera apropriação" marcado na parametrização do tipo do movimento no Backoffice. Caso a apropriação tenha sido feita, no Backoffice, numa data anterior ao primeiro período, a mesma será visualizada no primeiro período. Se a data da apropriação for posterior a data do último período, a mesma será visualizada no último período;
* **Obras e Projetos:**Caso as requisições sejam por obra (campo acima desmarcado), no relatório periódico de Cronograma Apropriado do Backoffice, as apropriações só ficarão visíveis para obras.   
  Para o cronograma apropriado, o valor das apropriações para a tarefa é somado e depois se calcula o percentual que o mesmo representa em relação ao valor da tarefa. Desse percentual chega-se à quantidade e ao valor. No relatório de cronograma planejado a quantidade apresentada está na unidade do Totvs Construção Obras e Projetos.   
  No relatório de cronograma apropriado a quantidade apresentada está na unidade do Totvs Construções Obras e Projeto.   
  O preço é o da compra efetivada no Backoffice.   
  Se o parâmetro 'Vigência de Preços' estiver ativo, os cronogramas previsto, medido e realizado são calculados considerando a vigência e a aplicação do preço dos insumos para cada período. Esse parâmetro é acionado através do menu Projetos | TOTVS Construção Obras e Projetos | Projetos (Ou atalho F6) | Cálculo | Fator K.   
  Caso o cronograma previsto não esteja 100 % programado haverá diferença entre os cronogramas com e sem vigência das etapas e obras;
* **Consulta Personalizada:**Esta consulta será Habilitada quando nos Parâmetros de Projeto, Menu Projeto | TOTVS Construção Obras e Projetos | Projetos (Ou atalho F6) | Apropriação | Apropriação BackOffice esteja preenchido as Consultas SQL Personalizadas para Dados de Apropriação;

**5- Períodos:**

Seleção de número de períodos (inicial e final) a ser impresso no cronograma:

* **De:**Informe o Período Inicial. Ex: 1;
* **Até:**Informe o Período Final. Ex: 100;

**6- Rep. Períodos:**

* **Num. dias:** O cabeçalho do cronograma será impresso através do número de dias do período;
* **Data:** O cabeçalho do cronograma será impresso através do intervalo de dados do período;

**7- Representação:**

* **Sem barra:** Não incluir barra de cor nos percentuais do Cronograma;
* **C****om barra:** Inclui uma barra de cor nos percentuais do Cronograma, para uma melhor de visualização;

**8- Cenário:**

Serão Exibidos todos os cenários disponíveis (filtrado pela Coligada corrente e Projeto corrente).

**9- Tipo de Planilha:**

Selecione a opção de Planilha que deseja visualizar no Relatório.

* **Planilha de Atividades;**
* **Planilha de serviços;**

**10- Tarefas:**

Faixa de Tarefas a serem impressas no Cabeçalho do Relatório.

* **Tarefa inicial:**Informe a Tarefa Inicial. Ex: 001;
* **Tarefa Final:**Informe a Tarefa Final. Ex: 004.03;

Após selecionar as opções de filtro, basta clicar no botão 'Ok' para que o relatório seja gerado.

---

Histograma

**Relatório Periódico - Histograma**

**1- De - Insumos:**

Será exibido dados do Histograma de Insumos e utilização desses Insumos (quantidade e valor) nos Períodos selecionados.

Acumular Valores e Valor Improdutivo

O usuário poderá Selecionar a opção "Acumular valores". Com essa opção os dados dos períodos serão acumulados nos Períodos (Previsto, Realizado, Medido e Apropriado) subsequentes;

Com esta opção desmarcada, os campos Valor e Quantidade do insumo serão seus respectivos valores totais. Ao marcar esta opção, os valores serão somatório dos valores dos períodos exibidos. Em caso de não existirem períodos, será exibido o valor e a quantidade total.

**Ordenação:**

Forma de ordenação do detalhe do relatório:

* **Código do insumo:** O detalhe do relatório será ordenado por "código do insumo";
* **Grupo de Custo:** O relatório será agrupado por grupo de custo [código - descrição];
* **Moeda:** Ao selecionar a ordenação por moeda, o sistema irá gerar um relatório ordenado pela moeda corrente e vigente no período de cada insumo.

O usuário poderá Selecionar a opção "Valor improdutivo" para:

* **Despesa;**
* **Receita;**

**2- De - Serviços:**

Será exibido dados do Histograma de Serviços.

Com essa opção selecionada, os dados serão agrupados por Composição e por Insumo. Ou seja, esses recursos não repetirão no detalhe do relatório. Com essa opção desmarcada, esses dados poderão repetir no detalhe do relatório.

Caso Utilize Vigência

Caso o Projeto utilize Vigência os campos "Acumula Valores" e "Valor improdutivo" serão desabilitados se a Ordenação for por Moeda.

Antes de Gerar o Relatório recomenda-se que seja Calculado a Curva S. Para isto basta selecionar a Opção:

**3- Grupo de Custo**

Selecione os Grupos de Custo referente ao que se deseja emitir o Relatório. Para isso basta selecionar os mesmo e utilizar as Setas. Veja:

**4- Tipo**

Essas colunas aparecerão ou não de acordo com a opção de seleção. Opções disponíveis:

* **Previsto;**
* **Realizado;**
* **Medido;**
* **Linha Base;**

**Apropriado:**

De acordo com as opções selecionadas, serão exibidos dados de:

* **Apropriação do Backoffice:**Para o cronograma apropriado do Backoffice, são considerados os movimentos que têm o parâmetro "Gera apropriação" marcado na parametrização do tipo do movimento no Backoffice. Caso a apropriação tenha sido feita, no Backoffice, numa data anterior ao primeiro período, a mesma será visualizada no primeiro período. Se a data da apropriação for posterior a data do último período, a mesma será visualizada no último período;
* **Obras e Projetos:**Caso as requisições sejam por obra (campo acima desmarcado), no relatório periódico de Cronograma Apropriado do Backoffice, as apropriações só ficarão visíveis para obras.   
  Para o cronograma apropriado, o valor das apropriações para a tarefa é somado e depois se calcula o percentual que o mesmo representa em relação ao valor da tarefa. Desse percentual chega-se à quantidade e ao valor. No relatório de cronograma planejado a quantidade apresentada está na unidade do Totvs Construção Obras e Projetos.   
  No relatório de cronograma apropriado a quantidade apresentada está na unidade do Totvs Construções Obras e Projeto.   
  O preço é o da compra efetivada no Backoffice.   
  Se o parâmetro 'Vigência de Preços' estiver ativo, os cronogramas previsto, medido e realizado são calculados considerando a vigência e a aplicação do preço dos insumos para cada período. Esse parâmetro é acionado através do menu Projetos | TOTVS Construção Obras e Projetos | Projetos (Ou atalho F6) | Cálculo | Fator K.   
  Caso o cronograma previsto não esteja 100 % programado haverá diferença entre os cronogramas com e sem vigência das etapas e obras;
* **Consulta Personalizada:**Esta consulta será Habilitada quando nos Parâmetros de Projeto, Menu Projeto | TOTVS Construção Obras e Projetos | Projetos (Ou atalho F6) | Apropriação | Apropriação BackOffice esteja preenchido as Consultas SQL Personalizadas para Dados de Apropriação;

**5- Períodos:**

Seleção de número de períodos (inicial e final) a ser impresso no cronograma:

* **De:**Informe o Período Inicial. Ex: 1;
* **Até:**Informe o Período Final. Ex: 100;

**6- Rep. Períodos:**

* **Num. dias:** O cabeçalho do cronograma será impresso através do número de dias do período;
* **Data:** O cabeçalho do cronograma será impresso através do intervalo de dados do período;

**7- Representação:**

* **Sem barra:** Não incluir barra de cor nos percentuais do Cronograma;
* **C****om barra:** Inclui uma barra de cor nos percentuais do Cronograma, para uma melhor de visualização;

**8- Cenário:**

Serão Exibidos todos os cenários disponíveis (filtrado pela Coligada corrente e Projeto corrente).

**9- Tipo de Planilha:**

Selecione a opção de Planilha que deseja visualizar no Relatório.

* **Planilha de Atividades;**
* **Planilha de serviços;**

**10- Tarefas:**

Faixa de Tarefas a serem impressas no Cabeçalho do Relatório.

* **Tarefa inicial:**Informe a Tarefa Inicial. Ex: 001;
* **Tarefa Final:**Informe a Tarefa Final. Ex: 004.03;

Cálculo

Para o Relatório Periódico do Histograma, os valores e quantidades apresentados é calculados com percentual Planejado no Cronograma Base sobre os valores dos insumos.

Após selecionar as opções de filtro, basta clicar no botão 'Ok' para que o relatório seja gerado.

---

Planilha

**Relatório Periódico - Planilha**

**1- Campos disponíveis:**

Selecione a(s) opção(s) que deseja visualizar no Relatório, entre elas:

* **Código;**
* **Nome;**
* **Descrição;**
* **Unidade;**
* **Código Auxiliar;**
* **Código Recurso Associado;**

**2- Opções:**

* **Incluir Serviços de Custo Indireto:**Com essa opção habilitada é possível visualizar no relatório os Serviços de Custo Indireto;

**3- Cenário:**

Serão Exibidos todos os cenários disponíveis (filtrado pela Coligada corrente e Projeto corrente).

**4- Tipo de Planilha:**

Selecione a opção de Planilha que deseja visualizar no Relatório.

* **Planilha de Atividades;**
* **Planilha de serviços;**

**5- Tarefas:**

Faixa de Tarefas a serem impressas no Cabeçalho do Relatório.

* **Tarefa inicial:**Informe a Tarefa Inicial. Ex: 001;
* **Tarefa Final:**Informe a Tarefa Final. Ex: 004.03;

Após selecionar as opções de filtro, basta clicar no botão 'Ok' para que o relatório seja gerado.

---
