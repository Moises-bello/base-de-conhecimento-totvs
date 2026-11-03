---
article_id: 360051168334
category: Portal de Gestão de Capital Humano
content_hash: 1d755af0093c3ba64be964635c4362f6ba0579175483551edf4dfbf99e495b86
fetched_at: '2026-06-28T22:42:59.252271+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Como efetuar substituição do aprovador do
  Portal em casos que esteja incapacitado de fazer a aprovação
type: support-article
updated_at: '2021-09-29T13:10:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051168334-RH-Linha-Protheus-PORTAL-GCH-Como-efetuar-substitui%C3%A7%C3%A3o-do-aprovador-do-Portal-em-casos-que-esteja-incapacitado-de-fazer-a-aprova%C3%A7%C3%A3o
---

**Dúvida**Como efetuar substituição do aprovador do Portal em casos que esteja incapacitado de fazer a aprovação?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Quando o aprovador (a) for desligado da empresa ou entrar de férias e precisar substituir a aprovação , poderá utilizar a rotina TCFA040 (Efetivar Solicitação) conforme orientações abaixo.  
  
Veja que o aprovador (a) é a *Lisa,* que possui algumas solicitações pendentes para aprovar ou reprovar:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079913454/mceclip0.png)  
  
O aprovador (a) foi demitido antes de efetuar as aprovações/reprovações do Portal:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080983833/mceclip1.png)  
  
Para alterar o aprovador (a), entre no módulo SIGAGPE (07) e acesse o menu: *Miscelânea > Portal Protheus > Efetivar solicitação > Subst. Aprovador.*Observação*:***Caso esteja utilizando uma versão anterior à 12.1.27 o grupo de perguntas deverá ser criado de forma manual no configurador. Caso esteja em uma versão superior ou igual a 12.1.27 a criação acontecerá automaticamente na atualização de release.**Para mais informações de como incluir o Grupo de Perguntas manualmente, acesse a documentação: [MP - PORTAL GCH - Qual o Grupo de Perguntas da Substituição do Aprovador do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051928453)  
 *![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079914574/mceclip2.png)*Será aberto a tela de Parâmetros: *![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079914734/mceclip3.png)*Preencha as perguntas de acordo com seu ambiente:  
 *![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079914934/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079915014/mceclip5.png)*Após preencher os parâmetros, confirme a configuração:   
 *![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079915034/mceclip6.png)*Será apresentado um log com o código das solicitações que foram substituídos pelo aprovador (a):  *![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079915074/mceclip7.png)*No módulo SIGAGPE, entre no Cadastro de Departamento (Atualizações > Cadastros > Departamentos) em que o aprovador estava e altere a "Matricula Responsável" para o novo aprovador:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007506602/mceclip0.png)Ao entrar no Portal com o login do novo aprovador (a), as solicitações do aprovador desligado foram alterados para o atual: *![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080985173/mceclip8.png)***Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
