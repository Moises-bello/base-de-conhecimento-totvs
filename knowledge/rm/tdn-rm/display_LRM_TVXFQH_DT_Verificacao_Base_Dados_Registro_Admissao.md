---
content_hash: 045bce1771d820ee4023ff495d3aba815c9c3608df6c6b0ad939f5a9f1c9c6a3
fetched_at: '2026-06-29T00:08:20.048476+00:00'
page_id: '267809966'
product: rm
source: tdn-rm
title: TVXFQH_DT_Verificacao_Base_Dados_Registro_Admissao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXFQH_DT_Verificacao_Base_Dados_Registro_Admissao
version: 110
---

# VERIFICAÇÃO DA BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Verificar Histórico de Situação com a data de admissão* |
| **Situação/Requisito:** | *Ao executar a verificação da base de dados não está validando se no histórico de situação existe um registro com a data de admissão.* |
| **Solução/Implementação:** | Ajustado a verificação da base de dados para validar se há histórico de situação com a data de admissão do funcionário, antes verificava apenas a quantidade de registros na tabela.  *Caso seja admitido por transferência será considerado a data de transferência.* |
| **Chamados relacionados:** | *TVXFQH* |

divs
