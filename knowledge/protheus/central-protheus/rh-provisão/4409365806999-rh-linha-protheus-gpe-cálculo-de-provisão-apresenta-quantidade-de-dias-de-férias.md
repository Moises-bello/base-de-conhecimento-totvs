---
article_id: 4409365806999
category: RH - Provisão
content_hash: 87eb22af969ef09568edbd726e3bddfaf2ac33aa7eebd84431a805d8ce98eb92
fetched_at: '2026-06-28T22:43:55.667913+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Provisão Apresenta Quantidade de Dias
  de Férias Vencidas Diferente de 30 dias
type: support-article
updated_at: '2024-09-23T17:21:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409365806999-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-Apresenta-Quantidade-de-Dias-de-F%C3%A9rias-Vencidas-Diferente-de-30-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26566383187095) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao calcular provisão de férias para um funcionário que possui direito à férias vencidas, o sistema apresenta quantidade diferente de dias.   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Na tabela **S042** há a possibilidade de definir os cálculos de férias de acordo com regras específicas de Acordos Sindicais ou entendimento da empresa.

**Solução**Quando existe pagamento diferenciado para dias de férias de acordo regras específicas de sindicatos ou mesmo por ações coletivas e entendimento da empresa, o sistema permite a configuração através do preenchimento da tabela **S042.**Caso seja apresentada quantidade de dias de Férias Vencidas incorretamente nos cálculos de provisão, verifique se a tabela S042 - Tabrla Dias de Férias está configurada de forma indevida.

Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas **(GPEA320)** / Selecione a tabela S042 e clique em Visualizar ou Alterar. Caso não possua nenhuma regra específica para cálculo de férias, esta tabela não deverá conter informações.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409365930007)**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como realizar no módulo Gestão de Pessoal a configuração para calcular férias diferente de 30 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024062911-MP-GPE-Como-realizar-no-m%C3%B3dulo-Gest%C3%A3o-de-Pessoal-a-configura%C3%A7%C3%A3o-para-calcular-f%C3%A9rias-diferente-de-30-dias?source=search)

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
