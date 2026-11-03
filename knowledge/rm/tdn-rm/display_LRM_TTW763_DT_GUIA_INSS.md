---
content_hash: 1ded36bdcb24a8cf3fd8236050c07a9592e5635ad70a93d2319a497be46ef004
fetched_at: '2026-06-29T00:06:20.914913+00:00'
page_id: '223159140'
product: rm
source: tdn-rm
title: TTW763_DT_GUIA_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTW763_DT_GUIA_INSS
version: 1
---

# GUIA INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | *Quando existe o evento 322 lançado no 13o. salário o sistema deduz o valor tanto na guia INSS de 13o. quanto na guia de folha normal.* |
| **Solução/Implementação:** | Ajuste na rotina de geração de guia de INSS para folha normal e 13o. para buscar os valores do evento e também lançar deduções corretamente. Ex: Lançado folha de 13o. salario contendo código de cálculo 322, o sistema agora deduz somente na guia de 13o. Quando lançado o evento 324 na rescisão, o sistema deduz somente da folha normal, e para casos de rescisão complementar onde exista diferença para licença maternidade, o sistema soma os valores das rescisões normal e complementar para dedução. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTW763 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
