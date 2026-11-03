---
content_hash: 341e3496a3e0023d528db3fc3b0f23d249c0445017fcb9140c8e9c8b9a64c470
fetched_at: '2026-06-29T00:08:15.655552+00:00'
page_id: '244918105'
product: rm
source: tdn-rm
title: TVNGPM_DT_Cadastro_Banco_Agencia_Conta_Convenio_Mensageria_Unica
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNGPM_DT_Cadastro_Banco_Agencia_Conta_Convenio_Mensageria_Unica
version: 108
---

# CADASTRO DE BANCO/AGÊNCIA/CONTA CORRENTE/CONTA CAIXA/CONVÊNIO ATRAVÉS DE MENSAGEM ÚNICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Cadastro de Banco/Agência/Conta corrente/Conta Caixa/Convênio utilizando a mensagem única BANK 2.001* |
| **Situação/Requisito:** | *Com a utilização de um autoinc para o cadastro de convênio, o sistema apresentava um erro ao acessar a coluna IDCONVENIO, ao receber a mensagem*  *BANK 2.001.* |
| **Solução/Implementação:** | *Foi incluído um tratamento interno para evitar o acesso à colunas não encontradas e, também, foram removidos os parâmetros AUTOINCCONTACAIXA e AUTOINCCONVENIO* *para que o sistema, por padrão, trabalhe com a geração de auto incremento para o cadastro de conta caixa e convênio.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |
| **Versão Corrigida:** | *11.83.55* |
| **Versão Expedida:** | *11.83.55.246* |

divs
