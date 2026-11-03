---
article_id: 4414665366807
category: Folha Mensal
content_hash: b193459796a251f68424fa0c2c4d6497faff564a0f0927993133f4f101168048
fetched_at: '2026-06-28T22:46:59.301570+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: INSS 13º outro emprego'
type: support-article
updated_at: '2024-10-04T18:37:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414665366807-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-INSS-13%C2%BA-outro-emprego
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:10 min****Dúvida**Como fazer para que o sistema considere o INSS de outro emprego relacionado ao 13º salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Os eventos de INSS de outro emprego utilizados no lançamento da folha normal não poderão ser utilizados para o lançamento de INSS de 13º Salários de outro emprego. Para que o sistema considere o valor corretamente, será necessário utilizar dois eventos, descritos abaixo:  
  
**Código de cálculo 144** - **INSS 13º Salário outro emprego**  
Base de Cálculo do tipo valor com porcentagem de incidência igual a zero.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12266428402711)  
  
**Código de cálculo: 182 - Base INSS 13º Outro Emprego Desconto Complementar**Evento do tipo Base de Cálculo, Valor e sem incidências. Informar neste evento a base de cálculo utilizada na outra empresa para o cálculo do desconto do INSS de 13º Salário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12266423062167)  
  
Este evento deve ser lançado quando houver necessidade de desconto do total descontado no outro emprego e não calculado o valor proporcionalizado, portanto na movimentação devem existir apenas os eventos com [182 - BASE INSS 13º OUTRO EMPREGO DESCONTO COMPLEMENTAR](https://tdn.totvs.com/pages/viewpage.action?pageId=452719852) e [144 - INSS 13º Salário outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718221).   
  
O cálculo do sistema procederá conforme o exemplo abaixo:  
  
**Exemplos:**1. **Base abaixo do Teto**  
Base de Cálculo INSS na Outra Empresa - CC182: 400,00  
INSS Descontado na Outra Empresa- CC144: 30,60 -> 7,65%  
Base de Cálculo INSS na Empresa Atual: 500,00  
Base Total do INSS na Competência: 900,00  
Alíquota devida do Mês de Competência: 9%  
Valor devido para desconto do INSS na Competência: 81,00  
Valor INSS desconta na Empresa Atual - CC102 ou CC11: 50,40 ->81,00 – 30,60  
  
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual.   
  
Assim, informando o evento de CC182 com o valor da base de cálculo da outra empresa - 400,00, o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência e deduzirá o valor informado no evento de CC144 - 30,60 - para o desconto do INSS na empresa - CC102 ou CC11.  
  
2. **Base acima do Teto**  
Base de Cálculo INSS na Outra Empresa- CC182: 1900,00  
INSS Descontado na Outra Empresa- CC144: 209,00 -> 11%  
Base de Cálculo INSS na Empresa Atual: 1000,00  
Base Total do INSS na Competência: 2900,00 -> ultrapassou limite para desconto do teto  
Valor devido para desconto do INSS na Competência: 275,95  
Valor INSS desconta na Empresa Atual- CC102 ou CC11: 66,95 -> 275,95 – 209,00  
  
Neste caso, a outra empresa descontou o INSS do empregado desconhecendo a base de cálculo do INSS da empresa atual.   
  
Assim, informando o evento de CC182 com o valor da base de cálculo da outra empresa -1900,00, o sistema calculará o total da base de cálculo do INSS, identificará o valor da alíquota devida do mês da competência. Neste caso, ultrapassou o limite para desconto do teto e deduzirá o valor informado no evento de CC144 - 209,00 - para o desconto do INSS na empresa- CC102 ou CC11.  
  
**Importante**O lançamento dos eventos, deverá ser por meio de código fixo, manual ou Eventos Adicionais.  
  
**Saiba Mais**  
[RH - RM - FOP - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020075531-RM-FOP-13%C2%BA-Sal%C3%A1rio)
