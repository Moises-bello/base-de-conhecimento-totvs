---
content_hash: 1607481fd4d456e30784f3b9b2198b36c718bb0cf769788ca6141cdc6067da76
fetched_at: '2026-06-29T00:08:24.864150+00:00'
page_id: '270907748'
product: rm
source: tdn-rm
title: MRH-3257_DT_Erro_Salvar_Cadastro_Sindicato
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3257_DT_Erro_Salvar_Cadastro_Sindicato
version: 110
---

# ERRO AO SALVAR DADOS NO CADASTRO DE SINDICATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Sindicato* |
| **Situação/Requisito:** | *Erro “Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados" ao salvar dados no cadastro de Sindicato, quando a alteração ocorre nas tabelas detalhe da PSINDIC.* |
| **Solução/Implementação:** | *Ajuste na gravação de dados do Sindicato, que estava impossibilitando alterações nos registros das pastas de Média e Remuneração Base.* |
| **Chamados relacionados:** | MRH-3257 |
| **Requisito (ISSUE):** | MRH-3257 |

divs
