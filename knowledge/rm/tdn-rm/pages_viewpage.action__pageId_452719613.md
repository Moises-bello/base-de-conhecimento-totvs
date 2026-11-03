---
content_hash: 344ccfe96f92e5e3864ebe5f650ac3668fa491dc3bb9be1bfabbbfd5f4f85922
fetched_at: '2026-06-29T00:10:08.958747+00:00'
page_id: '452719613'
product: rm
source: tdn-rm
title: Pasta Configurações - Avaliação de Desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719613
version: 2
---

**Pasta Configurações - Avaliação de Desempenho**

Nesta pasta, deverão ser definidos todos os parâmetros para o modelo de avaliação desejado.

**Modalidade:** Define qual a modalidade da avaliação será utilizada.

**90 graus** - É a modalidade onde o Chefe avalia os Subordinados diretos e indiretos.

**180 graus** - Modalidade onde o Chefe avalia os Subordinados diretos e indiretos e estes se auto-avaliam. Neste modelo haverá uma avaliação de consenso que será considerada para geração dos resultados.

Na avaliação consensual avaliadores e avaliados entram em um consenso sobre a nota que deverá ser atribuída aos itens avaliados.

Após a execução das avaliações pelos avaliadores e avaliados e importação dos resultados destas avaliações, será enviado, automaticamente, um e-mail para o avaliador avisando sobre a avaliação consensual que deverá ser realizada.

**360 graus** - Nesta modalidade, a avaliação é feita de modo circular por todos os elementos que mantêm alguma interação com o avaliado. Participam desta avaliação, o próprio avaliado, o chefe, os pares, os subordinados, os clientes e os fornecedores internos e outras pessoas que desejarem participar da avaliação, enfim, todas as pessoas ao redor do avaliado, em uma abrangência de 360 graus.

A avaliação feita pelo entorno é mais rica por produzir diferentes informações vindas de todos os lados e funciona no sentido de assegurar a adaptabilidade e o ajustamento do funcionário às variadas demandas que ele recebe de seu ambiente de trabalho ou de seus parceiros.

**Observações**

* A avaliação consensual apenas será gerada automaticamente quando houver na base de dados a estrutura de chefes/supervisores, já quando a avaliação for respondida apenas entre pares, a avaliação consensual deverá ser gerada manualmente pelo processo: "Gerar Consensual", que está disponível no anexo: Andamento das Avaliações.
* Cabe ressaltar que a utilização de uma avaliação 360 graus apenas deve ser feita em Empresas que já possuem cultura de avaliação e já passaram por outras modalidades com boa percepção de sua aplicabilidade e seus benefícios.

**Modelo:**

Define se o modelo da escala gráfica a ser utilizado será simples ou misto.

* **Simples** - Neste modelo de escala gráfica não será permitida a utilização de pesos para os itens avaliados.
* **Mista** - Neste modelo de escala gráfica poderão ser inseridos pesos para os itens que serão avaliados. A opção "Exibir peso", se for selecionada, permitirá a visualização dos pesos de todos os itens avaliados, sendo que não será possível exibir peso somente para alguns itens da avaliação. Para os avaliadores não será possível incluir pesos.

**Observação**

O peso permitirá diferenciar o grau de importância de um item avaliado em relação a outro para um mesmo indivíduo.

**Agrupar por:**

Define o agrupamento das competências que serão avaliadas.

* **Cargos** – Serão exibidos os cargos e todas as competências que estão vinculadas ás funções que pertencem ao cargo em questão.
* **Funções** - Serão exibidas as funções e todas as suas competências vinculadas.

**Observação**

Os participantes serão listados independente de terem o cargo em sua função, mas os participantes sem cargos não terão competências levadas para a avaliação.

**Itens a avaliar:** Deverão ser definidos quais os itens serão avaliados, podendo-se definir um ou mais itens.

**Competências técnicas** - Serão avaliadas as competências específicas para que o(s) funcionário(s) possa(m) exercer uma função e que estão vinculadas à função exercida por ele.

**Competências Comportamentais** – Serão avaliadas as competências que a Empresa espera do(s) seu(s) funcionário(s) e que estão vinculadas à função exercida por ele.

**Usar outras Competências -** Serão avaliadas as competências diferentes de técnicas e comportamentais e que estão vinculadas à função exercida pelo funcionário.

**Observação:**

As competências definidas por "outras competências" devem ser relacionadas ao tipo criado na tabela dinâmica VTIPOCOMP com o código diferente de 00001 e 00002.

**Fatores Organizacionais**

– Serão avaliados fatores que a organização considera importante, mas que não se enquadram no conceito de competência, por exemplo: assiduidade, pontualidade, respeito às normas da empresa.

Estes fatores estão vinculados à seção na qual o funcionário está lotado.

Os fatores organizacionais serão trazidos de acordo com a coligada do funcionário avaliado, ou seja, apenas da coligada da avaliação.

**Ações –** Serão avaliadas as ações existentes em planos de metas (modelo antigo) onde o funcionário esteja vinculado com uma participante do plano(s).

Selecionando esta opção serão considerados todos os planos de metas que possuam ações cadastradas, que estejam ativos e abertos (sem data de fechamento), mesmo se a data de abertura do plano de metas estiver fora do período da avaliação de desempenho, as ações do plano serão consideradas.

Desta forma, se um avaliado estiver participando de vários planos de metas e se estes tiverem ações, todas as ações serão consideradas como itens a serem avaliados.

**Metas -** Serão avaliadas as metas existentes no Plano de Metas (modelo novo) associado na Avaliação de Desempenho por Competências.

Selecionando esta opção o funcionário (avaliado) deverá ter sido atribuído como membro do grupo de avaliação e logo após atribuído também como membro da meta contida no plano. Se a atribuição não for realizada o sistema apresentará a mensagem que existem avaliados sem itens a serem avaliados no momento em que salvar a avaliação.

**Avaliadores -**Esta opção será habilitada caso a modalidade escolhida seja 360 graus. Poderá ser definido também se o funcionário deverá ou não realizar a sua auto-avaliação, caso seja necessário, basta selecionar a opção "Auto-avaliação".

Neste caso o funcionário irá auto-avaliar os mesmos itens selecionados na opção "Itens a avaliar".

**Exibir Peso -** Esta opção será habilitada caso o modelo de avaliação gráfica escolhida seja a mista.

Selecionando está opção o peso atribuído para cada item avaliado será exibido para o avaliado durante a execução da avaliação.

**Alterar escala (notas) -** Esta opção permite informar uma escala para a competência que o funcionário possui. O aplicativo irá disponibilizar algumas opções de escalas, porém, o usuário poderá redefini-las, excluí-las ou criar as suas próprias escalas.

O funcionário que obtiver nota abaixo da escala definida como "Ponto de Corte" terá a graduação da competência que está sendo avaliada, reduzida para um nível abaixo ao que ele possui.

Caso o funcionário alcance uma escala superior ao ponto de corte, o aplicativo não irá alterar a graduação da competência vinculada no funcionário.

**Observação**

Ponto de corte é o referencial do que se espera como resposta necessária para a realização adequada da tarefa que deve ser realizada utilizando o item avaliado. Este valor, na escala padrão corresponderá ao item "atende as necessidades", que poderá ser alterado de acordo com o interesse da política de gestão da organização.
