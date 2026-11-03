---
content_hash: 7d118cc9cb7bdf096a9ee26d3c643594167426cda5b4cb85bd5f35ac201472e1
fetched_at: '2026-06-29T00:11:26.406566+00:00'
page_id: '716359406'
product: rm
source: tdn-rm
title: infoRecurso
type: documentation
url: https://tdn.totvs.com/display/LRM/infoRecurso
version: 1
---

## Detalhamento dos recursos recebidos/repassados.

| Registro/Campo | Registro Pai | Ocorr | Tam | Descrição | Origem RM |
| --- | --- | --- | --- | --- | --- |
| infoRecurso | recursosRec recursosrep | 1-N |  | Detalhamento dos recursos recebidos/repassados |  |
| tpRepasse | infoRecurso | 1-1 | 1 | Tipo de repasse, conforme tabela abaixo:  Valores Válidos: 1 - Patrocínio; 2 - Licenciamento de marcas e símbolos; 3 - Publicidade; 4 - Propaganda; 5 - Transmissão de espetáculos. |  |
| descRecurso | infoRecurso | 1-1 | 20 | Descrição resumida do recurso recebido. |  |
| vlrBruto | infoRecurso | 1-1 | 14 | Preencher com o Valor Bruto do repasse efetuado a título de patrocínio, publicidade, licenciamento, etc  Validação: Deve ser maior que 0 |  |
| vlrRetApur | infoRecurso | 1-1 | 14 | Preencher com o valor da apuração da retenção que deve sofrer a associação desportiva  Validação: Deve ser igual a 5% de {vlrBruto} |  |
