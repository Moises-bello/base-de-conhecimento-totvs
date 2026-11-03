---
article_id: 360043031714
category: Chão de Fábrica (SIGASFC)
content_hash: f979a64c5c1a775734c084405709739c5fdf53d48848c35191b8573072e29632
fetched_at: '2026-06-28T22:42:49.864638+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Indicadores do Chão de Fábrica
type: support-article
updated_at: '2022-04-01T13:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043031714-Manufatura-Linha-Protheus-SIGASFC-Indicadores-do-Ch%C3%A3o-de-F%C3%A1brica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura**: 00:04:25 min****Dúvida**Quais são os indicadores do **Chão de Fábrica** e como são calculados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**  
**Q - Qualidade**: Mede a conformidade da produção e leva em consideração apenas refugo.  
**Qualidade = (QtdReportada / (QtdReportada - QtdRefugada)) \* 100****Q\_Real - Qualidade Real**: Qualidade de primeira vez, onde não foi necessário uma operação de retrabalho para deixar a peça conforme. Leva em consideração refugos e retrabalhos.  
 **QualidadeReal = (QtdReportada / (QtdReportada - (QtdRefugada + QtdRetrabalhada))) \*100****E - Eficiência**: Desempenho entre o resultado real e o esperado, ou seja, **Tempos reais x Tempos padrões**. É a capacidade de um Sistema ou processo em alcançar seus objetivos.  
 **Eficiência = (TempoPadrão / TempoReal) \*100**Para cálculo de tempo a fórmula inverte, quanto menor o tempo de execução real, melhor. Na avaliação de unidades, quanto maior a produção, melhor.   
 **Eficiência = (Realizado / Planejado) \* 100****U - Utilização**: Relação de consumo da capacidade efetiva sem considerarmos a efetividade do mesmo, ou seja, horas reais trabalhadas, apontamento de produção sem considerar o tempo de preparação.   
  
Pode ser calculado de duas formas:

* **Sem Unidade Capacidade:**  
   **Utilização = (TempoOperação / CapacidadeReal) \* 100**
* **Com Unidade Capacidade:****Utilização = (ΣQuantidadeProcessada / CapacidadeReal) \* 100**

Onde:  
**QtdProcessada = (CapacidadeUtilizada / UnidadesOperação) \* (QtdPrevistaSplit / QtdReportadaSplit)****D\_Real - Disponibilidade Real**: Mede a disponibilidade baseando-se nas paradas realizadas, considerando-se as paradas efetivadas que não alteram eficiência.  
 **DisponibilidadeReal = CapacidadeReal / CapacidadeProjeto****D\_Planejada - Disponibilidade Planejada**: Mede a disponibilidade baseando-se nas paradas programadas. Para disponibilidade planejada leva-se em consideração a capacidade efetiva, sem considerar as paradas programadas. Então disponibilidade planejada é igual capacidade efetiva divido pela capacidade do projeto.  
**DisponibilidadePlanejada = CapacidadeEfetiva /CapacidadeProjeto****NEE - Net Equipament Effectiveness - Eficiência Líquida**: mede o desempenho do tempo em funcionamento da máquina, desconsiderando o fator disponibilidade real, como no **OEE**.  
**NNE = QualidadeReal \* Eficiência****OEE - Overall Equipment Efficiency - Eficiência Global Equipamento ou Eficiência Geral Equipamento**: Mede o desempenho global de um processo ou Sistema. É a relação entre a disponibilidade real - horas considerando as paradas efetivadas, qualidade real - qualidade de primeira vez e eficiência.  
**OEE = DisponibilidadeReal \* QualidadeReal \* Eficiência****TEEP - Total Effective Equipment Productivity - Performance – Produtividade Efetiva Total do Equipamento**: é recomendado para recursos críticos, pois representa a **Produtividade Efetiva Total** do **Equipamento**. Por se tratar de medição de recurso crítico, todo o tempo possível para produção é considerado como tempo disponível do recurso, inclusive paradas programadas; assim, este indicador apresenta o percentual de produtividade em relação ao tempo total do recurso  
**TEEP = DisponibilidadeReal \* QualidadeReal \* Eficiência \* Utilização****BTS - Build To Schedule - Atendimento do programa de produção**: tem como objetivo analisar a produção de acordo com o programado, avaliando a capacidade de produzir como o programado, respeitando volume, sequência e o mix de produtos.  
 **BTS = (Volume x Mix x Seqüência) / 10000  
  
BTS\_V - Atendimento do programa de produção em relação à Volume**:  
 **% Volume = (Unidades Produzidas / Unidades Programas) x 100**  
 **BTS\_M - Atendimento do programa de produção em relação à Mix**:  
**Menor = Menor entre Unidades Produzidas e Unidades Programas % Mix = (Unidades produzidas do Mix / MENOR) x 100****BTS\_S - Atendimento do programa de produção em relação à Sequência**:  
**% Seqüência = (Unidades produzidas na Sequencia / Unidades produzidas do Mix) x 100**  
  
**TK - Takt Time - Ritmo Produção**: Demonstra o tempo de ciclo ajustado a procura, onde apresentamos o ritmo de saída de um produto na produção. Aonde o resultado é expresso em minutos por peça.  
**TaktTime = (CapacidadeReal \* 60) / QtdReporte**
