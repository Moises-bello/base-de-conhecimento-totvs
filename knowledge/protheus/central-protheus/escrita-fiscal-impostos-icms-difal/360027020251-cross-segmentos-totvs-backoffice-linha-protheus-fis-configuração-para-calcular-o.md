---
article_id: 360027020251
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: aa093fad9fcbb03f68621f881b5357f1c339fb3845b18e3d7a8316571423fb89
fetched_at: '2026-06-28T22:39:19.295359+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  calcular o diferencial(DIFAL) de alíquota nas operações de compras base simples?
type: support-article
updated_at: '2024-02-09T14:54:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027020251-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-calcular-o-diferencial-DIFAL-de-al%C3%ADquota-nas-opera%C3%A7%C3%B5es-de-compras-base-simples
---

**Dúvida**

Configuração para calcular o diferencial de alíquota nas operações de compras base simples?  
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para calcular o diferencial de alíquota configuro o TES conforme abaixo:

Calcula ICMS (F4\_ICM) = SIM  
Material de Consumo (F4\_CONSUMO) = SIM  
Calc Dif ICM (F4\_COMPL) = SIM   
Livro Fiscal de ICMS (F4\_LFICM) = Diferente de não

Base simples

Valor da mercadoria = 1000,00  
Base de calculo do icms = 1000,00 \*12% = 120,00  
Diferencial de alíquotas = 1000,00 \*18% = 180,00-120,00 = 60,00

Exemplo

MV\_estado = PR

Fornecedor = MG

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17789208403991)
