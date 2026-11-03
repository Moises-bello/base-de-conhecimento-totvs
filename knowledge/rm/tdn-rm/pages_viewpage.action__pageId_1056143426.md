---
content_hash: 22001ad4dcb490c705991107b8f6bb326fa8191cd6aefabae2e0b4e0b7ac825e
fetched_at: '2026-06-29T00:05:51.908436+00:00'
page_id: '1056143426'
product: rm
source: tdn-rm
title: Grupo para o Imposto Seletivo (IS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056143426
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| impostois | [rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227) | G | 0-1 | Grupo para o Imposto Seletivo (IS) - Reforma Tributária |  | Não será gerado |
| codigo | impostois | E | 0-1 | Código |  | Não será gerado |
| Tributo | impostois | G | 0-1 | Grupo para referente aos tributos do Imposto Seletivo (IS) - Reforma Tributária. |  | Não será gerado |
| CSTIS | Tributo | E | 0-1 | CST IS. |  | Não será gerado |
| cClassTribIS | Tributo | E | 0-1 | Classificação Tributária IS. |  | Não será gerado |
| vBCIS | Tributo | E | 0-1 | Base Cálculo IS. |  | Não será gerado |
| pIS | Tributo | E | 0-1 | Alíquota IS. |  | Não será gerado |
| pISEspec | Tributo | E | 0-1 | Alíquota Específica IS. |  | Não será gerado |
| uTrib | Tributo | E | 0-1 | Unidade Tributável. |  | Não será gerado |
| qTrib | Tributo | E | 0-1 | Quantidade Tributável. |  | Não será gerado |
| vIS | Tributo | E | 0-1 | Valor IS. |  | Não será gerado |
