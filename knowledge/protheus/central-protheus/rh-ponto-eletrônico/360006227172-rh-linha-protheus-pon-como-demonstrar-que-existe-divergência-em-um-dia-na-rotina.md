---
article_id: 360006227172
category: RH - Ponto Eletrônico
content_hash: 98da1975d3ca9770f710f617c0f7b3f026f63b835dc4d63ef5facc921b9a39ea
fetched_at: '2026-06-28T22:44:58.204090+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como demonstrar que existe divergência em um dia
  na rotina de Integrados
type: support-article
updated_at: '2026-04-08T14:48:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006227172-RH-Linha-Protheus-PON-Como-demonstrar-que-existe-diverg%C3%AAncia-em-um-dia-na-rotina-de-Integrados
---

**Dúvida**Como demonstrar que existe divergência em um dia na rotina de Integrados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Qualquer evento que for calculado durante o período pode ser considerado como uma divergência a ser tratada, de acordo com o seu cadastro.   
O Protheus permite através da rotina de Integrados, que seja exibido um ícone no calendário mostrando ao usuário quais dias tiveram estes eventos gerados.  
  
Para isso, são necessários alguns passos:  
1 - No ambiente Configurador, opção **Ambiente/Cadastros/Parâmetros** , habilite o parâmetro MV\_DIVMNIN para S. Para verificar a ocorrência de divergências na Manutenção de Lançamentos Integrados. Conteúdo: **S** para verificar ou **N** para não verificar (padrão).   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408173297687)  
  
2 - No Ponto Eletrônico(SIGAPON), rotina: Atualizações/Cadastros Ponto/Eventos, selecione o evento de divergência (por exemplo: atrasos, faltas ou horas extras) e, em seguida, a opção Alterar, disponível no menu.

Na pasta Geral, localize o campo Divergência P9\_DIVERGE e selecione a opção Sim. Veja exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17379703910807)

Após todas as configurações, quando acessar a rotina de **Integrados** e o funcionário tiver um evento classificado como **Divergência**, o calendário será exibido com o ícone abaixo:  
  
Quando estiver o icone ![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381391179927) Indica que  a falta está para ser descontada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381417884183)  
  
Já quando estiver o ícone ![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381477584023)Indica que a falta está abonada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381476219415)

Nota: A nova coluna do calendário conterá um indicador de divergência conforme as situações:

A existência de eventos divergentes ou de marcação em quantidade ímpar será demonstrada pela legenda: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381569231383)

Quando um evento de apontamento divergente for abonado, informado ou apresentar uma quantidade informada, será apresentada a legenda:![](https://centraldeatendimento.totvs.com/hc/article_attachments/17381570622615)

Quando o usuário apontar novamente as marcações e não resultar em eventos divergentes, o dia não apresentará o indicativo de divergência, ou seja, nenhuma legenda apresentará com divergências.

Quando as marcações em quantidade ímpar deixarem de ocorrer e não estiver apontado evento divergente, o dia não apresentará o indicativo de divergência, ou seja, nenhuma legenda apresentará com divergências.   
  
**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=233744574>
