---
content_hash: 18909ec9d80811bc4c24d0fe763f4a3f276edff61261fee5cae77ecfb94815f2
fetched_at: '2026-06-29T00:11:05.538499+00:00'
page_id: '632293895'
product: rm
source: tdn-rm
title: eSocial - Geração de evento de restituição de IRRF CC 122
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=632293895
version: 1
---

false

**A partir das Versões:**

* 12.1.29.292
* 12.1.31.207
* 12.1.32.144
* E superiores

# Objetivo:

---

       O objetivo deste documento é trazer informações de como enviar o evento S-1210 com um verba de restituição de IRRF.

---

**Passo 1**

Realizar o reenvio do evento com CC 122 - Restituição de I.R.R.F. para o eSocial. Ajustado a tag codIncIRRF para levar o codigo 31.

**Observação:** Pode ser incluido o evento manualmente lembrando somente de realizar o ajuste da competência.

**Passo 2**

Realize a geração dos eventos S-1200 e S-1210. Verifique que no envelope de pagamento foi lançada a verba de restituição de INSS.

**Atenção:**Não informar valores acima do desconto de IRRF ocorrido no mês ou em meses em que não ocorreram descontos de IRRF. O sistema não distribui o valor em outros meses.

S-1200                                                                                                                               S-1210
