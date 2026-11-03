---
article_id: 4409368700311
category: RH - Provisão
content_hash: 123a8ee9503dc173a16f4ca4d66cece7d38acd7f041b158e07ebf4c1726ff2f6
fetched_at: '2026-06-28T22:43:56.900110+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona o calculo de médias de 13º na provisão
  quando o MV_M13ANOC esta sendo utilizado
type: support-article
updated_at: '2025-10-24T13:01:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409368700311-RH-Linha-Protheus-GPE-Como-funciona-o-calculo-de-m%C3%A9dias-de-13%C2%BA-na-provis%C3%A3o-quando-o-MV-M13ANOC-esta-sendo-utilizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32997911958679) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o calculo de médias de 13º na provisão quando o MV\_M13ANOC esta sendo utilizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Os valores de média de 13º na provisão, poderão ser  apresentados de acordo  com  preenchimento do parâmetro **MV\_M13ANOC:**

**Com "1 = Sim"** segue a configuração tradicional, média de décimo terceiro salário deve considerar somente as verbas no ano corrente;

**Com "2 =** Não" a rotina verificará a quantidade de meses indicada no cadastro da verba ou no cadastro do sindicato sem levar em conta se está buscando a verba no ano anterior à data de referência.

Configurando **o parâmetro MV\_M13ANOC** com o conteúdo "2" (Não), obtém-se a seguinte situação:

-Quantidade de meses para média, definido no:  
**Cadastro de Sindicatos.**  
Se houver uma rescisão no mês de fevereiro/2021, e se forem definidos os três últimos meses para média (campo "Meses Méd. 1º", na pasta "Médias"), o sistema localiza as verbas para média nos meses de Novembro/2020, Dezembro/2020 e Janeiro/2021.

-Quantidade de meses para média, definido no:  
**Cadastro de Verbas.**  
Se houver uma rescisão no mês de fevereiro/2021, e se forem definidos os seis últimos meses para média numa determinada verba (campo "Médias 13º", na pasta "Médias"), o sistema localiza as verbas para médias dos meses de Agosto/2020, Setembro/2020, Outubro/2020, Novembro/2020, Dezembro/2020 e Janeiro/2021.  
  
**Obs:** Este parâmetro (MV\_M13ANOC) só terá efeito quando o parâmetro MV\_MEDDIRE estiver como "N", indicando o cálculo pelo sindicato ou meses da verba.

**Saiba Mais:**[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias?source=search)  
[MP - GPE - Como conferir o adicional de provisão de férias, Verba com ID 0254](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006906071-MP-GPE-Como-conferir-o-adicional-de-provis%C3%A3o-de-f%C3%A9rias-Verba-com-ID-0254)
