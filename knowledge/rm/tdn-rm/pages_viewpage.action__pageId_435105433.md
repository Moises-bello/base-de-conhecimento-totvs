---
content_hash: 61c8b8d5ca866896b5ec493f86062444c9bcf1daabb062ac04b4ceb94e0a4dd6
fetched_at: '2026-06-29T00:09:50.188646+00:00'
page_id: '435105433'
product: rm
source: tdn-rm
title: Outras Formas de Gerar uma Parcela de Resíduo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105433
version: 1
---

**Outras Formas de Gerar uma Parcela de Resíduo**    
Existem outras duas formas de gerar uma parcela de Resíduo:  
**Processo de Baixa do Último Lançamento Financeiro:** Ao baixar o último lançamento financeiro da venda com resíduo pendente, o sistema deve gerar automaticamente uma parcela de resíduo sem quitar a venda e sem interromper o processo de baixa. A venda continuará com status de Efetivada até que a parcela de resíduo seja totalmente baixada. Após a baixa desta parcela, a venda altera seu status para Quitada.  
**Processo de Quitação da Venda:** Ao executar o processo de Quitar Contrato na tela de Edição de Vendas, caso exista resíduo pendente, o sistema então deve gerar automaticamente a parcela de resíduo sem quitar a venda, mostrando uma mensagem de que ainda existem parcelas para serem quitadas.  
**Observações:**  
- As soluções acima, não se aplicam para Resíduo com Deflação. - No caso de Resíduo Projetado onde ainda não há alteração de índice para a última parcela o sistema não fará a geração posterior da parcela de resíduo.
