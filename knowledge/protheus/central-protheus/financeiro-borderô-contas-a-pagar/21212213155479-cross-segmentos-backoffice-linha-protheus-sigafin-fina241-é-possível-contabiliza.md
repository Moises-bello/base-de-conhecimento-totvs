---
article_id: 21212213155479
category: 'Financeiro - Borderô contas a Pagar '
content_hash: 9e3bc3e42bdea3d5ca880b095cc5604a1097e1f405598fc027c90a0aeef626b2
fetched_at: '2026-06-28T22:37:34.977106+00:00'
product: protheus
section_id: 35057529029143
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA241 É possível
  contabilizar off-line (CTBAFIN) pelo LP 531 no momento do cancelamento de borderô
  com impostos?
type: support-article
updated_at: '2026-03-25T19:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21212213155479-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA241-%C3%89-poss%C3%ADvel-contabilizar-off-line-CTBAFIN-pelo-LP-531-no-momento-do-cancelamento-de-border%C3%B4-com-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227234711) Tempo aproximado para leitura: 00:10:00 min  
  
**Dúvida**  
FINA241 É possível contabilizar off-line (CTBAFIN) pelo LP 531 no momento do cancelamento de borderô com impostos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Exemplo:

Tenho um título a pagar parametrizado para gerar os impostos Pis, Cofins e Csll (PCC) no momento da baixa do título (NF).

MV\_BX10925 = 1 Baixa

Porém em alguns cenários é usada a rotina "FINA241 - Borderô de pagamento de impostos" para provisionar os impostos sem que a NF seja baixada

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227235991)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227235991)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227236759)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227236759)

Neste momento os impostos serão gerados (provisionados), e a NF irá continuar em borderô

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227238039)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227238039)

Na rotina "FINA241 - Borderô de pagamento de impostos" não existe o pergunte <F12>  "Contabiliza online? sim ou não", logo a rotina sempre será chamado de forma on-line.

Mas existe como efetuar a contabilização de forma off-line, utilizando uma expressão em ADVPL para que o  sistema ao invés de posicionar em um campo exemplo SE5->E5\_VALOR no momento da chamada do "LP 530 - Lançamento Padrão Baixa a pagar", fazendo com que posicione ZERO, sempre que a rotina for "FINA241 - Borderô de pagamento de impostos", e neste caso o sistema não irá contabilizar de forma on-line sendo possível contabilizar de forma off-line (CTBAFIN)

Segue um exemplo de vários possíveis

IIF(FUNNAME() == "FINA241",0,SE5->E5\_VALOR)

Na rotina contabilizar off-line (CTBAFIN), neste momento consigo efetuar a contabilização da baixa e geração dos impostos através do  "LP 530 - Lançamento Padrão Baixa a pagar"

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213145111)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213145111)

Após a contabilização off-line (CTBAFIN), veja que o campo recebe o conteúdo E5\_LA=S.

Isso indica que o registro foi contabilizado.[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213146903)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213146903)

Agora iremos realizar o processo de cancelamento do borderô de impostos

Na rotina "FINA241 - Borderô de pagamento de impostos", ao cancelar

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227240343)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212227240343)

Será chamado o "LP 531 - Lançamento Padrão de Cancelamento de Baixas" de forma também on-line

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213148311)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213148311)

Neste caso será necessário sempre que seja efetuado a contabilização on-line do cancelamento do borderô de impostos, pois na tabela SE5 não é criado uma nova linha de estorno para que posteriormente consiga contabilizar de forma off-line

Com isso não poderá utilizar a mesma expressão em ADVPL da mesma forma que foi usado no "LP 530 - Lançamento Padrão Baixa a pagar" para o  "LP 531 - Lançamento Padrão de Cancelamento de Baixas"

É necessário que use uma expressão para se posicionar no campo E5\_VALOR  
Exemplo:  
IIF(SE5->E5\_MOTBX='PCC',SE5->E5\_VALOR,0)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213149207)](https://centraldeatendimento.totvs.com/hc/article_attachments/21212213149207)

Mais informações

[Borderô de Impostos (FINA241 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165366#Border%C3%B4deImpostos(FINA241SIGAFIN)-05.CONTABILIZA%C3%87%C3%83ODEBAIXASPORGERA%C3%87%C3%83ODEIMPOSTOS)
