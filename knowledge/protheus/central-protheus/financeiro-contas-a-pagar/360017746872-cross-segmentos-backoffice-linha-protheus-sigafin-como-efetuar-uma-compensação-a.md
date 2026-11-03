---
article_id: 360017746872
category: Financeiro - Contas a Pagar
content_hash: 31a9a306e50b80a9df6fc218be316c106d68e81da472b5818d6c6eb7a66fc883
fetched_at: '2026-06-28T22:38:08.494882+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como efetuar uma compensação
  a pagar com imposto IRRF sendo gerado na baixa
type: support-article
updated_at: '2022-08-05T00:16:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017746872-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-efetuar-uma-compensa%C3%A7%C3%A3o-a-pagar-com-imposto-IRRF-sendo-gerado-na-baixa
---

**Dúvida**Como efetuar uma compensação a pagar com imposto IRRF é gerado na baixa?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**  
Seguem os parâmetros da serem validados no módulo Configurador:

**MV\_BXTXA = 2**

**MV\_PABRUTO=2**

**MV\_BP10925= 2**

**MV\_PAPRIME=1**

Nesse **exemplo**, será utilizado o valor de R$ 10.000,00 para ambos os títulos:

                                                                              IRRF

                                                                              1,50%

Valor do título:                 10.000,00            150,00

Valor Líquido do **PA** = 9.850,00 e um **TXA** de 150,00

Valor Líquido do **NF** = 9.850,00 e um **TX** de 150,00

Neste caso, serão gerados 2 títulos de **IRRF**: um do tipo **TX** e outro **TXA.**

Portanto:

1.Efetue na rotina de compensação **CP** **(FINA340)**, alterar F12 da rotina, pergunta **Compensa Títulos?** = Normal.  
2.Compense os títulos de **NF** e **PA**.  
3.Quando for fazer o pagamento, fazer o pagamento pelo **TXA**.  
4.Poderá ser baixado pela rotina **Baixas a pagar automáticas- FINA090**

**Importante:**A legenda ficará **Amarela**, mas poderá efetuar a compensação dessa forma.

Em seguida na rotina de compensação **CP (FINA340**), alterar F12 da rotina, pergunta **Compensa Títulos?**  = Impostos  
Compense os títulos de **IRRF**: **TX** e **TXA**, partindo do **TX**
