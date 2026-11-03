---
article_id: 4412372487319
category: Financeiro - Contas a Receber
content_hash: ced0444d7313523d8b58f851b8b07e7f7718f3f7bb2a4fffd8651d3b20638f6a
fetched_at: '2026-06-28T22:38:12.832161+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA330 - Ao efetuar
  a compensação RA x NF com IR (Emissão) e PCC (Baixa) o sistema não compensa IR e
  sobra saldo de imposto de PCC
type: support-article
updated_at: '2021-11-05T19:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412372487319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Ao-efetuar-a-compensa%C3%A7%C3%A3o-RA-x-NF-com-IR-Emiss%C3%A3o-e-PCC-Baixa-o-sistema-n%C3%A3o-compensa-IR-e-sobra-saldo-de-imposto-de-PCC
---

**Dúvida**Ao efetuar a compensação RA x NF com IR (Emissão) e PCC (Baixa) o sistema não compensa IR e sobra saldo de imposto de PCC?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Financeiro- A Partir da versão  12

**Solução**No exemplo abaixo, se fizermos uma **baixa**/**compensação** parcial de R$ 984,00, vai sobrar R$ 16,00 de saldo na **NF**, sendo R$ 15,00 referente aos abatimentos (**IR**-) e R$ 1,00 pendente de baixa.  
No mesmo exemplo, se fizermos uma **baixa**/**compensação** total de R$ 985,00, o saldo do título principal vai zerar e, consequentemente, o abatimento (**IR-**) será baixado.  
Note que sobra R$ 0,01centavo de saldo no **título principal,** o abatimento ficará em aberto, até que o todo o saldo seja baixado.

**Exemplo:**NF de R$ 1000,00  
IR- de R$ 15,00  
Saldo para baixa/compensação: R$ 985,00

Quando um título é gerado com **imposto de renda** retido na emissão, é vinculado a ele um título de abatimento tipo **IR-** referente ao imposto. O saldo do título para baixa/compensação passa a ser o valor total menos o abatimento. Nesse contexto, o abatimento é baixado automaticamente pelo sistema quando o saldo do título principal zerar. 

**Importante**  
Portanto a causa o título principal fica com alguns centavos em aberto ao ser compensado e, consequentemente, o título **IR**- não é baixado.

Essa diferença de centavos entre o **RA** e a **NF** geralmente está relacionada ao arredondamento dos impostos. Se houver alguma dúvida sobre isso, os documentos abaixo podem ajudar:  
<https://tdn.totvs.com/display/public/PROT/FIS00024_Arredondamento_de_Impostos>
