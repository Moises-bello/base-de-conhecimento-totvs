---
content_hash: a0008414c75152206db5d701bbe6bd7b7ff1d52589b343e95d9044fee3969f29
fetched_at: '2026-06-29T00:11:46.443774+00:00'
page_id: '822682242'
product: rm
source: tdn-rm
title: toma/end
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822682242
version: 3
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **end** | **DPS/infDPS/toma** | **Sim** | **Grupo** | **Grupo de informações relativas ao endereço do tomador da nota.** |
| endNac | DPS/infDPS/toma/end |  | Endereço nacional do tomador |  |
| cMun | DPS/infDPS/toma/end/endNac |  | Se estado for Nacional, preenche com o nome do município selecionado; senão, preenche com texto informado no campo de município. |  |
| CEP | DPS/infDPS/toma/end/endNac |  | CEP do Cli/For | CEP do tomador da nota. |
| endExt | DPS/infDPS/toma/end | Não | Endereço do exterior do Cli/For | Será preenchido se a flag "Nacional" do estado selecionado não estiver marcada. |
| cPais | DPS/infDPS/toma/end/endExt | Não | Código do país do Cli/For |  |
| cEndPost | DPS/infDPS/toma/end/endExt | Não | CEP do Cli/For | CEP do tomador da nota. |
| xCidade | DPS/infDPS/toma/end/endExt | Não | Descrição do município do Cli/For | Descrição do município do tomador. |
| xEstProvReg | DPS/infDPS/toma/end/endExt | Não | Código do estado do Cli/For | Código do estado do tomador |
| xLgr | DPS/infDPS/toma/end | Sim | Rua do tomador | Rua do tomador |
| nro | DPS/infDPS/toma/end |  | Número do Cli/For | Número do endereço do tomador |
| xCpl | DPS/infDPS/toma/end |  | Complemento do Cli/For |  |
| xBairro | DPS/infDPS/toma/end |  | Bairro do Cli/For | Bairro do tomador |
