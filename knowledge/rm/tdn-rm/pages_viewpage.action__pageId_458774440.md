---
content_hash: e194eee8f22cfb285d13fa5c0e3324d09973d369dffac505f8c520e281b5ccbc
fetched_at: '2026-06-29T00:10:14.301745+00:00'
page_id: '458774440'
product: rm
source: tdn-rm
title: 4952845 FISCAL01-7995 - Escrituração Fiscal - Nota de Exportação com Remessa
  Simbólica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458774440
version: 4
---

# Escrituração Fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração Fiscal |
| **Situação/Requisito:** | No momento de escriturar uma nota de exportação o sistema está consistindo que a nota de remessa simbólica também seja escriturada retornando a seguinte mensagem:  \***"Movimentos relacionados ao item do movimento que se deseja escriturar, ainda não foram todos escriturados:"**\*  Conforme informado em documentação do produto dono do processo: É importante lembrar que esse Movimento tem a intenção de ser simbólico, e portanto não deveria possuir as seguintes opções:   * Integração com o Financeiro * Integração com a Contabilidade * Tributos * Preços * Faturamento * Escrituração   Portanto uma vez que a nota de remessa simbólica não foi emitida pelo cliente TOTVS mas precisa ter sua chave de acesso relacionada no XML de envio da exportação, entende-se que este movimento relacionado á exportação não deverá ser escriturado. |
| **Solução/Implementação:** | Foi adicionado uma consistência que valida se o parâmetro "**Remessa de Terceiros para Formação de Lote Simbólico**" está marcado no Tipo de Movimento, do Processo de Escrituração, para não escriturar os movimentos com essa parametrização. |
