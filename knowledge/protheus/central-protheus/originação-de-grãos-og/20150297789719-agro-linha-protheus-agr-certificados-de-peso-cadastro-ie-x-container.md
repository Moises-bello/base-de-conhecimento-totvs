---
article_id: 20150297789719
category: Originação de Grãos (OG)
content_hash: 24e9ef43f09ccfb7700200235e02644bea20a78ac0c1e2bf44b6f3dafd517992
fetched_at: '2026-06-28T22:45:37.523703+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Certificados de Peso  Cadastro IE X Container
type: support-article
updated_at: '2025-06-24T20:48:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20150297789719-Agro-Linha-Protheus-AGR-Certificados-de-Peso-Cadastro-IE-X-Container
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249805463) Tempo aproximado para leitura: **00:02:35 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para cadastrar corretamente o cadastro **IE** é apresentada a ocorrência **Certificados de Peso - Cadastro IE X Container** no rotina OGA710.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Esse incidente ocorre, pois é preciso realizar o o processo para cadastrar corretamente o cadastro **IE** no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, foi desenvolvido uma tela para vincular a **IE** à um **container** ou vários, posicionando na **IE** desejada, **ações Relacionadas container;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150297752599)**

Após o clique será aberto uma nova tela, nela será apresentado preenchido o valor da **Instrução de Embarque** onde consta o **código e o descritivo dela**,  
O código fica oculto, se trata do campo chave primária, o campo descritivo é o campo que vemos ao abrir uma **instrução de embarque**, clicando em incluir será aberto a tela de cadastro:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249807639)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249808919)**

Após confirmar os dados o **container vinculado a IE** ficará visível na tela inicial

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249810967)

Outra forma de abrir a tela é via **menu**, **atualizações originação comercialização de container**Nessa visão a única mudança é que o campo correspondente a **IE** ficará aberto para **via F3** ser pesquisado e informado

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249812631)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249813911)

E após o vínculo da **IE** ficará com essa visão

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249817367)

Após confirmar o registo constará no painel **IE X container**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20150249818903)

O Sistema valida se com a adição de mais um **container** não será ultrapassada a quantidade informada no campo **N7Q\_QTDCON - Q. Container**.  
No programa de **IE X container**, na inserção de um novo registro, ao selecionar a instrução de embarque, o Sistema valida se com a dição de mais um **container** não será ultrapassada a quantidade informada na **instrução de embarque** campo **N7Q\_QTDCON** da pasta **itens da IE**”.  
É Possível adicionar **containers** na instrução de embarque também por meio das outras ações da tela de alteração da instrução de embarque, ao tentar adicionar um novo **container** o Sistema faz a verificação e valida se com a adição de mais um **container** na **N7Q\_QTDCON** não será ultrapassada.  
Ao aprovar o peso certificado da **instrução de embarque**, o Sistema realiza o ajuste de peso da instrução de embarque, dos **processos de exportação e dos embarques gerados**, além disso vincula os contêineres aos seus respectivos **embarques**, são enviados apenas os contêineres com **status igual a 6  aprovado  
  
Saiba mais**Para maiores informações acesso os *links*:  
[Agro - Linha Protheus - AGR - Certificação de Peso - Rateio dos fardinhos no registro da chegada no armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012101322-Agro-Linha-Protheus-AGR-Certifica%C3%A7%C3%A3o-de-Peso-Rateio-dos-fardinhos-no-registro-da-chegada-no-armaz%C3%A9m)  
[Agro - Linha Protheus - AGR - Certificação de peso, movimentação de estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402115633687-Agro-Linha-Protheus-AGR-Certifica%C3%A7%C3%A3o-de-peso-movimenta%C3%A7%C3%A3o-de-estoque)  
[Agro - Linha Protheus - AGR - Certificação de peso, rateio dos fardos na atualização do Romaneio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011989241-Agro-Linha-Protheus-AGR-Certifica%C3%A7%C3%A3o-de-peso-rateio-dos-fardos-na-atualiza%C3%A7%C3%A3o-do-Romaneio)  
[Agro - Linha Protheus - AGR - Certificação de peso, vínculo de fardos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011600861-Agro-Linha-Protheus-AGR-Certifica%C3%A7%C3%A3o-de-peso-v%C3%ADnculo-de-fardos)
