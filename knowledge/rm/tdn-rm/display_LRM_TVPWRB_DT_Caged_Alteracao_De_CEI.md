---
content_hash: e008ac73793cba23c5d498d6d7105d183c59f51c3e207b22cdf42e68491c3bed
fetched_at: '2026-06-29T00:08:19.363060+00:00'
page_id: '267782853'
product: rm
source: tdn-rm
title: TVPWRB_DT_Caged_Alteracao_De_CEI
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPWRB_DT_Caged_Alteracao_De_CEI
version: 110
---

# GERAÇÃO DO CAGED COM ALTERAÇÃO DE CEI

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Relatório CAGED* |
| **Situação/Requisito:** | *Quando o funcionário possuía ao longo do mês alterações de seções , onde era alterado o CEI das mesmas , e o resultado da busca de todos históricos do funcionário na tabela de histórico ( PFHSTSEC) era retornada com ordem diferente da ordem da data da mudança, o sistema não estava levando o funcionário nem no registro de admissão nem de demissão, não gerando CAGED assim para o mesmo.* |
| **Solução/Implementação:** | *Foi ajustado o sistema para ordenar o histórico de seção por data de mudança, mesmo quando o mesmo não vem ordenado desta forma, fazendo com que o sistema consiga encontrar as alterações de CEI e leve o registro do funcionário tanto como demissão na seção anterior quanto como admitido na nova seção.* |
| **Chamados relacionados:** | TVPWRB |

divs
