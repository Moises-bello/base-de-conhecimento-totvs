---
content_hash: 0bbea125cb16deb8b7acf135bab71a85ca8596b08e485b0261ff4d8419cb30b8
fetched_at: '2026-06-29T00:10:53.838888+00:00'
page_id: '588687430'
product: rm
source: tdn-rm
title: Alterações S-1299
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=588687430
version: 5
---

false

**A partir das Versões:**

* 12.1.33.xxx
* 12.1.34.xxx
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1299 para o leiaute do eSocial Versão S-1.1.

Foi criado o campo **Possui Informações de pagamento de rendimentos do trabalho no periodo de apuração**  em RH | Folha de Pagamento | eSocial | Período de Apuração, ao selecionar esse campo o sistema irá gerar a nova tag evPgtos no evento S-1299.

**Observação:**

* Possui informações de pagamento de rendimentos do trabalho no período de apuração?  
  Valores válidos:  
  S - Sim  
  N - Não  
  Validação: Se for igual a [S], deve existir o evento S-1210 para o período de apuração, considerando o campo indGuia. Caso contrário, não deve existir o evento.
