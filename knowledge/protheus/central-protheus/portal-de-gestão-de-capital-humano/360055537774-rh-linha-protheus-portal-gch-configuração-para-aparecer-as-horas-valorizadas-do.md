---
article_id: 360055537774
category: Portal de Gestão de Capital Humano
content_hash: 49a7090d501d1fe098f34a0e6b50b686c988b1d051930a84591cb0b372be5a90
fetched_at: '2026-06-28T22:42:58.870490+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH -  Configuração para aparecer as horas valorizadas
  do Banco de Horas no Portal
type: support-article
updated_at: '2021-07-19T16:46:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055537774-RH-Linha-Protheus-PORTAL-GCH-Configura%C3%A7%C3%A3o-para-aparecer-as-horas-valorizadas-do-Banco-de-Horas-no-Portal
---

**Dúvida**Como configurar para aparecer as horas valorizadas no Banco de Horas do Portal GCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Essa melhoria foi implementada na versão 12.1.25 ou superior, mas poderão ser utilizadas nas versões 12.1.17 e 12.1.23, desde que o fonte EXTRABH.PRX esteja com a versão igual o superior a 07/05/2019 e seja feita a criação do parâmetro **MV\_IMPBHBX** manualmente no configurador.  
  
Acesse o link para informações do parâmetro: [Como configurar o parâmetro MV\_IMPBHBX](https://tdn.totvs.com/pages/viewpage.action?pageId=490635971)  
  
No Pacote Acumulado RH, consta a pasta RDMAKES, deverá copiar os arquivos EXTRABH.PRX, EXTRABH.ch e os arquivos com a extensão .TRES e colar na pasta Include e compilar esses arquivos.  
Saiba mais informações no artigo [Nova estrutura de tradução do Protheus - Arquivos .CH](https://tdn.totvs.com/pages/viewpage.action?pageId=181965465)  
  
![](https://p23.zdusercontent.com/attachment/888110/BIyx3hzTyWrsG6YWJVTbeJNzd?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..YNXEHUAt5N90MMEMmAjNTg.IJ5Qn8Hb7UbBkDuFgFCBgxHMUzodX7gmFmSvHn9hjzviwbFgzJE-mZbBpQPUzzQgX3jasGpY0FkNAFPGWIhzTBR8jzAXg3dyLcYS7FpK7nCy4nlHOClVxm4_XBFjlzsaD8wXKUdl-4JIqrP-A8rGr0tQ5LRUuBnaOPtgXz_rbina87KBsjcLwoqQgB4iwC6lEQa-3dASac6AZhDO_57mWj3EZGy8TFu7Nz-UNuBYxTriLSVrOCJq4U-oRp1Jsijop8hRVgB0LUkP0jHPtS1Me1_9_gIl_3Dr1Al40UCVz5E.B7R56iM9H7bzcxiKRmUNzQ)  
  
Após a compilação dos arquivos, será criado as colunas **Débt. Valorizado**, **Créd. Valorizado** e **Sal. Valorizado.** Segue link com mais informações:  
[Inclusão horas valorizadas do Banco de Horas no Portal](https://tdn.totvs.com/pages/releaseview.action?pageId=490635627)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096161413/mceclip0.png)  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções do Portal GCH:  
[Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
