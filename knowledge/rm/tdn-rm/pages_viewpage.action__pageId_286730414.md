---
content_hash: 9d7a9b9f72acfa08ffb71a7dab3896c9b94db73f9ca5b36a826fd9bf446212fb
fetched_at: '2026-06-29T00:08:41.478843+00:00'
page_id: '286730414'
product: rm
source: tdn-rm
title: RMCTB00003_Alteração do tipo de Conta Gerencial (Analítica/Sintética)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286730414
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Alteração do tipo de Conta Gerencial (Analítica/Sintética) |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo** Processo idealizado para correção de classificação incorreta de conta ou alterações quando da modificação da máscara gerencial:                  **Regras Gerais**  Para que o sistema aceite a alteração de uma conta gerencial, é necessário que a hierarquia do plano seja seguida, ou seja, a alteração de sintética para analítica e vice versa só é permitida se esta seguir a ordenação do plano a fim de manter a integridade do mesmo.  **Parametrização Necessária**  1 - Selecione ou edite a conta que deseja alterar. Ao selecionar ou editar, a conta em questão já aparecerá no filtro do processo:                              2 - Selecione a classificação da conta, conforme abaixo:                              3 - Após a execução a conta terá o valor alterado, conforme selecionado: |
| **Observações:** | Esta alteração somente será possível se a conta não estiver sendo utilizada em lançamentos contábeis ou em outros processos, por exemplo, uma conta contábil com a classificação analítica e que já teve movimentações (lançamentos salvos), não poderá ser alterada para sintética, somente após remover todos os lançamentos para uma outra conta conta contábil. |
