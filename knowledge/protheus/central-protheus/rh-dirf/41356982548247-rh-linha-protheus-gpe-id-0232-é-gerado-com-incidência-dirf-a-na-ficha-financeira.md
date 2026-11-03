---
article_id: 41356982548247
category: RH – DIRF
content_hash: d3c8f0b70680b4621eb0b26648d304f2fb2b1a872e99d1a62851f504763f6d1d
fetched_at: '2026-06-28T22:44:07.016499+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - ID 0232 é gerado com incidência DIRF "A" na ficha
  financeira mesmo quando configurado como "N"
type: support-article
updated_at: '2026-06-24T21:09:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41356982548247-RH-Linha-Protheus-GPE-ID-0232-%C3%A9-gerado-com-incid%C3%AAncia-DIRF-A-na-ficha-financeira-mesmo-quando-configurado-como-N
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41356982536599) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
ID 0232 é gerado com incidência DIRF "A" na ficha financeira mesmo quando configurado como "N"  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Foi realizado uma alteração na Ficha Financeira para sempre apresentar a incidência 1- DIRF com **'A',** para a verba com identificador de calculo **0232 (Inss Ferias Mes Seguinte).**  
A mudança permitirá que as verbas com Incidência de IR, sejam filtradas quando geradas como Planilha.

- Cadastro da verba de id 0232

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41395050747031)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41395050747671)

- Verba demonstrada na Ficha Financeira:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41467673179159)

A verba com identificador de cálculo 0232 pode aparentar estar sendo abatida do rendimento tributável, mesmo estando configurada com a opção “N”.   
Esse comportamento ocorre porque, no momento do fechamento da folha, as verbas de férias são lançadas de forma demonstrativa, contemplando tanto o pagamento quanto o desconto.   
Ao efetuar o fechamento da folha no mês inicial das férias, os valores correspondentes ao mês seguinte são apresentados na competência posterior como “Férias do mês”.   
Para garantir o correto abatimento dessas férias já quitadas, é gerada a verba “Férias pagas no mês anterior”. Essa verba considera o valor das férias do mês seguinte, deduzido do INSS sobre férias correspondente, com o objetivo de neutralizar os lançamentos.   
Dessa forma, como o valor do INSS sobre férias já foi abatido na verba “Férias pagas no mês anterior” na folha, esse mesmo valor deve ser igualmente abatido na DIRF, assegurando a consistência das informações.   
A explicação detalhada sobre esta tratativa, está nos vídeos do artigo abaixo:

[RH - Linha Protheus - GPE - Como conferir os rendimentos tributáveis da DIRF com férias mês e mês seguinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023944892-RH-Linha-Protheus-GPE-Como-conferir-os-rendimentos-tribut%C3%A1veis-da-DIRF-com-f%C3%A9rias-m%C3%AAs-e-m%C3%AAs-seguinte)

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/display/public/PROT/26623260+DRHROTPRT-27434+DT+Ficha+financeira)  
[RH - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
