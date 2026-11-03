---
content_hash: 24af727d00a7aaa157b95c8d724f2e80c1947aa363851d25dd2d92e5a8087750
fetched_at: '2026-06-29T00:10:44.688530+00:00'
page_id: '553337440'
product: rm
source: tdn-rm
title: Rascunhos04. Processo Desenvolvimento Ágil | Teste Integrado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337440
version: 1
---

5%90%

No Teste Integrado os itens desenvolvidos são testados em grupo para garantir o seu funcionamento. Tem como propósito verificar os requisitos funcionais, de desempenho e de confiabilidade, podendo detectar defeitos entre os componentes do sistema.

* **Planejamento:**o planejamento dos testes é realizado em conjunto com o Planejamento de Entregas, e por meio do detalhamento dos itens na atividade de **[Refinamento](http://tdn.totvs.com/pages/viewpage.action?pageId=274849740)**. Neste momento, o *Dev Team* juntamente com o *Product Owner* fazem o entendimento e detalhamento dos itens, além de definir os Critérios de Aceite, que servem como guia para o desenvolvimento e validação pelo usuário final.

* **Execução:**o Teste Integrado pode ser executado **manualmente ou de forma automatizada** por um integrante do *Dev Team* que possua conhecimento para executar esta atividade. Deve ser gerada a evidência contendo os itens mínimos: **ambiente utilizado, sequência dos testes realizados e resultados obtidos**. 
  + Caso o teste integrado já tenha sido efetuado ou seja executado posteriormente, é imprescindível que a **rastreabilidade** seja realizada dentro das issues no Jira com as devidas justificativas do porquê o teste não foi realizado na atividade em andamento.
  + Para as rotinas que serão automatizadas, é necessário criar ou manutenir os *scripts* de testes. A execução do *script* pode ocorrer dentro desta etapa ou do teste sistêmico (conforme necessidade). A evidência do teste ficará registrada na ferramenta padrão de cada segmento.

    [**Instrução de Trabalho - Dicas Relacionadas a Testes**](http://tdn.totvs.com/pages/viewpage.action?pageId=461920518)

* **Defeito:** Caso sejam identificados erros no desenvolvimento, deve ser criado um Defeito para registro e correção. As entregas poderão ser finalizadas somente após a correção de todos os defeitos identificados e/ou replanejamento dos mesmos para o *Product Backlog*.  
  [**Instrução de Trabalho - Como Criar Defeitos a partir da Tarefa Pai, do Kanoah ou Defeito Associado?**](http://tdn.totvs.com/pages/viewpage.action?pageId=461920572)
* Instruções específicas para Desenvolvimento Mobile: **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**

#FF8000#FFF8DCsolid

**SEGREGAÇÃO DE FUNÇÃO:**

Deve ser respeitada a regra de segregação de função entre as atividades de **Codificação** e **Teste Integrado**, ou seja, o integrante do *Dev Team* que executar a atividade de Codificação não poderá executar a atividade de Teste Integrado. Não se aplica a regra de segregação de função entre as atividades de Teste de Unidade e Teste Integrado.

0solid

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

27px

## 

560px

**ENTRADA(S):**

* Plano de Entregas
* Detalhamentos dos itens de *backlog*
* Subtarefas
* Impedimentos
* Defeitos
* Ambiente de teste disponível
* Fonte alterado e testado
* Dicionário de Dados / Telas criadas / atualizados e traduzidos
* Evidência(s) do Teste de Unidade
* **[Instrução de Trabalho - Dicas Relacionadas a Testes](http://tdn.totvs.com/pages/viewpage.action?pageId=461920518)**
* **[Instrução de Trabalho - Como Criar Defeitos a partir da Tarefa Pai, do Kanoah ou Defeito Associado?](http://tdn.totvs.com/pages/viewpage.action?pageId=461920572)**
* **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**
27px220px

**ENVOLVIDO(S):**

* ***[Dev Team](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
23px250px

**SAÍDA(S):**

* Evidência(s) do Teste Integrado
* Evidência(s) da Correção do Defeito (quando necessário)
* *Task Board*atualizado
* Indicadores Operacionais atualizados

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
