---
content_hash: 690d3bea92af8c0ff476847a73bbca07edbf5244ebbf4a3f03db3b60a20abdaa
fetched_at: '2026-06-29T00:10:58.245152+00:00'
page_id: '604529141'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento RM x TOTVS Moda - Situação de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604529141
version: 6
---

**Integração Folha de Pagamento RM x TOTVS Moda - Situação de Funcionários**

A Integração Totvs Folha de Pagamento RM x TOTVS Moda tem o objetivo de enviar a situação dos funcionários visando integrar estas informações para utilização dos dados com o backoffice TOTVS Moda.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

**Mensagem: GETEMPLOYEESITUATION**

**Versão: 1.000**

Envio da situação do funcionário para o TOTVS Moda. Ao enviar a mensagem para o RM, será retornado uma mensagem com a situação do funcionário em determinada data. Será utilizada a situação que estiver cadastrada no histórico de situação do funcionário em RM | RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Anexos | Histórico de situação para mapeamento de situação de funcionários enviado, de acordo com as situações disponíveis no TOTVS Moda.

**Exemplo de Json de Envio da mensagem:**
