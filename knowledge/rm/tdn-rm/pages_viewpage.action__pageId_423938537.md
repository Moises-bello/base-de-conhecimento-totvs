---
content_hash: 33116f9d51cb73ccef94b881b8dcee256057d62b9eb32ac234d9c6df771fd2ea
fetched_at: '2026-06-29T00:09:27.535442+00:00'
page_id: '423938537'
product: rm
source: tdn-rm
title: Considerar Indicador de Uso na Inicialização do Plano Marco 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938537
version: 2
---

Criado o parâmetro Considerar Indicador de Uso na Inicialização do Plano Marco que se encontra na Aba Identificação dos Parâmetros Gerais do Officina.   
 Com esse parâmetro habilitado os planos do tipo marco terão o seguinte comportamento:  
 Quando um plano for inicializado em um objeto de manutenção que já possua valor de indicador de uso, o sistema deve começar a contagem considerando o valor do indicador de uso inicializado.  
 Exemplo: Se a frequência do plano é igual a 100KM, e a inicialização do plano foi feita em um objeto com 50KM, o primeiro vencimento deve ocorrer com 150KM e não em 100KM como era feito anteriormente, o segundo vencimento deve ser com 250KM e não em 200KM e assim por diante. Caso a OS for gerada antes do vencimento, o sistema vai exibir uma mensagem informando quanto falta para vencer.  
 Se o parâmetro Considerar Indicador de Uso na Inicialização do Plano Marco for desmarcado o comportamento dos planos do tipo marco será como antes, o sistema vai começar a contagem considerando o valor do indicador de uso inicializado.
