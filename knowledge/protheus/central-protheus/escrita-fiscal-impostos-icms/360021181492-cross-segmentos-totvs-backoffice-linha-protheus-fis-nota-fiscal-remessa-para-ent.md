---
article_id: 360021181492
category: Escrita Fiscal - Impostos - ICMS
content_hash: 01bffc4ba46cde4fb38c91b04a9b9002c510018fbe40fc0aa0796e21460ba977
fetched_at: '2026-06-28T22:39:25.979247+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Nota fiscal remessa
  para entrega de simples faturamento
type: support-article
updated_at: '2022-10-26T13:46:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021181492-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-remessa-para-entrega-de-simples-faturamento
---

**Dúvida**Posso emitir nota fiscal de remessa para entrega futura com IPI na base do ICMS, sem destacar o IPI em campo próprio ?   
  
**Ambiente**Protheus - Faturamento - A partir da versão 11.80  
  
**Solução**

Criar uma TES especifica para Remessa de Entrega

Calcula icms = sim

L. fiscal icms = tributado

Calcula ipi = não

L. fiscal ipi = outros

Material de Consumo = Sim  
Ipi bs icms ( F4\_IPIVFCF) = 1=Nao;2=ICMS;3=ICMS/ST

Cod trib ipi = 99

Gera duplicata = não

Duplicata ST = não

**Parâmetro:**  
MV\_REMVFUT = "CFOP", deverá ser informado o CFOP da nota fiscal de ICMS Faturamento, por exemplo: "1111"

Assim o IPI será considerado na base de calculo do ICMS sem constar em campo próprio.
