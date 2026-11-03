---
content_hash: 37a6d1e925c702fef044ff2f0ec0fc6d20fdd5fb49372f65751a50658fb02e02
fetched_at: '2026-06-29T00:08:31.188880+00:00'
page_id: '273294920'
product: rm
source: tdn-rm
title: 470785 MSAU-6051 DT Permissões de Acesso na Tela de Faturamento de Remessa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273294920
version: 118
---

# Permissões de acesso na tela de faturamento de remessa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Perfis | Acesso a Menus |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Faturamento | Faturamento de convênios | |
| **Banco(s) de Dados:** | Oracle®, SQL Server® |

## Descrição

Foram criadas permissões de perfil, para limitar o acesso do perfil as opções de faturamento da tela de Faturamento para Convênios.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.102 da biblioteca do RM.

## Procedimento para Utilização

1. Acesse o cadastro de perfis do TOTVS Gestão Hospitalar e habilite as opção de faturamento localizados na arvore de acesso do menu de faturamento.
2. Em seguida, vincule o perfil à algum usuário do sistema.
3. Acesse o modulo TOTVS Gestão Hospitalar no menu Faturamento / Faturamento para Convênios.
4. Crie uma nova remessa ou acesse uma remessa já faturada.
5. Na tela de faturamento, as opções de faturamento devem estar habilitadas de acordo com permissões configuradas.

divs
