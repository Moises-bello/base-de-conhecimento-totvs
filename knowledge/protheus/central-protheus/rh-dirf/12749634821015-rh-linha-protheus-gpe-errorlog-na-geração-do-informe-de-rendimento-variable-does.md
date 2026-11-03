---
article_id: 12749634821015
category: RH – DIRF
content_hash: 5f2c22348fc39d7d0a69b8627611e5532fba84f7d71c85867254927100587004
fetched_at: '2026-06-28T22:44:07.003713+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error.log na geração do Informe de rendimento:
  variable does not exist LPULAHTML on U_IMPIRPF(IMPIRPF.PRX)'
type: support-article
updated_at: '2025-08-15T11:45:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12749634821015-RH-Linha-Protheus-GPE-Error-log-na-gera%C3%A7%C3%A3o-do-Informe-de-rendimento-variable-does-not-exist-LPULAHTML-on-U-IMPIRPF-IMPIRPF-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21386984779031) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Error.log na geração do Informe de rendimento: variable does not exist LPULAHTML on U\_IMPIRPF(IMPIRPF.PRX).  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Causa**Fontes IMPIRPF e IMPIRPJ estão desatualizados e compilados na utilização padrão da rotina.  
  
**Solução**Se for utilizada a rotina de impressão do Informe de Rendimentos padrão (sem customizações), **não** é necessário compilar os fontes IMPIRPF e IMPIRPJ, então descompile os fontes IMPIRPF e IMPIRPJ.  
  
Caso queira utilizar os *rdmakes* do Informe de Rendimento para customização, baixe os fontes atualizados do portal no *link* a seguir e realize a compilação do IMPIRPF e IMPIRPJ. Após a execução deste procedimento, o error.log deixará de ser apresentado:  
<https://suporte.totvs.com/portal/p/10098/download?e=1170810>

**Saiba mais**  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)   
[Layout DIRF 2024 - Receita Federal](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=134962)
