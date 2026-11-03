---
content_hash: 2d08b8aa2eda56ee8941edda1cd4f95144fb74ea7ee06c369ebf4b2da78e8cdf
fetched_at: '2026-06-29T00:10:03.104868+00:00'
page_id: '452719007'
product: rm
source: tdn-rm
title: Transferência manual de registros da ficha financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719007
version: 3
---

Esta rotina realiza a transferência dos registros da ficha financeira (**PFFINANC**) para a ficha financeira complementar (**PFFINANCCOMPL**), conforme o parâmetro definido em:  
**Parametrizador | Folha Mensal | Ficha Financeira | Parametro "Meses a manter na ficha financeira"**, que determina a quantidade de meses que devem permanecer na PFFINANC.

**Atenção:**

Durante a transferência, é aplicada a seguinte validação:

* Para funcionários com situação diferente de **Demitido**, não são transferidos os registros da ficha financeira cujo período seja **igual ou posterior ao período aquisitivo em aberto** do funcionário.
