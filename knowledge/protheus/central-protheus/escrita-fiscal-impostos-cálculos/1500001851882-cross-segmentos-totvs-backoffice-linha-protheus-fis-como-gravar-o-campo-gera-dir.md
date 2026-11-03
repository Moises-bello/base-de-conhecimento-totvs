---
article_id: 1500001851882
category: Escrita Fiscal - Impostos - Cálculos
content_hash: caa98006cfe31410ae0de66adfc7928a439753fd42c0899d81b3ddcb72a5ad9b
fetched_at: '2026-06-28T22:39:30.676637+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como gravar o campo
  Gera DIRF( E2_DIRF)=Sim para PIS , COFINS, CSLL e IRRF , a partir da Nota Fiscal
  de Entrada
type: support-article
updated_at: '2021-07-29T14:39:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001851882-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gravar-o-campo-Gera-DIRF-E2-DIRF-Sim-para-PIS-COFINS-CSLL-e-IRRF-a-partir-da-Nota-Fiscal-de-Entrada
---

**Dúvida**

Como gravar o campo Gera DIRF( E2\_DIRF)=Sim para PIS, COFINS, CSLL e IRRF, a partir da Nota Fiscal de Entrada?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

Ao incluir  um documento de entrada, informar o campo Gera DIRF = Sim e também o código de retenção.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102735673/mceclip0.png)

Para que seja exibido a opção conforme imagem acima se faz necessário ativar o parâmetro **MV\_VISDIRF** 1=Habilita; 2=Não habilita (Default);

Com esse parâmetro ativo, deve-se incluir os códigos de retenção no momento de digitação da nota fiscal de entrada.

Os títulos do tipo Tx devem estar com o campo**E2\_DIRF**= **Sim**, e o título do tipo NF com o campo**E2\_DIRF**= **Não**.

Informações adicionais:

Retenção PIS, COFINS  e CSLL

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076816>

Retenção IRRF

<https://tdn.totvs.com/pages/releaseview.action?pageId=47908805>
