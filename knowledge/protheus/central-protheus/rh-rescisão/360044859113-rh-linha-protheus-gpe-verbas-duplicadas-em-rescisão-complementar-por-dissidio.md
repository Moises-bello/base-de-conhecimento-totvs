---
article_id: 360044859113
category: RH - Rescisão
content_hash: a71942e61aeddd104995f7721a5bb2d5c023b2636ed671b6743b2841832ecdbe
fetched_at: '2026-06-28T22:43:54.497352+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas duplicadas em rescisão complementar por
  dissidio
type: support-article
updated_at: '2025-06-25T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044859113-RH-Linha-Protheus-GPE-Verbas-duplicadas-em-rescis%C3%A3o-complementar-por-dissidio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26440535248791)***Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Ao calcular rescisão complementar por dissidio, as verbas de encargos e suas bases estão duplicadas, sendo uma com origem G e outra com origem R  
  
**Ambiente**Microsiga Protheus - Gestão de Pessoal - A partir da Versão 12  
  
**Solução**As verbas de encargos (INSS, FGTS) e suas bases são duplicadas na rescisão complementar por dissidio pois as diferenças calculadas na rotina Dissidio Retroativo foram Geradas para Valores Futuros, e quando calculada a rescisão, o sistema busca essas verbas, e também calcula as diferenças apenas sobre as verbas rescisórias (saldo de salário, 13º na rescisão e demais verbas pagas na rescisão), então será feito o cálculo de INSS e FGTS sobre essas verbas com origem R separadamente.

Por isso no cálculo essas verbas estarão em duplicidade, sendo as com origem G vindas da rotina Dissidio retroativo que constam em Valores Futuros e as com origem R calculadas diretamente na rescisão conforme print abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061274433)

OBS.: Caso ao confirmar o cálculo sistema apresente mensagem de duplicidade, verifique a documentação abaixo:  
  
[MP - GPE - Mensagem: "Verificar o campo quantidade de lançamentos no cadastro da(s) verba(s) abaixo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205811)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
