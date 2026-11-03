---
content_hash: 87cfbeee831894166636dff029ac696fd4f76d8cf745d2ff029db8ea06e2983e
fetched_at: '2026-06-29T00:09:37.087574+00:00'
page_id: '425459558'
product: rm
source: tdn-rm
title: TOTVS Business Analytics - Dimensões/Fatos e Período Inicial e Final de Extração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459558
version: 4
---

**Dimensões/Fatos e Período Inicial e Final de Extração**

---

Conforme o conceito de Data Warehouse os Fatos e Dimensões são tabelas do banco de dados, só que no modelo dimensional adquirem nomes de Fatos e Dimensões de acordo com a função da tabela.  
    
 Um modelo dimensional conta basicamente comuma tabela de fatos central e tabelas dimensionais ligadas diretamente a elas, conforme a imagem abaixo demonstra:  
    
   
 Estes conceitos serão importantes para o mapeamento do agendamento para carga das dimensões e fatos. Com isto já podemos afirmar que tabelas fatos possuem uma quantidade de atualizações maior que as tabelas de dimensões. Além dos conceitos referentes às Dimensões Comuns e as tabelas fatos, existem dois conceitos **essenciais** para a integração, que são:

* Carga Inicial - Start - Período de Extração
* Finish - Período de Extração

O primeiro conceito tem o objetivo de gravar a data inicial referente à extração de dados via conceito.   
    
 O segundo conceito tem o objetivo de gravar a data final referente à extração de dados via conceito.  
    
 Estes conceitos devem ser executados na seguinte ordem:

* O conceito "Carga Inicial - Start - Período de Extração" deve ser o **primeiro** conceito a ser agendado via Job.
* O conceito "Finish - Período de Extração" deve o **último** conceito a ser agendado via Job.

***Observação:***

Sendo assim a execução destes conceitos são **obrigatórias** para o funcionamento da integração.  
    
 Conforme arquitetura utilizada, teremos alguns Data Mart´s e um Data WareHouse (Stage Area), sendo que a ferramenta ETL (Extract/transform/load) utilizada será o Conceito. Com isto foram criados 5 segmentos de dimensões:
