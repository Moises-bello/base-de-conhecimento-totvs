---
content_hash: 7a27b9fd2d80ba3ad47de35ee136af075e1bb7a7c0876532b399ee9ad151e5b2
fetched_at: '2026-06-29T00:09:50.109577+00:00'
page_id: '435105400'
product: rm
source: tdn-rm
title: Fórmula de Apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105400
version: 4
---

Neste anexo é possível associar a fórmula que é responsável pelo cálculo final da Apuração, os valores gerados por cada fórmula é que são integrados e contabilizados.  
  
 **ID da Fórmula:**  
 Valor Auto incremental que identifica a fórmula de apuração.  
  
 **Descrição:**  
 Informe a descrição da fórmula de apuração.  
  
 **Código da Fórmula:**  
 Informe qual a formula a ser utilizada no cálculo.  
  
 **Código do Evento Destino:**  
 Defina qual evento contábil receberá o valor calculado.

ObservaçãoApenas eventos contábeis definidos para o processo "Apuração de Resultado Contábil" serão considerados neste campo.

**Tratamento das SubUnidades:**  
 Informe como será o tratamento das subunidades para a composição da base de cálculo.  
 As opções são :

* Desconsidera SubUnidades - Calcula o valor para o empreendimento não aplicando o filtro de Contas Gerenciais, rateios e desconsiderando qualquer informação das subunidades (Se foram vendidas ou não).
* Todas as SubUnidades - Irá calcular o valor por SubUnidade para todas as SubUnidades.
* Apenas SubUnidades Vendidas - Considera no cálculo apenas SubUnidades com status = Vendido.
* Apenas SubUnidades Distratadas - Considera apenas SubUnidades que foram distratadas dentro do período de apuração, caso distratadas em períodos anteriores não serão consideradas.
