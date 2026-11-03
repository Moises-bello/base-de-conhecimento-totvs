---
content_hash: 95b3591960a028381b7a38e8041cbec80f48fe8841b4bd460bde8c9f2b087a90
fetched_at: '2026-06-29T00:12:07.305730+00:00'
page_id: '923178614'
product: rm
source: tdn-rm
title: Atendimento -WorkFlow de Aprovação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=923178614
version: 8
---

##### **A partir da versão 12.12506**

# **Gestão e Segurança na Aprovação de Contratos de Venda**

Para garantir uma melhor gestão e segurança na formalização dos contratos de venda, o sistema permite a configuração de um **workflow de aprovação** para a integração do **TAA** com os processos de **efetivação de contrato de venda, aditivo e distrato**.

## **Configuração do Workflow de Aprovação**

Para configurar esse processo, siga os passos abaixo:

1. **Criar um Tipo de Atendimento de [Aprovação de Workflow](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI)**.
2. **Preencher os parâmetros na [Etapa 4 - Integração com Agilis](https://tdn.totvs.com/pages/viewpage.action?pageId=435105270&draft=true)**.

## **Funcionamento do Workflow de Aprovação**

* A efetivação de qualquer processo **somente ocorrerá se a gestão aprovar**, proporcionando maior controle e agilidade no fluxo de trabalho.
* Sempre que um processo for submetido à efetivação, será automaticamente criado um **atendimento vinculado**.
* **No caso da venda**, o atendimento será gerado apenas se houver um **plano de financiamento que nunca foi efetivado**, já que é comum que o processo volte para ajustes antes da efetivação.
* Caso o processo seja **aprovado**, a efetivação poderá ser executada **automaticamente pelo sistema** ou **manual pelo usuário**.
* Se o processo for **reprovado**, a efetivação permanecerá **bloqueada**, e nenhuma ação automática será realizada. O usuário deverá executar a ação manualmente, se necessário.

## **Exclusão de Processos e Cancelamento da Integração**

Para excluir um **atendimento vinculado** a esses processos, é necessário remover os registros associados:

* **Contrato de Venda** → Excluir o **plano de financiamento vinculado**.
* **Distrato** → Excluir o **cadastro do distrato**.
* **Aditivo** → Excluir o **cadastro do aditivo**.

Essa exclusão garante a **eliminação da integração do registro**.

## **Visão dos Processos**

Para facilitar a **gestão dos processos aprovados e reprovados**, cada tela disponibiliza:

* **Número do atendimento**.
* **Status do atendimento**.

## **Critérios de Aprovação e Reprovação**

Para que um processo seja **aprovado** e a ação de efetivação seja executada, siga os passos abaixo:

**Configuração da Aprovação no TCGI**

1. Acesse o **cadastro do Tipo de Atendimento do TCGI**.
2. Na **etapa do Tipo de Atendimento do TAA**, configure o campo **Serviço Associado ao Tipo de Atendimento** e selecione a **integração 25 - Serviços do TIN**.
3. Clique em **Anexos → Etapas** e selecione a **etapa considerada como Aprovada**.
4. Edite o registro e acesse a aba **Ações Visíveis**.
5. Marque a opção correspondente: **Efetivar Venda/Distrato/Aditivo**.
6. Feche a tela de etapas e volte para a tela de **Tipo de Atendimento**.
7. Clique em **Anexos → Fluxo de Etapas**.
8. Localize o **fluxo de Aprovação/Concluir** e edite o registro.
9. Acesse a aba **Ações Visíveis** e marque as opções:
   * **Efetivar Venda/Distrato/Aditivo**
   * **Execução Obrigatória**
10. Feche todas as telas para concluir a configuração do fluxo de aprovação.

Para que um processo seja considerado **reprovado**, o status do atendimento deve estar em:

* `saConfirmado = "U"`
* `saConcluido = "O"`
* `saConcluidoAConf = "F"`
* `saConcluidoAut = "V"`

Esse fluxo garante **maior controle, segurança e agilidade** na gestão dos contratos de venda e seus respectivos processos.
