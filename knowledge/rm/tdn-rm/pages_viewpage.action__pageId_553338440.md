---
content_hash: 4a5b5a7ed674ed514fc07acfa23588381dc100c869680b96b2dba12cbde9afca
fetched_at: '2026-06-29T00:10:44.976584+00:00'
page_id: '553338440'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Criar Defeitos a partir da Tarefa Pai,
  do Kanoah ou Defeito Associado?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338440
version: 1
---

5%90%10%100%

1. Para criar um defeito, deve ser criada uma subtarefa de defeito abaixo de uma *Issue* (Manutenção/ Legislação/ Story/ Réplica/ Documentação) na ferramenta JIRA.

2. Os defeitos devem ser abertos e concluídos durante a execução da tarefa de teste. Se a tarefa de teste for concluída, não será possível realizar commit na subtarefa de defeito. 

É necessário incluir uma Evidência informando que o defeito foi corrigido. A evidência pode ser gerada nos seguintes formatos:

* + - Breve descrição na subtarefa do JIRA.
    - Anexar na subtarefa do JIRA imagens ou vídeos.

3. Caso esteja sendo realizado *Pair Programming* e for encontrado um defeito, o mesmo pode ser corrigido na hora, sem necessidade de registro na ferramenta JIRA.

4. O defeito pode ser criado a partir da Tela de uma Tarefa pai (**Story / Manutenção/ Legislação/ Réplica/ Documentação**) ou por meio da **ferramenta ***Test Management for*JIRA** (*Kanoah Tests)*.**

***Importante:*** Para **Fábrica de Software** o defeito também pode ser criado a partir de uma tarefa pai **(Customização)**.

Criar Defeito a partir da Tela de uma Tarefa Pai (Story / Manutenção / Legislação / Réplica / Documentação)

1. Para criar a subtarefa acesse a **tarefa pai**.
2. Clicar na opção **More > Create Subtask.**
3. Selecionar o tipo da subtarefa **Defeito (sub-tarefa)** no campo *Issue Type*.
4. Preencher os dados > Clicar em **Create**.

Para criar outra subtarefa na sequencia pode-se clicar na opção **Create another.**

Criar Defeito pelo Test Management for JIRA (Kanoah Tests)

1. Na tela da Execução de Testes seguir os seguintes passos:
2. Ir para a seção *Issues* e clicar na seta disponível ao lado direito.
3. Escolher a opção **Create Subtask**.
4. Escolha o **Projeto da Squad**.
5. Procure o ID da Tarefa Pai **(Story / Manutenção/ Legislação/ Réplica/ Documentação)**.

Criar Defeito Associado

Quando um Defeito criado estiver relacionado à correção de outro Defeito pode ser utilizada a opção de criação de link de **Defeito Associado**. Para isso deve-se seguir os passos:

1. No menu superior clique em **Workflow**.
2. Escolha a opção **Associar a defeito**.
3. Informar o **Defeito Associado** (o link utilizado deve ser o Associado à, não se deve alterar o link).
4. Clicar no botão **Associar a Defeito**.

O status do Defeito será **Associado** e será finalizado quando o **pai** for finalizado.

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
