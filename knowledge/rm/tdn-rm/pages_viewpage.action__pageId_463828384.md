---
content_hash: bc72ab940854cdc749a942d0a2999b42cc70216969f1d535846520e7b1797eb4
fetched_at: '2026-06-29T00:10:15.294314+00:00'
page_id: '463828384'
product: rm
source: tdn-rm
title: Status "Em Faturamento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463828384
version: 3
---

* **Objetivo:**

Atender as necessidades de nossos clientes que após gerarem movimentações no sistema, este processo corrige movimentos que por algum motivo o processo de faturamento tenha sido interrompido sem que seja pelo cancelamento da execução e assim o status dos movimentos tenham ficado com o status "**Em Faturamento**". 

Ao executar este processo, será iniciado a rotina de corrigir o status de todos os movimentos selecionados, fazendo com que voltem ao seu status inicial antes da interrupção do processo de faturamento.

Para correção, o processo realiza um filtro, exibindo na tela todos os movimentos dos tipos de movimento no qual o **usuário logado** tenha permissão de consultar nos parâmetros de "**Permissões por Tipo de Movimento**".

Caso tenha algum movimento que o usuário logado "**NÃO"**tenha permissão de consultar, os movimentos "**NÃO"**serão exibidos na tela para que sejam selecionados e consequentemente corrigidos os status.

Para conceder permissão de consulta, acesse o anexo "**Permissões por Tipo de Movimento**" do cadastro do usuário e marque a opção  "**Consultar**" para o tipo de movimento que deseje visualizar as movimentações no anexo do Cliente/Fornecedor.
