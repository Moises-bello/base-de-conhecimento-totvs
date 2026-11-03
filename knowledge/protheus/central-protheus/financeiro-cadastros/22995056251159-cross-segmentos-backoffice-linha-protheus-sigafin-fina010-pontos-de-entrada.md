---
article_id: 22995056251159
category: Financeiro - Cadastros
content_hash: 1208af55b2ce2b1a8351284046cd9eb196c52f8e962cf21b1dda564dae40be97
fetched_at: '2026-06-28T22:37:53.179906+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA010 - Pontos de
  entrada
type: support-article
updated_at: '2024-04-23T17:07:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22995056251159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA010-Pontos-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22995027156759) Tempo aproximado para leitura: **00****:05:00 min** **Dúvida**Quais os pontos de entrada da rotina FINA010 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**

Devido à necessidade de atualização do **cadastro de naturezas** para **MVC** e localização para os países **Brasil**, **Costa Rica**, **República Dominicana** e **México**, os pontos de entrada que existiam no programa **FINA010** (até a versão 12.1.16) foram descontinuados. Estes pontos de entrada eram:

**F010CAND** - Não documentado

**FIN010EXC** - <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6071270>

**FA010INC** - <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6071629>

**FIN010INC** - <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6071271>

**FA010ALT** - Não documentado

**FIN010ALT** - <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6071269>

**F10NATDEL** - <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6071396>

Todos os pontos de entrada acima citados e suas respectivas documentações foram descontinuados a partir da **versão 12.1.17**, devendo ser adotados os pontos de entrada padrão do **MVC**.

Para apoio na utilização dos pontos de entrada em **MVC**, seguir exemplos do link no saiba mais.

**Saiba mais:**[Pontos\_de\_Entrada\_do\_MVC\_na\_rotina\_de\_cadastro\_de\_naturezas\_FINA010](https://tdn.totvs.com/display/public/PROT/Pontos_de_Entrada_do_MVC_na_rotina_de_cadastro_de_naturezas_FINA010)
