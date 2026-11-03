---
content_hash: 64365c88490c9602380b897c81257805f4d6922c3d2ae09a61fc69f7b09228fa
fetched_at: '2026-06-29T00:10:45.816701+00:00'
page_id: '553339291'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339291
version: 1
---

5%90%ATENDIMENTO LINHA DE PRODUTO10%90%

**As demandas do produto TSS são avaliadas inicialmente pela área de Atendimento da Linha de Produto.**

1. **Suporte no ERP da linha de produto,** a área de Atendimento deve atender a demanda do Cliente seguindo o **[Processo de Atendimento](http://tdn.totvs.com/display/NPROC/Home+Processo+Atendimento+-+Segmentos).**
2. **Nos casos em que a demanda for somente do produto TSS**, a área de Atendimento deve transferir o *ticket* para a área de Atendimento do TSS.
3. **Nos casos em que a demanda depender de Desenvolvimento**, a área de Atendimento deve criar uma *Issue* para o Projeto da SQUAD da Linha de Produto.
ATENDIMENTO TSS10%90%

**A área de Atendimento do TSS deve avaliar a demanda recebida da Linha de Produto.**

1. **Suporte no TSS**, a área de Atendimento deve atender a demanda do Cliente seguindo o **[Processo de Atendimento](http://tdn.totvs.com/display/NPROC/Home+Processo+Atendimento+-+Segmentos).**
2. **Nos casos em que a demanda depender de Desenvolvimento**, a área de Atendimento deve criar uma *Issue* para o Projeto da SQUAD do TSS.
   1. Projetos TSS: **DSERTSS2** utilizado para NFSE e **DSERTSS1** utilizado para outras demandas.
DESENVOLVIMENTO LINHA DE PRODUTO OU TSS10%90%

**TSS - Demandas com impacto no ERP x TSS**

1. ***Issue* Clone**
2. **Links (depende de, *relates to*).**
3. **Filtros**
4. **Dashboards**

1. ***Issue* Clone**  
   A área de Desenvolvimento da Linha de Produto deve criar uma ***Issue* Clone** para o Desenvolvimento do TSS.
   1. A *Issue Clone* é interna. A Issue que está com a linha de produto é que possui vínculo com o *ticket* do Cliente.
   2. As Issues devem ser relacionadas por meio de ***link*** no JIRA.

**1.1 Como clonar tarefa / subtarefa?**

As tarefas / subtarefas podem ser clonadas para facilitar a réplica de informações para uma nova tarefa / subtarefa. Para criar siga as orientações abaixo:

1. 1. Clicar em **More**.
   2. Escolher a opção **Clone**.
   3. Informar um **resumo (summary)** para a tarefa / subtarefa clonada.
   4. Clicar em **Create**.

1. 1. A Issue de Clone é criada no mesmo projeto da *Issue* original. Para que a demanda seja enviada para o outro time é necessário mover a *Issue* para o projeto que você deseja criar a demanda.
   2. Para mover, clique em **More** > **Move**.
   3. Deve ser informado o **Projeto** e a ***Issue Type***.
   4. Projetos TSS: **DSERTSS2** utilizado para NFSE e **DSERTSS1** utilizado para outras demandas.

1. 1. Clique em ***Next*** e **confirme**.
   2. Na tarefa / subtarefa clonada é criado com um **link** do tipo **Clone**. Este link é somente informativo, não possui nenhuma parametrização na ferramenta.
   3. Sugere-se que para **produtos com integração** seja utilizado outro tipo de Link **(“Dependente de”** ou **“Relates to”).** Caso uma das opções seja utilizada, o link Clone pode ser excluído. A utilização destes links facilitará sua gestão e a configuração do seu Dashboard.
2. **Links (depende de, *relates to*)**

**2.1 Depende de**

O link **dependente de** pode ser utilizado em situações que a *Issue* precise estar relacionada a outra *Issue* e uma não pode ser concluída sem que a outra também esteja concluída. **Este tipo de link é indicado para produtos com integração e que as alterações precisam ser liberadas em conjunto.**

Na tarefa principal, onde está o link **dependente de** possui uma validação que não permite finalizar a etapa de **Teste Integrado** para **Expedição/Teste Integrado Concluído**, sem que a *Issue* a qual possui dependência esteja concluída.

Após conclusão da *Issue* com dependência a transição de **Liberar para Expedição** ou **Finalizar Teste Integrado** fica novamente disponível.

2.1.1 **Como Criar Link Depende de:**

1. 1. Clique em **More** > **Link**.
   2. Na issue original, do Cliente por exemplo, deve ser informado o tipo de link “**Depende de**” e informado a issue que será vinculada, ou seja, qual issue precisará ser finalizada antes da issue atual.
   3. Clique no botão **Link** para confirmar.
3. **2.3 Relates to**

O link **Relates to** pode ser utilizado em situações que a Issue precise estar relacionada a outra Issue para manter a rastreabilidade, mas que uma não dependa da outra para liberação ao Cliente.   Esse tipo de link é apenas informativo para auxiliar na visualização e acompanhamento em Dashboards. **Este tipo de link é indicado para produtos com integração.**

2.2.1 **Criar Link Relates to:**

1. 1. Clique em **More** > **Link**.
   2. Deve ser informado o **tipo de link** e a **Issue original** que será vinculada.
   3. Clique no botão **Link** para confirmar.

**3. Filtros**

Para criar filtros consulte as orientações descritas no **[Manual do JIRA](http://tdn.totvs.com/pages/viewpage.action?pageId=270897823)**.

**3.1 Sugestões de filtros para o produto TSS**

**Filtro utilizado para identificar as dependências**

* + **Quais Issues do meu projeto dependem de outras Issues para serem concluídas.**
    - project = 'PROJETO PRODUTO' and issueFunction in linkedIssuesOf("", "É dependência para") and (status not in ("Teste Integrado Concluído", "Pronto para Expedição", "Concluído", Expedido))

* + **Quais Issues de outros projetos estou dependendo para Liberar a minha Issue.**
    - issueFunction in linkedIssuesOf("project ='PROJETO PRODUTO' ", "Dependente de") AND STATUS NOT IN (Concluído, "Teste Integrado Concluído", Expedido, "Pronto para Expedição")

**Filtro utilizado para identificar os Relacionamentos**

* + **Quais Issues que estão relacionadas ao projeto com o link Relates to.**
    - issueFunction in linkedIssuesOf("project = 'PROJETO PRODUTO' ", "relates to") ORDER BY status

**4. Dashboard**

O ***Dashboard*** pode ser utilizado para a gestão e o controle das atividades criadas / executadas pelas Equipes dentro da ferramenta JIRA.

**4.1 Como criar um dashboard?**

1. 1. No menu superior, clique em ***Dashboards* > *Manage Dashboards* > *Create new dashboard***.
   2. Preencha os campos.
   3. Clique em *Add.*
   4. Escolha os *gadgets* de sua preferência.

**4.2 Como consultar um *Dashboard*existente?**

Acesse um *Dashboard* criado e incluia no favorito do usuário. Siga as instruções:

1. 1. ***Dashboards* > *Manage Dashboards.***
   2. Selecione no menu esquerdo a opção ***Search*** e utilize uma das opções para localizar o *Dashboard* desejado.

1. 1. Para que o *Dashboard* apareça na tela do usuário é necessário clicar na  (**estrela)** para marcar a opção desejada.

**4.3 Como editar Dashboard e Gadget?**

Para que seja possível editar um *Dashboard* compartilhado por outra pessoa, o usuário deve realizar uma copia deste *Dashboard.*

**4.3.1 Copiando *Dashboards* existentes**

1. 1. No *Dashboard* desejado, acesse a opção **Tools** > **Copy *Dashboard***.
   2. Informe o nome do seu *Dashboard*.
   3. Clique no botão **Add**.

1. 1. A partir da cópia realizada o *Dashboard* é do usuário e pode ser editado o **layout, gadgets e filtros**.
   2. O *Dashboard* pode ser compartilhado com outros usuários, porém é importante que os filtros desse *dashboard* também estejam compartilhados.

**4.3.2 Editando os *Gadgtes do Dashboard***

1. 1. Clique no botão  e na opção **Edit** para editar o *Gadget.*

1. 1. Ajuste filtro, colunas e o número de registro.
   2. Para facilitar a busca selecione o filtro desejado e utilize a opção ***Advanced Search*** .

**4.4 Incluindo novos Gadgets**

O usuário deve avaliar quais informações deseja acrescentar em seu *Dashboard*.

1. 1. Para incluir um *Gadget* acesse ***Add Gadget*** e selecione a opção ***Load all Gadget**.*
   2. Clique em ***Add Gadget*** e a opção escolhida será inserida no seu *Dashboard*.

1. 1. Os Gadgets mais utilizados são:
      1. **Filters Results:** demonstra o resultado de um filtro onde o usuário pode selecionar quais colunas deseja visualizar.
      2. **Two Dimensional Filter Statistics**: demonstra a soma de dados com base em dois campos.
      3. **Pie Chart:** demonstra um gráfico de pizza, com base em um filtro e pode ser utilizado qualquer campo para agrupar as informações.
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
