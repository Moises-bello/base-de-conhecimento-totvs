---
article_id: 360034656653
category: ADVPL - Classe e Função
content_hash: 45891ce860ce1a907501a22ceac8746699f9e52594afaf81be7dc7d5361ee956
fetched_at: '2026-06-28T22:40:17.109590+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Qual a finalidade
  da utilização do parâmetro lSoftSeek na função DbSeek
type: support-article
updated_at: '2022-03-28T13:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034656653-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-a-finalidade-da-utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-lSoftSeek-na-fun%C3%A7%C3%A3o-DbSeek
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**  
Qual a finalidade da utilização do parâmetro lSoftSeek na função DbSeek ( ) ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Quando enviamos por meio da função DbSeek uma chave de busca para o banco de dados, internamente ele realiza um LIKE('XXX%') , desta forma, caso seja encontrado um valor que atenda aos caracteres envolvidos até o momento, será retornado verdadeiro:

![](https://totvssuporte.zendesk.com/attachments/token/ksIhK7k011yFP6F1aZramPbzZ/?name=inline1386924414.png)​

![](https://totvssuporte.zendesk.com/attachments/token/2b1T3OUg6GKo90x9doXpf95Hc/?name=inline1443353058.png)​  
  
No que se refere ao parâmetro lSoftSeek, ele tem como finalidade encontrar valores aproximados, veja o exemplo abaixo:  
  
Caso lSoftSeek esteja com valor falso e for informado um conjunto de valores **inválidos** para busca, a função irá retornar falso e posicionar no último registro do arquivo de trabalho:

![](https://totvssuporte.zendesk.com/attachments/token/esJrM4x8L16afXCqSrCN7iPtf/?name=inline-1761294132.png)​  
  
Contudo, caso lSoftSeek esteja com valor verdadeiro e seja informado um conjunto de valores **inválidos** para busca, a função também irá retornar falso, porém irá posicionar no registro mais próximo do valor informado:

![](https://totvssuporte.zendesk.com/attachments/token/1QzBQMwKjb6isngj1UcZjMwas/?name=inline-293880189.png)​  
  
Desta forma, caso visualizado o estado do arquivo de trabalho, será possível ver os dados do posicionamento:

![](https://totvssuporte.zendesk.com/attachments/token/vL4mXANC1gQ8PrksoTTqjDcwY/?name=inline-1845470469.png)​  
  
Diferente de quando lSoftSeek está com valor falso:

![](https://totvssuporte.zendesk.com/attachments/token/pyX8Mns3oI2A4XBMhOtJowgsm/?name=inline-1602763666.png)​  
  
**Saiba mais**  
[SoftSeek() e procura com chaves parciais](http://tdn.totvs.com/display/framework/SoftSeek%28%29+e+procura+com+chaves+parciais)  
[DBSeek](http://tdn.totvs.com/display/tec/DBSeek)
