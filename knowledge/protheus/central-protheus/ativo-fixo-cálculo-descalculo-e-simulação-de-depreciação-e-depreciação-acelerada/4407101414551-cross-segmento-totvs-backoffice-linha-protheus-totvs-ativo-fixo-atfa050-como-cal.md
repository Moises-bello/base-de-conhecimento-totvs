---
article_id: 4407101414551
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: dc4ee99808c72285d11be6749adca2f91e997e80dc24aa2642ee433bbf019bbe
fetched_at: '2026-06-28T22:41:43.344214+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento -TOTVS Backoffice Linha Protheus - TOTVS Ativo Fixo - ATFA050
  - Como calcular o PIS e COFINS sobre a depreciação do bem
type: support-article
updated_at: '2021-09-15T14:25:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407101414551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Ativo-Fixo-ATFA050-Como-calcular-o-PIS-e-COFINS-sobre-a-deprecia%C3%A7%C3%A3o-do-bem
---

**Dúvida**Como calcular o PIS e COFINS sobre a depreciação do bem?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Ativo Fixo- Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1. TES - Notas de Entrada:**

Atualiza ativo F4\_ATUATF= SIM  
PIS/ COFINS (F4\_PISCOF) = Ambos  
Cred.PIS/COF (F4\_PISCRED) = Credita  
Tp Reg (F4\_TPREG) = Cumulativo ou Não Cumulativo  
Sit. Trib. PIS (F4\_CSTPIS) = 50 a 66  
Sit. Trib. COF (F4\_CSTCOF) = 50 a 66  
L. Fisc. ICMS (F4\_LFICM) ; L. Fiscal IPI (F4\_LFIPI) ou L. Fiscal ISS (F4\_LFISS) = Preenchimento diferente de NÃO - Deve ser configurado o campo de um dos livros fiscais com opção diferente de NÃO, para geração dos valores de PIS COFINS nas tabelas SF3 e SFT.  
  
**2. Produto:**

Perc. PIS (B1\_PPIS) = Informe a alíquota  
Perc. COFINS (B1\_PCOFINS) = Informe a alíquota  
Para o cálculo do PIS COFINS apuração o sistema verifica primeiro as alíquotas informadas na exceção fiscal, após produto, caso não tenha alíquota, serão verificados os parâmetros MV\_TXPIS e MV\_TXCOFIN.  
  
**3. Fornecedor:**

Rec. PIS (A2\_RECPIS) = Não  
Rec. COFINS (A2\_RECCOFI) = Não

**4.Parâmetros:**

MV\_BSCREPC = 2 (2 = Valor de Aquisição do Ativo)

**5. MATA103:**

Incluir uma NF com os dados mencionado anteriormente.  
Verifique que a SF3 e SFT são preenchidas.

**6. ATFA240:**

Classificar o Bem.  
N1\_MESCPIS= 48 (exemplo)  
N1\_CALCPIS = 3 - Fração  
N1\_CODBCC= 09 = Crédito com Base nos Encargos de Depreciação

Incluir o tipo 01

**7. ATFA050:**

Calculo mensal

**8.FISA001:**

Realizar a apuração do Pis e Cofins.  
Verifique o valor da base de cálculo é a depreciação do bem cadastrado:

![](https://totvssuporte.zendesk.com/attachments/token/MnKhn3jGOL1hTsasOepK0ReVa/?name=inline467609907.png)

**Saiba mais:**  
Contabilização PIS/COFINS:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018783812>

<https://tdn.totvs.com/pages/releaseview.action?pageId=51253269>

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076810>
