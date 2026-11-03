---
content_hash: 6f5ef6d81f4dd17724f134355aa003b8170ccc7eb36a61a8cb8918b9f0182ade
fetched_at: '2026-06-29T00:09:54.298079+00:00'
page_id: '444607665'
product: rm
source: tdn-rm
title: Qual a função do parâmetro "Considerar todas as coligadas" ?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444607665
version: 7
---

# Objetivo:

---

O objetivo deste documento é informar o funcionamento do parâmetro: "Considerar todas as coligadas ". O parâmetro foi criado para que as rotinas do eSocial se tornem mais dinâmicas quanto à seleção de todas as coligadas (Painel de Multi Coligadas).

---

# Os processos contemplados com essa funcionalidade são:

---

- Gerar XML (Eventos Não Periódicos)

- Gerar XML (Eventos Periódicos)

- Integrar com o TAF

- Atualizar Status  Integração com o TAF

---

# Funcionalidade :

---

Este parâmetro possibilita que, quando um usuário montar o perfil de execução dos processos acima citados, e salvar este perfil marcando este novo parâmetro, o sistema considerará automaticamente e selecionará as novas coligadas adicionadas, sem a necessidade de editar o perfil nos processos.

Para os usuários que trabalham com  agendamento de Jobs manterá dinâmica suas rotinas do eSocial garantindo que todas as coligadas sejam consideradas.

---

**Exemplo: Gerar XML (Eventos de Tabelas e Não Periódicos)**

* **Perfil salvo com o parâmetro "Marcado" :**

Na tela "Seleção de coligadas " confirmado o parâmetro " **Considerar Todas as coligadas**":

* A última coligada apresentada é  a coligada de código 19.

* No cadastro de coligadas foi incluída uma nova coligada.

Executando o processo selecionando o perfil criado anteriormente.

* Será visualizada a nova coligada e virá marcada na seleção.

* ****Perfil salvo com o parâmetro "Desmarcado" :****

  A nova coligada será visualizada, porém, virá desmarcada na seleção.

 

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.23 |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

Andreia Valquiria Pereira

Hugo de Oliveira Costa
