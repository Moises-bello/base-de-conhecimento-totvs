---
content_hash: 932a577cb55c002b29fd084da035e3b57e0a3911a8a5c0845d187806e71ce515
fetched_at: '2026-06-29T00:09:30.345270+00:00'
page_id: '425458435'
product: rm
source: tdn-rm
title: Pesquisa de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Pesquisa+de+Atendimento
version: 1
---

**Pesquisa de Atendimento**

---

**Na pesquisa de atendimento obrigar preenchimento do campo produto quando pesquisa por texto**   
   
Um dos critérios que existe disponível na pesquisa de atendimentos é a pesquisa por textos de acompanhamento. Esta pesquisa envolve encontrar um determinado texto (ou palavras) em um dos campos solicitação, discussão, solução. Tal recurso é muito poderoso e ajuda a encontrar problemas similares entre solicitações/chamados mas o ponto a se atentar com relação a seu uso é a possibilidade de queda de performance que ele pode gerar no sistema e até mesmo para outros usuários, isto porque sobrecarrega o banco de dados devido ao tipo dos campos que armazenam as informações de solicitação, discussão e solução.   
   
A fim de evitar que inadvertidamente alguns usuários utilizem este critério de pesquisa, gerem uma sobrecarga no banco de dados e penalize o desempenho para outros usuários, este parâmetro obrigado que o critério "produto" seja preenchido quando o usuário deseja utilizar a pesquisa por campos texto de acompanhamento, assim o sistema irá efetuar a pesquisa nos campos texto mas somente para atendimentos que possuem aquele determinado produto.
