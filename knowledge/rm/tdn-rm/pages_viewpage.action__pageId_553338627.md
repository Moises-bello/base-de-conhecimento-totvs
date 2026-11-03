---
content_hash: 58572013c605d79c50db9e9b71f2f1a6838d0bd482c684fedce4703a6ba4c428
fetched_at: '2026-06-29T00:10:45.483678+00:00'
page_id: '553338627'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho |  Mobile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338627
version: 1
---

90%10%100%TESTES

Nesta página estão descritas as particularidades da atividade de Testes para o processo Mobile.

**No processo Mobile são executadas as seguintes etapas de testes:**

* Teste de Unidade: esta etapa é obrigatória e sugere-se que seja executado de forma automatizada;
* Teste Integrado: esta etapa é obrigatória e sugere-se que seja executado de forma automatizada;
* Teste Sistêmico: esta etapa é opcional, fica a critério de cada equipe avaliar a necessidade de execução.

**Sugere-se que além dos tipos de testes executados, sejam avaliados e executados os itens de verificação:**

* Compatibilidade: verifica a interação e a comunicação com o Sistema operacional;
* Mobilidade: verifica a capacidade de comunicação com outros aplicativos;
* Instalação: testar se a instalação da aplicação foi OK;
* Desempenho: verifica se o aplicativo demonstra lentidão;
* Funcionalidade: verifica se o aplicativo executa as tarefas que devem ser executadas.

No desenvolvimento Mobile, os testes são executados em dispositivos móveis ou emuladores e podem ocorrer de forma manual ou automatizada.

**Regras para Automação dos Testes (conforme processo padrão):**

