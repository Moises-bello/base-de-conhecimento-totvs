---
content_hash: 3e455ba206d8a03500034f0ccfdfcfe4c0cb6485682013257441166d0d00eb81
fetched_at: '2026-06-29T00:11:04.166026+00:00'
page_id: '625471476'
product: rm
source: tdn-rm
title: TestePortal Chatbot Carolina | Assistant - Curadoria
type: documentation
url: https://tdn.totvs.com/display/LRM/TestePortal+Chatbot+Carolina+%7C+Assistant+-+Curadoria
version: 1
---

none30px

Olá, por aqui você encontra um conteúdo sobre curadoria de um chatbot, o que é isso, quais as responsabilidades de um curador e como realizar algumas análises para executar a curadoria.

**1.****O QUE É CURADORIA?**

O trabalho de criar um chatbot não termina quando ele é publicado. O chatbot é dinâmico e precisa ser aprimorado constantemente para sua performance atender os clientes de forma eficiente.

Um chatbot depois de “pronto” ele não está “finalizado”. É estranho ler essa frase, mas ele está conversando com humanos todos os dias, entendendo como as pessoas se comunicam e recebendo assuntos do interesse do usuário, é importante ele tratar essas novas linguagens. Neste momento entra a curadoria.

A curadoria de um chatbot vai além de olhar apenas métricas, como usuários online, número de interações e retenção. É necessária a avaliação **qualitativa** para entender como os usuários estão interagindo com a assistente e se as perguntas estão sendo respondidas de forma assertiva.

Ao longo do tempo o chatbot tende a receber mais visitantes por dia, com o aumento do volume de informações coletadas a avaliação qualitativa começa a ter perdas de desempenho, deste modo outras abordagens começam a ser utilizadas, a utilização de amostras e parâmetros estatísticos são bem comuns nesses casos.

## **2.****QUAIS SÃO AS RESPONSABILIDADES DE UM CURADOR?**

As ações do curador refletem diretamente na performance da assistente. Consideramos o principal processo a posteriori lançamento, pois entrega credibilidade para o negócio. Os novos artigos que são criados podem gerar problemas na compreensão da assistente, por esse motivo a curadoria deve ser feita por analistas conhecedores dos produtos e módulos contemplados pela assistente, facilitando o entendimento dos conteúdos (artigos) existentes na base de conhecimento. O curador terá acesso às demandas e problemas mais relevantes para os usuários e poderá propor melhorias para que a assistente atenda de forma assertiva e eficaz os usuários.

Algumas das atividades do curador:

* Analisar as interações dos usuários com a assistente - é possível verificar a linguagem que o usuário utiliza para fazer as perguntas e como podemos ajustar nossas documentações;
* Analisar o texto que são apresentados - É importante que a informação não tenha cortes, e que os links tenham relação com a pergunta do usuário;
* Analisar os artigos que são apresentados - É importante que os artigos estejam nos parâmetros pré-definidos, pois tem impacto direto no resultado mostrado pelo chatbot;
* Identificar nas perguntas mais recorrentes o que a assistente ainda não entendeu - oportunidade para criação de mais conteúdos;
* Analisar se a pergunta que o usuário fez está relacionada com o módulo que ele selecionou - dessa forma conseguimos identificar falhas de busca do usuário e podemos pensar em como orientar e levar o cliente a selecionar o módulo correto;
* Analisar erros cometidos pelo chatbot para possíveis melhorias.

## **3.****COMO UM CURADOR REALIZA TODAS ESSAS ANÁLISES?**

Se a sua solicitação de melhoria for sobre o fluxo de atendimento, humanização, jornada da assistente e layout, não se esqueça de avaliar os itens abaixo, essas informações são importantes e devem ser enviadas no corpo da sua solicitação.

3

15px100%Resposta negativa

A resposta da pesquisa é importante pois temos visibilidade do que foi ou não satisfatório para o usuário. Se não atendeu as expectativas do usuário, temos a certeza que precisamos fazer alguma ação para que em seu próximo retorno ele seja atendido da forma correta.

Existem cenários que o cliente pode negativar uma pesquisa, alguns motivos são:

* Não encontrou a resposta que esperava;
* O conteúdo não foi relevante;
* A resposta foi muito complexa para um chatbot;
* A própria jornada desse usuário não foi agradável.

Por este motivo é tão importante entender a atuação da curadoria.

Quando o usuário responde negativamente uma pesquisa ele pode informar o motivo que está insatisfeito, motivo este que é a base para iniciar uma ação.

Para listas os tickets, deve ser criada a visualização com as seguintes regras:

* Status maior que Em Espera
* Origem ticket oficial é Carol Assistant
* Tags contém ao menos uma dos seguintes csat\_bad
* Tags contém ao menos uma dos seguintes <tag do segmento: assistant\_plataformas, assistant\_supply, assistant\_saude, assistant\_services>
* *É necessário que as tags csat\_bad e segmentos estejam em condições diferentes, para não ser considerada como “OU”.*
* As colunas apresentadas podem ser a critério da informação que cada curador prefere visualizar.

Sem resposta de pesquisa

A resposta da pesquisa é importante pois temos visibilidade do que foi ou não satisfatório para o usuário. Mas quando o usuário não responde a pesquisa, como podemos analisar esse atendimento? Foi satisfatório ou não?

O usuário pode não ter respondido a pesquisa por:

* Não ter correspondido à expectativa;
* Encontrar o que procurava na primeira consulta;
* Dúvida pontual;

É difícil identificar o motivo do não engajamento na pesquisa, mas pode ser analisada a pergunta que foi feita e a resposta que foi apresentada no atendimento.

Para listar os tickets, deve ser criada a visualização com as seguintes regras:

