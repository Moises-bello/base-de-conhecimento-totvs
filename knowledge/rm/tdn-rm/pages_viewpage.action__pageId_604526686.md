---
content_hash: 34f516efa69ced9d91184418944212e9c9d6305f27df6caf29755dc5a867235b
fetched_at: '2026-06-29T00:10:58.231689+00:00'
page_id: '604526686'
product: rm
source: tdn-rm
title: Totvs Folha de Pagamento x TOTVS Moda – Pagamento de Comissões
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604526686
version: 5
---

**Integração Totvs Folha de Pagamento RM x TOTVS Moda - Pagamento de Comissões**

A Integração Totvs Folha de Pagamento RM x TOTVS Moda - Pagamento de Comissões tem o objetivo de receber pagamentos de Comissões do BackOffice TOTVS Moda para que os mesmos sejam lançados no Envelope de Pagamento do Totvs Folha de Pagamento RM.

Para enviá-las, deve-se parametrizar primeiramente as seguintes informações:

**Mensagem: MONTHLYPAYROLL**

**Versão: 1.000**

Envio do pagamento de comissões de vendedores/funcionários para o envelope de pagamento do Totvs Folha de Pagamento RM.

**Exemplo de Json de Envio da mensagem:**

Dessa forma, a integração atenderá os seguintes objetivos:

1) É necessário informar no BackOffice TOTVS Moda o código o evento que será usado para lançamento de pagamento de comissão e o código de evento para pagamento de comissão.

2) É necessário integrar o funcionário que irá receber o lançamento de pagamento de comissão com o BackOffice TOTVS Moda.

3) Os pagamentos serão enviados por competência e irão sobrescrever os antigos enviados pela integração, caso sejam da mesma competência, Chapa e Origem da integração.

4) Para lançar grupo de eventos para os movimentos integrados, será necessário marcar o campo 'Lançar eventos da integração com outros aplicativos' nos parâmetros de grupo de eventos.

5) Feita a parametrização o usuário clica em 'Lançar', o sistema busca na base de dados os movimentos integrados conforme parâmetros informados. Caso exista, o movimento é lançado.

Para verificar se a integração dos dados foi enviada corretamente para o TOTVS Moda, após acionar os gatilhos citados acima acesse o módulo RM | RH | Integração | EA 2.0 | Mensagens | Gerenciamento de Mensagens, pesquise pelo registro com identificador "MONTHLYPAYROLL', clique na pasta 'Dados da execução' , onde poderá verificar os dados de execução da mensagem.
