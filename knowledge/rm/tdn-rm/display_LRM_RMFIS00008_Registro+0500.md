---
content_hash: 19f7329f268f1db3510a282fa85be654ef16f03e99e31f76b4505b7f19eccc9a
fetched_at: '2026-06-29T00:08:42.967683+00:00'
page_id: '301177480'
product: rm
source: tdn-rm
title: RMFIS00008_Registro 0500
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00008_Registro+0500
version: 6
---

# Assunto:

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.x |
| **Ocorrência:** | Geração do registro 0500 - Plano de Contas Contábeis |
| **Ambiente:** | Corpore RM |
| **Passo a passo:** | De acordo com o manual do EFD Contribuições o registro 0500 tem o objetivo de identificar as contas contábeis utilizadas pelo contribuinte em sua Escrituração Contábil, relacionadas às operações representativas de receitas, tributadas ou não, e dos créditos apurados.    **Geração do registro no TOTVS Gestão Fiscal**    O sistema irá buscar a conta contábil parametrizada nos Dados Fiscais do Produto.     * Cadastro | Produto | Anexos | Dados Fiscais do Produto - Campo Conta Contábil Sped.       OBS: Atualmente o sistema utiliza esse campo para geração do Registro 0500 e preenchimento dos campos 17-COD\_CONTA do registro A170 e campo 37-COD\_CONTA do registro C170.  A parametrização acima pode ser utilizada para geração do registro 0500 e preenchimento dos campos 37-COD\_CONTA do registro C170 e campo 23-COD\_CONTA do registro D100 da rotina **Sped Fiscal.**      Segue trecho do arquivo gerado.  |0500|01010001||A|3|0.1.1|Lucro do Exercício||| |
| **Observações:** |  |
