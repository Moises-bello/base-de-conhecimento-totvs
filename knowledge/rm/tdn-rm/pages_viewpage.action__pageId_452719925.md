---
content_hash: 0dd857b92bb2f50a67872013aa4fdae651b0597a5731ee0d9d4e04dacdafe423
fetched_at: '2026-06-29T00:10:10.738177+00:00'
page_id: '452719925'
product: rm
source: tdn-rm
title: Código de Cálculo 181 - Base INSS Outro Emprego Desconto Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719925
version: 4
---

Evento do tipo Base de Cálculo, Valor e sem incidências. Informar neste evento a base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS. Este evento deve ser lançado quando houver necessidade de desconto do total descontado no outro emprego e não calculado o valor proporcionalizado, portanto na movimentação deve existir apenas os eventos com CC 181 – Base INSS Outro Emprego Desconto Complementar e CC29 - INSS Outro Emprego. O cálculo do sistema procederá conforme o exemplo abaixo:   
   
**Exemplos**  
1) (Base abaixo do Teto)  
Base de Cálculo INSS na Outra Empresa (CC181): 400,00   
INSS Descontado na Outra Empresa (CC29): 30,60 (7,65%)   
Base de Cálculo INSS na Empresa Atual: 500,00   
Base Total do INSS na Competência: 900,00   
Alíquota devida do Mês de Competência: 9%   
Valor devido para desconto do INSS na Competência: 81,00   
Valor INSS desconta na Empresa Atual (CC03): 50,40 (81,00 – 30,60)   
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (400,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC29 (30,60) para o desconto do INSS na empresa (CC03).

2) (Base acima do Teto)  
Base de Cálculo INSS na Outra Empresa (CC181): 1900,00   
INSS Descontado na Outra Empresa (CC29): 209,00 (11%)   
Base de Cálculo INSS na Empresa Atual: 1000,00   
Base Total do INSS na Competência: 2900,00 (ultrapassou limite para desconto do teto)   
Valor devido para desconto do INSS na Competência: 275,95   
Valor INSS desconta na Empresa Atual (CC03): 66,95 (275,95 – 209,00)   
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (1900,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência (neste caso, ultrapassou o limite para desconto do teto) e deduzirá o valor informado no evento de CC29 (209,00) para o desconto do INSS na empresa (CC03).  
 

Dica

Quando houver cálculo de múltiplos vínculos e em um dos envelopes for lançado o evento de código de cálculo 181 - Base INSS Outro Emprego Desconto Complementar com o valor maior ou igual a base teto INSS, será necessário clicar no Recálculo do envelope de cada um dos vínculos para que os eventos de base relacionados as faixas de INSS sejam lançados no envelope onde o evento de código de cálculo 181 - Base INSS Outro Emprego Desconto Complementar esteja lançado.

**Observação**

Quando é informada a Base de INSS do externo, utilizando os CC's 72 ou 181 para CLT ou o CC 418 para autônomo, o sistema calcula o desconto de INSS do externo, e não considera o valor informado pelo usuário no CC 29.   
Para utilizar o desconto do INSS do externo como referência do cálculo o correto é informar somente o CC 29.   
O CC 29 pode ser utilizado para informar o desconto do INSS de qualquer vinculo externo, seja CLT ou autônomo.  
Somente no caso de informar a Base de INSS do externo, onde o sistema que irá calcular do valor descontado, que é necessário diferenciar o número do código de cálculo, CC 418 para autônomo e CC's 72 e 181 para CLT.

---

Códigos de Cálculo
