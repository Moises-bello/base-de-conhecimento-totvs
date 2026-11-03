---
article_id: 20866411516567
category: Gestão de Transportes (TMS)
content_hash: f31ba2b6df6ac31a668ce5e751d16411c9a0ff8cab73759d680f127db6678698
fetched_at: '2026-06-28T22:45:27.363082+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Calculo de impostos no faturamento automático
  de documentos de apoio
type: support-article
updated_at: '2024-01-26T15:17:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20866411516567-Log%C3%ADstica-Linha-Protheus-TMS-Calculo-de-impostos-no-faturamento-autom%C3%A1tico-de-documentos-de-apoio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20866375689623) Tempo aproximado para leitura: **00:01:20 min****Ocorrência**No módulo **SIGATMS - Gestão de Transportes**, ao realizar o **Faturamento automático - TMSA491** de documentos de apoio, os impostos calculados estão incorretos no novo documento gerado.  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Esse incidente ocorre devido as parametrizações dos impostos do **TES - Tipos de Entrada e Saída - MATA080** utilizado nos documentos de apoio estarem diferente do **TES** utilizado para o novo documento gerado.  
  
**Solução**Para solucionar essa situação, o **TES - Tipos de Entrada e Saída - MATA080** utilizado nos documentos de apoio deve ser igual ao **TES** utilizado no documento de transporte gerado pelo **Faturamento automático - TMSA491** de documentos de apoio, com exceção apenas dos campos **L.Fiscal ISS - F4\_LFISS = Não** e **L.Fisc. ICMS - F4\_LFICM = Não**, que devem ser utilizados com esta parametrização apenas no **TES** dos documentos de apoio por serem documentos não fiscais.  
  
**Saiba mais**[Logística - Linha Protheus - TMS - Procedimentos para gerar o Documento de Apoio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034655553-Log%C3%ADstica-Linha-Protheus-TMS-Procedimentos-para-gerar-o-Documento-de-Apoio)  
[Logística - Linha Protheus - TMS - NFS-e Nota fiscal de Serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026010451-Log%C3%ADstica-Linha-Protheus-TMS-NFS-e-Nota-fiscal-de-Servi%C3%A7o)  
[Fatura de Documentos do Tipo Apoio (TMSA491 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=499356855)
