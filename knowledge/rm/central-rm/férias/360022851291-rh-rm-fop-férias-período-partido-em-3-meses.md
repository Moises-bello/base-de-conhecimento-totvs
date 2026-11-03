---
article_id: 360022851291
category: Férias
content_hash: 839cc796b71d6ee5c90816a748f6243cf7ca1f3e9e5c3815c1dd0b015c3ca9c8
fetched_at: '2026-06-28T22:46:56.459676+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: período partido em 3 meses'
type: support-article
updated_at: '2025-01-20T21:36:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022851291-RH-RM-FOP-F%C3%A9rias-per%C3%ADodo-partido-em-3-meses
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**  
Como cadastrar férias que abrangem até 3 competências no sistema?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Para alguns casos específicos será necessário realizar a parametrização descrita neste artigo. Veja abaixo em quais casos será necessário:

1. Quando houver 30 dias de férias iniciados em 31 de janeiro em ano que não é bissexto. Neste caso seria 1 dia em janeiro, 28 dias em fevereiro e 1 dia em março.
2. Quando houver 30 dias de férias desconsiderando feriados. Por exemplo: início em 30 de novembro, desconsiderando feriados de 24/12, 25/12, 31/12 e 01/01, resultaria em 1 dia em novembro, 28 dias em dezembro e 1 dia em janeiro.
3. Férias considerando somente dias úteis, ou seja desconsiderando todos os feriados, sábados e domingos, pode resultar em até 40 dias consecutivos.

**Solução**  
Nas situações descritas é possível que as férias do funcionário atinjam 3 competências. Nestes casos, o sistema solicitará a criação dos eventos de Código de Cálculo 349, 350 e 351, que deverão ser criados segundo a documentação abaixo:

* [Código de Cálculo 349 - INSS Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719459)
* [Código de Cálculo 350 - Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719949)
* [Código de Cálculo 351 - Adicional de 1/3 Férias no Terceiro Mês](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719883)

Além da criação dos eventos associados aos códigos de cálculo acima, o processo deverá ser executado para cálculo e finalização correta das férias, conforme passos abaixo:  
  
1. No primeiro mês, realize o processo normal de cadastro, cálculo e lançamento das férias.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8020656495639/mceclip0.png)  
  
Envelope:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8020694070679/mceclip1.png)  
  
2. No segundo mês, finalize as férias  com as seguintes datas 01/02/2022 e 01/03/2022.. Serão lançadas apenas as bases de código de cálculo 44, 78 e 131. O funcionário permanecerá na situação F - Férias até o próximo mês.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8020730476567/mceclip2.png)  
  
3. No terceiro mês, ao finalizar as férias novamente serão lançados as mesmas bases, código de cálculo 44, 78 e 131, mas demonstrando os valores deste mês. A situação do funcionário será alterada para A - Ativo, e os dados de férias serão atualizados no cadastro do período aquisitivo.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8020732807191/mceclip3.png)  
  
  
**Importante**  
No lançamento do segundo mês, geralmente serão lançados 28 ou 29 dias de férias, por exemplo. Neste caso será necessário lançar um complemento salarial para completar o pagamento dos 30 dias do mês ao funcionário. Normalmente o complemento é pago como salário normal, no lançamento normal da folha da empresa.  
  
**Saiba Mais**  
[RH - RM - FOP - Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento)  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo)
