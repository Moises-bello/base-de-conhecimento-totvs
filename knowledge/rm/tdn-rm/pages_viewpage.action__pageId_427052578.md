---
content_hash: 990711a867baa2d552057c55dc421f2c6eb566da42200fe0dfab35bcaf7da88a
fetched_at: '2026-06-29T00:09:38.635880+00:00'
page_id: '427052578'
product: rm
source: tdn-rm
title: DT Nome social - Mensagens de notificação biblioteca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427052578
version: 4
---

# NOME SOCIAL - MENSAGENS DE NOTIFICAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | **TOTVS Gestão Bibliotecária** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mensagens de notificação | Mensagens de notificação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Reservas confirmadas, vencidas e canceladas | Reservas | | Sugestão de compras adquirida | Sugestão de compras | | Envio de e-mails de devolução prevista e atraso | Utilitário de envio de e-mails | | Envio de e-mails de área de interesse | Utilitário de envio de e-mails | | Envio de e-mails de texto livre | Utilitário de envio de e-mails | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | N/A |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | N/A |
| **Pacote:** | N/A |

## Descrição

Adaptação das mensagens de notificação para exibição do nome social, caso essa informação esteja cadastrada..

Mensagens que foram alteradas para considerarem a informação do nome social, no lugar do nome:

* Notificações gerais para usuários com áreas de interesse cadastradas;
  + Tags que receberam o tratamento: [NOMEUSUARIO]
* Informar aos usuários da biblioteca sobre reservas confirmadas;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
* Entrar em contato com usuários que possuem devoluções em atraso;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
* Informar aos usuários da biblioteca sobre devolução prevista;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
* Notificação geral (texto livre) para os usuários da biblioteca;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
* Notificação para usuários da biblioteca com reservas vencidas;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
* Informar aos usuários da biblioteca que suas sugestões de compra foram adquiridas;
  + Tags que receberam o tratamento: [NOMEUSUARIO].
