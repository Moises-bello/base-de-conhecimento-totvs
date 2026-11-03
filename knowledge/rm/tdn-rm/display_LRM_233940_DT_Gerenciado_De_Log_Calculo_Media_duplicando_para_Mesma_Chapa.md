---
content_hash: 9fd7e12add51dee753af71dc396fa329daf2654b15a6965146cfa38e66748b7b
fetched_at: '2026-06-29T00:08:23.127790+00:00'
page_id: '269449281'
product: rm
source: tdn-rm
title: 233940_DT_Gerenciado_De_Log_Calculo_Media_duplicando_para_Mesma_Chapa
type: documentation
url: https://tdn.totvs.com/display/LRM/233940_DT_Gerenciado_De_Log_Calculo_Media_duplicando_para_Mesma_Chapa
version: 108
---

# Gerenciador de Log

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *TOTVS Folha de Pagamento.* |
| **Função:** | *Emissão de Logs de Calculo e Média.* |
| **Situação/Requisito:** | *Foi identificado que em base de dados em que a chapa se repete em N Coligadas e o Cálculo da folha é feito para N Coligadas gerando o mesmo Id De log de execução. No modulo de gerenciado de log tanto para Cálculo como para Média estava gerando N Logs para Mesma chapa.* |
| **Solução/Implementação:** | *Foi incluído a coligada na junção do Log com o cadastro de funcionário e o Período e com isso o sistema passou a emitir o log de Cálculo e Log de Média de forma especifica para chapa e coligada.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *233940.* |
| **Requisito (ISSUE):** | [MRH-3094](http://jiraproducao.totvs.com.br/browse/MRH-3094)*.* |

divs
