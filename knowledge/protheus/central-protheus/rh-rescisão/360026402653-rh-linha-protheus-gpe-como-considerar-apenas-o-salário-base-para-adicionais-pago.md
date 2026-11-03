---
article_id: 360026402653
category: RH - Rescisão
content_hash: da6e41818aad157fef231eb8e0ecc7f82e705872040e7f2dc35541984b718a3b
fetched_at: '2026-06-28T22:43:52.041094+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como considerar apenas o salário base para adicionais
  pagos sobre verbas em verbas indenizatórias (mnemônico P_RESADISB)
type: support-article
updated_at: '2025-04-16T20:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026402653-RH-Linha-Protheus-GPE-Como-considerar-apenas-o-sal%C3%A1rio-base-para-adicionais-pagos-sobre-verbas-em-verbas-indenizat%C3%B3rias-mnem%C3%B4nico-P-RESADISB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31469237217559)**Tempo aproximado para leitura:**00:02:30 min**

**Dúvida**Ao calcular uma rescisão de um funcionário que recebe adicionais (periculosidade, insalubridade ou ATS) e esse adicional é sobre verbas, como fazer com que para as verbas indenizatórias (aviso prévio, 13º e férias), a base de cálculo do adicional seja apenas sobre o salário base, sem considerar as verbas que compõem esse adicional?  
  
**Ambiente**OTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Ao calcular a rescisão de um funcionário que recebe adicionais sobre verbas (periculosidade, insalubridade ou ATS), para que para as verbas indenizatórias (aviso, 13º e férias), os adicionais sejam pagos apenas considerando o salário base, foi criado o **mnemônico** **P\_RESADISB**, onde deve ficar com

**.T.** para que o cálculo seja conforme mencionado:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003542982)

Abaixo, exemplo onde funcionário tem periculosidade sobre verbas, então na rescisão a periculosidade sobre os dias trabalhados será calculada sobre o salário base mais as verbas que estão lançadas na rescisão e no cadastro delas esta com SIM para periculosidade:  
Salário base: 2000,00  
Periculosidade sobre salário base: 600,00  
Periculosidade sobre verbas rescisão: 662,63   
Base de cálculo para as verbas indenizatórias: 2600,00 pois como o mnemônico  P\_RESADISB esta parametrizado com .T., é considerada para as verbas indenizatórias a periculosidade apenas sobre o salário base (600,00), não a periculosidade sobre salário base + verbas (662,63):  
  
Periculosidade sobre verbas referente aos dias trabalhados:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040892694)  
  
Periculosidade apenas sobre salário base considerada para calculo das verbas indenizatórias ID 0673:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041723513)

Obs: O mnemônico citado deve interferir apenas no cálculo dos adicionais quando estes estão definidos para calcular sobre SALÁRIO + Verbas, ele não foi desenvolvido para utilização quando a base de cálculo é Salário Mínimo + Verbas.

****Saiba Mais:**  
Para adquirir maior conhecimento acesse o link abaixo:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
