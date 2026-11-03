---
article_id: 5815642144407
category: Encargos
content_hash: 77c49dc632cc92d09840a38997ab00387fed34dd2a03a20685389f4d4523b01f
fetched_at: '2026-06-28T22:46:53.131033+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Erro na Integração contábil "Não foi possível incluir o lançamento
  contábil no lote XXX pois existem partidas com o valor igual a zero"
type: support-article
updated_at: '2025-03-14T10:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5815642144407-RH-RM-FOP-Erro-na-Integra%C3%A7%C3%A3o-cont%C3%A1bil-N%C3%A3o-foi-poss%C3%ADvel-incluir-o-lan%C3%A7amento-cont%C3%A1bil-no-lote-XXX-pois-existem-partidas-com-o-valor-igual-a-zero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:31 min**

**Dúvida**Como realizar a correção do erro do erro apresentado durante a integração contábil "**Não foi possível incluir o lançamento contábil no lote XXX pois existem partidas com o valor igual a zero**"

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**Essa mensagem de erro é apresentada quando dentro do Lote Contábil existirem partidas com o valor 0 portanto, para conferência, deverá selecionar o Lote recém gerado e na aba Partida, validar se existe algum registro com valor zerado ou negativo, caso exista valor zerado, deverá excluir a partida. Segue a tela informada:

**![](https://totvssuporte.zendesk.com/attachments/token/FVxiIhxEguIFDcqgX01kV1YJ8/?name=inline148924605.png)**

Conforme exemplo acima, o terceiro registro está com o valor 0, então deverá realizar a exclusão do registro. Ao realizar esse processo o erro será corrigido.  
  
**Saiba mais**  
[RH - RM - FOP - Exclusão de lote contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001533881-RH-RM-FOP-Exclus%C3%A3o-de-lote-cont%C3%A1bil)
