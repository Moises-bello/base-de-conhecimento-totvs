---
article_id: 7885099165591
category: ADVPL - Classe e Função
content_hash: e1fa4102a044f83f751581d4f393730e6fa12e40c22d2018fbb72338c7da8db0
fetched_at: '2026-06-28T22:40:20.738464+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função MayIUseCode
type: support-article
updated_at: '2022-08-02T12:04:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7885099165591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-MayIUseCode
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como utilizar corretamente a função MayIUseCode() ?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL - Todas versões  
  
**Solução**A função **MayIUseCode** tem o objetivo de reservar uma palavra, ou seja, quando uma estação reserva uma palavra (como por exemplo "DesktopTeste01") a outra estação não conseguiria utilizar.  
Essa função tem o intuito de reservar uma cadeia de caracteres para um usuário ou *thread* especifica, essa reserva é feita a nível de *thread*, não tem qualquer relação com qualquer tabela ou alias especifico.  
A função **não efetua um DbSeek em nenhuma tabela**, a reserva serve apenas para garantir que determinado código não está em uso por outra estação.  
Por exemplo, vamos supor, que seja colocado no inicializador padrão do campo código do cliente, uma função de usuário que faça um *select Max(a1\_cod)* na tabela SA1, e devolva o último código cadastrado mais 1.  
Nesse caso de uso, se mais de uma estação clicar em incluir cliente ao mesmo tempo o código informado para as duas estações será o mesmo, para esta situação pode-se utilizar a função **MayIUseCode** para garantir que o código a ser retornado não esteja em uso por outra thread, mesmo que não tenha sido gravado ainda.  
  
**Saiba mais**  
[Função MayiUseCode()](https://jiraproducao.totvs.com.br/browse/DFRM1-29948)
