---
content_hash: b46a243d7036f3dbd9556470aaa3d23b036b6dcbc79ca435e6ea4b468a58af3f
fetched_at: '2026-06-29T00:08:40.147829+00:00'
page_id: '286211100'
product: rm
source: tdn-rm
title: DT_205518_MATFATCMPCRM01-139_Manifestação_Destinatário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286211100
version: 101
---

# Manifestação do Destinatário

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Manifestação Automática* | MovMDeEnvioAutomaticoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Manifestação do Destinatário* | *MovMDeAction* | |  |  | |
| **Cadastros Iniciais:** | *Manifestação do Destinatário* |
| **Parâmetro(s):** | *Parâmetros -> 04.03 - Integrações -> 04.03.03 - Fiscal -> 04.03.03.01 - Dados Fiscais -> Parâmetros por Filial -> Manifesto Destinatário* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | 205518 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-139 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TMDE e TMDEEVENTHISTORICO* |
| **Sistema(s) Operacional(is):** | Windows |
|  |  |

## Descrição

Durante a manifestação automática da NF-e, o sistema realiza uma pesquisa na base de dados, procurando movimentos que possuem as chaves de acessos selecionadas na visão dos manifestos, caso sejam encontrados registros, automaticamente é enviado um evento do tipo "**210200 – Confirmação da Operação**’".

A informação referente ao movimento localizado na base de dados, que antes era salva no campo **TMDE.IDMOV**, a partir de agora será mantida no campo **Desc. Status do Evento** da tela de eventos "**TMDEEVENTHISTORICO.STATUSEVENTORESPDESC**", Exemplo:

**Importante:**No conversor da versão 12.1.18 está contido um script que será responsável por:

* Converter as informações do Movimento da tabela TMDE para TMDEEVENTHISTORICO.
* Excluir o campo IDMOV da tabela TMDE.

divs
