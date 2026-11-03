---
article_id: 360048215393
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 14cf0070b59bbbfe3e92b2b38606bfd8ae53b69d5ce11c7fb8e7f5e034ecfca5
fetched_at: '2026-06-28T22:39:20.395790+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como Configurar Decreto
  35.701/2010 de PE, cálculo diferenciado de ICMS ST com redução de ICMS próprio?
type: support-article
updated_at: '2022-08-02T13:53:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048215393-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-Decreto-35-701-2010-de-PE-c%C3%A1lculo-diferenciado-de-ICMS-ST-com-redu%C3%A7%C3%A3o-de-ICMS-pr%C3%B3prio
---

**Dúvida**Como Configurar Decreto 35.701/2010 de PE, cálculo diferenciado de ICMS ST com redução de ICMS próprio?  
   
 **Ambiente**Protheus - Fiscal - A partir da versão 11.80]  
  
**Solução**Conforme determinado no decreto 35.701/2010 para vendas (saídas) ocorridas para o estado de Pernambuco, deverá ocorrer uma redução do ICMS próprio no cálculo do ST.

No cadastro de produtos SB1 ou na exceção fiscal SF7, cadastrar o MVA, no nosso exemplo 50%

Cliente = PE

TES

Calcula icms = sim

L. fiscal icms =tributado

CST = 00

MKp icm comp = não

Marg solid = branco ou configuração

Perc. REd. PE = 41,18

O sistema possui um campo na TES chamado **Perc.Red. PE (F4\_PR35701)** que permite aplicar um percentual de redução sobre o valor do ICMS, no momento de subtraí-lo da base de ICMS ST, conforme determinado no decreto 35.701/2010 para vendas (saídas) ocorridas para o estado de Pernambuco.

Para melhor entendimento de seu funcionamento, abaixo segue memória de cálculo:  
  
Valor dos produtos........................................................R$ 10.000,00  
Total...............................................................................R$ 10.000,00  
ICMS normal destacado ( 10.000,00 x 7%).....................R$ 700,00  
CALCULO DO ICMS ST  
MVA 50,00%  
Base de cálculo (10.000,00 x 50,00%) .............................R$ 15.000,00  
ICMS S/Base(15.000,00 x 17,00%)....................................R$ 2.550,00  
ICMS próprio destacado a deduzir (700,00 x 41,18%).........R$ 288,26  
ICMS ST a recolher .............................................................R$ 2.261,74

Note que apenas na composição do cálculo do ICMS ST é que o ICMS próprio deve sofrer essa redução. (O percentual a ser informado é de acordo com a necessidade e legislação vigentes, sendo que o 41,18% foi utilizado apenas como exemplo)  
  
  
**Importante**  
Esta configuração será utilizada apenas quando a UF destino for **PE** e apenas ocorrerá na **saída**.
