---
article_id: 360063693393
category: Folha Mensal
content_hash: ea39885b6c95466828ae753fcf92bd5b5afff176eca1228a7431624f2206bd16
fetched_at: '2026-06-28T22:46:59.432783+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: Quando utilizar os códigos de cálculo
  72, 181 e 29 no cálculo de INSS Múltiplos Vínculos?'
type: support-article
updated_at: '2024-10-04T18:29:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063693393-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-Quando-utilizar-os-c%C3%B3digos-de-c%C3%A1lculo-72-181-e-29-no-c%C3%A1lculo-de-INSS-M%C3%BAltiplos-V%C3%ADnculos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:07:36 min  
  
Dúvida**Quando utilizar os códigos de cálculos 72, 181 e 29 no cálculo de INSS Múltiplos Vínculos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para situações em que o funcionário **atinge o teto no outro vínculo**, ou seja, fora descontado por total, basta lançar o evento de código de cálculo 72 com o valor da base salarial do outro vínculo.

* **Código de Cálculo 72 - Base INSS Outro Emprego**

Evento do tipo Base de Cálculo, Valor e sem incidências. Este evento deverá ser lançado para funcionários que tenham mais de um emprego.

**Observação:** Este evento será utilizado como base de INSS de outros empregos. Se informado, será calculado o INSS proporcional, e o Código de Cálculo 29 que deverá ser descontado no outro emprego.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13134538258071)  
  
Caso contrário, para situações em que o funcionário **não atingiu o teto** , ou seja, o desconto for proporcional deverá ser utilizado o código de cálculo 181 para informar a base e será lançado o evento de código de cálculo 29, onde deverá ser informado o valor que já foi descontado na outra empresa.

* **Código de Cálculo 181 - Base INSS Outro Emprego Desconto Complementar**

Evento do tipo Base de Cálculo, Valor e sem incidências. Informar neste evento a base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13134592854423)

* **Código de Cálculo 29 - INSS Outro Emprego**

Evento do tipo Base de Cálculo, Valor e sem incidências.. Este evento será calculado sobre o valor lançado no código de cálculo 072 (Base de INSS Outro Emprego).  
  
**Observação**

Este código de cálculo somente poderá ser lançado quando não for necessário o cálculo do INSS proporcional.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13134582935703)  
  
O evento CC 181 deve ser lançado quando houver necessidade de desconto do total descontado no outro emprego e não calculado o valor proporcionalizado, portanto na movimentação deve existir apenas os eventos com CC 181 – Base INSS Outro Emprego Desconto Complementar e CC29 - INSS Outro Emprego. O cálculo do sistema procederá conforme os exemplos abaixo:  
  
**1) (Base abaixo do Teto)**

Base de Cálculo INSS na Outra Empresa (CC181): 400,00  
INSS Descontado na Outra Empresa (CC29): 30,60 (7,65%)  
Base de Cálculo INSS na Empresa Atual: 500,00  
Base Total do INSS na Competência: 900,00  
Alíquota devida do Mês de Competência: 9%  
Valor devido para desconto do INSS na Competência: 81,00  
Valor INSS desconta na Empresa Atual (CC03): 50,40 (81,00 – 30,60)  
  
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (400,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC29 (30,60) para o desconto do INSS na empresa (CC03).

**2) (Base acima do Teto)**

Base de Cálculo INSS na Outra Empresa (CC181): 1900,00  
INSS Descontado na Outra Empresa (CC29): 209,00 (11%)  
Base de Cálculo INSS na Empresa Atual: 1000,00  
Base Total do INSS na Competência: 2900,00 (ultrapassou limite para desconto do teto)  
Valor devido para desconto do INSS na Competência: 275,95  
Valor INSS desconta na Empresa Atual (CC03): 66,95 (275,95 – 209,00)  
  
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual. Assim, informando o evento de CC181 com o valor da base de cálculo da outra empresa (1900,00), o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência (neste caso, ultrapassou o limite para desconto do teto) e deduzirá o valor informado no evento de CC29 (209,00) para o desconto do INSS na empresa (CC03).  
  
**Saiba mais**

[RM - FOP - Como calcular funcionário de múltiplos vínculos em coligadas distintas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059947853-RM-FOP-Como-calcular-funcion%C3%A1rio-de-m%C3%BAltiplos-v%C3%ADnculos-em-coligadas-distintas-)

[RM - FOP - Como calcular funcionário de múltiplos vínculos numa mesma coligada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059841373-RM-FOP-Como-calcular-funcion%C3%A1rio-de-m%C3%BAltiplos-v%C3%ADnculos-numa-mesma-coligada-)

[RM - FOP - Como parametrizar o módulo Folha de Pagamento para Múltiplos Vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057899874-RM-FOP-Como-parametrizar-o-m%C3%B3dulo-Folha-de-Pagamento-para-M%C3%BAltiplos-V%C3%ADnculos)

[RM - FOP - Quais são os códigos de cálculo para o cálculo de múltiplos vínculos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058694713-RM-FOP-Quais-s%C3%A3o-os-c%C3%B3digos-de-c%C3%A1lculo-para-o-c%C3%A1lculo-de-m%C3%BAltiplos-v%C3%ADnculos-)
