---
article_id: 38103649458455
category: Folha Mensal
content_hash: 008c65ad6617e9c9c33b292e1d72546e734e1884b65459e98725ee7207e2c532
fetched_at: '2026-06-28T22:46:57.966204+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Diferença de centavos no teto do INSS'
type: support-article
updated_at: '2026-02-02T16:47:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38103649458455-RH-RM-FOP-Folha-Mensal-Diferen%C3%A7a-de-centavos-no-teto-do-INSS
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38103665781911) Tempo aproximado para leitura: **00:01:28 min**  
  
**Ocorrência**  
No calculo do INSS o teto está sendo 2 centavos a menos do previsto nas documentações. O valor calculado pelo produto é 988,07 quando na documentação é dito que o teto é 988,09.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Em conformidade com as diretrizes do eSocial, o produto não adota critérios de arredondamento no cálculo do INSS. Dessa forma, quando o resultado do cálculo apresenta mais de duas casas decimais, o valor é **truncado**, o que pode ocasionar a diferença anteriormente mencionada.

De acordo com o **Manual de Orientação do eSocial**, para fins de cálculo e totalização, o procedimento correto consiste na truncagem dos valores. Esse método reflete o comportamento oficialmente adotado pelo próprio eSocial nos eventos de retorno, tais como **S-5001, S-5002, S-5011 e S-5012**, conforme detalhado a seguir:  
"*Cabe destacar que para efeito de apuração dos valores tributados são consideradas duas casas decimais **sem arredondamentos**. O truncamento é realizado em todos os cálculos dos eventos totalizadores*".  
  
**Link da Consultoria de Segmento**: [eSocial - Arredondamento - Arredonda ou Trunca - Consultoria de Segmentos - TDN](https://tdn.totvs.com/display/public/ConSeg/eSocial+-+Arredondamento+-+Arredonda+ou+Trunca)
