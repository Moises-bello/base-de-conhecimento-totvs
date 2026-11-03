---
content_hash: f706c5855bb50b8925c471e188ae77c8cfb0850aab4146e333ca54ef40f548c7
fetched_at: '2026-06-29T00:06:28.889168+00:00'
page_id: '233764722'
product: rm
source: tdn-rm
title: TU8048_DT_Erro_Cancelar_Movimento_Servidor_AWS
type: documentation
url: https://tdn.totvs.com/display/LRM/TU8048_DT_Erro_Cancelar_Movimento_Servidor_AWS
version: 120
---

# CANCELAMENTO DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de Movimento* |
| **Situação/Requisito:** | Ao realizar o cancelamento de movimento gravando ocorre o erro: The network path was not found. Esse erro ocorre apenas no servidor AWS. |
| **Solução/Implementação:** | *Sistema passa a utilizar o atributo FileServerPath, referente ao config do host, para que seja informado onde o produto irá gravar o arquivo temporário no servidor.* |
| **Chamados relacionados:** | *TU8048* |

divs
