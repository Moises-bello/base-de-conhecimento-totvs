---
content_hash: 63946ffa191917e8dd850323615e1cd23d17ac263fede6e39843425b0a974757
fetched_at: '2026-06-29T00:11:22.533614+00:00'
page_id: '705452371'
product: rm
source: tdn-rm
title: 9 - Processo de Ajuste de Transação Pontual - A partir da versão 12.1.2205
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=705452371
version: 11
---

O processo permite ajustar pontualmente o status de uma transação que esteja diferente no painel do Shipay / RASS e na tela de transações no RM.

Acessar:

**Contas a Pagar / Receber | Transações**

Selecionar a transação, acessar processos | Ajuste de transação e avançar o processo.

Somente transações dentro do sistema com status pagamento solicitado, confirmado, expirado e canceladas serão processados. Transações que não tem esse status serão indicados no log do processo.  
Status serão modificados quando:

* Status solicitado no RM e cancelado na operadora > altera status e inclui histórico;
* Status expirado no RM e aprovado na operadora > executa baixa;
* Status expirado no RM e cancelado na operadora > altera status e inclui histórico;
* Status cancelado no RM e com outro status na operadora > inclui registro no log e não executa nenhuma ação.
