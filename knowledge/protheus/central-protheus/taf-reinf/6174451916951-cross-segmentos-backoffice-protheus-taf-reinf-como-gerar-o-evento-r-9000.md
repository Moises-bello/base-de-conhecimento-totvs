---
article_id: 6174451916951
category: TAF - REINF
content_hash: a129dfb9bb6863dc85bceecc48f6c9cf40082528d73c2ea355a3868b36978203
fetched_at: '2026-06-28T22:41:33.504158+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como gerar o evento
  R-9000
type: support-article
updated_at: '2023-04-04T12:07:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6174451916951-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-o-evento-R-9000
---

**Dúvida**Como gerar o evento de exclusão R-9000.   
  
**Ambiente**A partir da release 27  
  
**Solução**

Em cada evento, na tela de acompanhamento de transmissão, na aba **Autorizados**, irá aparecer a opção de selecionar o registro e o botão “Excluir Evento R-9000”.

Neste botão haverá 2 opções: Apenas "**Excluir**" ou "**Excluir e Transmitir**".

* Ao clicar no opção Apenas **Excluir**, será exibida uma mensagem para confirmar e prosseguir, através do transmitir no card R-9000 (conforme ilustração abaixo ).
* Ao clicar na opção **Excluir e Transmitir,** será exibida uma mensagem para confirmar e prosseguir, através do acompanhar no card R-9000.

![exclus_o_1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6173560573591/exclus_o_1.gif)

  Em todos os cards dos eventos, irão constar a propriedade "Excluídos" (responsável pela contagem do evento R-9000 pendentes e transmitidos), exceto nos de totalizadores (R-5001 e R-5011) e no próprio R-9000.

![exclus_o_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6173570104599/exclus_o_2.png)

#### **Como realizar a transmissão do evento**

  Caso o usuário tenha escolhido a opção 'Excluir e Transmitir', não será necessário executar esse passo.

Após a exclusão de algum evento transmitido, o próximo passo é voltar na tela inicial, consultar o período, clicar no card R-9000, opção pendentes e transmitir.

Importante: Na mesma grid é possível desfazer a exclusão ao invés de transmitir ([veja como desfazer a exclusão](https://tdn.totvs.com/display/TAF/Painel+REINF#PainelREINF-Comodesfazerumaexclus%C3%A3o) ).

![exclus_o_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6173625265303/exclus_o_3.gif)

#### **Como realizar a consulta do evento**

Após realizar a transmissão, o item sairá da grid, volte para o card R-9000 e clique em acompanhar.

Caso a consulta ocorra com sucesso o registro constará em transmitidos e autorizados.

![exclus_o_4.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6173640100887/exclus_o_4.gif)
