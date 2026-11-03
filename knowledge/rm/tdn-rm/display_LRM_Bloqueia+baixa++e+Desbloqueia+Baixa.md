---
content_hash: 4ee79a2e2600fbab02cf5b81505fec862cb0eb9e1c43464038ae59381ed9ea33
fetched_at: '2026-06-29T00:09:18.536328+00:00'
page_id: '421388717'
product: rm
source: tdn-rm
title: Bloqueia baixa  e Desbloqueia Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Bloqueia+baixa++e+Desbloqueia+Baixa
version: 10
---

**Bloqueia Baixa**

O bloqueio para baixa será feito através do menu: Processos | Baixa | Bloqueia Baixa.  
Um lançamento financeiro bloqueado não pode ser baixado, não permite a emissão de cheque nem remessa de cobrança ou de pagamento eletrônico.   

Um lançamento financeiro poderá ser bloqueado para baixa no momento da inclusão no sistema, bastando ativar os parâmetros "[Incluir Lançamento a Pagar Bloqueado para Baixa](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)" e "[Incluir Lançamento a Receber Bloqueado para Baixa](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)", desde que seu valor seja superior ao valor mínimo parametrizado. Também pode ser configurado nos [parâmetros](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar) se o bloqueio será simples ou duplo.

**Observação:**

Os parâmetros definidos em "[Bloqueio para Baixa](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)" são considerados tanto para lançamentos a pagar quanto para lançamentos a receber.

**Desbloqueia Baixa**

Um lançamento bloqueado para baixa só poderá ser desbloqueado através da visão de Lançamentos pelo menu Processos: Baixa | Desbloqueia Baixa.  Se o parâmetro "[Desbloqueio Duplo deve ser feito por usuários diferentes](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar)" estiver marcado, os dois desbloqueios deverão ser feitos por supervisores diferentes. Caso esteja desmarcado, os desbloqueios poderão ser feitos pelo mesmo supervisor.
