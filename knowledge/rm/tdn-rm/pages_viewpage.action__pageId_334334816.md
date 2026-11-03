---
content_hash: 8ffe8f3ad30e2ce548bfb3d57305a224f7b5008e34956d387a4d190e35a6ec20
fetched_at: '2026-06-29T00:08:50.412239+00:00'
page_id: '334334816'
product: rm
source: tdn-rm
title: 1193715 RMSAU-1677 DT Acesso Web Service Orizon Solicitação Procedimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334816
version: 4
---

# Acesso Web Service Orizon Solicitação Procedimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Agenda de Atendimento | | Registro de Atendimento (Guia / Autorização) | |
| **Parâmetro(s):** | Realiza a integração por web service da Orizon |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Ao solicitar procedimentos por autorização através de web service utilizando o registro de atendimento na aba de guia autorização, ou pela agenda de atendimentos o sistema vai se encarregar de enviar os procedimentos solicitados e retornar se o mesmo esta aprovado, negado ou em análise.

## Procedimento para Configuração

*(***CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospiralar (RM Saúde)**, acesse **Cadastros/Faturamento/Condições Contratuais com Convênios**. Selecione o convênio desejado e na aba Eletrônico ||| Tiss configure o parâmetro a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Realiza a integração por web service da Orizon |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Desmarcado |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar, acesse Atendimento/ Pronto Atendimento / Ambulatório / Registro de Atendimentos Externos.

O sistema apresenta a janela de Registro de Atendimento

       2.            Cadastre o atendimento para o paciente desejado utilizando um convênio previamente configurado para web service e com o parâmetro de integração Orizon marcado.

       3.            Na aba de Guia/Autorização adicione uma nova guia e clique no botão solicitação autorização TISS e confirme o processamento.

       4.            Sistema deve retornar a solicitação
