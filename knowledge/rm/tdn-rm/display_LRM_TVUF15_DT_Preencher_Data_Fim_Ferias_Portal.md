---
content_hash: 4343da2f1368925be9026650c8de1973e3f60c0d4d91897efce80dacf753ce8c
fetched_at: '2026-06-29T00:08:20.020562+00:00'
page_id: '267808216'
product: rm
source: tdn-rm
title: TVUF15_DT_Preencher_Data_Fim_Ferias_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUF15_DT_Preencher_Data_Fim_Ferias_Portal
version: 110
---

# SUGESTÃO DE FÉRIAS PELO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Sugestão de férias* |
| **Situação/Requisito:** | Ao editar uma sugestão de férias no RM Portal, alterando a data de início de férias, após clicar em salvar, não está alterado a data fim das férias e sim quantidade de dias de férias informado no campo Dias de Férias.  Exemplo:    Antes de editar a data início:  Início das férias: 01/03/2016  Quantidade de dias:20  Fim das férias:20/03/2016    Foi alterado a data início para: 03/03/2016  Assim o sistema alterou a quantidade de dias de férias de 20 dias para 18 pois manteve a data final de férias no dia 20/03/2016.    Porém o correto seria as férias ficarem da seguinte forma:    Início das 03/03/2016  Quantidade de dias:20  Fim das férias:23/03/2016 |
| **Solução/Implementação:** | *Foi ajustado o sistema para que no momento em que a data início for preenchida e houver número de dias informado o sistema calcule automaticamente a data fim de férias e não que altere mais a quantidade de dias de férias.* |
| **Chamados relacionados:** | *TVUF15* |

divs
