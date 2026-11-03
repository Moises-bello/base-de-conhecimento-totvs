---
content_hash: 16182d53bcc4d9cc4ac4557cad51fc3bac429fec889c330db904f91cf6b4704a
fetched_at: '2026-06-29T00:11:49.783094+00:00'
page_id: '838210925'
product: rm
source: tdn-rm
title: Fluxo de Aprovação de Lançamentos Manuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=838210925
version: 32
---

**Conteúdo**

truesquare

## **01. Sobre**

Um fluxo de aprovação para a inclusão de lançamentos contábeis manuais é essencial para garantir a **integridade**, **precisão** e **conformidade** dos registros contábeis, além de fortalecer os controles internos e a governança corporativa como um todo.

Através deste recurso garantimos:

* **Controle de qualidade**: como uma camada adicional de controle de qualidade sobre os lançamentos contábeis manuais, visando garantir que os lançamentos sejam revisados por partes independentes e competentes antes de serem registrados nos livros contábeis.
* **Prevenção de erros**: permitindo que os lançamentos sejam revisados quanto à precisão e conformidade com as políticas contábeis da organização, reduzindo significativamente a probabilidade de erros ou omissões nos registros contábeis.
* **Mitigação de fraudes**: garantida pela revisão e aprovação dificultando que os dados sejam manipulados indevidamente, promovendo dessa forma, a transparência e a prestação de contas dentro da organização.
* **Conformidade regulatória**: com o atendimento à regulamentações específicas que exigem controles rigorosos sobre os registros contábeis, ajudando a demonstrar a conformidade com essas regulamentações em caso de auditorias externas ou revisões regulatórias.
* **Auditoria interna eficaz**: facilitando o trabalho da equipe de auditoria interna ao fornecer um rastro claro de quem revisou e aprovou os lançamentos contábeis, simplificando o processo de revisão durante as auditorias internas e permitindo uma identificação rápida de quaisquer problemas ou discrepâncias.

## **02. Configuração**

Para habilitar os Processos de Aprovação de Lançamentos Manuais é preciso habilitar o parâmetro "**Utilizar Fluxo Aprovação**" disponível na Etapa 1 - Manutenção dos Lotes Contábeis.

  
Atençao!!!

O campo 'Utilizar Fluxo Aprovação' só pode ser desmarcado quando não houver nenhum lote pendente de aprovação ou já aprovado. Certifique-se de que todos os lotes estão em estado de edição antes de desmarcar este campo.

  

## **03. Funcionamento**

#### **Lote Zero**

**🟢 Parâmetro "Utilizar Fluxo Aprovação" MARCADO**

* **Regra Geral:** O sistema impede o usuário de realizar a inclusão, alteração ou exclusão de lançamentos manuais no Lote Zero.
* **Exceção (Exclusão):** Usuários que possuem a permissão "Aprovar Lote" têm a permissão liberada para realizar a **exclusão** de lançamentos que já foram integrados ao Lote Zero.
* **Restrição de Alteração:** A alteração de lançamentos integrados permanece **bloqueada**, mesmo para aprovadores. Permitir edições diretas iria contra a premissa fundamental do Fluxo de Aprovação, que é garantir o controle rigoroso dessas informações.
* **Processos Não Afetados:** As rotinas abaixo continuam permitidas e não sofrem bloqueio:

  + Transferência de Grupos Contábeis;
  + Estorno de partidas no Lote Zero por outros módulos;
  + Equivalência Patrimonial;
  + Ajuste de Conversão de Multimoeda.

**🔴 Parâmetro "Utilizar Fluxo Aprovação" DESMARCADO**

* O sistema permite ao usuário realizar livremente a inclusão, alteração ou exclusão de lançamentos manuais no Lote Zero.

---

#### **Lote N**

**🟢 Parâmetro "Utilizar Fluxo Aprovação" MARCADO**

