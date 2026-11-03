---
article_id: 19491888987671
category: TAF - REINF
content_hash: 901aa8349ff6027f31568d1463dfcffcddca42dec66153620e2a990147b5a0c5
fetched_at: '2026-06-28T22:41:33.482791+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF  - Como incluir um pagamento
  com Dedução por Pensão Alimentícia?
type: support-article
updated_at: '2023-12-01T19:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19491888987671-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-incluir-um-pagamento-com-Dedu%C3%A7%C3%A3o-por-Pens%C3%A3o-Aliment%C3%ADcia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19491888951319) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Como incluir um pagamento com dedução por dependentes?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice Linha Protheus - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

1 - Preencher no cadastro do Participante no TAF os dados do Dependente:

![PLS 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491856437783)

2 - Além dos campos descritos na orientação:  [- TAF - REINF - Como integrar o evento R-4020 (Pagamento) manualmente no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14156667590167-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4020-Pagamento-manualmente-no-TAF-) deve ser preenchida também a aba de dedução no pagamento:

![pagto ded.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491904886167)

**Regras de preenchimento:**

* + Deduções (Preencher apenas se houver a previsão de deduções de impostos)
    - Tipo de Dedução (V4I\_TPDEDU) Preencher de acordo com as opções disponibilizadas no leiaute da EFD-REINF.
    - Valor Dedução (V4I\_VLRDED) do imposto que será abatida do valor do IR. Ao preencher este campo, os valores que serão retornados pelo governo no evento R-9005 será o valor do IR subtraído do Valor da dedução.
    - Valor Dedução Suspensa (V4I\_VLDEDS) - Informar valores de deduções que possuem exigibilidade suspensa devido a processo judicial.
    - Número da Previdência (V4I\_NUMPRE) - Número de Inscrição da entidade de previdência complementar. Necessário se Tipo Dedução igual 2, 3 ou 4.
    - Ente Previdenciário (V4I\_IENTID) - Possui informações da entidade de previdência complementar? S - Sim;N - Não. Informação obrigatória e exclusiva se {indTpDeducao} = [2, 3, 4]}.
    - Valor Funpresp (V4I\_VLFPRE) - Valor da contribuição do ente público patrocinador da Fundação de Previdência do Servidor Público (Funpresp). Informar somente se {indTpDeducao} = [4].
    - Beneficiário Pensão Alimentícia (Preencher somente nas situações em que o tipo de dedução = 5 ou 7)
      * Código do Dependente (V85\_CODDEP) - Informar o código do dependente cadastrado na rotina de cadastros de participantes (TAFA053 - Tabelas C1H e V3R).
      * Valor dedução (V85\_VALDEP) - Valor da dedução do dependente
  + Isenções (Preencher apenas nas situações em que existir isenção de imposto)
    - Tipo Isenção (V4J\_CDTPIS) - Preencher com o tipo da isenção de acordo com as opções disponibilizadas no layout da EFD REINF.
    - Valor da parcela Isenta (V4J\_VLRISE)
    - Descrição Isenção (V4J\_DRENDI) - Preencher quando tipo da isenção = 99 - Outros
