---
content_hash: 4b9c635eee1a93f982bf7d11b3c1b630fbe34232d4f3036635042a8c07203535
fetched_at: '2026-06-29T00:09:01.161867+00:00'
page_id: '372551331'
product: rm
source: tdn-rm
title: 2990144 FINANCEIRO01-7372 DT Cancelamento de Acordo de Lançamento com Baixa
  Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372551331
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Cancelamento de Acordo |
| **Situação/Requisito:** | Ao cancelar um acordo de um lançamento que já tinha baixa parcial, o sistema não atualiza o valor líquido do registro. |
| **Solução/Implementação:** | Constatamos que o sistema sobrescrevia o valor parcialmente baixado ao executar o cancelamento de acordo. O defeito foi corrigido. Constatamos também que o cálculo se corrige se a baixa parcial for cancelada e novamente informada, de modo que é possível corrigir sem a necessidade de um script de ajuste. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 2990144 |
| **Requisito:** | FIN000166 |
| **Documento de Referência:** | Não se aplica |
| **Pacote:** | Informe o [linkdopacote] |
