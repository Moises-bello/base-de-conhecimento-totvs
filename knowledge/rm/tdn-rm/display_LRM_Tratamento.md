---
content_hash: f93766f21574813c25988ba1deb7b2cf1977873761ccacb5b2b284ad0993a21c
fetched_at: '2026-06-29T00:11:11.802495+00:00'
page_id: '650485113'
product: rm
source: tdn-rm
title: Tratamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Tratamento
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização - Versões até 2510**
3. **Exemplo de utilização - Versões a partir 2602**

Tratamento1. Visão Geral

## **01. VISÃO GERAL**

A funcionalidade centraliza a gestão dos protocolos e ciclos do tratamento oncológico dos pacientes.

2. Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO - Versões até 2510.**

Ao acessar o menu de Oncologia, será aberta a tela com as seguintes abas: Diagnósticos e Estadiamento, Tratamentos e Quimioterapia.

Ao clicar na aba de "Tratamentos", será exibido para o usuário os campos: "Finalidade protocolo", "Buscar protocolo" e o botão "Adicionar".

Ao selecionar uma finalidade, serão listados apenas os protocolos que compõem aquele grupo de finalidade. Este campo não é obrigatório, o usuário poderá selecionar um protocolo sem a necessidade de escolher uma finalidade. 

O usuário poderá pesquisar no campo qual o protocolo deseja adicionar antes de selecionar. O botão adicionar será habilitado após selecionar um protocolo.

Ao clicar no botão "Adicionar", o sistema listará o protocolo e as fases de quimioterapia que o compõem.

Em cada etapa do protocolo serão exibidas as seguintes informações:       

* Status da etapa: "Não iniciado", "Em tratamento", "Suspenso" e "Finalizado";
* Quantidade de ciclos;
* Duração do ciclo;
* Intervalo entre ciclos;
* Tipo de tratamento;
* Finalidade

Para iniciar um tratamento o usuário deverá clicar no botão "Iniciar tratamento".  Ao clicar no botão "Iniciar tratamento", o usuário deverá confirmar se deseja iniciar o tratamento.

Ao iniciar o tratamento o sistema deverá apresentar a data de início e mudar o status de "NÃO INICIADO" para "EM TRATAMENTO".

É possível excluir um protocolo que não tenha nenhuma fase iniciada ou suspensa. Caso contrário, o botão "Excluir" ficará desabilitado. Ao clicar no botão "Excluir", o protocolo será excluído imediatamente, sem necessidade de confirmação do usuário. 

Após iniciar o tratamento, o botão "Iniciar tratamento" não será mais exibido e o botão "Suspender" ficará habilitado:

Se o usuário clicar no botão "Suspender", uma modal de confirmação será exibida e para confirmar a suspensão deverá obrigatoriamente preencher uma justificativa. Após informar a justificativa, o tratamento exibirá o status "SUSPENSO" e a data de suspensão.  

 

Os tratamentos só podem ser iniciados quando o atendimento do paciente estiver com o status aberto.

## **2.1****HISTÓRICO DE TRATAMENTO**

O usuário poderá visualizar o histórico de todos os tratamentos vigentes e também os que foram suspensos para o paciente. Nesta seção, o usuário poderá consultar o profissional responsável pelo início ou suspensão do tratamento e a data/hora da ação.

3. Exemplo de utilização - Versões a partir 2602

## **03.** **EXEMPLO DE UTILIZAÇÃO - Versões a partir 2602**

A tela de Tratamentos do módulo de Oncologia no PEP foi atualizada na versão **12.1.2602**. Além da interface renovada, foram incorporados recursos que ampliam o controle sobre protocolos, ciclos e logs de alterações.

A aba Tratamento apresenta uma tabela com todos os tratamentos criados para o paciente. Cada protocolo e cada um de seus ciclos aparece como uma linha independente, permitindo gestão detalhada. 

Campos exibidos na tabela:

* **Status**  (os protocolos são apresentados por ordem dos status: "Em andamento", "Não iniciado", "Finalizado" e "Suspenso")
* **Protocolo prescrito**
* **Finalidade**
* **Fase**
* **Duração do ciclo**
* **Intervalo entre os ciclos**
* **Quantidade de ciclos**

Ao clicar no botão **“Adicionar”**, o sistema abre uma tela com os campos necessários para programar o tratamento oncológico.

