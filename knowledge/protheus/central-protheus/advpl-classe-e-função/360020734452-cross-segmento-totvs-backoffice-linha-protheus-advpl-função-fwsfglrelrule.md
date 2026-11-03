---
article_id: 360020734452
category: ADVPL - Classe e Função
content_hash: a98c8ef21a5ff7b8a05d424aa21c7dc36c8d48c704c13ce1686de0c672173212
fetched_at: '2026-06-28T22:40:16.757543+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função FWSFGlRelRule
type: support-article
updated_at: '2021-10-26T21:25:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020734452-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-FWSFGlRelRule
---

**Dúvida**Existe alguma função que traga as regras de privilégios de um grupo de usuários?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Neste caso pode utilizar a função FWSFGlRelRule, conforme sintaxe abaixo:

Esta função retorna os dados do relacionamento das regra de acesso com o grupo de usuários do sistema extraídos do arquivo de senhas ( SUPERFILE )

Parâmetros:

xSeek -> Id ou RecNo de identificação do grupo

Retorno:

aRule -> Array com o relacionamento da regra de acesso e o grupo de usuário. O array tem o seguinte formato:  
[1] RecNo da tabela  
[2] XML

**Saiba Mais****[Funções](http://tdn.totvs.com/pages/releaseview.action?pageId=212898493)**
