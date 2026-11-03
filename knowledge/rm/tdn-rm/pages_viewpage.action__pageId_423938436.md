---
content_hash: 1afba178647f68c05c96d7ce6b5e74f0d86cdaf1f83dc246f3ca19e8a1e2e436
fetched_at: '2026-06-29T00:09:26.825790+00:00'
page_id: '423938436'
product: rm
source: tdn-rm
title: Lote Oficial / Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938436
version: 43
---

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

Através deste módulo é possível controlar o cadastro geral de *Lançamentos Contábeis.*

Um Lançamento Contábil pode ser considerado como um *agrupador* das Partidas de uma determinada operação, onde as Partidas representam os Débitos e Créditos que compõem cada operação sempre realizada em uma *mesma data*. O registro dos lançamentos contábeis é realizado utilizando-se o método das Partidas Dobradas, não havendo Débito sem Crédito correspondente. Desta forma, um Lançamento pode ser composto por uma única Partida que contenha nela mesma o Débito e o Crédito de determinada operação ou por várias partidas de Débitos e Créditos que representem determinada operação, onde a soma dos valores da(s) partidas(s) de Débito deve sempre ser igual à soma dos valores da(s) partida(s) de Crédito.

Na tela principal, também chamada tela de *Visão dos Lançamentos*, é possível ter uma visão geral do cadastro de todos os Lançamentos Contábeis.

A forma de apresentação e organização dos lançamentos na tela principal dependerá da forma escolhida para visualizá-los. Para visualizar os lançamentos agrupados por determinada informação, arraste o cabeçalho da coluna desejada para o Painel de Agrupamento de Colunas, espaço localizado acima dos nomes das colunas. É possível fazer combinações de agrupamentos e quebras apenas arrastando, como desejar, os cabeçalhos das colunas. Arraste, por exemplo, para a parte superior a coluna '*Id Lançamento*'. Desta forma cada lançamento e suas respectivas partidas serão apresentadas separadamente. Pode-se também criar filtros para seleção dos lançamentos através do Gerenciador de Filtros (localizado na Barra de Ferramentas).  
   
Na parte inferior desta visão existe a informação sobre os totais de débito e de crédito e a diferença entre estes totais. Se for necessário obter os totais de débito e crédito somente de alguns lançamentos, faça um filtro para mostrar somente estes ou, na própria tela de visão, clique selecionando somente as partidas dos lançamentos desejados, assim o sistema refaz e apresenta o cálculo dos totais das partidas que estiverem selecionadas.  
   
Quando se **Edita** um lançamento contábil é possível visualizar o cadastro geral de todas as Partidas que compõem este Lançamento. Na linha de *Status* desta nova visão serão apresentados os valores totais de Débitos e Créditos deste lançamento e possíveis diferenças entre os mesmos. Se alguma de suas partidas for selecionada, o sistema passará a apresentar os totais referentes à(s) partida(s) selecionada(s). Também será apresentada uma mensagem sobre a situação atual do lançamento aberto em edição, informando se ele se encontra liberado para edição ou bloqueado com outro usuário. Se o lançamento estiver bloqueado, ele ficará disponível apenas para consulta.  
Dizemos que um Lançamento está "*Bloqueado"* com um usuário, sempre que a soma dos Débitos não for igual à soma dos Créditos. Neste caso o campo Bloqueio/Usuário, que fica presente na tela principal dos lançamentos (*Visão dos Lançamentos*), ficará preenchido como o nome do usuário que estiver incluindo/editando este lançamento. Se outro usuário editar este lançamento bloqueado, todos os seus campos ficarão desabilitados, pois somente o usuário responsável pela diferença poderá dar manutenção no mesmo. Até que esta diferença seja sanada, o lançamento permanecerá "*Bloqueado"*. No momento da inclusão/edição de um lançamento, mesmo que não haja diferença entre a soma dos débitos e dos créditos, este permanecerá bloqueado com o usuário que o estiver editando e só será desbloqueado quando a tela for fechada e não houver diferença.  
   
Para **Excluir** um lançamento, selecione suas partidas e acione o botão Excluir, e muita atenção, pela tela principal (*Visão dos Lançamentos*), não é possível excluir somente uma partida de um lançamento, mesmo selecionando somente uma partida a exclusão será de todo o lançamento e das partidas que o compõem. Se desejar excluir somente uma partida, primeiro edite o lançamento depois selecione a partida desejada e acione o botão Excluir da tela de visão das partidas do lançamento, desta forma, somente a partida selecionada será excluída.  
   
Para **Incluir** um Lançamento Contábil deve ser informada a *Descrição* e a *Data* e, posteriormente, a inclusão de suas *Partidas* de Débito e de Crédito.   
A *Data* do lançamento deve estar dentro do período contábil e do período de digitação permitido para o usuário.  
   
**Observações**

