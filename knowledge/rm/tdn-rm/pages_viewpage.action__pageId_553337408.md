---
content_hash: b05a5bd85fbebda8ef4f8022aac1f2f1ec78a5c267f7dc5eff62116e45c9f759
fetched_at: '2026-06-29T00:10:44.680686+00:00'
page_id: '553337408'
product: rm
source: tdn-rm
title: Rascunhos04. Processo Desenvolvimento Ágil | Desenvolvimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337408
version: 1
---

5%90%

Na etapa de Desenvolvimento podem ser executadas as atividades de Codificação, Modelagem de Dicionário de Dados, Documentação do Produto e Teste de Unidade.

* **Codificação:** o Desenvolvedor inicia a codificação do fonte a partir do momento em que os itens estão detalhados no Plano de Entregas e forem definidas a forma de execução de trabalho da equipe. Em manutenções do produto deve ser avaliada a necessidade de repetir a correção em uma versão superior ou inferior à que está planejada.

[**Instrução de Trabalho - Como Realizar Check-in no TFS?**](https://tdn.totvs.com/x/ElaIGw)

[**Instrução de Trabalho - Como Realizar Check-in n****o Azure DevOps?**](http://tdn.totvs.com/pages/viewpage.action?pageId=506389377)

[**Instrução de Trabalho - Como Criar Issues de Réplica (Issues de Manutenção)?**](http://tdn.totvs.com/x/WlaIGw)

[**Instrução de Trabalho - Como Acompanhar Retorno do Cliente na Liberação Emergencial?**](http://tdn.totvs.com/x/A1eIGw)

[**Instrução de Trabalho - Quando Usar a Issuetype Apoio - Cliente (Issues sem Commit de Fonte)?**](http://tdn.totvs.com/x/KleIGw)

[**Instrução de Trabalho - Como Tratar Demandas de Ajuste na Base do Cliente?**](http://tdn.totvs.com/x/wFiIGw)

**[Instrução de Trabalho - Como Realizar Integração de produtos parceiros?](https://tdn.totvs.com/x/AMSAHQ)**

#FF8000#FFF8DCsolid

**IMPORTANTE:**

**PROCEDIMENTO PARA CLIENTES PRIME**

* Para os Clientes Prime deverá **SEMPRE** ser realizada a liberação de correção ou contorno através da **Liberação Emergencial**, pois isso é importante para:
  + Que essa informação seja enviada ao Zendesk, e seja registrada essa data para avaliar se houve o cumprimento da Faixa 3, e;
  + Agilizar a solução ao Cliente.

[**Instrução de Trabalho - Como Realizar Liberação Emergencial?**](http://tdn.totvs.com/x/mVaIGw)

#FF8C00#FAFAD2dashed55px100%

As atividades realizadas na etapa de desenvolvimento devem considerar os critérios estabelecidos conforme *DoR (Definition of Ready)* e *DoD (Definition of Done)* alinhados a **LGPD** *(Lei Geral de Proteção de Dados)* e ao ***Privacy By Design***.

**[Instrução de Trabalho - Privacy by Design e Privacy by Default](https://tdn.totvs.com/x/A6eVI)**

* **Modelagem de Dicionário de Dados:** quando necessário, deve realizar a modelagem de dicionário de dados ou solicitar para a equipe responsável. Durante ou após o desenvolvimento, também pode enviar para tradução sistêmica o dicionário de dados, as telas e o help dos campos.  
  [**Instrução de Trabalho - Como Solicitar Alteração no Modelo de Dados?**](http://tdn.totvs.com/x/rQelGw)

* **Documentação do Produto:** a Documentação do Produto pode ser elaborada durante o desenvolvimento por qualquer integrante do *Dev Team* que possua conhecimento do que está sendo liberado (inovações ou manutenções do produto). *Vide as documentações obrigatórias e opcionais em **[Processo de Desenvolvimento Ágil | Documentação](http://tdn.totvs.com/pages/viewpage.action?pageId=458764731)***

* **Teste de Unidade:** o teste de unidade deve ser executado por um recurso do *Dev Team* que realizou a Codificação e também pode ser validado por um par. O teste de unidade é composto pelo teste unitário de fontes e compilações e podem ser executados nos seguintes formatos:
  + **Teste Manual:** o teste manual é executado nesta fase com base no que foi desenvolvido para este item. Sua evidência é registrada de forma breve, informando os testes realizados (pode ser utilizado o campo comentário da tarefa ou ser incluído um anexo - template Word, contendo print screen de telas e logs).
  + **Teste Automatizado**: para as rotinas que serão automatizadas é necessário criar ou manutenir os scripts de testes. A execução do script pode ocorrer dentro desta etapa ou do teste sistêmico (conforme necessidade). A evidência do teste ficará registrada na ferramenta padrão de cada segmento.
  + Caso ocorra a **validação do Teste de Unidade** por um par, novos testes podem ser realizados para complementar os que já foram executados, sendo necessário anexar uma nova evidência.  
    [**Instrução de Trabalho - Dicas Relacionadas a Testes**](http://tdn.totvs.com/x/BlmIGw)

* Instruções específicas para Desenvolvimento Mobile: **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**

#FF8000#FFF8DCsolid

**SEGREGAÇÃO DE FUNÇÃO:**

Deve ser respeitada a regra de segregação de função entre as atividades de **Codificação** e **Teste de Unidade,**quando houvera validação do teste por um par. O recurso que executar a atividade de Codificação não poderá executar a atividade de Teste de Unidade.

* Quando a atividade de Teste de Unidade for realizada somente pelo Desenvolvedor, recomenda-se que a evidência de teste seja incluída na subtarefa de Codificação, não precisando criar uma nova subtarefa para execução do Teste de Unidade.
* Quando a validação do Teste de Unidade for realizada por um par, neste caso deve ser criada uma nova subtarefa e respeitada a regra de segregação de funções entre as subtarefas de Codificação e Teste de unidade.
* Esta validação não é obrigatória no Processo de Desenvolvimento Ágil.

Não se aplica a regra de segregação de função entre as atividades de **Teste de Unidade** e **Teste Integrado**.

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
* **[Instrução de Trabalho - Como Realizar Check-in no TFS?](http://tdn.totvs.com/x/ElaIGw)**
* **[Instrução de Trabalho - Como Criar Issues de Réplica (Issues de Manutenção)?](http://tdn.totvs.com/x/WlaIGw)**
* **[Instrução de Trabalho - Como Realizar Liberação Emergencial?](http://tdn.totvs.com/x/mVaIGw)**
* **[Instrução de Trabalho - Como Acompanhar Retorno do Cliente na Liberação Emergencial?](http://tdn.totvs.com/x/A1eIGw)**
* **[Instrução de Trabalho - Quando Usar a Issuetype Apoio - Cliente (Issues sem Commit de Fonte)?](http://tdn.totvs.com/x/KleIGw)**
* **[Instrução de Trabalho - Como Tratar Demandas de Ajuste na Base do Cliente?](http://tdn.totvs.com/x/wFiIGw)**
* **[Instrução de Trabalho - Como Solicitar Alteração no Modelo de Dados?](http://tdn.totvs.com/x/rQelGw)**
* **[Instrução de Trabalho - Dicas Relacionadas a Testes](http://tdn.totvs.com/x/BlmIGw)**
* **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**
27px270px

**ENVOLVIDO(S):**

* ***[Dev Team](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
23px200px

**SAÍDA(S):**

* Fonte alterado e testado
* Dicionário de Dados / Telas criadas / atualizados e traduzidos
* Evidência(s) do Teste de Unidade
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
