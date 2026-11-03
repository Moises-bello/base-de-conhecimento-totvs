---
article_id: 19139742747671
category: RH - Cadastros
content_hash: 89d6055afcb8e9a2a0551942dd2667e467df88439f2d7bd46d330d827e415a1b
fetched_at: '2026-06-28T22:44:52.737862+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Ao tentar alterar o MV_PONMES, é gerada a mensagem
  "Não é possível selecionar um período já existente no cadastro de períodos (Tabela
  SPO). Verifique o período informado"
type: support-article
updated_at: '2026-02-03T17:00:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19139742747671-RH-Linha-Protheus-PON-Ao-tentar-alterar-o-MV-PONMES-%C3%A9-gerada-a-mensagem-N%C3%A3o-%C3%A9-poss%C3%ADvel-selecionar-um-per%C3%ADodo-j%C3%A1-existente-no-cadastro-de-per%C3%ADodos-Tabela-SPO-Verifique-o-per%C3%ADodo-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19139758691479) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
No módulo de **Ponto Eletrônico,** na [Rotina Período de Apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)**,** ao tentar alterar o parâmetro **MV\_PONMES** é apresentado a mensagem "Atenção! Existem inconsistências a serem verificadas. Não é possível selecionar um período já existente no cadastro de períodos (Tabela SPO). Verifique o período informado."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19139726397207)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Esse incidente ocorre, quando informado no MV\_PONMES um período que **já consta fechado** na tabela SPO, e que pode ser consultado na própria rotina de Período de Apontamento, com legenda de cor vermelha.  
O incidente também pode ocorrer se o usuário **indevidamente criar um período** utilizando o botão **Incluir**, que gera um registro na rotina de Período de Apontamento com a legenda de cor verde.  
  
**Solução**  
Para solucionar essa ocorrência, na [Rotina Período de Apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290), em **Atualizações > Cadastro do Ponto > Período de Apontamento,** verifique se o período que deseja informar no parâmetro **MV\_PONMES** consta na rotina de Período de Apontamento.  
  
Exemplo abaixo de um período fechado corretamente pelo usuário/sistema, onde a legenda tem cor vermelha. Neste caso, não podemos informar um período no MV\_PONMES com datas entre 01.06.2023 e 30.06.2023:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154697273623)  
  
  
Abaixo, temos um exemplo de registro que foi **criado indevidamente pelo usuário** utilizando o botão de Incluir, e a legenda tem cor verde. Neste caso, é possível excluir este registro clicando em **Outras Ações > Excluir:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154697290007)

**Importante:** Na rotina de Período de Apontamento não deve ser utilizada a opção **Incluir**, o procedimento correto é que após o Fechamento Mensal, o sistema faça a abertura do Período de Apontamento subsequente alterando automaticamente o conteúdo do parâmetro **MV\_PONMES** e automaticamente subirá o período fechado na tela inicial identificado com a legenda vermelha.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290?source=search)  
[RH - Linha Protheus - PON - Após o fechamento mensal, o sistema não alterou o período de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012922731-RH-Linha-Protheus-PON-Ap%C3%B3s-o-fechamento-mensal-o-sistema-n%C3%A3o-alterou-o-per%C3%ADodo-de-apontamento?source=search)