* **[Planning](http://tdn.totvs.com/pages/viewpage.action?pageId=274850066)[:](http://tdn.totvs.com/pages/viewpage.action?pageId=274850066)** a equipe deve lembrar de reservar pontos dentro do Plano de Entregas para automatizar as rotinas de testes necessárias;

* **[Teste de Unidade / Teste Integrado](http://tdn.totvs.com/pages/viewpage.action?pageId=275304986)[:](http://tdn.totvs.com/pages/viewpage.action?pageId=275304986)** para as rotinas que serão automatizadas é necessário criar ou manter os *scripts* de testes. A execução do *script* pode ocorrer dentro destas etapas ou   
  da etapa de teste sistêmico (conforme necessidade). A evidência do teste ficará registrada na ferramenta padrão de cada segmento;

* **[Teste Sistêmico](http://tdn.totvs.com/pages/viewpage.action?pageId=275304986)[:](http://tdn.totvs.com/pages/viewpage.action?pageId=275304986)** os scripts que foram criados / executados durante as etapas de Teste de Unidade e Teste Integrado podem ser executados novamente, para garantir que os resultados dos testes sejam os mesmos. A evidência do teste automatizado ficará registrada na ferramenta padrão de cada segmento.

Ferramentas para testes

Na atividade de Testes - Mobile, as equipes podem utilizar as ferramentas que melhor lhes atendam a necessidade tecnológica (escopo do produto e teste que será executado) de cada segmento/área. 

Para Mobile, poderá ser utilizado o pacote ferramental que melhor atender a necessidade, e é importante avaliar:

* A plataforma que será utilizada: Android ou IOS.
* A linguagem de desenvolvimento: Nativa ou Híbrida.

**Exemplos de Ferramentas**

Sugere-se algumas ferramentas de mercado que são utilizadas por algumas equipes na TOTVS:

* Linguagem híbrida: Appium, Jasmine, Angular, Karma, Protractor, TestFlow, Ionic, Xamarin.
* Linguagem nativa: Expresso (Android) e XCTest (IOS).

Alguns segmentos apresentaram as ferramentas que utilizam, para conferir as gravações, acesse: **[Mobile - Testes (Ferramentas)](http://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6066430)**.

Boas práticas

***(Test Driven Development)*** baseia-se em três passos, vermelho-verde-refatora. O vermelho é a escrita do primeiro teste antes mesmo da lógica existir. O verde é o ponto em que a lógica para que o teste previamente criado, passe. Esta lógica deve ser desenvolvida da forma mais simples possível, eliminando complexidades desnecessárias e fazendo com que a evolução do código ocorra de forma segura. O refatora é a melhoria do código e neste ponto são removidas duplicações, múltiplas responsabilidades e o código fica cada vez mais próximo de sua versão final.

Na técnica de desenvolvimento TDD os testes são escritos antes da implementação do sistema, sendo o ciclo de desenvolvimento da seguinte forma: escrever um teste unitário que falhe antes de escrever qualquer código funcional (Red); escrever o código funcional até que o teste unitário passe (*Green*); no final, caso seja necessário, efetua uma reestruturação do código, remover as redundâncias e melhora a própria estrutura, assegurando que os testes unitários continuam todos a ter sucesso (*Refactor*).

É recomendado que os testes sejam automatizados, de forma que o seu código seja sempre compilado e executado como parte integrante do processo normal. Desta forma que a adição de uma nova funcionalidade ou a reestruturação do código não quebrem as funcionalidades já implementadas.

**Vantagens**

* Diminui o número de bugs (se algo não é possível de ser testado é que pode ter sido desenvolvido de forma errada);
* Permite que aplicação final seja mais robusta;
* Gasta menos tempo na manutenção da aplicação;
* Na implementação de códigos modular e flexível incentiva a programação por camadas;
* Sugeri a criação de códigos que possam ser testados de forma isolada e independente;

**Dificuldades/ Obstáculos**

* No início o programador irá gastar mais tempo para escrever códigos;
* Em linguagens de programação que não exista um framework de testes unitários o processo pode se tornar engessado e difícil;
* Pode ter dificuldades com o software que foi desenvolvido em linguagens de programação legadas.

***As três leis do TDD***

1.Você não pode escrever código de produto que não seja fruto de fazer passar um teste de unidade que falha.

2.Você não pode escrever num teste além do mínimo necessário para o teste falhar, e erros de compilação são falhas.

3.Você não pode escrever códigos de produção que seja além do necessário para fazer o teste passar.

***(Quadrante do Teste Ágil)***Também como boa prática, algumas equipes utilizam o quadrante de teste ágil, que foi criado por Brian Marick. No quadrante temos técnicas de testes para cada categoria, objetivando alcançar diferentes propósitos.

A realização de teste ágil não é feita apenas na etapa final, como ocorre na execução de teste tradicional, o time de desenvolvimento antecipa essa atividade, através de práticas de integração conjunta, desenvolvimento em pares, TDD (Test Driven Development) e automatização. Para conhecer o detalhamento do quadrante, consulte a publicação do **[News do Ágil.](http://tdn.totvs.com/pages/releaseview.action?pageId=331853085.)**

DESIGN

O Design do Aplicativo facilita a interação entre o usuário e o aparelho, a User Interface usa diversos elementos para isso, tais como: cores, textos e botões.

UX – User Experience, é a disciplina responsável por projetar percepções e experiências de uso, que sejam encantadoras para fidelizar e conquistar clientes. Para criação de um aplicativo é indispensável que este conceito seja validado. Esta atividade pode ser realizada pelo Design da equipe ou do UX LAB da TOTVS, que com base nos conhecimentos de Design Tkinking levanta as necessidades do produto.

Conheça o caminho para solicitar um projeto com a equipe de [**UX LAB TOVS.**](https://fluig.totvs.com:443/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6538948)

Para mantermos a padronização visual dos produtos da TOTVS, abaixo contém orientações que foram disponibilizados por determinadas áreas, com objetivo de orientar as equipes no desenvolvimento e publicação do seu aplicativo. para responder as reviews dos usuários nas lojas.

* **Ícones:**  A equipe de Marketing disponibilizou um *guideline*para o desenvolvimento de App - [**Ícones para aplicativos**.](https://fluig.totvs.com:443/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6538642)

* **Reviews**: O Marketing também elaborou um [**Guia de Boas Práticas**,](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6538993) para responder as reviews dos usuários nas lojas.

Para ter acesso aos materiais e demais assuntos do desenvolvimento Mobile, acompanhe o Fórum MOBILE no **[Ryver](https://totvs.ryver.com/)**.

EXPEDIÇÃO

Para publicação do aplicativo em uma das store (Apple/Google) é necessário solicitar a criação do aplicativo na conta corporativa da TOTVS. A solicitação deve ser enviada para **[suporte.mobile@totvs.com.br](mailto:suporte.mobile@totvs.com.br)** com os nomes dos colaboradores que deverão ter acesso.

#FF8000#FFF8DCsolid

**AVISO:**

Antes de disponibilizar o aplicativo, certifique-se de que os padrões de identidade visual, estabelecidos pelo Marketing foram atendidos. Com isso, mantemos uma padronização visual dos produtos TOTVS.

Documentação

**Politica de privacidade**

A Política de Privacidade é um registro eletrônico, onde o usuário é informado que os seus dados serão coletados e utilizados, assim que o usuário fizer o registro no aplicativo. Por isso é de extrema importância que a versão publicada tenha sida valida pela área Jurídica da TOTVS.

O conteúdo não pode ser alterado, caso tenha alguma dúvida ou particularidade do App, abra um ticket para: **[eng.corp.desenv@totvs.com.br](mailto:eng.corp.desenv@totvs.com.br).**

Ferramental (JIRA)

**Release Mobile**

Foi disponibilizada para as equipes de Desenvolvimento Mobile, uma nova issue type, que irá facilitar as atividades de expedição de um aplicativo, para que a squad não deixe de executar nenhuma atividade que seja essencial para a expedição de uma nova versão do aplicativo. O uso desta **issue type é opcional** ficando a critério da squad criar uma Story ou Release Mobile para a expedição do aplicativo.

O objetivo desta issue type é facilitar, pois ao iniciar a issue do tipo **Release Mobile**, serão criadas automaticamente subtarefas com as seguintes descrições:

* Geração do pacote Android
* Geração do pacote iOS
* Publicação Beta Android
* Publicação Beta iOS
* Testes Android
* Testes iOS
* Atualização Guia de Uso
* Atualização Release Notes
* Atualização Vitrine
* Merge
* Publicação Produção Android
* Publicação Produção iOS

para acessar as instruções na utilização das issue types.

5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
