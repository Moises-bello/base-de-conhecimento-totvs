---
article_id: 21730726391319
category: Materiais - Compras (SIGACOM)
content_hash: 69242a47e6cefc374653386ffe3c2fe958bbd17da213ae2b750f8d829ba68abf
fetched_at: '2026-06-28T22:41:17.658696+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - error.log type mismatch
  on .AND. on IMPXTRA(COMXCOL2.PRW).
type: support-article
updated_at: '2024-06-07T18:35:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21730726391319-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-error-log-type-mismatch-on-AND-on-IMPXTRA-COMXCOL2-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21730718610583) Tempo aproximado para leitura: **00:02min****Ocorrência**Ao executar a o rotina **SCHEDCOMCOL** está sendo gerado o error.log **type mismatch on .AND. on IMPXTRA(COMXCOL2.PRW).**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Causa**O error.log é devido ao parâmetro MV\_XMLCAUT estar com o tipo de dados incorreto.  
  
**Solução**

* **Acesse o módulo do configurador:**

  + Consulte o parâmetro MV\_XMLCAUT está declarado e confirme que ele está definido como tipo caractere (C).
* **Atualize o parâmetro:**

  + Altere o conteúdo do parâmetro MV\_XMLCAUT para que seja do tipo lógico (L) em vez de caractere (C).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24034381234967)

* **Teste:**

  + Após fazer as alterações, teste o sistema para garantir que o problema foi resolvido.

***Saiba Mais :***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - "Ocorrências/Duvidas" X "Soluções" do Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20524264821655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncias-Duvidas-X-Solu%C3%A7%C3%B5es-do-Importador-XML-x-TOTVS-Transmite?source=search)
* [Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](http://xn--cross%20segmento%20-%20backoffice%20(linha%20protheus)%20-%20sigacom%20-%20integrao%20importador%20xml%20x%20totvs%20transmite-ulk18b/)
* [IX12 - Automação Cadastral - Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=773517403)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
