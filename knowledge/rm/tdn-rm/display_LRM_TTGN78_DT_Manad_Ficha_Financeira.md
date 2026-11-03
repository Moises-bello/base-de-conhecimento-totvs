---
content_hash: 10c0bd9a82422daa1f7ad8caaed92f0884e17869e29b53baf23933a3404c6940
fetched_at: '2026-06-29T00:06:11.752359+00:00'
page_id: '203770725'
product: rm
source: tdn-rm
title: TTGN78_DT_Manad_Ficha_Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGN78_DT_Manad_Ficha_Financeira
version: 3
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
| **Chamados relacionados:** | *TTGN78* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
