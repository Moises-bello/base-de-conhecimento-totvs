---
content_hash: ec7454b66ea62b5cd31b535032876e01a44e74c7492e1db67213f3b21fff6662
fetched_at: '2026-06-29T00:10:53.882754+00:00'
page_id: '589507516'
product: rm
source: tdn-rm
title: Alterações S-1260
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589507516
version: 2
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1260 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {**ideAdquir**}: alterada condição. | O (se {indComerc} igual a [3, 7, 8]) N (nos demais casos) | F (se indComerc = [3, 7, 8]); N (nos demais casos) |
| Grupos {**ideEvento**}: Campo {indApuracao} Excluído |  | Campo excluído. |
| Grupos {**ideEvento**}: Campo {**indGuia**} incluído. |  | Indicativo do tipo de guia. Valores válidos: 1 - Documento de Arrecadação do eSocial - DAE. |
| Grupos {**ideEstabel**}: Campo {**nrInscEstabRural**} alterada validação. | Tamanho  15.  Preencher com o número de inscrição no CAEPF do estabelecimento rural. Validação: A inscrição informada deve constar na tabela de Estabelecimentos S-1005 | Tamanho  14.  Preencher com o número de inscrição no CAEPF do estabelecimento rural. Validação: Deve ser um número de inscrição válido e existente na Tabela de Estabelecimentos (S-1005). Se indGuia estiver preenchido, o número de inscrição deve possuir tpCaepf em S-1005 = [3]. |
| Grupos {**ideAdquir**}: Campo {**nrInsc**} Alterado tamanho | Tamanho  15. | Tamanho  11 ou 14. |
