---
content_hash: a4173b9e2298495b5a9750181a23f5d59e9e90fd3dc4047721007c7a2c693f63
fetched_at: '2026-06-29T00:10:44.653299+00:00'
page_id: '553337327'
product: rm
source: tdn-rm
title: Rascunhos03. Processo Desenvolvimento Ágil | Planning
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337327
version: 1
---

5%90%

A etapa de ***Planning*** contempla:

* O **[Refinamento](http://tdn.totvs.com/pages/viewpage.action?pageId=274849740)** dos itens de *backlog;*
* O evento de *Planning, que* é realizado em duas etapas.  
  + Na primeira, o *Product Owner* apresenta a visão de negócio e os itens do *Product Backlog* priorizados;
  + Na segunda etapa, o *Dev Team* define a melhor forma de construção dos itens, considerando a priorização do *Product Owner* e realizando a quebra dos itens em tarefas.

A importância do Refinamento:

* Garante a provisão contínua de itens adequadamente detalhados;
* Meta do Plano de Entregas *(A meta é um objetivo de negócios a ser alcançado por meio da entrega. Recomenda-se que os itens planejados sejam desenvolvidos respeitando a sua prioridade)*;
* Seleção de itens que irão compor o *Backlog* do Plano de Entregas *(Os itens de maior prioridade devem estar adequadamente compreendidos e detalhados para que o Dev Team concentre seus esforços exclusivamente nas atividades de desenvolvimento).*

O *Dev Team* deve lembrar de reservar pontos dentro do Planopara automatizar as rotinas de testes necessárias, avaliando a melhor estratégia de acordo com os métodos e critérios definidos para apoiá-los (para mais detalhes, consulte abaixo a atividade de Seleção de Itens e Planejamento da Construção).

[**Instrução de Trabalho - Evento - Planning**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771014)

Para equipes que utilizam *Sprints* para o planejamento de entregas:

* O evento deve ser realizado no primeiro dia do *Sprint;*
* *Timebox* do Evento: 2 a 8 horas *(2 horas por semana, lembrando que 1 Sprint não deve ter mais que 4 semanas)*;
* Avaliação da necessidade do uso de Classe de Serviço;
* Ao finalizar o evento teremos dois artefatos prontos: Meta do *Sprint* e o *Sprint Backlog.*

Para equipes que utilizam Fluxo Puxado para o planejamento de entregas, recomenda-se:

* O evento seja realizado a cada 2 semanas;
* O *Timebox* é de acordo com a definição da equipe;
* Definição/Manutenção das Classes de Serviço que serão utilizadas;  
  + [**Instrução de Trabalho - Classes de Serviço e Como Utilizar nas Issues**](http://tdn.totvs.com/pages/viewpage.action?pageId=463827913)
* Ao finalizar o evento teremos dois artefatos prontos: Meta do Plano e Plano de Entregas.

[**Instrução de Trabalho - Procedimentos Antes de Rejeitar ou Não Rejeitar uma Issue**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771487)

**Participantes:** *Dev Team*, *Product Owner*, *Agile Master* e convidados que possuem dependência com a entrega.

### Seleção de Itens e Planejamento da Construção

No caso de novos projetos ou participantes na equipe, o *Agile Master* apoia como facilitador, demonstrando as opções de processos, ferramentas e conceitos ágeis, tais como:

* **[Processo de Desenvolvimento Ágil TOTVS](http://tdn.totvs.com/pages/viewpage.action?pageId=274853261)**;
* JIRA;
* *Planning Poker, Task Board, Spike*, Gráfico *Burndown*.

**Automação: Critérios**

Métodos e critérios que podem ser utilizados para priorizar os itens que serão automatizados, visando a qualidade do produto final.

**Métodos**

* + - Automatizar rotinas novas;
    - Rotinas / funcionalidades críticas;
    - Rotinas / funcionalidades com maior índice de defeitos abertos na versão anterior;
    - Rotinas / funcionalidades repetitivas (Ex.: Cadastro, Login, Consulta).

**Boas práticas**

* + - Automatizar somente rotinas com resultado esperado conhecido.

#FF8C00#FAFAD2dashed55px100%

Ao planejar a Entrega, deverá ser reforçada a necessidade de desenvolvimento de produto com atenção a privacidade e a segurança de dados pessoais. As *issues* selecionadas precisarão refletir os critérios de *DoR (Definition of Ready)* e *DoD (Definition of Done)* em aderência a **LGPD** *(Lei Geral de Proteção de Dados)* e ao ***Privacy By Design***.

**[Instrução de Trabalho - Privacy by Design e Privacy by Default](https://tdn.totvs.com/x/A6eVI)**

[**Instrução de Trabalho - Como Criar e Iniciar um Sprint no JIRA?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771084)

[**Instrução de Trabalho - Como Criar Subtarefa no JIRA?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771126)

[**Instrução de Trabalho - Como Alterar o Tipo de Tarefa / Issutype?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771170)

[**Instrução de Trabalho - Como Fazer Alterações em Bloco no JIRA?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771218)

[**Instrução de Trabalho - Como Clonar Tarefas / Subtarefas?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771276)

[**Instrução de Trabalho - Como Realizar Links entre Issues no JIRA (Depende de, Relates to)?**](http://tdn.totvs.com/pages/viewpage.action?pageId=458771354)

[**Instrução de Trabalho - Como Criar Issues Associadas ou Realizar Associação de Issues?**](http://tdn.totvs.com/x/WnrvH)

[**Instrução de Trabalho - Como Utilizar o Business Value?**](https://tdn.totvs.com/x/MY3EHg)

0solid

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

27px

## 

560px

**ENTRADA(S):**

* *Release Backlog*
* Velocidade Estimada
* Retornos do Desenvolvimentos anteriores
* Ações do *Retrospective*
* Ações do *Review*
* **[Conceito de Preparado e Pronto (DoR e DoD)](http://tdn.totvs.com/pages/viewpage.action?pageId=275474864)**
* Questões Técnicas
* Dependências
* Disponibilidade de Recursos
* Capacidade Produtiva
* **[Instrução de Trabalho - Evento - Planning](http://tdn.totvs.com/pages/viewpage.action?pageId=458771014)**
* **[Instrução de Trabalho - Classes de Serviço e Como Utilizar nas Issues](http://tdn.totvs.com/pages/viewpage.action?pageId=463827913)**
* **[Instrução de Trabalho - Procedimentos Antes de Rejeitar ou Não Rejeitar uma Issue](http://tdn.totvs.com/pages/viewpage.action?pageId=458771487)**
* **[Instrução de Trabalho - Como Criar e Iniciar um Sprint no JIRA?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771084)**
* **[Instrução de Trabalho - Como Criar Subtarefa no JIRA?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771126)**
* **[Instrução de Trabalho - Como Alterar o Tipo de Tarefa / Issutype?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771170)**
* **[Instrução de Trabalho - Como Fazer Alterações em Bloco no JIRA?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771218)**
* **[Instrução de Trabalho - Como Clonar Tarefas / Subtarefas?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771276)**
* **[Instrução de Trabalho - Como Realizar Links entre Issues no JIRA (Depende de, Relates to)?](http://tdn.totvs.com/pages/viewpage.action?pageId=458771354)**
* **[Instrução de Trabalho - Como Criar Issues Associadas ou Realizar Associação de Issues?](http://tdn.totvs.com/x/WnrvH)**
* **[Instrução de Trabalho - Como Utilizar o Business Value?](https://tdn.totvs.com/x/MY3EHg)**
27px270px

**ENVOLVIDO(S):**

* ***[Product Owner](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
* ***[Dev Team](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
* ***[Agile Master](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451)***
* Convidados
23px200px

**SAÍDA(S):**

* Plano de Entregas

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

***\* Obrigatório***

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
font-size: 15px !important;
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
hr {
border-bottom: 1px solid #FF8000;
}
]]>
