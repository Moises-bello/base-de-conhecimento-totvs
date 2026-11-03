---
article_id: 6179514370455
category: Férias
content_hash: 55778f1aaa019c76ba42ef8bae9290c9a04f4f276319e2b214ef7a62f396fdbb
fetched_at: '2026-06-28T22:46:56.288400+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: Férias não atinge o teto de INSS na mesma
  coligada'
type: support-article
updated_at: '2025-01-22T20:49:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6179514370455-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-F%C3%A9rias-n%C3%A3o-atinge-o-teto-de-INSS-na-mesma-coligada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29429836663703) Tempo aproximado para leitura: **00:09:30 min****Dúvida**Como lançar férias de múltiplos vínculos quando o INSS não atinge o teto na mesma coligada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar esta dúvida, realize os seguintes passos:  
  
**1.**Parametrizar o sistema para o processo de múltiplos vínculos para atender o cálculo de INSS conforme o eSocial.

* Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Configurações | Parametrizador | Folha Normal | Geral;
* O sistema não irá trabalhar mais com chapa centralizadora, para atender o eSocial;
* Marcando esse parâmetro em uma coligada, todas deverão estar marcadas;
* O sistema irá validar a base de calculo através do CPF do funcionário.

Acessando o caminho: **Configurações | Parametrizador | Folha normal | Geral  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29429836665239)**

**2.**Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:  
  
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
  
**3.**Com a parametrização e o cadastro dos eventos acima, o sistema poderá processar o cálculo de múltiplos vínculos. Veja abaixo um exemplo do cálculo para esta situação, considerando não atinge o teto de INSS Cálculo:  
  
**- Cálculo da Chapa 00098**  
  
No cálculo de férias, o sistema irá calcular a primeira chapa. Neste caso será a chapa 00050, com os seguintes cálculos:  
  
**INSS**  
Férias no mês: **01/04/2022 a 30/04/2022**  
Dias de férias no mês: **30**  
Total da Base de INSS do 1º mês: **5.555,56**  
INSS: 7,5000% \* Base(1.212,00) = 90,90  
INSS: 9,0000% \* Base(1.215,35) = 109,38  
INSS: 12,0000% \* Base(1.213,68) = 145,64  
INSS: 14,0000% \* Base(1.914,53) = 268,03  
INSS 1o.mês: 613,95  
Valor do evento: **613,95  
  
IRRF**  
Nro. dependentes de IRRF: 0  
Valor a deduzir por dependentes: 189,59  
Valor do INSS: **613,95**  
Base de IRRF: **4.941,61**  
Limite Superior da Faixa na Tabela de IRRF: 9.999.999.999,00  
Percentual da Faixa na Tabela de IRRF: 27,5000 %  
Valor a Deduzir da Faixa na Tabela de IRRF: 869,36  
Valor do IRRF: Base(4.941,61) \* 27,5000% - 869,36 = 489,582750  
Valor do evento: **489,58**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6179214737559)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6179502111895)  
  
**- Calculo chapa 00099**No calculo de férias, o sistema já calculou a primeira chapa 00098. Com base nos dados da primeira chapa, o sistema irá realizar o calculo da chapa 00099. Segue cálculo:  
  
**INSS**  
Base de INSS Chapa 00098 (Col.1) 1o. Mês: **5.555,56**  
Total da Base de INSS do 1º mês: **9.722,23**  
  
Férias no mês: **01/04/2022 a 30/04/2022**  
Dias de férias no mês: **30**  
Total da Base de INSS do 1º mês: **9.722,23**  
INSS: 7,5000% \* Base(1.212,00) = 90,90  
INSS: 9,0000% \* Base(1.215,35) = 109,38  
INSS: 12,0000% \* Base(1.213,68) = 145,64  
INSS: 14,0000% \* Base(3.446,19) = 482,46  
INSS 1o.mês: **828,38**  
  
**INSS descontado na Chapa 1\_00098: 613,95**  
Abatendo INSS já descontado no mês: 828,380000 - 613,95 = 214,430000  
Valor do evento: **214,43  
  
IRRF**  
Base de IRRF Chapa 00098: **5.555,56**  
  
Total Base de IRRF: **9.722,23**  
Nro. dependentes de IRRF: 0  
Valor a deduzir por dependentes: 189,59  
Valor do INSS: **214,43**  
  
INSS descontado na Chapa 00098: **613,95**  
  
Base de IRRF: **8.893,85**  
Limite Superior da Faixa na Tabela de IRRF: 9.999.999.999,00  
Percentual da Faixa na Tabela de IRRF: 27,5000 %  
Valor a Deduzir da Faixa na Tabela de IRRF: 869,36  
Valor do IRRF: Base(8.893,85) \* 27,5000% - 869,36 = 1576,448750  
  
IRRF descontado na Chapa 00098: **489,58**  
  
Abatendo IRRF já descontado: 1.576,44 - 489,58 = 1.086,86  
Valor do evento: **1.086,86  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6179355962903)**Como o desconto da chapa anterior não atingiu o teto, o sistema deduziu já descontado de INSS da segunda chapa para realizar o desconto até o teto.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6179451996311)  
  
  
  
**Saiba Mais**[Múltiplos Vínculos que necessitam de Recálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=465386747)  
[Novo Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=546683921)  
[Configurações Gerais - FOP](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719263)
