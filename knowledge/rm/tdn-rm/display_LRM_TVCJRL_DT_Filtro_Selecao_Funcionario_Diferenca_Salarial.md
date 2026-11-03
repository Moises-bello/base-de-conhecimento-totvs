---
content_hash: f678f5a82a1b9778614e9667cc7f549e9f5fef30e8eebaf26e2d5042b91b9c70
fetched_at: '2026-06-29T00:08:14.696573+00:00'
page_id: '244713156'
product: rm
source: tdn-rm
title: TVCJRL_DT_Filtro_Selecao_Funcionario_Diferenca_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCJRL_DT_Filtro_Selecao_Funcionario_Diferenca_Salarial
version: 117
---

# DIFERENÇA SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | Ao gerar a diferença salarial com um filtro de código da filial, por exemplo:   Campo: Código da Filial  Operador: =  Texto: []  Informando 1 no campo de execução do filtro e mandar executar o processo da diferença, o sistema apresenta o erro abaixo:  System.ApplicationException: Erro ao carregar dados dos funcionários: ---> System.Data.SqlClient.SqlException: Conversion failed when converting the varchar value "[Cód.Filial]" to data type smallint. |
| **Solução/Implementação:** | *Ajustado o preenchimento do filtro com parâmetros quando realiza a diferença salarial.* |
| **Chamados relacionados:** | *TVCJRL* |

divs
