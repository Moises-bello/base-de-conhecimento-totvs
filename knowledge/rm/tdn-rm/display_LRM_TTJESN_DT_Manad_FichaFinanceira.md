---
content_hash: 983d1777f60876f1440666efe5d4eb011701db2381039b5e95f8e2ca1a462cdb
fetched_at: '2026-06-29T00:06:11.855025+00:00'
page_id: '204964217'
product: rm
source: tdn-rm
title: TTJESN_DT_Manad_FichaFinanceira
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJESN_DT_Manad_FichaFinanceira
version: 1
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *MANAD.* |
| **Situação/Requisito:** | Ao gerar o MANAD para o funcionário com período de geração que ultrapassa a data do seu último movimento ocorre erro: System.Data.SqlClient.SqlException (0x80131904): The conversion of a varchar data type to a datetime data type resulted in an out-of-range value. |
| **Solução/Implementação:** | *Ajuste na sentença SQL que retorna os registros da ficha financeira do funcionário. Havia um tratamento referente a data de pagamento para os registros cujo código de cálculo fosse 62, 99 que estava causando o erro de banco de dados.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTJESN* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8.* |
