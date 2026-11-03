---
article_id: 360026311013
category: Portal de Gestão de Capital Humano
content_hash: 941d67e48b426bf8eb98d8b2cf4ac04fdceac7a1fdad9cbf41979ad2074888be
fetched_at: '2026-06-28T22:43:00.080452+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Manutenção das marcações no portal  após
  o término do período.
type: support-article
updated_at: '2022-09-14T13:09:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026311013-RH-Linha-Protheus-PORTAL-GCH-Manuten%C3%A7%C3%A3o-das-marca%C3%A7%C3%B5es-no-portal-ap%C3%B3s-o-t%C3%A9rmino-do-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00** min  
 **Dúvida**Como configurar o sistema para realizar a manutenção das marcações no Portal GCH após o expirado da fim do período, mesmo o período estando aberto quando já ultrapassou a data fim do período? **Ambiente**TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**No portal GCH é possível consultar as marcações e incluir uma marcação faltante e/ou um pré abono.   
Para isso o lançamento deve estar dentro do período em aberto do Ponto.  
  
**Parâmetro(s):**   
MV\_PONMES/ MV\_GETMAUT/ MV\_COLMARC/ MV\_DABERTO/ MV\_DFECHAD   
  
**Tabelas Utilizadas:**RH3 - Solicitações ao RH / RH4 - Alteração Cadastral/ RGK - Histórico de aprovações do portal /

SP8 – Movimento de Marcações /  RS3 - Tab Aux Solic Portais - Ponto

**Procedimento para Utilização:**Ao acessar o Portal Gestão do Capital Humano terá a nova opção de Marcação de Ponto nos menus,   
com as mesmas funcionalidades das demais, permitindo que você faça marcações para você ou para alguém da sua equipe.   
Será apresentado o período de marcação do período ativo, e nela o funcionário poderá selecionar o dia em que deseja inserir a marcação manual, será apresentado as marcações já existentes na tela complementando com as marcações que estão aguardando aprovação que serão salvas em uma nova tabela auxiliar(RS3).   
  
O parâmetro MV\_COLMARC será utilizado para obter quantidade de Entradas padrão, ou seja, se o parâmetro estiver preenchido com **2**, serão apresentadas na tela do portal quatro colunas (duas entradas e duas saídas). Caso exista mais marcações do que a quantidade padrão definida, serão apresentadas colunas até o limite de marcações do dia, ou seja, existindo 16 marcações,   
serão apresentadas 16 colunas.   
O limite mínimo sempre será composto baseado no parâmetro MV\_COLMARC. As marcações oriundas do remote, sejam elas do relógio de ponto, TSA ou ainda incluídas manualmente pelo módulo de Ponto Eletrônico não poderão ser alteradas/excluídas.  
  
A partir da seleção da data nesta tela será apresentado uma nova tela onde poderá ser informado o horário de forma manual e uma justificativa. Todas as solicitações deverão seguir o padrão existente de aprovação até que esteja na etapa de aprovação do RH, nesta etapa ao ser aprovada   
será efetuada a marcação na tabela SP8.   
  
O parâmetro **MV\_DABERTO** permite fazer inclusão de marcações após o término do período e nele será informado a quantidade de dias corridos em que a tela de inclusão manual deverá estar disponível para ajustes manuais em marcações não informadas. Vale destacar que se seu conteúdo estiver com Zero "0" não terá nenhum dia de acréscimo.  
  
O parâmetro **MV\_DFECHAD** estabelece a quantidade de dias que ficará fechado para manutenção após o término do parâmetro anterior, exemplos:   
  
Período 11/01/2018 à 10/02/2018 MV\_DABERTO = 2 MV\_DFECHAD = 4 Dias 11 e 12/02/2018 o sistema deverá permitir inclusão manual e de 13/02/2018 a 16/02/2018 o sistema estará fechado para manutenção.   
No dia 17/02/2018 estará disponível o novo período de marcação 11/02/2018 a 10/03/2018 para inclusões de marcações manuais. Não será permitido a inclusão de marcações com data maior que o dia atual.  
  
**Saiba Mais**  
[Artigos sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-Portal-de-Gest%C3%A3o-de-Capital-Humano)
