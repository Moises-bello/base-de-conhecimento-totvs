---
content_hash: 35fd57ba9ac68621c4e0748100726942bb522ee11e41ba2bef2d5cca61f1c8c3
fetched_at: '2026-06-29T00:05:55.281958+00:00'
page_id: '128683355'
product: rm
source: tdn-rm
title: Criação de Gráfico Drill Down
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=128683355
version: 18
---

# Índice

---

.\*ndice:

# Objetivo

---

      O objetivo deste documento é a auxiliar usuários na criação de um Gráfico Drill Down utilizando como fonte de dados uma consulta SQL. Gráficos do Tipo **Drill Down**, possibilitam a exploração das informações em **diferentes níveis de detalhes**, de forma **hierárquica**.

# Como Criar

---

      Para criar um Gráfico Drill Down, acesse o menu***Gestão | Gráficos***e clique no botão ***Novo***. Na tela de cadastro, será necessário preencher os campos obrigatórios, como: titulo, categoria e fonte de dados. Neste exemplo, utilizaremos uma Consulta SQL como Fonte de Dados. Assim, será necessário preencher também o campo Consulta SQL.

      Veja o documento para visualizar detalhadamente como criar um novo gráfico.

      Após salvar a tela, o RM solicitará que seja feita a configuração do gráfico. Para isso, clique no botão ***Sim***ou acesse o menu ***Processos > Assistente de Configuração de Gráfico**.*

# Configurando o Gráfico Drill Down

---

     O Assistente de Configuração apresenta opções de **Construção**e de **Apresentação**. No exemplo desta página, será feita a criação de Gráfico em Barra.

false

**CONFIGURAÇÕES DE CONSTRUÇÃO**

Assistente de ConfiguraçãoCenárioCenárioCenário

**Exemplo:**

Neste exemplo, utilizaremos uma consulta SQL que terá como resultado dados de funcionários, coletados das tabelas PFUNC e PSECAO. Como mostrado abaixo:

A consulta abaixo retornará dados dos campos: CHAPA, NOME, SALARIO, FUNÇÃO E SEÇÃO

sql1Consulta:trueTipo de GráficoTipo de GráficoTipo de Gráfico

**Tipo de Gráfico**

Nessa tela deve ser selecionado qual o tipo de gráfico será construído. Selecione o tipo **Barra** e clique em **Próximo**.

SériesSériesSéries

**Séries**

 Devemos cadastrar nesta tela as séries do gráfico. Seguindo o exemplo da consulta SQL, serão incluídas 3 séries:

* Série1 (SEÇÃO): Responsável por exibir o Total de Salários por Seção.
* Série 2 (FUNÇÃO): Responsável por exibir o Total de Salários por Função de uma determinada Seção.
* Série 3 (FUNCIONÁRIO): Responsável por exibir o Salário das Chapas de uma determinada Seção e Função. Será exibido o valor dos salários das chapas correspondentes a função selecionada. Ao selecionar **qualquer função**, o gráfico exibirá os salários das chapas **correspondentes** a mesma.

Apenas a Série 1 ficará 'Visível' e as demais ficarão invisíveis, assim, ao abrir o gráfico apenas os dados da Série 1 serão exibidos. Ao clicar nos itens da Série 1, será exibido os dados da Série 2 e posteriormente da Série 3. A configuração ficará como mostrado na figura abaixo:

Preencha também o campo 'Texto' que está disponível na aba Opções da Série, para todas as séries:

Lembre-se

As informações no Gráfico do Tipo Drill Down são exibidas de forma **hierárquica**.

Para cadastrar uma série, clique no botão **Adicionar** e defina o nome da série.

DadosDadosDados

**Dados**

Aqui faremos a configuração para ligar as Séries aos dados retornados pela Consulta SQL. Essa tela possui três abas de configuração: **Pontos**, **Binding de Séries** e **Série auto-criada**.

Na aba **Binding de Séries** serão exibidas as 3 séries cadastradas. Faremos a seguinte configuração:

**Selecione a Série 1**

* Clique no campo SEÇÃO
* Propriedades do Argumento **(Selecione Table1.SECAO)**
* Propriedades do Valor **(Selecione Table1.SALARIO)**
* Desta forma, acabamos de ligar a Série 1 do Gráfico ao Código da Seção retornado pela SQL.

**Selecione a Série 2**

* Clique no campo FUNÇÃO
* Propriedades do Argumento (Selecione Table1.FUNCAO)
* Propriedades do Valor (Selecione Table1.SALARIO)
* Desta forma, estamos informando que o campo SALARIO deverá ser somado para cada função.

