---
content_hash: 72173b169666c395a98f686db5938f77f5627c463419d72cf7e610a57ed50025
fetched_at: '2026-06-29T00:09:58.458044+00:00'
page_id: '452699686'
product: rm
source: tdn-rm
title: 4761574 FISCAL01-7686 DT Sped Fiscal - D190 - Campo 4
type: documentation
url: https://tdn.totvs.com/display/LRM/4761574+FISCAL01-7686+DT+Sped+Fiscal+-+D190+-+Campo+4
version: 2
---

# Escrituração Fiscal - Valor Situação Tributária

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Geração do SPED Fiscal |
| **Situação/Requisito:** | Na geração do SPED FISCAL, o registro D190 campo 4 (alíquota) não está sendo preenchido. |
| **Solução/Implementação:** | Foi efetuado o tratamento para o sistema zerar a alíquota do ICMS na geração do D190 quando a operação tributária for "Diferencial de Alíquota" e com os tipos de tributação "Isento", "Outros", "Sem ICMS", "Diferido, "Não Incidência" e "Suspenso". |
