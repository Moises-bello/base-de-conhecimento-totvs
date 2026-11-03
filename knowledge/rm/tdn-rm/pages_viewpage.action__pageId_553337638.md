---
content_hash: fd8cc27f536475887e79fb1601c6913f90af79a6ed6c99762dd51f7678c5eca3
fetched_at: '2026-06-29T00:10:44.754124+00:00'
page_id: '553337638'
product: rm
source: tdn-rm
title: Rascunhos04. Processo Desenvolvimento Ágil | Teste Sistêmico (Reescrita)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337638
version: 1
---

5%90%

### **Objetivo**

O objetivo deste documento é esclarecer o processo de Teste Sistêmico na TOTVS.

### **O que é o Teste Sistêmico?**

O Teste Sistêmico é um período que antecede sempre a liberação de uma nova *Release* dos produtos da TOTVS e visa garantir a qualidade dos desenvolvimentos e manutenções implementadas nesta nova *Release*, ou seja, incrementos e alterações no produto desde a última liberação da *Release* anterior.

### **Escopo**

Pode ser realizado o [**Refinamento**](http://tdn.totvs.com/pages/viewpage.action?pageId=274849740) no início da atividade de Teste Sistêmico para detalhar o escopo do Teste. A duração do Teste Sistêmico segue o cronograma do Calendário Geral TOTVS conforme necessidade de cada Linha de Produto. Os GCADs de cada linha são os responsáveis por manter este Calendário atualizado.

**Teste Sistêmico**

Se desejável, pode ser utilizado a *issuetype* de Teste Sistêmico para planejamento dentro do Planejamento de Entrega.

**Manutenção**

Atualmente as *issues* de Manutenção são registradas para correção e/ou manutenção em *Releases* vigentes já liberadas ao mercado ou então em *Releases* futuras quando possuem alteração em Dicionário de Dados.

Correções em *Releases* vigentes e disponíveis no mercado, não necessitam passar pelo processo de Teste Sistêmico, pois são aplicadas diretamente nas *Releases* vigentes em mercado, desde que válidas conforme política de ciclo de vida.

Caso surjam manutenções críticas, ou que sejam avaliadas como prioritárias, o *Product Owner* pode planejar para serem corrigidos neste período. Neste caso, elas devem ser ajustadas dentro da *Release* que está em sistêmico. A data de corte é o final do sistêmico, desde que as manutenções sejam devidamente testadas.

### Execução

O Teste Sistêmico pode ser executado **manualmente**, de forma **automatizada** ou **misto** (quando o membro do *Dev Team* faz uma mescla, olha o cód. fonte + execução da rotina automática).

Recomendamos a utilização do *Plugin Test Management (Kanoah)* para criação de Casos de Testes e Ciclo de Testes para registro dos testes executados durante o Teste Sistêmico.

**Evidência dos Testes para execução Manual**

Deve ser gerada a evidência dos testes realizados contendo os itens mínimos: **ambiente utilizado, sequência dos testes realizados e resultados obtidos**.

**[Instrução de Trabalho - Dicas Relacionadas a Teste Sistêmico](http://tdn.totvs.com/pages/viewpage.action?pageId=463799824)**

**Evidência dos Testes para execução automática**

Os times que executam os testes de forma automatizada, a evidência pode estar registrada dentro da ferramenta de automação, desde que garanta a histórico e os itens mínimos acima mencionados.

**[Instrução de Trabalho - Como Criar Defeitos a partir da Tarefa Pai, do Kanoah ou Defeito Associado?](http://tdn.totvs.com/pages/viewpage.action?pageId=461920572)**

### Considerações para o processo de Teste Sistêmico

O processo de teste sistêmico deve contemplar dentro do último Planejamento de Entregas, que antecede o lançamento de uma nova versão/*Release*. Este Plano de Entregas pode conter demais itens que não sejam de teste.

Por motivos de classificação em indicadores, o ideal é que seja utilizada uma *issuetype* específica para as demandas de teste sistêmico.

O time de Engenharia local, que pode ser o time de GCAD da linha, realiza uma comunicação para as *Squads* sobre a realização dos testes sistêmicos daquele período. Se desejável, pode ser realizado um *Kick Off* para alinhamento das expectativas e abrangência bem como sobre o monitoramento do teste sistêmico.

**Congelamento de entrada de demandas**

O período de teste sistêmico deve aplicar uma data de corte para a entrada de novas demandas para a próxima *Release* para garantir a qualidade do produto que será liberado.

Para a **Linha Protheus**, não há congelamento de RPO, pois os *commites* são realizados na *branch* única, desta forma, utilizam o ambiente D-1.

### FAQ

**Existe um tipo de *issue* (*Issuetype*) específica para atividades de Teste Sistêmico?**

Sim. A *issuetype* “Teste Sistêmico” serve para que sejam registradas demandas específicas para as atividades durante o período de teste sistêmico.

Isto não proíbe a utilização de diferentes *issuetypes* já conhecidas para seus devidos fins, ou seja, manutenções, defeitos e legislações que serão desenvolvidos neste mesmo período, também poderão ser incluídos no mesmo Plano de Entregas do período de teste sistêmico.

* Instruções específicas para Desenvolvimento Mobile: **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**

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
* Evidência(s) do Teste Integrado
* Evidência(s) da Correção do Defeito (quando necessário)
* Documento Técnico elaborado e traduzido
* Documento de Referência elaborado e traduzido (quando necessário)
* *How To*elaborado e traduzido (opcional)
* Repasse realizado
* Plano de Teste de Performance
* **[Instrução de Trabalho - Dicas Relacionadas a Teste Sistêmico](http://tdn.totvs.com/pages/viewpage.action?pageId=463799824)**
* **[Instrução de Trabalho - Como Criar Defeitos a partir da Tarefa Pai, do Kanoah ou Defeito Associado?](http://tdn.totvs.com/pages/viewpage.action?pageId=461920572)**
* **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**
27px220px

**ENVOLVIDO(S):**

* ***[Dev Team](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
23px250px

**SAÍDA(S):**

* Evidência(s) de Teste Sistêmico
* Relatório de análise (evidência de execução dos testes)
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
