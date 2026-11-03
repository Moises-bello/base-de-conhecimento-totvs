---
article_id: 23060993444375
category: ADVPL - Classe e Função
content_hash: 562bb31cdf51ccff73902491da7cb79480d86c152d332e17339755f210b7bc44
fetched_at: '2026-06-28T22:40:15.842619+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: AjustaIndex:
  Falha ao Ajustar os arquivos Index do App'
type: support-article
updated_at: '2024-04-25T19:32:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23060993444375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-AjustaIndex-Falha-ao-Ajustar-os-arquivos-Index-do-App
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23061038967447) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Erro AjustaIndex: Falha ao Ajustar os arquivos Index do App  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para corrigir este erro deve ajustar o arquivo angular.json da forma abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23060993420695)

Após realizar essa configuração, deve ser gerado novamente o Build e validar se na pasta *dist/nome\_projeto* não foi criada nenhuma pasta com o nome browser.  
Com essa configuração, as próximas vezes que for gerar o Build já vai gerar as pastas na estrutura de pastas que esperamos.  
 **Saiba Mais**

[POUI](https://po-ui.io/)

[FWCallApp](https://tdn.totvs.com.br/display/public/framework/FwCallApp)
