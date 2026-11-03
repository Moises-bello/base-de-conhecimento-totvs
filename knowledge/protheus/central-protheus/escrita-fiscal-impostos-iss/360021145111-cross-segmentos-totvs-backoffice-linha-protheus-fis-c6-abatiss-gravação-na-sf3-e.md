---
article_id: 360021145111
category: Escrita Fiscal - Impostos - ISS
content_hash: 6962e5412d402818b28ddde9b79218ad6a80d2657b979cfd35045dbd4d67051b
fetched_at: '2026-06-28T22:39:35.101856+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  C6_ABATISS - Gravação
  na SF3 e SFT
type: support-article
updated_at: '2021-06-17T12:23:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021145111-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C6-ABATISS-Grava%C3%A7%C3%A3o-na-SF3-e-SFT
---

**Dúvida**

O valor informado do Abatimento de ISS (C6\_ABATISS), onde é gravado na SF3 e SFT?

**Ambiente**  
Protheus – Pedido de venda  – Versão 12.1.17  
  
  
**Solução**

Ao informar o valor do abatimento do ISS no campo do pedido C6\_ABATISS, após da geração da nota fiscal, o valor do abatimento é informado no campo F3\_ISSSUB: Valor do abatimento na base de cálculo do ISS, calculado no faturamento do serviço, referente aos valores de subempreitada.

Em conjunto existe o parâmetro MV\_NFSEDED, nele devem ser informado o valor lógico .T. para somar o valor desconto em valor deduções ou .F. para não somar o valor do desconto em valor deduções.

Caso não exista este parâmetro em sua base, o mesmo devera ser criado manualmente conforme link abaixo:

Segue link:  **<http://tdn.totvs.com/display/public/PROT/TVRLDL_DT_NFSE_PARAMETRO_MV_NFSEDED>**  
  
Após criar o parâmetro conforme a documentação deste link , feche o sistema, abre novamente e realize novo pedido e transmissão desta nota fiscal.
