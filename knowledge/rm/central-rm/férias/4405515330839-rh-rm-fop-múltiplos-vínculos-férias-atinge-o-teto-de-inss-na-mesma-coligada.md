---
article_id: 4405515330839
category: Férias
content_hash: 310b5c63c36b065a9678870a7fc6d69c7bf52c96711a535389435db15d15606f
fetched_at: '2026-06-28T22:46:56.386725+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: Férias atinge o teto de INSS na mesma
  coligada'
type: support-article
updated_at: '2024-10-04T18:34:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405515330839-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-F%C3%A9rias-atinge-o-teto-de-INSS-na-mesma-coligada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26844420256791) Tempo aproximado para leitura: **00:10:01 min****Dúvida**Como lançar férias de múltiplos vínculos quando o INSS atinge o teto na mesma coligada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar esta dúvida, realize os seguintes passos:  
  
**1.** Parametrizar o sistema para o processo de múltiplos vínculos para atender o cálculo de INSS conforme o eSocial.

* Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Configurações | Parametrizador | Folha Normal | Geral;
* O sistema não irá trabalhar mais com chapa centralizadora, para atender o eSocial;
* Marcando esse parâmetro em uma coligada, todas deverão estar marcadas;
* O sistema irá validar a base de calculo através do CPF do funcionário.

Acessando o caminho: **Configurações | Parametrizador | Folha normal | Geral  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26844390376983)**

**2.** Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:  
  
[417 - Base Tributada de INSS Autônomos Múltiplos Vínculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=492700190)  
[418 - Base de INSS Autônomo outro Emprego](http://tdn.totvs.com/pages/viewpage.action?pageId=510508458)  
[428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)  
[429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)  
[430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)  
[431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)  
[432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)  
[433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)  
[434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)  
[435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)  
  
Os códigos de cálculo abaixo deixaram de ser utilizados:  
  
[387 - Base tributada de INSS folha Múltiplos vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)  
[388 - Base tributada de INSS 13º Múltiplos vínculos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)  
  
Todos os eventos citados são do tipo Base/Valor.  
  
**3.** Com a parametrização e o cadastro dos eventos acima, o sistema poderá processar o cálculo de múltiplos vínculos. Veja abaixo um exemplo do cálculo para esta situação, considerando o atingimento do teto de INSS Cálculo:  
  
**Cálculo da Chapa 00100**  
  
No cálculo de férias, o sistema irá calcular a primeira chapa. Neste caso será a chapa 00100, com os seguintes cálculos:  
  
**- INSS**  
Férias no mês: **01/04/2022 a 30/04/2022**  
Dias de férias no mês: **30**  
Total da Base de INSS do 1º mês: **27.777,77**  
INSS: 7,5000% \* Base(1.212,00) = 90,90  
INSS: 9,0000% \* Base(1.215,35) = 109,38  
INSS: 12,0000% \* Base(1.213,68) = 145,64  
INSS: 14,0000% \* Base(3.446,19) = 482,46  
INSS 1o.mês: 828,38  
Valor do evento: **828,38(atingiu o teto)  
  
- IRRF**Base de IRRF:   
Proventos = **27.777,77**  
Descontos = 0,00  
Valor Dedutível = 0,00  
Base Líquida = **27.777,77**  
  
Nro. dependentes de IRRF: 0  
Valor a deduzir por dependentes: 189,59  
Valor do INSS: **828,38**  
Base de IRRF: **26.949,39**  
Limite Superior da Faixa na Tabela de IRRF: 9.999.999.999,00  
Percentual da Faixa na Tabela de IRRF: 27,5000 %  
Valor a Deduzir da Faixa na Tabela de IRRF: 869,36  
Valor do IRRF: Base(26.949,39) \* 27,5000% - 869,36 = 6541,722250  
Valor do evento: **6.541,72****Recibo de férias chapa 00100****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6180029200791)  
  
Envelope  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6180081625239)****Calculo chapa 00101**No calculo de férias, o sistema já calculou a primeira chapa 00100 (que atingiu o teto). Com base nos dados da primeira chapa, o sistema irá realizar o calculo da chapa 00101. Segue cálculo:  
  
**- INSS**Base de INSS:   
Proventos = **5555,56**  
Descontos = 0  
Base Líquida = **5555,56**  
  
Base de INSS Chapa 00100 (Col.1) 1o. Mês: **27.777,77**  
Total da Base de INSS do 1º mês: **33.333,33**  
  
Férias no mês: **01/04/2022 a 30/04/2022**  
Dias de férias no mês: **30**  
Total da Base de INSS do 1º mês: 33.333,33  
INSS: 7,5000% \* Base(1.212,00) = 90,90  
INSS: 9,0000% \* Base(1.215,35) = 109,38  
INSS: 12,0000% \* Base(1.213,68) = 145,64  
INSS: 14,0000% \* Base(3.446,19) = 482,46  
INSS 1o.mês: **828,38**  
  
**INSS descontado na Chapa 1\_00100: 828,38**  
Abatendo INSS já descontado no mês: 828,380000 - 828,38 = 0,000000  
  
Valor do evento: **0,00  
  
- IRRF**  
Base de IRRF:   
Proventos = **5.555,56**  
Descontos = 0,00  
Valor Dedutível = 0,00  
Base Líquida = **5.555,56**  
  
Base de IRRF Chapa 00100: **27.777,77**  
  
Total Base de IRRF: **33.333,33**  
Nro. dependentes de IRRF: 0  
Valor a deduzir por dependentes: 189,59  
  
**INSS descontado na Chapa 00100: 828,38**  
  
Base de IRRF: **32.504,95**  
Limite Superior da Faixa na Tabela de IRRF: 9.999.999.999,00  
Percentual da Faixa na Tabela de IRRF: 27,5000 %  
Valor a Deduzir da Faixa na Tabela de IRRF: 869,36  
Valor do IRRF: Base(32.504,95) \* 27,5000% - 869,36 = 8069,501250  
  
**IRRF descontado na Chapa 00100: 6.541,72**  
  
Abatendo IRRF já descontado: 8.069,50 - 6.541,72 = 1.527,78  
Valor do evento: **1.527,78**  
  
**Recibo de férias chapa 00101**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6180109635991)  
  
**Envelope**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6180118984343)  
  
Como o desconto da chapa anterior atingiu o teto, o sistema deduziu e não descontou INSS da segunda chapa.  
  
**Saiba mais:**[Múltiplos Vínculos que necessitam de Recálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=465386747)  
[Novo Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=546683921)  
[Configurações Gerais - FOP](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263)
