---
article_id: 1500009371242
category: Gestão de Distribuição (SIGAOMS)
content_hash: e939d84c232c0c0cf4182c10c48b5368a2c6b0287d185c1d10868c10e7f5f66a
fetched_at: '2026-06-28T22:45:50.003187+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Pedidos sem roteirização na Montagem de
  Carga - OMSA200
type: support-article
updated_at: '2024-05-03T20:08:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009371242-Log%C3%ADstica-Linha-Protheus-OMS-Pedidos-sem-roteiriza%C3%A7%C3%A3o-na-Montagem-de-Carga-OMSA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23218377725463) Tempo aproximado para leitura: **00:02:54** **min**  
**Dúvida**Porque são apresentados **pedidos sem roteirização** na **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**As etapas do processo de montagem de carga são independentes, o que significa que o Sistema permite selecionar **as Rotas**, **as Zonas**, **os Setores** e **os Pedidos**, de acordo com a necessidade.  
  
Assim, é possível:

* Selecionar um Pedido sem que o Setor ao qual este pertence esteja marcado.
* Selecionar um Setor sem que a Zona a qual este pertence esteja marcada.
* Selecionar uma Zona sem que a Rota a qual esta pertence esteja marcada.

Caso tenha **Pedidos de Venda  de um cliente que não possui roteirização cadastrada**, ou seja, o Sistema não tem referência de **rotas**, **zonas** ou **setor para este cliente**, **nos blocos Rotas, Zonas e Setor** será apresentada uma caixa de verificação com a descrição igual a **999999 - Pedidos sem roteirização**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018328101)

Para que os pedidos de venda sejam apresentados com a roteirização, deverá realizar os cadastros e relacionamentos abaixo:

* Acesse **Atualizações/Roteirização/Zonas - OMSA070**, efetue o cadastro de uma zona de entrega
* Acesse **Atualizações/Roteirização/Setores por Zonas - OMSA080**, efetue o cadastro dos setores vinculados à zona de entrega
* Acesse **Atualizações/Roteirização/Pontos por Zona e Setor - OMSA090**, efetue o cadastro de pontos por zona e setor. Nesse cadastro é realizado o relacionamento da **Zona**, **Setores por Zona** e **Ponto por Setor**, definindo como serão considerados os setores. Podendo ser  por **Cliente** ou **Códigos de Endereçamento Postal**.
* Acesse **Atualizações/Roteirização/Rotas - OMSA100**, efetue o cadastro das rotas de acordo com a zona e os setores.

Instruções detalhadas sobre **Cadastros Básicos** para utilização da rotina **Montagem de Carga - OMSA200** estão no *link*: [Logística - Linha Protheus - OMS - Quais são os cadastros básicos para utilização da rotina de Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009375522-Log%C3%ADstica-Linha-Protheus-OMS-Quais-s%C3%A3o-os-cadastros-b%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-da-rotina-de-Montagem-de-Carga-OMSA200)  
  
**Saiba mais**  
Para obter informações adicionais, acesse o *link*:  
[Montagem de Carga - OMSA200 - SIGAOMS](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)  
[Logística - Linha Protheus - OMS - Cadastros Básicos para utilização do SIGAOMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021897892-MP-OMS-Cadastros-B%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-do-SIGAOMS)  
[Logística - Linha Protheus - OMS - Quais os motivos para um pedido não aparecer na montagem de carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025954851-MP-OMS-Quais-os-motivos-para-um-pedido-n%C3%A3o-aparecer-na-montagem-de-carga)  
[Logística - Linha Protheus - OMS - Opções disponíveis no Botão Carregamento na rotina de Montagem de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027375252-MP-OMS-Op%C3%A7%C3%B5es-dispon%C3%ADveis-no-Bot%C3%A3o-Carregamento-na-rotina-de-Montagem-de-Cargas)  
[Logística - Linha Protheus - OMS - Busca do CEP a ser considerado na Montagem de Carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027564691-MP-OMS-Busca-do-CEP-a-ser-considerado-na-Montagem-de-Carga)
