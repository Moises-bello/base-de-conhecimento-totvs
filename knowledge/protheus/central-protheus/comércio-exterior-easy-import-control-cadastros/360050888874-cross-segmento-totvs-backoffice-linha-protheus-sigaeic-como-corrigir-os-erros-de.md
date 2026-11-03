---
article_id: 360050888874
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: cf994c7d1118321398520f4767a35d9c438c428b5a4e5980493a6c6cf167bb39
fetched_at: '2026-06-28T22:39:52.179416+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como corrigir
  os erros de Data width error - Field
type: support-article
updated_at: '2022-04-27T20:17:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050888874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-corrigir-os-erros-de-Data-width-error-Field
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como corrigir os erros de ***Data width error - Field***?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080032213/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 11.80.  
  
**Solução**Os erro de estouro de tamanho de campo ( ***Data width error - Field:***) estão ocorrendo devido ao numero informado no cadastro de via de transporte nos valores de frete por Kg.  
Informe um valor de 1, caso não tenha um valor especificado, pois este são utilizados para os cálculos do titulo de previsão e esta retornando valores muitos grandes (**995999999999.900390**), que não esta sendo suportados pelos campos.  
  
Para ajuste acesse:  
1° O módulo SIGAEIC em Atualizações \ Cadastros \ Vias de Transporte (EICCV100).   
2° Posicione na via de transporte, selecione alterar.  
3° Posicione em Frete p/KG , selecione enter.  
4° Após modifique os dados conforme orientado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078911194/mceclip1.png)  
Informe:

```
Ate= 1  
Valor p/Kg1 = 1
```
