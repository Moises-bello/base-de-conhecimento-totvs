---
article_id: 360041636893
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: f450b8feab194658386c9ed6747f15ede025fb9ce1271fdfae9ed1622b615eb6
fetched_at: '2026-06-28T22:39:36.877264+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o PIS
  e COFINS monofásico nas entradas
type: support-article
updated_at: '2021-06-24T12:52:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041636893-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-PIS-e-COFINS-monof%C3%A1sico-nas-entradas
---

**Dúvida**Qual a configuração para calcular o PIS e COFINS Monofásico?  
  
**Ambiente**Protheus - Compras – A partir da versão 12.1.17  
  
**Solução**

Seguem as configurações para PIS e COFINS monofásico nas entradas:

**TES:**

Aba Impostos  
Livro ICMS ou ISS = diferentes de Não -> Deve ser configurado campo de um dos livro com a opção diferente de não para geração dos valore de PIS COFINS nas tabelas SF3 e SFT.

Aba impostos:

PIS/COFINS (F4\_PISCOF) = Ambos   
Cred. Pis/Cof (F4\_PISCRED) = Calcula

ABA Outros  
Sit Trib Pis (F4\_CSTPIS)= 73  
Sit Trib Cof (F4\_CSTCOF)= 73
