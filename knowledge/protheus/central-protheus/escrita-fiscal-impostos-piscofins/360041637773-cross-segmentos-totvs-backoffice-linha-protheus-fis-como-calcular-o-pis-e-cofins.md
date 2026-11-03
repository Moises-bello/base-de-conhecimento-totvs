---
article_id: 360041637773
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 3c7c12199a74bad4d674690e9374c0962d26d7a1031669988e77b0ea91bdf011
fetched_at: '2026-06-28T22:39:36.879955+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o PIS
  e COFINS monofásico nas saídas
type: support-article
updated_at: '2023-07-06T19:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041637773-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-PIS-e-COFINS-monof%C3%A1sico-nas-sa%C3%ADdas
---

**Dúvida**Qual a configuração para calcular o PIS e COFINS Monofásico?  
  
**Ambiente**Protheus - Faturamento – A partir da versão 12.1.17  
  
**Solução**

Seguem as configurações para PIS e COFINS monofásico nas entradas:

**TES:**

Aba Impostos  
Livro ICMS ou ISS = diferentes de Não -> Deve ser configurado campo de um dos livro com a opção diferente de "NÃO" para a geração dos valores do PIS/COFINS na tabela SFT.

**OBS: A tabela SF3 será gerada normalmente, porém NÃO levará as informações do PIS/COFINS.**

**Aba impostos:**

PIS/COFINS (F4\_PISCOF) = Ambos   
Cred. Pis/Cof (F4\_PISCRED) = Calcula

**ABA Outros**  
Sit Trib Pis (F4\_CSTPIS)= 04 e 06  
Sit Trib Cof (F4\_CSTCOF)= 04 e 06