* Status maior que Em Espera
* Origem ticket oficial é Carol Assistant
* Tags não contém nenhuma das seguintes csat\_bad, csat\_good
* Tags contém ao menos uma dos seguintes <tag do segmento: assistant\_plataformas, assistant\_supply, assistant\_saude, assistant\_services>
* *É necessário que as tags “csat\_bad, csat\_good” e “segmentos” estejam em condições diferentes, para não ser considerada como “OU”.*
* As colunas apresentadas podem ser a critério da informação que cada curador prefere visualizar.

Como analisar o atendimento

Quando o atendimento tem uma resposta negativa existe o campo motivo negativado que apoia na análise. Ao abrir o ticket procure pelo campo “Motivo Negativado”, se o campo estiver preenchido será mais fácil de analisar.

No exemplo abaixo temos um atendimento que o usuário respondeu como negativo porque o “Retorno coerente, porém minha dúvida não foi respondida”.

Agora a análise deve ser no corpo do ticket, pois nele contém todas as informações.

1. O usuário pode fazer até 3 perguntas caso a assistente não encontrar uma resposta, todas as perguntas estarão descritas no ticket, se existir mais de uma pergunta, precisa ser analisado o motivo delas não terem sido respondidas;

2. Se a resposta for padrão, será apresentado primeiro um artigo e mais duas sugestões de resposta, se existir;

Análise no artigo

1. No primeiro momento é verificada a seção que está o artigo, para analisar a relação desta seção com o módulo que o usuário selecionou;

2. Deve ser analisado os dois campos que a assistente considera quando pesquisa a base de conhecimento: título e dúvida;

3. Deve ser relacionado com a pergunta do usuário, identificando coerência entre a pergunta do usuário com o que está nesses campos;

4. Outra análise que deve ser realizada é nas tags. Abra o editor deste artigo e verifiquei as tags;

5. Dentro do editor clique em “Configurações do artigo”;

**Dentro da plataforma**

6. Consulte se o artigo que deveria ser exibido na consulta está na plataforma para ser consultado;

7. Clique em Explorer / Protheus Documents.

8. Nessa página são apresentados todos os artigos que são considerados na busca da Carolina;

9. Filtre pelo Módulo e consulte o artigo pelo título ou pelo seu ID.

10. Se ele estiver na plataforma verifique os campos Question, Solution, e labels.

11. Caso não encontre o artigo verifique se está dentro do padrão KCS, caso não esteja é necessário realizar as devidas alterações para que seja apresentado.

Banco de palavras

O banco de palavras é o local para gerenciar abreviações e suas definições. Ele realiza a substituição das palavras dos artigos entregando mais possibilidades de acertos nas consultas.

Localize no Explore, Abbreviations and acronyms;

Pesquise a palavra que deve ser cadastrada para verificar se já existe uma definição, caso já esteja cadastrada com outra definição, pode ser realizado um outro cadastro.

Clique nas reticências / New Record, para um novo cadastro;

Informe a abreviação ou uma palavra que tenha outras definições;

Existe um processo de conhecimento de 1h para que o reconhecimento da palavra.

Sinônimos dos módulos

A consulta do usuário na assistente começa com a informação do módulo, mas como o usuário denomina o módulo, essa é uma pergunta que deve ser prevista pelo curador, e deve ser cadastrada na plataforma para que a assistente consiga entender o usuário.

Clique no Explore / Module Parameters;

Consulte o módulo que deve conter um apelido e clique sobre ele para abrir;

Verifique no campo Module Parameters se já contém o apelido que deve ser cadastrado;

Caso não contenha clique em Edit e adicione a palavra separando por vírgula.

Artigos (edição e criação)

Antes de falar em padronização de artigos é necessário conhecer a estrutura do Guide (Base de conhecimento) onde eles são criados.

A organização do Guide é formada pela Categoria / Seção / Subseção / …

Seguindo esta organização a Categoria é representada pelo macrossegmento, a seção pelo produto e a subseção pelo módulo, é possível adicionar mais uma subseção representada pelo agrupador de rotina, mas não é considerado uma obrigatoriedade.

A necessidade de criar uma separação pelo agrupador de rotina, quando existem muitos artigos dentro de um módulo. Outro ponto importante é entender que não necessariamente vamos ter artigos para todos os módulos, ou para todos agrupadores de rotina, e caso não existam essas seções não precisam ser criadas.

**Como o artigo é reconhecido pela assistente?**

Simples, é necessário que ele esteja no modelo KCS, o padrão adotado pela TOTVS para construção de artigos.

**Como fazer a formatação no modelo KCS?**

1. Um artigo na base de conhecimento deve ser objetivo e escrito em uma linguagem acessível. Ele pode conter soluções para um erro, respostas para dúvidas, e também pode ajudar o usuário seguindo passos para chegar em um resultado;

2. Existem 3 (três) templates que devem ser seguidos, dúvida resposta, duvida passos e ocorrência. Veja cada um dos templates <clicando aqui>;

3. As imagens devem ser adicionadas pela inclusão de imagens na edição do artigo e não copiadas e coladas;

4. Os vídeos devem ser adicionados pela inclusão de vídeos na edição do artigo e não colados diretamente no artigo.

5%
#title-text {
display: none !important;
}
]]>
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 5px;
padding-right: 5px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.expand-control-text {
color: #000000;
font-size: 15px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #16c4d6;
}
a:not(.aui-button,.aui-dialog2-header-close) {
color: #5c4397;
}
.aui-label {
background-color: #bae5ea;
font-size: 15px;
}
.wiki-content img.confluence-embedded-image, .wiki-content img.editor-inline-macro, .wiki-content table.wysiwyg-macro {
cursor: pointer;
}
]]>
