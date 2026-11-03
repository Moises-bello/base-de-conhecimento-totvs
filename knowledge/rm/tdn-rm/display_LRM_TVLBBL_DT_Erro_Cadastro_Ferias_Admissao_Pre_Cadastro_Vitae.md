---
content_hash: c50996b182c7b7ee6ca3def5f090b1774a46b4076f36bd8782c824f848e7690a
fetched_at: '2026-06-29T00:08:15.637172+00:00'
page_id: '244917149'
product: rm
source: tdn-rm
title: TVLBBL_DT_Erro_Cadastro_Ferias_Admissao_Pre_Cadastro_Vitae
type: documentation
url: https://tdn.totvs.com/display/LRM/TVLBBL_DT_Erro_Cadastro_Ferias_Admissao_Pre_Cadastro_Vitae
version: 115
---

# CADASTRO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Férias* |
| **Situação/Requisito:** | *A*o admitir um funcionário que possui requisição de admissão vinda do RMVitae o sistema busca para os dados da admissão a data atual do sistema, pegando assim o dia / mês / ano /minuto/ segundo , assim inclui dentro da tabela PFUFERIAS os valores do início e fim do período aquisitivo com este formado de data.     Porém ao acessar o cadastro de férias o sistema não entende este formato de data e apresenta erro de referência de objeto. |
| **Solução/Implementação:** | *Ajustado o cadastro de férias quando há hora na data do período aquisitivo.*  *Foi ajustado para que ao finalizar este período aquisitivo o próximo fica sem essa informação de hora.* |
| **Chamados relacionados:** | *TVLBBL* |

divs
