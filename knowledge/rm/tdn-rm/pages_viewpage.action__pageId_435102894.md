---
content_hash: a6e3227a15ec79e1c616824a6a78160386ab61b66738426caef16189eb4366cf
fetched_at: '2026-06-29T00:09:45.937238+00:00'
page_id: '435102894'
product: rm
source: tdn-rm
title: 4039335 FISCAL01-6871 DT - Escrituração Fiscal - O índice fora dos limites
  da matriz
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435102894
version: 1
---

# Escrituração Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Escrituração de Lançamentos Fiscais |
| **Situação/Requisito:** | Ao realizar o processo de Escrituração migrado, foi apresentado erro:  *Erros ao Validar Movimentos*  *Movimento: 000587667*  *Erro: O índice estava fora dos limites da matriz.*  *Movimento: 000010015*  *Erro: O índice estava fora dos limites da matriz.* |
| **Solução/Implementação:** | Foi alterado a consistência que verifica a existência do Endereço de Entrega e Endereço de Coleta no Movimento.  *Obs sobre o erro:* O erro no processo de Escrituração Fiscal ocorria quando o Movimento havia sido parametrizado como CTRC porém sem Endereço de Coleta e Endereço de Entrega. |
