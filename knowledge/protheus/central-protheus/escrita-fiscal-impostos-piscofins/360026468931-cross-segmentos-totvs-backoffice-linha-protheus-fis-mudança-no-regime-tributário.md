---
article_id: 360026468931
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: c1299d0fdc67e3ce0e78f9357358320f16abc9a173806041388be1168a0a4cf3
fetched_at: '2026-06-28T22:39:36.950867+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Mudança no Regime
  Tributário (Lucro Presumido ou Lucro Real)
type: support-article
updated_at: '2023-05-10T21:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026468931-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Mudan%C3%A7a-no-Regime-Tribut%C3%A1rio-Lucro-Presumido-ou-Lucro-Real
---

**Dúvida**

Cliente precisa alterar o seu regime tributário, quais campos ou parâmetros são necessários para ocorrer essa mudança?  
  
**Ambiente**

Protheus - MATA080 - A partir da versão 11.80  
  
**Solução**Primeiramente deverá ser alterado o parâmetro MV\_CODREG para 3 pois dessa forma o sistema entende que a empresa não está enquadrada no Simples Nacional.  
  
No cadastro do TES deverá ser utilizar o campo Sit. Trib. (F4\_SITTRIB) para informar a CST da operação, ou seja, não deverá ser utilizado o campo Cod. Sit. SN (F4\_CSOSN).  
  
Para adoção de regime diferentes entre as empresas é necessário que o TES e os parâmetros sejam exclusivos para cada empresa. Não orientamos que sejam realizadas alterações nos TES existentes.

**Para que seja adotado o regime cumulativo ( Lucro Presumido) segue dados abaixo:**

**Parâmetros (Cadastro Configurador):**  
MV\_TXPIS - Onde será colocada a alíquota do PIS (0,65)   
MV\_TXCOFIN - Onde será colocada a alíquota do Cofins (3,0)

**Campos do TES:**Tp Reg (F4\_TPREG) = Regime cumulativo  
PIS/COFINS (F4\_PISCOF)= AMBOS  
Sit.Trib.Pis (F4\_CSTPIS) = 01 A 49 para saída e 50 a 66 para entrada  
Sit. Trib. COF (F4\_CSTCOF) = 01 A 49 para saída e 50 a 66 para entrada  
Cred PIS/COFINS (F4\_PISCRED)= NÃO CALCULA para entrada e DEBITA para saída.

**Para a adoção do regime não cumulativo (Lucro Real) segue dados abaixo:  
  
Parâmetros (Cadastro Configurador):**

MV\_TXPIS - Onde será colocada a alíquota do PIS (1,65)   
MV\_TXCOFIN - Onde será colocada a alíquota do Cofins (7,6)

**Campos do TES:**  
Tp Reg (F4\_TPREG) = Regime não cumulativo  
PIS/COFINS (F4\_PISCOF)= AMBOS  
Sit.Trib.Pis (F4\_CSTPIS) = 01 A 49 para saída e 50 a 66 para entrada  
Sit. Trib. COF (F4\_CSTCOF) = 01 A 49 para saída e 50 a 66 para entrada  
Cred PIS/COFINS (F4\_PISCRED)= Credita para entrada e Debita para saída.

Documentações referente PIS e COFINS Retenção e Apuração disponível em: 

Retenção:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6076816>

Apuração:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6076810>
