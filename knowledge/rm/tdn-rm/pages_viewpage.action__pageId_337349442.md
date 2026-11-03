---
content_hash: 36d22834dd6b6fe4a361ecffafd06cfbfa3c793c13d15c6c57db76e5503c614a
fetched_at: '2026-06-29T00:08:51.570339+00:00'
page_id: '337349442'
product: rm
source: tdn-rm
title: 'FISCAL01-2956 - NFS-e - TC 2.00 - Erro ao processar consulta dos arquivos
  Totvs Colaboração. Motivo: Elemento raiz inexistente.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337349442
version: 92
---

# NFS-e - TC 2.00 - Erro ao processar consulta dos arquivos Totvs Colaboração. Motivo: Elemento raiz inexistente

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Retorno de autorização da NFS-e |
| **Situação/Requisito:** | Ao consultar a autorização de um registro é apresentado a mensagem:  ***Erro ao processar consulta dos arquivos Totvs Colaboração. Motivo: Elemento raiz inexistente..***  Mesmo apresentando o erro, o status no RM mudou para Aprovado, porém o XML não carregou no registro.  Após foi efetuado a tentativa de cancelamento da NFS-e, porém ao consultar o mesmo é apresentado o erro:  ***"Erro ao processar consulta dos arquivos Totvs Colaboração. Motivo: Object reference not set to an instance of an object.."*** |
| **Solução/Implementação:** | Efetuadas evoluções na consulta de NFS-e do TOTVS Colaboração para que a consulta seja executada com sucesso mesmo se o Neogrid não retorne o XML da prefeitura. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | 1892408 |
| **Requisito:** | -- |

divs
