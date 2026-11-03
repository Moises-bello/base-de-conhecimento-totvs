---
content_hash: bae24884a64f1edcd75b825e4eab823c20144eb26cd9ead908e6b434bf2271d9
fetched_at: '2026-06-29T00:10:11.137382+00:00'
page_id: '452719950'
product: rm
source: tdn-rm
title: Cancelamento de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719950
version: 4
---

Através deste processo é possível cancelar as férias que foram previamente cadastradas e/ou calculadas no mês e/ou próximo mês, ou cancelar apenas o abono pecuniário cadastrado e/ou calculado sem o gozo das férias.  
   
**Atenção I:**  
Para cancelamento apenas do abono pecuniário, quando não existe gozo de férias, é utilizada a data de pagamento como base de verificação.  
   
**Atenção II:**  
Somente serão canceladas as férias que ainda não foram lançadas para o envelope, ou seja, cuja a situação de férias seja 'M-Marcadas'.

**Armazena liquido como Evento Programado:**

Este parâmetro será utilizado para guardar o liquido de férias pago ao funcionário, caso seja necessário o cancelamento das férias marcadas antes do lançamento no envelope do funcionário, para desconto posteriormente através de lançamento de Evento Programado.

**Observação:**

* Serão cancelados todos os períodos de gozos de férias que contemplam o período informado na tela deste processo.
* Ao realizar o processo de cancelamento das férias,  será gerado o Evento de Exclusão (S-3000) para o eSocial.
