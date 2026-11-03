---
content_hash: daf3874a0d24269c81a70bcb4293fce4abdfa30f16ffa0930dbbe4cae7ccfcff
fetched_at: '2026-06-29T00:06:25.116844+00:00'
page_id: '224132319'
product: rm
source: tdn-rm
title: TUDAP3_DT_Permissão_Perfil_Exportar_Todos_Pedidos_Matrix
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224132319
version: 123
---

# Criada permissão de perfil para exportar todos os pedidos do arquivo Matrix

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Segurança | Permissão de acesso por perfil |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Unidade de Diagnóstico | Controle de pedido de exames | |
| **Parâmetro(s):** | O parâmetro de integração com o Matrix deverá estar ativado. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |

## Descrição

É necessário que somente alguns usuários específicos tenham permissão de imprimir todos os pedidos de exames do tipo de arquivo do Matrix. Foi criada permissão para que os usuários vinculados a um perfil tenham acesso a imprimir todos os pedidos de exames do arquivo Matrix.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão **12.1.9.003** do executável do RM Saúde.

## Procedimento para Utilização

1. Acesse o menu **Cadastros / Segurança / Perfis**.
2. Selecione um perfil.
3. Acesse a Aba “**Acesso a Menus**” e marque o parâmetro “**Exportar Todos Pedidos Matrix**”.
4. Vincule um usuário ao perfil configurado.
5. Acesse o Menu **Unidades de Diagnóstico / Controle de pedido de exames**.
6. Em seguida, clique em “**Troca de informações com o Matrix**”.
7. Verifique se estará habilitada a opção “**Exportar Todos os Pedidos**”.

divs
