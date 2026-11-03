---
article_id: 1500011627062
category: Encargos
content_hash: 6d482be40d012902bad18b5f2aa79e1df611db7fa79e3f01c86322cde378a582
fetched_at: '2026-06-28T22:46:53.235414+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Dedução de salário licença maternidade e 13º salário
  licença maternidade para tomador de serviços'
type: support-article
updated_at: '2025-03-13T10:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011627062-RH-RM-FOP-SEFIP-Dedu%C3%A7%C3%A3o-de-sal%C3%A1rio-licen%C3%A7a-maternidade-e-13%C2%BA-sal%C3%A1rio-licen%C3%A7a-maternidade-para-tomador-de-servi%C3%A7os
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:01:40 min  
  
Dúvida**Como solucionar os erros:  
**100298 - Para o código de recolhimento indicado, o valor da dedução Salário Maternidade só poderá vir informado se houver recolhimento de pessoal administrativo da Empresa** quando todos os funcionários estão no tomador;  
**100299 - Para o código de recolhimento indicado, o valor da dedução 13º Salário Licença Maternidade só poderá vir informado se houver recolhimento de pessoal administrativo da Empresa** quando todos os funcionários estão no tomador.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Ao importar arquivo no SEFIP o validador aponta a seguinte inconsistência:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415838794647/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415807823511/mceclip1.png)  
  
Isso ocorre pois há lançamento de dedução de licença maternidade ou 13º licença maternidade, porém não há nenhum funcionário administrativo. Para os casos onde não haja funcionários administrativos, pois todos estão associados ao tomador, poderá utilizar a seguinte **saída de contorno**:  
  
Retirar no validador o valor de dedução de salário maternidade ou 13º salário maternidade que estava sendo levado para a empresa **CNPJ – Administrativo.**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018767922/mceclip2.png)  
  
Informar o devido valor como dedução para o tomador de serviços no campo **deduções**:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018771182/mceclip3.png)  
  
Desta forma, o valor a deduzir será lançado para o tomador quando não houver funcionários no CNPJ administrativos.

**Importante**Reforçamos que o processo sugerido acima é uma **saída de contorno** para uma situação muito específica, uma vez que o SEFIP não está preparado para receber esta situação de forma nativa. Sendo assim, é necessário validar este processo internamente antes de seguir sua execução.
