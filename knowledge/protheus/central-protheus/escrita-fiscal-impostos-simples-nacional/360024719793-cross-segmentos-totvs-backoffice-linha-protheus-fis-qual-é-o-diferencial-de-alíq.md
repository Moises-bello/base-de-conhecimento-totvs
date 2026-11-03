---
article_id: 360024719793
category: Escrita Fiscal - Impostos - Simples Nacional
content_hash: 2b9fcf1d4a40cd25d84cec38f901b44117c6fe92bb93c9baba96193c3893885c
fetched_at: '2026-06-28T22:39:37.596283+00:00'
product: protheus
section_id: 1500001538461
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual é o diferencial
  de alíquota para o fornecedor optante pelo Simples Nacional?
type: support-article
updated_at: '2021-07-01T13:07:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024719793-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-%C3%A9-o-diferencial-de-al%C3%ADquota-para-o-fornecedor-optante-pelo-Simples-Nacional
---

**Dúvida**

Qual é o diferencial de alíquota para o fornecedor optante pelo Simples Nacional?  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Configuração do sistema:

**Fornecedor:**

Opt Simp Nac (A2\_SIMPNAC) = SIM

**TES:**

Calcula ICMS (F4\_ICM) = SIM

Material de Consumo (F4\_CONSUMO) = SIM

Markup ICMS Complementar (F4\_MKPCMP) = NÃO

Cons. Red. ICMS no Comp. (F4\_COMPRED) = NÃO

**Exceção Fiscal:**

Alíquota Interna (F7\_ALIQINT)= Alíquota do simples

Alíquota Externa (F7\_ALIQEXT) = Alíquota do simples

Uf Busca (F7\_UF\_BUSCA) = ORIGEM

Amarre a exceção ao **Cadastro do Produto**, campo **Grupo Trib** (B1\_GRTRIB) - informe o  grupo de tributação cadastrado no campo **GRUPO** (F7\_GRTRIB) da Exceção Fiscal.

Ou se preferir altere a alíquota do ICMS diretamente no documento de entrada no campo **Aliq. ICMS (D1\_PICM)**

**Exemplo:**

Nota valor de R$1000,00

Alíquota de ICMS: 3,1%

Valor de ICMS – R$31,00

ICMS diferencial de alíquota = (1000,00 \* 18%) – (1000,00 \* 12%)  = R$60,00
