---
article_id: 360017781931
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 07588c5844a749179be01c38867f2c7155dc49eb62e25a1c4eda07d1be3cd664
fetched_at: '2026-06-28T22:42:02.337501+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Error log "type mismatch on +  on SPEDLC195(SPEDXFUN.PRW)"
type: support-article
updated_at: '2025-02-11T21:20:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017781931-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Error-log-type-mismatch-on-on-SPEDLC195-SPEDXFUN-PRW
---

**Ocorrência**Ao gerar o arquivo do Sped Fiscal o sistema está apresentando o error log:  
"type mismatch on + on SPEDLC195(SPEDXFUN.PRW)"  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
   
 **Causa** Esse incidente ocorre, pois o cadastro de Fórmulas (tabela SM4) ou Informações Complementares (tabela CCE) está incorreto ou não existe nas tabelas mencionadas.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
1. Procure no error log o campo **FT\_NFISCAL**;  
2. Identifique as notas fiscais que possuem o campo **FT\_FORMULA** OU **FT\_OBSERV**preenchido;  
  
![errorlog_type_mismatch_on____on_SPEDLC195_SPEDXFUN.PRW_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360013080271/errorlog_type_mismatch_on____on_SPEDLC195_SPEDXFUN.PRW_.gif)  
  
 3. Verifique se o cadastro da Fórmula ou Informações Complementares estão corretos na filial onde a nota fiscal foi lançada. O código da Fórmula (SM4) ou Informação complementar (CCE) deve existir nas respectivas tabelas.

Segue validação do fonte:

**If cMVSPDTC95 <> "4"**  
   
 **If cMVSPDTC95 $ "1|3" .And. !Empty((cAliasSFT)->FT\_FORMULA)**  
 **cMsgmCompl := (cAliasSFT)->(Formula((cAliasSFT)->FT\_FORMULA)+FT\_OBSERV)**  
 **Elseif cMVSPDTC95 $ "1|2"**  
 **cMsgmCompl := CCE->CCE\_DESCR**
