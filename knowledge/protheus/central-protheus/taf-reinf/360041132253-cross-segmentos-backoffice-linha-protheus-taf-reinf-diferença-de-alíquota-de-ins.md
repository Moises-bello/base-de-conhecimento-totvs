---
article_id: 360041132253
category: TAF - REINF
content_hash: 096811d3b7db2b6c4328f19b0d59a5b6a1e36a4fa0a6225cd23fe7bd33096f5d
fetched_at: '2026-06-28T22:41:33.385088+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos -  Backoffice Linha Protheus - TAF - REINF -  Diferença de
  alíquota de INSS, 3,5% porém no site do e-cac registrou 11%?
type: support-article
updated_at: '2023-03-30T16:46:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041132253-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Diferen%C3%A7a-de-al%C3%ADquota-de-INSS-3-5-por%C3%A9m-no-site-do-e-cac-registrou-11
---

**Dúvida**Como solucionar a diferença de alíquota de INSS, 3,5% porém no site do e-cac registrou 11%?  
  
**Ambiente**  
Microsiga Prottheus – TAF – A partir da versão 12.1.17  
  
**Solução**A Receita Federal  não verifica a alíquota informada na nota fiscal de serviço, é verificado as informações do Participante, aplicando a alíquota correspondente e por estas informações define se o participante tem direito ao CPRB ou não.

No cadastro de participante ajustar o campo C1H\_CPRB (0 – Não é contribuinte da Contribuição  
previdenciária sobre a Receita Bruta –Retenção 11%) 1 – Contribuinte da Contribuição previdenciária sobre a receita bruta –Retenção 3,5%.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053566094/mceclip1.png)

Além do ajuste no cadastro de participante se faz necessário alterar a alíquota na nota fiscal de serviço nas rotinas TAFA062E para notas de entrada e TAFA062S para notas de saída.

Após alteração caso o período esteja fechado precisa-se reabrir o período Processando e Transmitindo o registro de reabertura R-2098.

Efetuar a apuração do evento R-2010 ou R-2020 e transmitir.

 Para integração correta ao TAF é necessário ajustar o cadastro de fornecedor no campo A2\_CPRB (Indicativo se o Prestador é contribuinte da CPRB, a qual reduz a alíquota de INSS).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053568674/mceclip0.png)

**IMPORTANTE:**

Quando a entrega do participante for por "CNO" é preciso que o campo **ON\_INDCPRB (Rotina MATA322)** esteja vazio assim respeitando o preenchimento do campo **C1H\_CPRB**, do TAF.

![CNO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12205065263255)

Informações adicionais:

<https://tdn.totvs.com/display/public/TAF/Painel+REINF>
