---
content_hash: 690783f8752b4928e291c97794f9682dd8f4d1e99e08266fa01cac6b5c988873
fetched_at: '2026-06-29T00:06:14.637414+00:00'
page_id: '210048246'
product: rm
source: tdn-rm
title: DT_Melhorias_Envelope_e_Rodape_Mdi
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhorias_Envelope_e_Rodape_Mdi
version: 4
---

# MELHORIAS DE USABILIDADE ENVELOPE .NET E RODAPÉ MDI

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Configurações* | *Envelope de Pagamento* | |
| **Versões/Release:** | *12.1.6* |

## Descrição

No Envelope de Pagamento do funcionário foi inserido campos de incidência de pensão.  
No Rodapé MDI uma barra de status exibe as informações da competência do RM Labore.

## Procedimento para Utilização **Envelope de pagamento**

Na tabela de eventos do envelope de pagamento tem os campos “Base Folha”, “Férias”, “13º Salário”, “Participação nos lucros”.

**Rodapé MDI**

Uma barra de status exibe as informações da competência do Totvs Folha de Pagamento como, mês da competência atual, ano da competência atual, mês caixa, descrição do período.

A barra de status é exibida apenas quando o sistema ativo for o Totvs Folha de Pagamento.

Ao atualizar através de qualquer processo ou tela do sistema alguma informação exibida pela barra de status, os valores devem ser atualizados automaticamente.

Rotinas que podem atualizar informações da barra de status:

-**Configurações / Parametrizador / Folha de Pagamento / Configuração da Competência.**

-**Configurações / Locais.**

-**Rotina de liberação de competência**
