---
content_hash: 7b22a76616fbc8a0c8de6a7a01969f0af97bd895152c4946821690ccd79ccf10
fetched_at: '2026-06-29T00:10:15.941915+00:00'
page_id: '465390299'
product: rm
source: tdn-rm
title: Acompanhar execução das contabilizações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465390299
version: 19
---

---

Na geração da contabilização / estorno por competência do TOTVS Educacional com o objetivo de fracionar os processos, foi desenvolvida funcionalidade que particiona de forma automática os contratos selecionados, criando novos processos e os colocando em execução.

Na tela de geração de contabilização / estorno assim que for disparada a execução, o sistema fará uma carga de todos os contratos, conforme selecionado ou definido nos filtros ordenando os mesmos por matriz aplicada.

Após a carga dos contratos, o sistema consultará os parâmetros de fracionamento abaixo, para saber se utilizará o fracionamento de processos bem como qual será o número de contratos por fracionamento.

* "Utiliza fracionamento de processos: Indica se o fracionamento de processos (jobs) está habilitado.
* "N° de contratos por fracionamento: Indica o número limite de contratos que o sistema considerará por fracionamento.
* Nº máximo de processos por contexto: Número limite de processos a serem gerados pelo fracionamento, ou seja, o sistema somente criará processos até o número máximo especificado por esse parâmetro.

Caso o fracionamento tenha sido realizado, o sistema habilitará o botão "Monitorar processos em execução", ao ser clicado fechará o formulário de contabilização / estorno e exibirá uma tela de acompanhamento da contabilização / estorno.

Se o usuário quiser acompanhar todos os subprocessos não concluídos, poderá acessar a tela de acompanhamento da execução de contabilizações através do menu Financeiro / Contábil l Contabilidade l Acompanhar execução das contabilizações.

**Teremos a possibilidade de executar filtros mais completos e demais funcionalidades, conforme descrito abaixo:**

**Filtro Genérico:**  
O acompanhamento agora permite que sejam feitos filtros personalizados, para que o usuário possa visualizar somente o desejado.  
Ao final da contabilização / estorno, o sistema exibe o botão de "Monitorar processos em execução". Este botão abre somente o acompanhamento da contabilização / estorno dos contratos que foram solicitados naquele momento.  
Este é o filtro padrão do sistema, onde é possível aperfeiçoar as buscas com informações básicas como: Usuário, data de inicio, data de término, status e progresso, por exemplo.

**Interrupção do processo:**  
Foi disponibilizado uma funcionalidade que permite que o processo seja abortado, em caso de solicitação indevida.  
Esta opção só pode ser acionada para processos em andamento.

**Exclusão:**  
Inserimos também o botão de exclusão. A exclusão pode ocorrer para monitoramentos concluídos ou interrompidos.  
Ressaltamos que não será possível excluir processos em andamento, sendo assim, necessário solicitar a interrupção do processo antes.

**Desabilita e Habilita execução dos processos:**Foi disponibilizado em ambientes Três Camadas os botões que Desabilita e Habilita a execução de processos não iniciados.  
Esta opção só pode ser acionada para processos que ainda não foram iniciados.

  Informações Complementares.

---

[Fracionamento do processo de contabilização](http://tdn.totvs.com/pages/viewpage.action?pageId=465385372)