| Campo | Obrigatório? | Descrição |
| --- | --- | --- |
| Finalidade do tratamento | ✔ | Define o objetivo terapêutico |
| Protocolo prescrito | ✔ | Seleção do protocolo cadastrado no sistema |
| Fase do protocolo | ✔ | Define qual fase está sendo iniciada |
| Data prevista do primeiro ciclo | ✔ para iniciar / ✘ apenas para incluir o tratamento | Essencial para iniciar o tratamento |
| Datas previstas dos demais ciclos | ✘ | Podem ser definidas ou editadas depois |
| Início do tratamento | ✔ ao iniciar | Define a efetiva entrada do paciente no protocolo |

Após incluir um novo protocolo de tratamento, as informações serão listadas na tabela principal. Para visualizar o detalhamento do cronograma dos ciclos, basta expandir o registro, onde serão exibidas as seguintes colunas:

* **Status do ciclo**
* **Ciclo**
* **Prestador**
* **Data de início**

Após a adição de um protocolo a possibilidade de ação na tela fica diferenciada na fase ou no ciclo.  O usuário pode ter algumas ações relacionada a todos os ciclos da fase ou ações em ciclos isolados da mesma fase.

Ações relacionadas a **fase:**

| Ações | Descrição |
| --- | --- |
| **Suspender** | Interromper todos os ciclos e fase que compõem o tratamento |
| **Editar** | Possibilidade de editar a previsão de todos os ciclos e alterar inicio do tratamento |
| **Mais ações > Finalizar tratamento** | Finalizar o tratamento |
| **Mais ações > Log das alterações** | Log das alterações  do usuário no protocolo selecionado |

Ações relacionadas aos **ciclos:**

| Ações | Descrição |
| --- | --- |
| **Suspender** | Suspender o ciclo selecionado |
| **Editar** | Possibilidade de editar apenas o ciclo selecionado |
| **Mais ações - Log das alterações** | Log das alterações do usuário no ciclo selecionado |

**Logs de alterações** na aba de tratamentos:

Para garantir a segurança assistencial, a rastreabilidade das ações realizadas e os profissionais envolvidos no tratamento, o sistema registra automaticamente todas as interações realizadas nas fases e ciclos dos protocolos.

Ao clicar na opção "Log de alterações", o sistema listará a data e hora da alteração, usuário responsável e justificativa (quando aplicável) dos seguintes eventos:

* Criação
* Início
* Alteração da data prevista
* Suspensão
* Finalização da fase do protocolo

Logs da fase:

Logs dos ciclos:

## **3.1** **EVOLUÇÃO DOS STATUS DO TRATAMENTO**

As fases dos tratamentos adicionados podem assumir os seguintes status:

| Status | Descrição |
| --- | --- |
| **Não iniciado** | Adicionado e aguardando início do primeiro ciclo |
| **Em tratamento** | Ciclo iniciado formalmente pelo profissional responsável |
| **Suspenso** | Tratamento suspenso manualmente antes do término programado |
| **Finalizado** | Encerrado após conclusão dos ciclos |

Ao editar um tratamento ainda não iniciado, o sistema:

* Carrega todos os campos preenchidos anteriormente
* Permite alterar datas, fases e informações clínicas
* Atualiza o status quando o médico optar por **i****niciar o tratamento**
* Permite alterar a data de todos os ciclos com cálculo automático

Os **ciclos** dos protocolos podem assumir os seguintes status:

| Status | Descrição |
| --- | --- |
| **Programado** | Adicionado e aguardando início |
| **Iniciado** | Iniciado formalmente pelo profissional e apresenta data de início prevista |
| **Suspenso** | Suspenso manualmente antes do término programado |
| **Finalizado** | Encerrado após conclusão dos ciclos |

## **3.2** **INTEGRAÇÃO ENTRE TRATAMENTO E PRESCRIÇÃO**

Para garantir segurança assistencial, rastreabilidade e consistência entre tratamento, prescrição e farmácia, o sistema aplica regras automáticas de validação das datas dos ciclos e dos dias de quimioterapia.

Essas regras funcionam com ou sem a funcionalidade de agendamento habilitada e orientam quando uma data pode ou não ser alterada:

* A data inicial do ciclo define o limite mínimo para todos os dias de tratamento posteriores.
* A data de um dia de quimioterapia nunca pode ser anterior à data de início do ciclo.
* Os dias do ciclo devem seguir ordem cronológica, ou seja:

  + Um dia não pode ser anterior ao dia imediatamente anterior.
* Após a envio da solicitação das medicações de qualquer dia para a farmácia:

  + A data do ciclo não pode ser maior que a menor data já liberada.

Essas validações são automáticas e impedem inconsistências no fluxo assistencial.
