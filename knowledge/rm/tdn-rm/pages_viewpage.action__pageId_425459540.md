---
content_hash: 0e396fa545740ad9b4013ab20e0a6ad3c1966f4f933d281f2d58b6cc8ff1c651
fetched_at: '2026-06-29T00:09:36.878715+00:00'
page_id: '425459540'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Liberar Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459540
version: 3
---

**Backoffice RM x Protheus SigaMNT - Liberar Ordem de Serviço**

---

A funcionalidade  Liberar Ordem de Serviço é executada através do Protheus SigaMNT e tem o objetivo de alterar o Status de uma Ordem de Serviço que esteja com o Status "Pendente". Quando uma Ordem de Serviço é incluída,  um dos seus campos é responsável por informar seu status inicialpodendo ser alterado para "Liberado" e fazendo  com que a Ordem de Manutenção seja criada no Backoffice RM. Serão enviados  ao Backoffice RM somente as Ordens de serviço que forem alteradas do Status "Pendente" para "Liberado" ficando a cargo do usuário  a decisão de criá-lo ou não como "Liberada".

**Pré-Condições:**

1: Cadastrar manualmente o DE-PARA de Coligada e Filial RM x Empresas e Filiais Protheus

2: Ter incluído uma Ordem de Serviço Manual(Preventiva) ou Corretiva.  
   
**Executando o Processo:**  
   
**Passo 1:** Acessar: Protheus SigaMNT / Atualizações/ Ordem de Serviço / Liberar O.S.  
**Passo 2:** Selecione uma Ordem de Serviço com o Status "Pendente" e execute o processo de Liberação de Ordem de Serviço.  
**Passo 3:** Será enviada uma mensagem ao Backoffice RM para Incluir os movimentos  a seguir, com o valor zerado (0):

* Ordem de Manutenção
* Solicitação de Armazém ou Solicitação de Compra.