**Selecione a Série 3**

* Clique no campo FUNCIONARIO
* Propriedades do Argumento **(Selecione Tabe1.CHAPA)**
* Propriedades do Valor **(Selecione Table1.SALARIO)**

Desta forma, estamos informando que o campo SALARIO deverá ser exibido para cada seção.

Após configurar a **Propriedade do Agrupamento** e a **Propriedade do Valor,** acesse a aba **Pontos** e visualize os dados que serão utilizados na representação do gráfico:

Drill DownDrill DownDrill Down

**Drill Down**

Nessa tela são parametrizadas as ações que serão realizadas pelo Gráfico. Vamos configurar para que o gráfico possibilite a navegação entre os níveis da hierarquia criado nas séries.

**Selecione a Série 1 (SEÇÃO)**

* No Campo **gatilho**: Selecione a opção: Clique Simples
* **Tipo de Drill Down:** Selecione a opção GRÁFICO
* **Série de destino**: Selecione a opção FUNÇÃO

Resumidamente, estamos dizendo que ao clicar nos itens da Série 1 (SEÇÃO), o gráfico da Série 2 (FUNÇÃO) será carregado, ou seja, na Série 1 são exibidos **os valores** de salários por seção. Se clicarmos na barra de qualquer SEÇÃO exibida, será carregado um segundo gráfico que refere-se a Série 2 (FUNÇÃO) que exibirá o total de salários por função da seção.

**Selecione a Série 2 (FUNÇÃO)**

* No Campo **gatilho**: Selecione a opção: Clique Simples
* **Tipo de Drill Down:** Selecione a opção GRÁFICO
* **Série de destino**: Selecione a opção FUNCIONÁRIO

Com essa configuração, ao clicar em uma das barras da Série 2 (FUNÇÃO), será exibido os salários de cada funcionário (CHAPA) da determinada função selecionada.

**Por último, devemos configurar a Série 3 (FUNCIONÁRIO)**

* No Campo **gatilho**: Selecione a opção: Clique Simples
* **Tipo de Drill Down:** Selecione a opção DADOS

Neste caso, não temos mais gráficos a serem exibidos. Estamos no último nível de informação da consulta SQL.

Desta forma, o sistema exibirá apenas um quadro com um resumo das informações quando clicarmos em uma das barra da Série 3 (FUNCIONÁRIOS).

**Visualizando o Gráfico Drill Down**

Ao finalizar o Assistente de configuração de Gráficos será apresentada a mensagem para visualização do Gráfico. Clique em **Sim** para visualizar o Gráfico.

ApresentaçãoApresentaçãoApresentação

**Configurações de Apresentação**

**Recursos adicionais (Configurações de Formatação)**  
  
**Gráfico:** Personalize as propriedades do Gráfico ***(Cor de Fundo, Estilo de Preenchimento)***  
**Diagrama:** Personalize as propriedades do Diagrama ***(Margens, Layout do Papel)***  
**Painéis:** Customize diagrama de Paineis   
**Eixos:** Visualização e Posição dos eixos: X e Y do Diagrama   
**Séries:** Personaliza as opções de exibição tipo específico de uma série ***(Aparência, cor, borda, Sombra)***  
**Rótulo de Ponto:** (Layouts de Configuração, Configurações do Texto, Configurações de Sobreposição).   
**Títulos de Gráfico:** (Adicione e personalize Título de Gráfico).   
**Legenda:** (Personalize propriedades de Legenda)   
**Anotações:** (Cria Anotações ancorado em um gráfico) 

Para mais informações sobre a customização do gráfico e as configurações de apresentação, acesse o documento **[Configuração de Gráfico](http://tdn.totvs.com/pages/viewpage.action?pageId=271847659).**

# Visualização do gráfico

---

     Ao abrir a visualização do gráfico criado neste documento, será exibido um gráfico de barras onde cada uma refere-se a uma SEÇÃO. Observe que os valores apresentados referem-se aos salários de cada funcionário existente naquela SEÇÃO.

Para visualizar os salários por FUNÇÃO, basta clicar em qualquer barra do Gráfico. Neste instante será apresentado o Gráfico com os valores salariais por função. No gráfico abaixo é possível visualizar as Funções mais os valores salariais respectivos a cada seção.

Clique sobre a FUNÇÃO para visualizar os funcionários dessa função. Para visualizar os dados da consulta SQL, basta clicar em **Dados de Origem.**Como mostrado na figura abaixo:

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Inclusão de Gráficos Drill Down

falsefalse

**Status:** Finalizado

false

**Data:** 02/08/2017

false

**Autores:**
