---
article_id: 360061824993
category: Materiais - Compras (SIGACOM)
content_hash: 404065f06cda48a63eaf64504c6090af32cb120fb6838159e4bb2b6a5e20c8cc
fetched_at: '2026-06-28T22:41:13.017809+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  MATA235 -  Eliminação
  de resíduo não faz nada, não executada
type: support-article
updated_at: '2022-06-30T14:07:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061824993-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA235-Elimina%C3%A7%C3%A3o-de-res%C3%ADduo-n%C3%A3o-faz-nada-n%C3%A3o-executada
---

**Ocorrência**Ao executar a rotina MATA235 - eliminação de resíduo o existe não efetua a eliminação e não é exibida nenhuma mensagem de alerta ou erro.  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Possíveis Causas :**

1. Uma grande possibilidade, desta ocorrência é por conta da existência de "sujeira" no campo ***C7\_QTDACLA***, isso é derivado da alteração de casas decimais nos campos de quantidade, efetuar a limpeza no campo ***C7\_QTDACLA*** e executar a limpeza novamente.  
  
Para que isso não ocorra novamente deve revalidar as alterações de casas decimais que foram executadas, deixando o campo ***C7\_QTDACLA***, ***C7\_QUJE*** com a quantidade de casas decimais igual ao restante de campos de quantidade do sistema.

2. Data de Entrega do resíduo, diferente com a data do pedido :

![Entrega.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7137298028311/Entrega.png)

Pedido de Compras :

![dtEntre.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7137304192535/dtEntre.png)

![20220630_105249.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7137479456023/20220630_105249.gif)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
