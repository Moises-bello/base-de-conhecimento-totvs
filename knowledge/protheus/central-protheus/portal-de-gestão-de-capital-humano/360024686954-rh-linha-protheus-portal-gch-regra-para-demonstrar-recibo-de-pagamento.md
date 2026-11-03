---
article_id: 360024686954
category: Portal de Gestão de Capital Humano
content_hash: 775bd66034c007c4ce1172d9aebecf938e9b10f6557259dc03d2c110cae5f5eb
fetched_at: '2026-06-28T22:42:59.019340+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Regra para demonstrar recibo de pagamento
type: support-article
updated_at: '2024-04-19T20:12:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024686954-RH-Linha-Protheus-PORTAL-GCH-Regra-para-demonstrar-recibo-de-pagamento
---

**Dúvida**Como disponibilizar o recibo de pagamento do mês em aberto?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**A Validação que o sistema faz para demonstrar é:  
  
Data Base **(windows)** + Data Pagamento Definido no cadastro de Períodos **(SIGAGPE )** + Conteúdo do parâmetro MV\_TCFDFOL **(pode ser negativo).**Realize as seguintes verificações:  
  
1. Acesse o módulo configurador (No módulo Configurador, acesse o menu *Ambientes > Cadastros > Parâmetros)* e localize o parâmetro **MV\_TCFDFOL**, este parâmetro pode conter o conteúdo negativo caso queira disponibilizar antes da dada de pagamento.  
  
**OBS: Esse valor pode mudar conforme a necessidade, é apenas um exemplo.**![](http://tdn.totvs.com/download/attachments/239026981/image2016-6-10%2013%3A50%3A31.png?version=1&modificationDate=1465573929000&api=v2)  
  
2. Confira a data de pagamento no  cadastro de períodos.  
  
![](http://tdn.totvs.com/download/attachments/239026981/image2016-6-10%2013%3A50%3A48.png?version=1&modificationDate=1465573931000&api=v2)  
  
Data Pagamento no cadastro de períodos: **06/06/2016 - Mês Aberto**Parâmetro **MV\_TCFDFOL: -2**Data do Windows: **01/06/2016**Exemplo 01: Mostra recibo := dDataBase >= Data Pagamento Períodos + conteúdo do parâmetro MV\_TCFDFOL.  
  
01/06/2016 >= 06/06/2016 + (-2)  (Repare que após reduzir -2 do conteúdo do parâmetro MV\_TDFDFOL a data de pagamento ficou 04/06/2016 conforme abaixo).  
  
01/06/2016 >= 04/06/2016  
  
O resultado é Falso, portanto não exibe o recibo no portal deste período, ou seja como a data do Windows é 01/06/2016 e o resultado do cálculo da regra foi 04/06/2016 só irá mostrar o recibo quando a data do Windows for 04/06/2016.

![image2016-6-10 13:51:27.png](http://tdn.totvs.com/download/attachments/239026981/image2016-6-10%2013%3A51%3A27.png?version=1&modificationDate=1465573932000&api=v2)  
  
Exemplo 02:  Mostra recibo := dDataBase >= Data Pagamento Períodos + conteúdo do parâmetro MV\_TCFDFOL.  
  
04/06/2016 >= 06/06/2016 + (-2)  (Repare que após reduzir -2 do conteúdo do parâmetro MV\_TDFDFOL a data de pagamento ficou 04/06/2016 conforme abaixo).  
  
04/06/2016 >= 04/06/2016

Resultado é Verdadeiro, portanto exibe o recibo no portal deste período, ou seja como a data do Windows é 04/06/2016 e o resultado do cálculo da regra também foi 04/06/2016 irá mostrar o recibo normalmente.

![](http://tdn.totvs.com/download/attachments/239026981/image2016-6-10%2013%3A51%3A50.png?version=1&modificationDate=1465573933000&api=v2)  
  
**Observação: O Aplicativo Meu RH segue o mesmo conceito.  
  
Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
