---
content_hash: 3e7a5ea3216401128c0277cc32e290bf998d8571cf9876c04deb4a2392b957bd
fetched_at: '2026-06-29T00:09:24.816551+00:00'
page_id: '423938026'
product: rm
source: tdn-rm
title: Cadastro de Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938026
version: 26
---

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Dica!

A partir da Release 12.1.2402 este cadastro passa a oferecer a integração com o File Repo. Para mais informações consulte nossa documentação neste [link](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828).

Imagem

Responsável por armazenar todas as informações relacionadas ao Patrimônio (antiga tela de cadastro de Bem) este cadastro permite que sejam visualizados todos os patrimônios existentes na base de dados, bem como a realização de ocorrências (Baixa, Acréscimo e Transferência Monetária) e Transferência de Controle, além da contabilização de aquisição.

Ao acessar a visão de Patrimônios cadastrados (executando o filtro desejado) a partir do Menu Cadastros/Patrimônios pode-se visualizar informações tais como o Grupo de Patrimônio, o status da contabilização da aquisição, filial, departamento entre outros dados.

A tela de patrimônio está divida em abas que serão descritas a seguir:

falseOrientações para preenchimento dos camposa,b,c,d,e,fleftaDados Gerais

**Dados Gerais**

Serão apresentadas nesta aba informações tais como o código do patrimônio, seu tipo (Título ou Patrimônio), a descrição, os códigos da filial e fornecedor, o código de barras, a data de aquisição, o valor do patrimônio, o grupo de patrimônio relacionado ao mesmo, a moeda e o cenário de cálculo entre outras informações. Também deverá ser definido, nesta aba, o centro de custo, o departamento, responsável e o local referentes ao Patrimônio.

bGarantias/Apólices de Seguros

**Garantias/Apólices de Seguros**

Permite que  e garantias sejam vinculadas ao patrimônio de forma a manter um controle efetivo destes dados.

cContabilidade

**Contabilidade**

O cadastro de default contábil do patrimônio, que será utilizado pelo processo de contabilização, deverá ser definido nesta aba. Além do default contábil pode-se também informar o rateio gerencial e o de reavaliação que serão utilizados na contabilização de depreciação/correção.

dCálculos/Ocorrências

**Cálculos/Ocorrências**

Todos os valores existentes para o Patrimônio tais como valor base corrigido, a taxa de depreciação, a depreciação mensal e a acumulada, o saldo residual bem como a moeda, a data referente ao cálculo e o cenário serão exibidos nesta aba. Serão exibidos valores por moeda e por índice (caso esteja parametrizado para utilizar índice) para cada cenário associado ao grupo de patrimônio utilizado pelo patrimônio.

**Ocorrências**

Todas as ocorrências realizadas no patrimônio seja ela Baixa, Acréscimo ou Transferência Monetária serão exibidas nesta aba. Ao editar uma ocorrência serão exibidas informações como o tipo de ocorrência (Baixa, Acréscimo ou Transferência Monetária), os patrimônios de origem e destino, a moeda/índice, a data da ocorrência e os valores (em moeda e índice). Por esta aba pode-se também realizar a contabilização da ocorrência. Para isto deve-se selecionar a ocorrência desejada e acessar a opção Contabilização/"o tipo de ocorrência". Após realizar a contabilização da ocorrência, caso deseje, pode-se visualizar os lançamentos contábeis a partir da opção "Visualizar a Contabilização da ocorrência".

eHistóricos de Controle

**Históricos de Controle**

Armazena as informações referentes a Filial, o Departamento, o Centro de Custo, a Localização e o Responsável vinculadas ao patrimônio. A cada transferência de controle estas informações serão atualizadas de maneira a facilitar, por parte do usuário, o controle do patrimônio. Os dados exibidos nesta aba são: o código da transferência, a data de entrada e saída, os usuários de criação e alteração, e as datas de criação e alteração.

eHistórico de Inventário

**Histórico de Inventário**

Armazena informações referentes ao Histórico de Inventário do Patrimônio.

Para Históricos gerados via Processo de Inventário, serão exibidos dados de: data e identificador do inventário, layout, filial, centro de custo, departamento, local, responsável, usuários de criação e alteração, e as datas de criação e alteração.

Para Históricos gerados via Inventário Mobile e que tenham sido Integrados ao Patrimônio, serão exibidos dados de: data e identificador do inventário, filial, centro de custo, departamento, local, usuários de criação e alteração, datas de criação e alteração e Usuário responsável pelo Inventário.

