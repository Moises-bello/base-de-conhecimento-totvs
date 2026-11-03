---
article_id: 360035081174
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 96b8f14d81505d2c9d83d5199c3fe560b0d476c7e0ed05468ad92f8e77212305
fetched_at: '2026-06-28T22:40:40.294841+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF TAFA433 - Compensação
  do Prejuízo
type: support-article
updated_at: '2023-11-13T15:47:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035081174-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-TAFA433-Compensa%C3%A7%C3%A3o-do-Preju%C3%ADzo
---

**Dúvida**Como faço para preencher as informações sobre a Compensação do Prejuízo para que possa ser visualizado na Simulação da apuração da rotina TAFA433:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046428373)  
  
**Ambiente**Protheus – Contabilidade Gerencial – 12.1.17 ou posterior  
  
**Solução**

Para a que o campo fique preenchido, deve-se verificar os seguintes pontos no TAF:

1- Primeiramente deverá verificar se houve prejuízo no período anterior e se esses lançamentos de Prejuízo estão cadastrados na rotina de Contas da Parte B (TAFA436):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045595014)

No exemplo acima, tenho no mês 01 o lançamento de 50 reais + 10 reais de saldo anterior, contendo no mês de Janeiro, 60 reais a serem compensados no mês 02.

2- Após verificar se o lançamento está correto, será necessário verificar se a conta verificada na rotina TAFA436 está corretamente preenchida na rotina TAFA433(Evento tributário), esta conta tem de estar alimentando a aba Compensação de Prejuízo/Base Negativa:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045595374)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045595514)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045595554)

\*Lembrando que todos os campos devem estar corretamente preenchidos para que gere os dados corretamente, principalmente o campo T0O\_EFEITO que é utilizado no filtro para buscar os dados do cadastro da parte B

3- Lembre também que para que a Compensação possa ser realizada, os valores da parte A do LALUR (Resultado Contábil) devem estar positivos.

4- Segue exemplo de como ficou preenchido o campo na simulação do exemplo utilizado nos campos acima:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045596954)

Veja mais:

[MP\_TAF\_LALUR COMPENSAÇÃO DE PREJUÍZO, PARTE B COM REFLEXO NA PARTE A.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037921673-MP-TAF-LALUR-COMPENSA%C3%87%C3%83O-DE-PREJU%C3%8DZO-PARTE-B-COM-REFLEXO-NA-PARTE-A-?source=search)

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)
