---
article_id: 22173631868951
category: Materiais - Compras (SIGACOM)
content_hash: daf1239417c898ac4cf3ad70d3bd356a7961b5c8aa88828519047a611fc56b50
fetched_at: '2026-06-28T22:41:14.156028+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao incluir documento
  de entrada gera errorlog type mismatch on +  on A103GRVATF(MATA103.PRW)
type: support-article
updated_at: '2024-03-19T11:22:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22173631868951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-incluir-documento-de-entrada-gera-errorlog-type-mismatch-on-on-A103GRVATF-MATA103-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22173631865239) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao incluir um documento de entrada usando uma TES que atualiza um ativo fixo, sistema gera errorlog ***type mismatch on + on A103GRVATF(MATA103.PRW) 22/02/2024 11:00:30 line : 7791***

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Protheus Compras - Todas as versões  
  
**Solução**Abra o errorlog gerado e busque por MV\_CBASEAF, conforme print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22173631866007)

Verifique se o Conteúdo desse Parâmetro está entre Aspas Duplas. O Conteúdo do Parâmetro é armazenado no campo X6\_CONTEUD e, conforme podemos ver no print acima, ele está sem aspas duplas. Isso faz com que o sistema entenda que se trata de um parâmetro Numérico, porém é um parâmetro do tipo Caractere (X6\_TIPO = C). Para solucionar essa ocorrência, basta colocar Aspas duplas no Conteúdo do parâmetro, conforme exemplo do print  acima das demais linguagens do parâmetro em Espanhol e Inglês.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
