---
content_hash: 8ef75bf473c21b933ddeab92e66fd3e4c451b22486ecb3c94de17e3ad19bd58b
fetched_at: '2026-06-29T00:08:06.962818+00:00'
page_id: '236598261'
product: rm
source: tdn-rm
title: TUUSD4_DT_Produdo_Nao_Pode_Repetir_Publicacao_Compras
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUSD4_DT_Produdo_Nao_Pode_Repetir_Publicacao_Compras
version: 117
---

# SOLICITAR COMPRA DE EXEMPLARES / CADASTRO PUBLICAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Solicitar compra de exemplares / Cadastro Publicação* |
| **Situação/Requisito:** | *Ao utilizar o processo "Solicitar compra de exemplares", o sistema não está permitindo adicionar um produto que já exista para uma publicação.* |
| **Solução/Implementação:** | *Foi identificado que o sistema faz uma validação para verificar se já existe o produto para alguma outra publicação, porém não foi encontrado nenhuma evidência da necessidade dessa validação para permitir somente um produto, sendo assim, a validação foi removida e o processo de "Solicitar compra de exemplares" é executado com sucesso a mesma validação também foi removida do cadastro de publicação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUW673* |
| **Requisito (ISSUE):** | *N/A* |

divs
