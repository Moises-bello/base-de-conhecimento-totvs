---
article_id: 360036335714
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: b41acc2e18aa491b64c169907460b1070f53f3fc4aa6c8b4367a7b876b60ee6f
fetched_at: '2026-06-28T22:42:12.709791+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DRCST - Registro
  2120: Campo S_VL_BCST_INT deve ser maior que ''0'' (zero).'
type: support-article
updated_at: '2022-08-18T17:58:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036335714-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DRCST-Registro-2120-Campo-S-VL-BCST-INT-deve-ser-maior-que-0-zero
---

**Ocorrência**Ao validar o arquivo da DRCST são apresentados os erros:  
Registro 2120: Campo S\_VL\_BCST\_INT deve ser maior que '0' (zero).  
Registro 2120: Campo VLM\_UNIT\_BCST deve ser maior que '0' (zero).  
Registro 2120: Campo S\_VL\_ICMS\_ST deve ser maior que '0' (zero).  
Registro 2120: Campo VLM\_UNIT\_ICMS\_ST deve ser maior que '0' (zero).

**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta para o Cálculo da Substituição Tributária na entrada de NF.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Em caso de entrada de mercadoria adquirida do Substituto Tributário com ICMS Retido, CST do ICMS igual a 10, verifique se os campos FT\_BASERET e FT\_ICMSRET estão preenchidos na tabela SFT.

2. Em caso de entrada de mercadoria adquirida de fornecedor Substituído com ICMS ST recolhido anteriormente e CST do ICMS igual a 60, verifique se os campos FT\_BASNDES e FT\_ICMNDES estão preenchidos na tabela SFT.  
  
**Obs.:** Normalmente, o valor do ICMS ST recolhido anteriormente é informado no campo Informações Complementares da nota fiscal do fornecedor.
