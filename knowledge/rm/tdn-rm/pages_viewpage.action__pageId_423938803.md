---
content_hash: 46011e348eb9667b4321f147c2a89593b51e8a687e06860e10404016cd12a385
fetched_at: '2026-06-29T00:09:29.085942+00:00'
page_id: '423938803'
product: rm
source: tdn-rm
title: Rastrear Origem de Lançamentos Contábeis 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938803
version: 4
---

Esta funcionalidade tem como objetivo mostrar de forma gráfica e estruturada toda a operação que deu origem ao lançamento contábil e suas respectivas partidas.   
   
Este recurso possibilita ainda consultar diretamente a origem do lançamento, bastando dar duplo clique no diagrama apresentado para que a tela de entrada do sistema de origem seja aberta, sem a necessidade de acessar diretamente o sistema de origem para realizar tal consulta.  
   
**Exemplo de utilização:**  
   
Muitas operações efetuadas em sistemas externos ao da contabilidade podem gerar automaticamente no TOTVS Gestão Contábil um lançamento contábil correspondente. Se desejar saber informações sobre a operação que deu origem a este lançamento, sem ter que acessar diretamente o sistema de origem, basta selecionar o lançamento e acessar o Anexo 'Rastrear origem' que uma tela gráfica com diagramas contendo informações sobre a operação de origem e as respectivas partidas geradas será mostrada.  
   
  
   
No exemplo apresentado, a parte de cima mostra informações resumidas sobre a origem do lançamento e a parte de baixo sobre as partidas contábeis geradas.  
Se você clicar duas vezes sobre o gráfico que contem as informações sobre o Movimento-1286, o sistema abrirá automaticamente a tela de entrada do respectivo aplicativo para que você consulte como desejar os dados que deram origem ao lançamento. Neste exemplo, o sistema abrirá a tela do movimento número 180431 diretamente no sistema Totvs Gestão de Estoque, Compras e Faturamento.   
Da mesma forma, se você clicar em um dos gráficos que contem informações sobre as partidas contábeis geradas, o sistema abrirá a tela do respectivo lançamento contábil.  
   
Este recurso também permite rastrear e identificar a origem de lançamentos contábeis agrupados, estornados e de estorno, fornecendo informações sobre sua composição.  
    
**Importante:**  
   
Para rastrear a origem dos lançamentos contábeis, é preciso que o sistema de origem já tenha sido convertido para o Novo Modelo de BackOffice da linha RM e esteja gerando os lançamentos nesta nova plataforma .Net.   
   
A origem de tais lançamentos pode ser consultada tanto para os lançamentos que ainda estiverem no **lote N** como para os que já estiverem no lote oficial da contabilidade (**lote zero**).  
   
Hoje este recurso já está disponível para lançamentos originados do TOTVS:

* Gestão de Estoque, Compras e Faturamento;
* Gestão Educacional;
* Gestão Financeira;
* Gestão Fiscal.

---
