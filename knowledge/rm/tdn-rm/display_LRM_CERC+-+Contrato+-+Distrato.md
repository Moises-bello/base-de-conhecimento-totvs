---
content_hash: f12cdf967093e7033e112302d11eaeee96b44798d35f7667618b26d08d13660a
fetched_at: '2026-06-29T00:11:32.768611+00:00'
page_id: '748067790'
product: rm
source: tdn-rm
title: CERC - Contrato - Distrato
type: documentation
url: https://tdn.totvs.com/display/LRM/CERC+-+Contrato+-+Distrato
version: 2
---

Ao distratar um contrato no TCGI o mesmo será enviado para a CERC com a seguinte informação, o Json irá com o campo tipoOperação igual a "AD" e com isso o contrato terá todas as parcelas canceladas.  
Quando o distrato tiver um fluxo de pagamento a devolver da incorporadora para o comprador ou mesmo a receber por parte do comprador o mesmo será tratado da seguinte forma:  
xxxxxxxxxxx  
  
No caso de distrato que venha a ser desfeito, o TCGI irá dispará o Json com o campo tipoOperação igual a "I" para inativar o contrato distratado na CERC e juntamente irá outro Json com os dados do contrato com o campo tipoOperacao igual a "C" para que o mesmo seja recriado no portal da CERC.
