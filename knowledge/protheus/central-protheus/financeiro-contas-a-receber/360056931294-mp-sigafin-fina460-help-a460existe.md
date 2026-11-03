---
article_id: 360056931294
category: Financeiro - Contas a Receber
content_hash: 34f37834ec14c09491cfdf5b633e25bf4f4df1c1bd0db9b3d4b459f5dc699126
fetched_at: '2026-06-28T22:38:15.077792+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - FINA460 - Help: A460EXISTE'
type: support-article
updated_at: '2021-04-28T15:16:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056931294-MP-SIGAFIN-FINA460-Help-A460EXISTE
---

**Ocorrência**Ao realizar a uma liquidação através da rotina **FINA460** - Liquidações contas a receber é exibido o Help: **A460EXISTE**  
  
**Ambiente**Protheus – Financeiro – A partir da versão 11.80  
  
**Causa**Já existe na tabela SE1 um título com a chave primaria prefixo+número+parcela+tipo que está sendo utilizada na geração do novo título nos campos **FO2\_PREFIX**, **FO2\_NUM**, **FO2\_PARCEL** e **FO2\_TIPO** da tabela **FO2**.  
  
**Solução**Altere algum dos registros **FO2\_PREFIX**, **FO2\_NUM**, **FO2\_PARCEL** e **FO2\_TIPO** da tabela **FO2** para que a liquidação seja possível.
