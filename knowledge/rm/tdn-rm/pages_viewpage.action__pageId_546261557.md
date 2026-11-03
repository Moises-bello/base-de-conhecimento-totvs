---
content_hash: bf5daeb11516879101838415c8d5d30d9d8aa27a25c7a180cf80359cb4f47299
fetched_at: '2026-06-29T00:10:41.663472+00:00'
page_id: '546261557'
product: rm
source: tdn-rm
title: Mapa de Tipos de Movimento por Classificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546261557
version: 64
---

# Implementação do Mapa de Tipos de Movimento por Classificação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | MovMapaClassificacaoAction | Mapa de Tipos de Movimento por Classificação | |
| **Tickets relacionados** | -- |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O mapa de tipo de movimento por classificação permite localizar facilmente em qual menu cada movimento foi vinculado, o mapa permite fácil navegação assim como pesquisa pelo tipo de movimento além da opção de expandir e colapsar todo o mapa tornando seu uso simples e prático. 

O mapa também permite alterar a vinculação dos movimentos obedecendo as mesmas regras do parametrizador de movimento, esse recurso necessita concessão de permissão ao usuário enquanto a visualização é livre.

Esse recurso facilita para os novos usuários entender a localização de cada movimento no sistema, facilita implantações com uso de aceleradores ao permitir os usuário entender o mapa de tipos de movimento e suas classificações.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de 12.1.29.

## Procedimento para Utilização

-- Acessar o "Gestão de Estoque, Compras e Faturamento" → Utilitários → Mapa de Tipos de Movimento por Classificação.

O Menu estará disponível caso o usuário tenha permissão de acesso, a qual pode ser configurada através do Cadastro de Perfil de usuário → Acesso a Menus:

Através da Tela, é possível alterar a classificação do tipo de movimento, desde que o usuário tenha a permissão "09.05.01 - Alterar Classificação". Para alterar, basta arrastar o tipo de movimento para a classificação desejada.

divs
