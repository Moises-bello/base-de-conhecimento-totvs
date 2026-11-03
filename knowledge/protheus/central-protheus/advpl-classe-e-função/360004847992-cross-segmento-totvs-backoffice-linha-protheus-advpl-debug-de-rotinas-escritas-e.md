---
article_id: 360004847992
category: ADVPL - Classe e Função
content_hash: 4c6a57355a4b7b043ffeeb5d88e151e0ef6745b25b1212997b461dbcf5272354
fetched_at: '2026-06-28T22:40:15.741272+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Debug de rotinas
  escritas em ASP/Portal
type: support-article
updated_at: '2021-05-21T17:56:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004847992-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Debug-de-rotinas-escritas-em-ASP-Portal
---

**Dúvida**Como  realizar o debug de fontes desenvolvidos em ASP ou Portal Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para debugar fontes ADVPL ASP

1) Marque as opções “Incluir informações de depuração em ADVPL ASP”, “Exibir conteúdo do ADVPL ASP progressivamente no Browser” e “Permitir depuração de múltiplas threads”;  
2) Adicione os pontos de parada no programa ADVPL ASP;   
3) Para debugar, ao invés de informar o nome da função informe um módulo qualquer, SIGAADV por exemplo e clique em executar;   
4) Acesse o Protheus e deixe o remote parado;   
5) Abra o Browser e execute a rotina ADVPL ASP;   
6) Ao executar a rotina o processo irá parar nos pontos de parada do fonte ADVPL ASP.

Atualmente temos a ferramenta de desenvolvimento TDS:

[TDS Versão 11.2](http://tdn.totvs.com/pages/viewpage.action?pageId=23200029)

[TDS Versão 11.3](http://tdn.totvs.com/pages/viewpage.action?pageId=189302040)

 No caso o funcionamento para o debug continua o mesma.
