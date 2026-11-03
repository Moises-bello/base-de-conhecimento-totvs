---
article_id: 24395450648983
category: Escrita Fiscal - Impostos - IR
content_hash: 25d19fc50e216d432ae5a1dd11f62a92b70eeb6ef01b548ed98838f94deb2177
fetched_at: '2026-06-28T22:39:31.930731+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – GROSS UP – Cálculo
  do IRRF em uma nota de importação de serviço.
type: support-article
updated_at: '2026-02-26T20:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24395450648983-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-GROSS-UP-C%C3%A1lculo-do-IRRF-em-uma-nota-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o
---

**Dúvida**Como criar uma nota de importação de serviço com cálculo do IRRF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

**Natureza**  
Calcula IRRF (A2\_CALCIRF) = Sim  
Percentual de cálculo de IRRF (A2\_PERCIRF) = 15%

**FORNECEDOR**  
Tipo (A2\_TIPO) = X – Outros  
Estado (A2\_EST) = EX  
Cálculo IRRF = 1 - Normal (calculo na emissão / 2 – IRRF Baixa (calculo no momento da baixa do NF no Financeiro)  
IRRF Prog (A2\_IRPROG)= Não  
Base Calc IRRF (A2\_GROSSIR) = 1 / 2 / 3

**1**=Imp. Serv. IRRF: Esta opção o sistema fará o Gross UP na base de cálculo do IRRF e na base de Cálculo do PIS e COFINS Importação.  
**2**=Imp. Serv. IRRF + CIDE: Com esta opção o sistema fará o Gross UP na base de cálculo do IRRF, do PIS Importação, Cofins Importação e também na base de cálculo da CIDE.  
**3**=Imp. Serv. IRRF + Val. Serviço: Com esta opção o sistema fará Gross UP na base de cálculo do IRRF, PIS e COFINS importação e também no valor do Serviço, consequentemente alterando a base de cálculo do CIDE, do ISS, do total da nota e do valor da duplicata.

**PRODUTOS**  
Impos Renda (B1\_IRRF) = Sim  
Redução de IRRF (B1\_REDIRRF) - Caso haja redução

**TES**   
Gerar Duplicatas (F4\_DUPLIC) = Sim  
Calcula ISS (F4\_ISS) = Sim  
CFOP (F4\_CFO) = iniciando com 3

**Boletim técnico:**  
[IRRF - GROSS UP - Cálculo do IRRF na Importação de Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=646677931)   
[Cálculo do IRRF na importação de serviço Gross UP](https://tdn.totvs.com/pages/releaseview.action?pageId=354451487)
