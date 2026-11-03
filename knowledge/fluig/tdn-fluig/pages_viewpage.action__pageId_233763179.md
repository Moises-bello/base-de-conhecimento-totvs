---
content_hash: 60287f1b54b0994706b7cecd98ea6723c4f81cee64ebb84bf16c50dc308e4184
fetched_at: '2026-06-28T21:35:20.333646+00:00'
page_id: '233763179'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Converter solicitações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233763179
version: 25
---

# Falando de converter solicitação...

---

A finalidade deste recurso é converter solicitações abertas em versões de processo mais antigas para versões mais novas. Isso é feito mapeando as atividades do processo da versão mais antiga para atividades da versão mais nova. Assim, a solicitação do processo antigo recebe todas as funcionalidades e atividades da versão mais nova com uma simples conversão.

Em uma aplicação correta da melhoria continua em processos de negócio, uma solicitação workflow deveria iniciar e terminar na mesma versão de um processo.

O principal motivo pelo qual é permitido o versionamento de processos é justamente oferecer a oportunidade melhoria nos processos, buscando otimizar o tempo gasto em suas tarefas ou permitir uma melhor distribuição de recursos de uma organização, tanto financeiros como humanos. Outro motivo pelo qual a plataforma oferece a conversão de solicitações workflow, é como último recurso para as situações aonde não seja possível:

* O usuário responsável por uma tarefa não conseguir movimentar a mesma para outra atividade.
* O usuário gestor do processo não conseguir movimentar a solicitação workflow.
* Do ponto de vista de negócios, o cancelamento da solicitação e inicio de uma outra não seja possível .

Ressaltando que, ao executar a conversão de solicitações, algumas regras da plataforma deverão ser consideradas, como:

* Serão executados os eventos de processos que afetam tanto a atividade origem como a atividade destino.
* O usuário que recebe a tarefa deverá ser um usuário incluso no mecanismo de atribuição definido para a tarefa destino.
* O privilégio de usuário administrador não ultrapassa as limitações impostas pelo mecanismo destino.
* Não é possível converter solicitações de processos cujo fluxo esteja pendente em uma atividade de sub processo no momento da conversão.
* Solicitações que possuem atividades configuradas como consenso só poderão ser convertidos se a nova versão também possuir essas atividades devidamente mapeadas como consenso.
* A versão do formulário da solicitação será mantida após a conversão.

A criação de versões de processos específicas para ajustes e correções técnicas que permitam a solicitação workflow não são recomendadas e devem ser evitadas ao máximo. Acesse a FAQ [BPM 097](http://tdn.totvs.com/x/WkIMEQ) e veja a lista com algumas ações que podem ser tomadas pelo desenvolvedor de processos a fim de propiciar o desenvolvimento de processos que necessitem destas manutenções constantes sem que para isso seja necessário versionar o processo com tanta frequência.

Precisa de ajuda?Acesse a **Central de ajuda** da plataforma clicando no ícone **Assistente** – localizado no lado superior direito do cabeçalho – e, em seguida, clicando na aba **Central de ajuda** para obter informações específicas sobre este recurso, além de *links* com documentações relacionadas. [Saiba mais](http://tdn.totvs.com/x/ZMhSDg).

## Converter solicitações

---

**01.** No menu principal, clique em **Processos**.

**02.** Clique em **Converter solicitações**.

**03.** Selecione o processo no qual deseja converter as solicitações.

**04.** Na seção **Dados do processo**, serão exibidos a versão e as solicitações abertas. Selecione a versão do processo na qual se deseja converter as solicitações.

#f2f2f2#f2f2f2

Somente é possível converter solicitações que estejam abertas, por isso, a versão do processo selecionada deve conter solicitações abertas.

**05.** Na seção **Atividades do processo** é possível visualizar quantas atividades existem e quantas tarefas encontram-se abertas em cada atividade. Selecione a atividade do processo que deseja converter.

**06**. Clique em **Avançar** – localizado no canto superior direito da tela.

**07.** Em **Versão destino**, selecione a versão para a qual as solicitações que estão na versão origem serão convertidas.

**08.** Para cada atividade da versão origem, selecione uma atividade da versão destino.

#f2f2f2#f2f2f2

Para cada atividade da versão antiga do processo deve ser mapeada uma atividade da versão destino. Esse mapeamento é necessário para relacionar as atividades que são iguais ou semelhantes entre as duas versões do processo.

**09.** Clique em **Avançar**, localizado no canto superior direito da janela.

**10.** Na listagem de solicitações exibida, selecionar quais delas devem ser convertidas.

**11.** Acionar **Avançar** – localizado no canto superior direito da tela.

**12.** Clique em **Converter**.

#f2f2f2#f2f2f2

Ao converter as solicitações, todas as tarefas pendentes são finalizadas e novas tarefas são criadas para as atividades de destino. Ao término da conversão, é possível visualizar o log para verificar se o processo foi concluído com êxito.

Fique atento!

Esta documentação é válida a partir da atualização**Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
