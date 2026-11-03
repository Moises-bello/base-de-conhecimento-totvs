---
article_id: 360045159334
category: RH - Provisão
content_hash: e37afae0496bd08c16c3ed830b9fc5c680382d933edb11fa6e6c3b43c998e024
fetched_at: '2026-06-28T22:43:55.955956+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Na coluna de adicionais de 13º na provisão está
  puxando o valor integral das médias no mês de Janeiro
type: support-article
updated_at: '2024-10-25T20:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045159334-RH-Linha-Protheus-GPE-Na-coluna-de-adicionais-de-13%C2%BA-na-provis%C3%A3o-est%C3%A1-puxando-o-valor-integral-das-m%C3%A9dias-no-m%C3%AAs-de-Janeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27338580000535) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Nos adicionais de 13º está puxando o valor integral das médias no mês de Janeiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Se o Mnemônico **P\_MEDDIREN** estiver configurado com **S**, o Total das Médias é calculado considerando os avos de Direito do Funcionário.

Para mais informações sobre o mnemônico [Clique Aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=224112471)

**Por exemplo**:

Em Janeiro funcionário recebe 5.000,00 de comissão, caso o mnemônico P\_MEDDIREN esteja configurado com S, as médias de pagamento serão 5.000,00 /1 = 5.000,00.

E assim por diante, caso haja soma dos valores nas médias sempre serão considerados os avos de direito para divisão.

Verifique no caso abaixo:

No mês 01/2020 referente a 13º funcionário tinha o valor 2.572,17 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063546373)  
  
No relatório de provisão apresenta exatamente o valor que ele tem no relatório de médias 2.572,17  quando se trata de 13º as médias são direito adquirido dessa forma a conta sempre vai ser o valor das médias dividido pelos avos de direito ou seja 2.572,17 dividido por 1 =2.572,17

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062656954)

Verifique que no mês 02/2020 no relatório de médias trouxe o valor para pagamento de 1.286,09 , o valor total 2.572,17 dividido pelos avos de direito no caso 2 ou seja 2.572,17 /2=1.286,08

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062657354)

No relatório de provisão do mês 02/2020 deverá vir o valor de R$ 1.286,09 na coluna de adicionais.

**Observação:** Só será dividido por 12 vezes os meses de direito os adicionais por tempo de serviço, periculosidade, insalubridade, adicional de transferência e cargo de confiança.

**Saiba mais:**

[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o) **[-](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)** [Provi](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)[são](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