eHistóricos de Alocação

**Históricos de Alocação**

Armazena as informações referentes a Filial, o Departamento, o Centro de Custo, a Localização e o Responsável das alocações realizados o patrimônio. A cada alocação de patrimônio estas informações serão atualizadas de maneira a facilitar, por parte do usuário, o controle do patrimônio. Os dados exibidos nesta aba são: o código da alocação, a data de entrada e saída, os usuários de criação e alteração, e as datas de criação e alteração.

**Observação**

Caso o parâmetro "Usar funcionários do RM Labore como responsáveis" estiver selecionado a palavra Responsável será substituída por Funcionários fazendo uma referencia aos funcionários cadastrados na base de dados.

eHistórico Cálculo/Ocorrência

**Histórico Cálculo/Ocorrência**

Responsável por guardar o histórico dos valores (em ) e de ocorrências (Baixa, Acréscimo e Transferência Monetária) realizadas no patrimônio após cada fechamento de período. Por medida de segurança não será permitia a alteração das informações exibidas nesta aba.

Todas as abas citadas anteriormente bem como os recursos associados a elas podem também ser visualizadas a partir dos Anexos da visão de Patrimônios.

**Inclusão de Patrimônio**

Antes de realizar a inclusão de um Patrimônio deve-se verificar, entre as informações relacionados ao Patrimônio.Net, os seguintes itens:

* Existir moeda e índice (caso necessário) e suas respectivas cotações preenchidas corretamente para o período desejado;
* Cálculo com o tipo e periodicidade definidos;
* Cenário com cálculo, moeda e índice devidamente associados;
* Grupo de Patrimônio com a taxa e o cenário associado;

As primeiras informações a serem preenchidas são referentes a aba Identificação. Nesta etapa somente as abas Identificação, Dados Adicionais e Observação estarão habilitadas. Após preencher as informações das abas citadas acima, dando destaque para os campos obrigatórios, e clicando no botão salvar será exibida uma mensagem confirmando a inclusão do patrimônio. Caso seja confirmado, o restante dos dados da outras abas será preenchido.

**Observação**

Caso os dados da aba "Aquisição por moedas/índices" e "Cenários para cálculos" não sejam preenchidos pode-se verificar o cenário existente no grupo de patrimônio associado ao patrimônio em questão, além do cálculo associado a este cenário.

Com estas informações devidamente preenchidas deve-se executar o processo "Criar Moeda/Cenário de Cálculo". Este processo irá preencher os dados referentes a moeda, índice, o cálculo e o cenário associados ao grupo de patrimônio.  
Durante a aquisição caso a opção "Contabilizar Aquisição" esteja selecionada, a tela de contabilização de aquisição será exibida. Desta forma a contabilização será realizada respeitando o evento contábil associado ao cenário definido no grupo de patrimônio do patrimônio em questão. Ao optar em não contabilizar a aquisição, porém deixando a opção "Contabilizar Aquisição" marcada, a contabilização do patrimônio ficará com o status pendente podendo assim ser contabilizado posteriormente. Para visualizar a contabilização da aquisição do patrimônio deve-se acessar a aba Dados Gerais/Cenários para cálculos, editar o cenário existente e escolher a opção "Visualizar contabilização da aquisição".

Após a inclusão do patrimônio deve-se executar o processo de Cálculo de depreciação. Este processo irá realizar o calculo do patrimônio preenchendo todos os valores, em moeda e índices, respeitando a valor de aquisição e as cotações (da moeda e índice). Estes valores podem ser conferidos na aba Cálculos/Ocorrências na opção Cálculo Razão.

**Integrações**

Ao editar um Patrimônio que foi gerado a partir de um Contrato ou de uma Nota Fiscal, será possível visualizar uma aba chamada "Integrações", nela são listados os cadastros de Nota Fiscal, Contrato ou Objeto de Manutenção, de acordo com o tipo da Integração que gerou o Patrimônio.  
Informação:   
           - Para contratos versão 2.0, detalhes adicionais devem ser consultados diretamente no cadastro do contrato.  
           - Contrato não encontrado: Caso o patrimônio esteja vinculado a um contrato que tenha sido excluído ou cujo item tenha sido alterado, na aba de contratos será exibido um alerta informando que os dados do contrato não foram encontrados.

Processos









* [Exclusão de Patrimônio](https://tdn.totvs.com/pages/viewpage.action?pageId=673796536)
Veja também
