---
article_id: 360020897552
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 245acf1b8c5ef8d8566a25bea9e526fc816e971d03172685e70973d4eb4ff766
fetched_at: '2026-06-28T22:42:11.808046+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - NOVAGISS - A
  alíquota do ISS (campo VL_ALIQUOTA) não está sendo levada para o arquivo
type: support-article
updated_at: '2022-08-18T14:05:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020897552-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-NOVAGISS-A-al%C3%ADquota-do-ISS-campo-VL-ALIQUOTA-n%C3%A3o-est%C3%A1-sendo-levada-para-o-arquivo
---

**Dúvida**Por que a alíquota do **ISS**, campo **VL\_ALIQUOTA** da **NOVAGISS** não está sendo levada no arquivo magnético gerado?  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**A alíquota do **ISS** será levada para o arquivo magnético da **NOVAGISS**, campo **VL \_ALIQUOTA**, somente se o fornecedor for optante do **Simples Nacional**, onde o campo **A2\_SIMPNAC** deverá ser preenchido como a opção 1-Sim.

O fornecedor sendo do regime **Simples Nacional (A2\_SIMPNAC = SIM)** a informação do campo (**F3\_ALIQICM**) será levada para o arquivo.