* **Novos Campos:** O cadastro de Lotes N Contábeis passará a exibir os campos de "Status" e "Usuário Solicitante".
* **Status Padrão:** Ao criar um lote, o status inicial será sempre "Em Edição".
* **Controle de Status:** O status de aprovação só poderá ser alterado por meio de processos do sistema (não manualmente).
* **Bloqueios por Status:** Lotes N que estiverem com o status **"Aguardando aprovação"** ou **"Aprovado"** não permitem a inclusão, alteração ou exclusão de lançamentos.

**🔴 Parâmetro "Utilizar Fluxo Aprovação" DESMARCADO**

* O cadastro de lotes não exibirá os campos de Status de Aprovação.
* A manutenção dos lançamentos dos lotes funcionará normalmente, sem a aplicação de novas regras.

## **04. Status**

Possibilidades de Status de Aprovação dos Lotes.

Em Edição

* É permitido efetuar inclusão/alteração ou exclusão de Lançamentos
* Não pode ser integrado ao Lote Zero

Aguardando Aprovação

* Não é permitido efetuar nenhuma inclusão/alteração ou exclusão de Lançamentos
* Não pode ser integrado ao Lote Zero

Aprovado

* Não é permitido efetuar nenhuma inclusão/alteração ou exclusão de Lançamentos
* Enquanto o Lote estiver neste Status, poderá ser Integrado ao Lote Zero

## **05. Processos**

**Solicitar Aprovação**

* Para Solicitar Aprovação o usuário precisa ter permissão de Solicitador
* Só pode ser feito em lotes do módulo Contábil
* O processo de Solicitação alterará o Status de Aprovação do Lote de **"Em Edição"** para **"Aguardando Aprovação"**
* Para todos os lotes processados com sucesso, será enviado um e-mail com as informações dos lotes aos **"Usuário aprovador"** responsáveis.
* Na visão de Lotes são apresentadas as informações **"Status de Aprovação"** e **"Usuário solicitante da aprovação"**.

**Aprovação**

* Para aprovar qualquer solicitação de Lote o usuário precisa de permissão de Aprovador
* O Processo altera o Status de Aprovação de **"Aguardando Aprovação"** para **"Aprovado"**
* Usuários que incluíram ou alteraram algum lançamento não poderão aprovar a Solicitação.
* Nas partidas dos lançamento contábil do lote são apresentadas as informações **"Data Aprovação"** e **"Usuário Aprovação"**.

**Retornar para "Em Edição"**

* Para retornar o lote para "Em Edição", o usuário precisa de permissão de Retornar Lote para "Em Edição"
* O retorno do Lote para "Em Edição" poderá ocorrer somente em lotes que estejam com Status **"Aguardando Aprovação"** ou **"Aprovado"**
* O Processo retornará o Status de Aprovação do lote para **"Em Edição"**
* Ao final do processo, as informações de **"Usuário solicitante"**, **"Usuário Aprovação"** e **"Data de aprovação"** serão removidas
* Para todos os lotes processados com sucesso, será enviado um e-mail com as informações dos lotes ao **Usuário solicitante**.

**Integração Lote Zero**

* Só poderá integrar ao Lote Zero lotes com Status de Aprovação **"Aprovado"**
* Após integrar ao Lote Zero, todos os lançamentos do Lote N serão migrados para o Lote Zero, o Status de Aprovação do Lote N retornará para "Em Edição" ou o Lote será excluído, dependendo da parametrização

**Observações**

* Somente Lotes com Status de Aprovação "Aprovado" podem ser integrados ao Lote zero
* Somente poderá incluir/alterar ou excluir lançamentos que estiverem em Lote com Status de Aprovação **"Em Edição"**
* A configuração para envio do e-mail e **sempre centralizada** na Coligada Global
* **Para configurar o envio de e-mail: [Configurar envio de e-mail RM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6603997367319-Framework-Linha-RM-Frame-Realizar-login-com-senha-de-app-para-envio-de-e-mail-Gmail)**

## **06. Materiais de Apoio**

VídeosleftfadeWebinarWebinarWebinarnoneVideo WebinarHow ToHow ToHow TononeVideo How To
