---
article_id: 360028341972
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c7eece2e364c4acdf6fb98b79093dcb04041d2049fbdcd5c432869ae07810bed
fetched_at: '2026-06-28T22:42:10.830109+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIMESC Registro
  47 está sendo gerado indevidamente
type: support-article
updated_at: '2022-08-17T20:20:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028341972-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIMESC-Registro-47-est%C3%A1-sendo-gerado-indevidamente
---

**Ocorrência  
  
Registro 47** da **DIMESC** não deve ser gerado no arquivo magnético.  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**  
Ocorre devido o campo  **Tp. Contr. Soc** (**A2\_TIPORUR**) estar preenchido.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique o campo **Tp. Contr. Soc** (**A2\_TIPORUR**) está preenchido para as operações com o **CFOP**;  
2. Se estiver preenchido, deixe o campo em branco e verifique se a geração do **Registro 47** persiste.
