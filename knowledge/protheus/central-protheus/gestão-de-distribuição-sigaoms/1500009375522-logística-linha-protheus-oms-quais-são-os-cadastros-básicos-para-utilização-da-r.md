---
article_id: 1500009375522
category: Gestão de Distribuição (SIGAOMS)
content_hash: aa28d0319abdf279cc4ea8f8a0311dd2dadfe29415c22b6ed7cfb89ec789a36c
fetched_at: '2026-06-28T22:45:50.102696+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Quais são os cadastros básicos para utilização
  da rotina de Montagem de Carga - OMSA200
type: support-article
updated_at: '2024-05-03T19:55:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009375522-Log%C3%ADstica-Linha-Protheus-OMS-Quais-s%C3%A3o-os-cadastros-b%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-da-rotina-de-Montagem-de-Carga-OMSA200
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23008517709207)***Tempo aproximado para leitura: **00:03:12** **min**  
**Dúvida**Quais são os cadastros básicos para utilização da rotina de **Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1-Acesse **Atualizações/Roteirização/Zonas - OMSA070**, efetue o cadastro de uma zona de entrega:

![ZONAS.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4416260740887)

2-Acesse **Atualizações/Roteirização/Setores por Zonas - OMSA080**, efetue o cadastro dos setores vinculados à zona de entrega:

![setor.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4416267108375)

3-Acesse **Atualizações/Roteirização/Pontos por Zona e Setor - OMSA090**, efetue o cadastro de pontos por zona e setor. Nesse cadastro é realizado o relacionamento da **Zona**, **Setores por Zona** e **Ponto por Setor**, definindo como serão considerados os setores. Podendo ser  por **Cliente** ou **Códigos de Endereçamento Postal**.

![pontos_por_setor.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4416253323159)

4-Acesse **Atualizações/Roteirização/Rotas - OMSA100**, efetue o cadastro das rotas de acordo com a zona e os setores.

![rotas.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014480141)

5-Acesse **Atualizações/Pedidos/Pedidos de Venda - MATA410**, efetue a inclusão de um pedido de venda, informando no campo carga **C5\_TPCARGA** o valor **1 - Utiliza** e libere o pedido normalmente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014481481)

6-Acesse **Atualizações/Cargas/Montagem de Carga - OMSA200**,  verifique a parametrização do grupo de perguntas para que as cargas sejam apresentadas de acordo com a data e range desejados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014208762)

7-No menu **Carregamento**, clique na opção **Montagem de Carga**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014209382)**

Neste momento é possível configurar quais pedidos devem ser apresentados para montagem da carga, filtrando também por cliente e demais propriedades de acordo com a necessidade.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014483861)

Os **Modelos de Carga - OMSA180**, disponibilizam um recurso extra para filtragem dos pedidos e produtos que serão alocados em uma carga. Neste sentido, é possível que sejam montadas cargas exclusivas para produtos secos, produtos químicos ou perecíveis, permitindo assim o direcionamento delas a veículos especiais de acordo com o modelo de carga selecionado. Todo **Modelo de Carga** deve estar vinculado a um **Tipo de Carga**, correspondente a um registro da **tabela DU**, do arquivo de **Tabelas Genéricas - SX5**. Para que o filtro seja efetivo no momento da montagem das cargas, é necessário vincular um **Modelo de Carga** ao cadastro de cada um dos **Produtos - MATA010**, a serem distribuídos - campo **B1\_TIPCAR**.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014211482)

8-Selecione os pedidos que farão parte da carga e confirme:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23008517718039)

**Importante**  
Para a utilização do **TOTVS OMS - Order Management System** e do processo de **Montagem de Carga** é necessário que o parâmetro **MV\_INTDL** esteja ativo.  
  
**Saiba mais**Mais informações poderão ser acessadas no *link's*:  
[Logística - Linha Protheus - OMS - Quais os motivos para um pedido não aparecer na montagem de carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025954851-MP-OMS-Quais-os-motivos-para-um-pedido-n%C3%A3o-aparecer-na-montagem-de-carga)  
[Logística - Linha Protheus - OMS - Opções disponíveis no Botão Carregamento na rotina de Montagem de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027375252-MP-OMS-Op%C3%A7%C3%B5es-dispon%C3%ADveis-no-Bot%C3%A3o-Carregamento-na-rotina-de-Montagem-de-Cargas)  
[Logística - Linha Protheus - OMS - Busca do CEP a ser considerado na Montagem de Carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027564691-MP-OMS-Busca-do-CEP-a-ser-considerado-na-Montagem-de-Carga)  
[Logística - Linha Protheus - OMS - Cadastros Básicos para utilização do SIGAOMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009371242-Log%C3%ADstica-Linha-Protheus-OMS-Pedidos-sem-roteiriza%C3%A7%C3%A3o-na-Montagem-de-Carga-OMSA200)
