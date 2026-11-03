---
content_hash: ab8ef0043fca5c79da1e26c704fb18ff2b1705febb295a87993c41dc03b506d3
fetched_at: '2026-06-29T00:09:49.133023+00:00'
page_id: '435105241'
product: rm
source: tdn-rm
title: Composição da base de cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105241
version: 5
---

Neste anexo serão definidos como serão buscados os valores que serão utilizados nas fórmulas de Apuração para se calcular os resultados.  
    
 Campos a serem preenchidos:  
    
 **ID do evento de Apuração:**  
 Valor auto incremental que identifica o evento da composição da base de cálculo.  
    
 **Descrição:**  
 Informe a descrição da base de Cálculo. *Ex.: Base de Cálculo do Projeto de Empreendimento*.

* Para realizar a apuração das vendas que possuem aditivo de troca de subunidades, pode ser necessário que se trabalhe hora com informações da subunidade anterior, hora com informações da subunidade nova. Para estes casos, quando uma composição precisar buscar dados referentes à subunidade anterior, deverá ser incluído, no final da descrição, a tag "#GER\_ANT" (sem as aspas). Um exemplo desta utilização é quando precisa-se transferir o saldo

**Tratamento das Subunidades:**  
 Informe como será o tratamento das subunidades para a composição da base de cálculo.  
 As opções são :

* Desconsidera SubUnidades - Calcula o valor para o empreendimento não aplicando o filtro de Contas Gerenciais, rateios e desconsiderando qualquer informação das subunidades (Se foram vendidas ou não).
* Todas as SubUnidades - Irá calcular o valor por SubUnidade para todas as SubUnidades.
* Apenas SubUnidades Vendidas - Considera no cálculo apenas SubUnidades com status = Vendido.
* Apenas SubUnidades Distratadas - Considera apenas SubUnidades que foram distratadas dentro do período de apuração, caso distratadas em períodos anteriores não serão consideradas.
* Subunidades que entraram por troca - Irá considerar as subunidades que passaram a fazer parte da venda, por meio do aditivo de troca de subunidade.
  + Para realizar a apuração das vendas que possuem aditivo de troca de subunidades, pode ser necessário que, ao processar as subunidades que entraram por troca, em algum momento, se trabalhe com informações da subunidade anterior (que saiu da venda pelo aditivo). Para estes casos, quando uma composição precisar buscar dados referentes à subunidade anterior, deverá ser incluído, no final do campo descrição, a tag "#GER\_ANT" (sem as aspas). Um exemplo desta utilização é quando precisa-se transferir o saldo das contas gerenciais das respectivas subunidades.
* Subunidades que saíram por troca - Irá considerar as subunidades que foram removidas da venda, por meio do aditivo de troca de subunidade.

**Aplica a fração ideal nos valores apurados:**  
 Informe se deseja multiplicar o valor apurado pela composição pelo valor da fração ideal da subunidade.

ObservaçãoCaso o tratamento de subunidades esteja definido como "Desconsidera Subunidades" este parâmetro estará desabilitado

---

Informações ComplementaresValores de Origem
