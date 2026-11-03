---
content_hash: 788c875915864f054b1271a62159920ee1bb309ab547f6c2588e0952d7c497e7
fetched_at: '2026-06-29T00:08:33.364673+00:00'
page_id: '274314698'
product: rm
source: tdn-rm
title: 672756 MATFATCMPCRM01-372 DT Permissão no DataServer MovMovimentoTBCData
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274314698
version: 107
---

# Segurança no DataServer MovMovimentoTBCData

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Consumo de DataServer através de WebService* | *MovMovimentoTBCData* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Permissões por Perfil de Usuário* | *GAUTZMENU* | |  |  | |
| **Cadastros Iniciais:** | *Perfil de Usuário*  *Movimento* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | 672756 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-372 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *GAUTZMENU e TMOV* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Com o objetivo de prover uma maior segurança ao utilizar nossos DataServers através de WebService, foi criado o item ***Integração com WebService do Movimento (MovMovimentoTBCData)*** em "Acesso a Menus" no cadastro de perfil de usuários. Este item será responsável por permitir a consulta de movimentos através do ReadRecord no DataServer **MovMovimentoTBCData**.

Além da melhoria acima, foi corrigida uma falha de segurança no sistema, a qual permitia que usuários **não autorizados** realizassem consultas no DataServer de movimento através do ReadRecord. Com este ajuste, o DataServer de movimento passa a considerar as permissões por tipo de movimento do cadastro de usuário, somente os usuários que possuem permissão para consultar determinado tipo de movimento estarão autorizados a utilizar o recurso.

divs