* Na inclusão de um lançamento, o campo *Data* já poderá vir preenchido com a data informada nas *Preferências do Usuário*.
* Quando o sistema estiver parametrizado para não permitir diferenças, enquanto houver em algum lançamento diferença entre os totais de débitos e de créditos, na inclusão de um novo lançamento o campo Data já virá preenchido com a data da diferença, somente permitindo inclusão de lançamentos em outra data no momento em que a diferença encontrada for sanada.
* Para inclusão de lançamentos dentro do lote, quando as datas inicial e final da Capa do Lote forem iguais, o sistema irá sugerir esta mesma data na inclusão dos lançamentos para este lote.
* Em algumas situações o usuário pode filtrar apenas parte do lançamento, por exemplo: Em um mesmo lançamento possui 4 partidas, sendo 2 partidas para a filial 01 e 2 partidas para a filial 02, o usuário cria um filtro para ver somente partidas da filial 01, neste caso ao editar o lançamento não está sendo mostrada todas as partidas do lançamento. Caso o filtro ocasione diferença na visualização, será apresentada uma diferença de débito x créditos, porém o lançamento não contém diferença, pois as informações apresentadas no status correspondem às partidas filtradas e exibidas na tela. Quando esse tipo de filtro for utilizado, será disponibilizado na barra de tarefas na visão de lançamento contábil um botão de recálculo, através dessa funcionalidade será possível consultar situação da totalidade dos débitos e dos créditos do lançamento contábil.
* A forma como o sistema está parametrizado irá influenciar diretamente na inclusão/edição dos lançamentos e suas partidas, por isto verifique os Parâmetros do Sistema, principalmente o processo do assistente de implantação referente a Lançamentos.
* Não é permitido efetuar quaisquer manutenções (inclusão, exclusão, alteração) em partidas do lançamento caso a data do partida seja menor que a data de conciliação de suas contas contábeis. Acessar [Conciliação](https://tdn.totvs.com/pages/viewpage.action?pageId=686485866) para maiores detalhes sobre Conciliar/Desconciliar, Concluir conciliação, Conta conciliada, Data de conciliação, etc.

Clique no botão **Informação,** localizado na linha de *Status* da tela de visão das partidas do lançamento, para obter informações sobre as teclas de atalho.  
   
**Importante**  
Pode-se ter acesso à tela dos Lançamentos através do menu **Lote Oficial/Lançamentos**, que foi explicado acima, ou então através do menu **Acesso Rápido,** que está disponível a partir da versão 11.81.  
   
O "**Acesso Rápido**" é um recurso que possibilita acessar através de uma pesquisa rápida a partida de um lançamento contábil. Pode-se parametrizar o sistema para que ao indicar os dados para a pesquisa rápida de uma partida, esta já seja apresentada aberta na tela em forma de edição e para que todas as alterações realizadas na partida ou até mesmo inclusões sejam salvas automaticamente no banco de dados. Para obter mais informações sobre esta funcionalidade assim como as parametrizações necessárias clique em [Acesso Rápido](http://tdn.totvs.com/pages/viewpage.action?pageId=51254200).   
   
Alguns aplicativos incluem diretamente no TOTVS Gestão Contábil os lançamentos contábeis provenientes de suas operações e movimentações. Estes lançamentos vêm para os *Lotes* destinados e parametrizados para este fim. Os lançamentos que estiverem em *Lotes* não serão considerados para apuração de resultados, listagem dos relatórios oficiais, entre outros procedimentos. Para considerá-los, deve-se primeiro *Integrá-los* ao Lote Oficial da Contabilidade. Para maiores informações clique em Lotes.  
   
**Incluir lançamento para Centro de Custo Inativo:**  
O parâmetro "Permitir Lançamento com Centro de Custo inativo por módulo " será habilitado somente se o parâmetro "Barrar Lançamento com centro de custo inativo" estiver marcado.

O parâmetro "Permitir Lançamento com Centro de Custo inativo por módulo " habilitará um controle para que o usuário possa selecionar o módulo no qual vai permitir contabilizações com centro de custo inativo.

Se o parâmetro "Barrar Lançamento com centro de custo inativo" estiver marcado, na tela de contabilização (TOTVS Gestão Contábil ou outro módulo) no lookup de centro de custo não será permitido a visualização ou seleção de centro de custo inativo, entretanto, dependendo do parâmetro "Permitir Lançamento com Centro de Custo inativo por módulo" o centro de custo poderá ser visualizado.

Exemplo:

Marcamos o parâmetro "Barrar Lançamento com centro de custo inativo" e o "Permitir Lançamento com Centro de Custo inativo por módulo". Selecionamos o módulo Patrimônio, neste caso se entrar na tela de contabilização do patrimônio vou poder visualizar e selecionar centro de custo inativo.  
   
**Contra partidas:**  
Quando a opção referente a salvar a partida antes de salvar o lançamento contábil existente nas Preferências de Usuário estiver marcada ao incluir um lançamento contábil a regra de inclusão de contrapartida existente no parâmetro "Aplica contra partida automaticamente na inclusão de lançamentos" não será aplicada.  
   
**Data Extemporânea:**

Campo incluído para possibilitar ao usuário corrigir entregas de obrigações acessórias de períodos anteriores. O campo só poderá ser preenchido para lançamentos oriundos do TOTVS Gestão Contábil.

Utilização de WebService/Api

Para utilizar o webservice RMSRestDataServer em requisições REST do tipo **GET** é necessário informar no **Header** da requisição a coligada para que a busca dos dados seja feita. Dessa forma:  
Requisição <http://localhost:8051/RMSRestDataServer/rest/CtbLanData>  
  
Caso não informado, nenhum registro será retornado.

Anexos


* [Diferenças em Laçamentos do Lote](http://tdn.totvs.com/pages/viewpage.action?pageId=423938711)

Processos





Veja também







* [Atualizar valor das multi moedas](https://tdn.totvs.com/x/OHhZIw)
* [API - Lançamento e Partida](https://tdn.totvs.com/pages/viewpage.action?pageId=834806131)
