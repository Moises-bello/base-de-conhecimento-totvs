---
article_id: 31123810204311
category: Rental by ItUp Business
content_hash: 6a964f70a380deee57842f4b8dcf7247d15906534bc5f34825302a3310a5a6bb
fetched_at: '2026-06-28T22:36:20.677058+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Pontos de entrada da rotina
  Orçamento (LOCA021).
type: support-article
updated_at: '2026-04-09T12:49:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31123810204311-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Pontos-de-entrada-da-rotina-Or%C3%A7amento-LOCA021
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31123810180887) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Pontos de entrada da rotina **Orçamento** (**LOCA021**)  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**

Lista dos pontos disponíveis na rotina **Orçamento** (**LOCA021**):

Os parâmetros de entrada de cada ponto estão disponíveis na documentação:

**[Pontos de Entrada - Locação - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=592556514)**

|  |  |
| --- | --- |
| **LCJLFQRY** | PONTO DE ENTRADA DESCONTINUADO |
| **LCJLFINI** | Ponto antes da geração do faturamento |
| **LCJTES** | Alteração da TES título antes da geração do faturamento |
| **LCJLFITE** | Alteração dos dados antes da geração do faturamento |
| **LCJLFFRT** | Manipulação do valor do frete antes da geração do faturamento |
| **LCJNAT** | Alteração da natureza antes da geração do faturamento |
| **LCJLFCAB** | Manutenção de campos no cabeçalho e itens, antes da geração do pedido de vendas no faturamento automático. |
| **LCJATZAG** | Alteração dos dados da tabela FPA, logo após o faturamento |
| **LCJATFIM** | Após a geração do faturamento |
| **LCJSER** | Alteração da série da nota fiscal de saída |
| **LCJF1VLD** | Valida se o faturamento pode ser realizado. |
| **LOCA021B** | Ponto de entrada logo após as perguntas do processamento do faturamento automático (não funciona para os jobs) |
| **LOCA021P** | Adiciona valores às colunas customizadas no Ponto de Entrada LOCA021Q na interface de Seleção dos projetos, quando a pergunta "Seleção?" está configurada como "Sim". Deverá sempre ser executado junto com o Ponto de Entrada LOCA021Q. |
| **LOCA021Q** | Adiciona colunas na interface de Seleção dos projetos, quando a pergunta "Seleção?" está configurada como "Sim". Deverá sempre ser executado junto com o Ponto de Entrada LOCA021P. |
| **LCJLFFIM** | Ponto de Entrada no Final do Faturamento Automático |
| **LOCA021C** | Ponto de entrada para alteracão dos dias fixos = 30 |
| **LOCA021D** | Ponto de entrada para alterar o período de locação gravado da SC6 |
| **LOCA021R** | Ponto de entrada para alteração dos parâmetros de cálculo |
| **CLIBLOQ** | Tratamento para bloquear a emissão de faturamento por cliente |
| **LCJATFPG** | Alterar dados da FPG - Custo Extra |
| **LOCA021A** | Alterar código e descrição do produto na FPG - Custo Extra |
| **LOCA061Z** | Alterar dados do pedido de venda no faturamento automático |
| **LOCA021E** | É possível validar antes do processamento do faturamento automático, os itens selecionados (locação, ou custo extra) |
