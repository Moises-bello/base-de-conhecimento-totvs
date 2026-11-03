---
content_hash: c6afc6c286df62b611190addde139693f1623c72afb89b7a96e18aed8b2282cc
fetched_at: '2026-06-29T00:10:10.489986+00:00'
page_id: '452719852'
product: rm
source: tdn-rm
title: Código de Cálculo 182 - Base INSS 13º Outro Emprego Desconto Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719852
version: 2
---

Evento do tipo Base de Cálculo, Valor e sem incidências. Informar neste evento a base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS de 13º Salário. Este evento deve ser lançado quando houver necessidade de desconto do total descontado no outro emprego e não calculado o valor proporcionalizado, portanto na movimentação devem existir apenas os eventos com CC 182 – Base INSS 13º Outro Emprego Desconto Complementar e CC144 - INSS 13o Salário Outro Emprego. O cálculo do sistema procederá conforme o exemplo abaixo:

**Exemplos**

1) (Base abaixo do Teto)  
 Base de Cálculo INSS na Outra Empresa (CC182): 400,00  
 INSS Descontado na Outra Empresa (CC144): 30,60 (7,65%)  
 Base de Cálculo INSS na Empresa Atual: 500,00  
 Base Total do INSS na Competência: 900,00  
 Alíquota devida do Mês de Competência: 9%  
 Valor devido para desconto do INSS na Competência: 81,00  
 Valor INSS desconta na Empresa Atual (CC102 ou CC11): 50,40 (81,00 – 30,60)  
 Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC182 com o valor da base de cálculo da outra empresa (400,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC144 (30,60) para o desconto do INSS na empresa (CC102 ou CC11).  
    
    
 2) (Base acima do Teto)  
 Base de Cálculo INSS na Outra Empresa (CC182): 1900,00  
 INSS Descontado na Outra Empresa (CC144): 209,00 (11%)  
 Base de Cálculo INSS na Empresa Atual: 1000,00  
 Base Total do INSS na Competência: 2900,00 (ultrapassou limite para desconto do teto)  
 Valor devido para desconto do INSS na Competência: 275,95  
 Valor INSS desconta na Empresa Atual (CC102 ou CC11): 66,95 (275,95 – 209,00)  
 Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC182 com o valor da base de cálculo da outra empresa (1900,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência (neste caso, ultrapassou o limite para desconto do teto) e deduzirá o valor informado no evento de CC144 (209,00) para o desconto do INSS na empresa (CC102 ou CC11).  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
