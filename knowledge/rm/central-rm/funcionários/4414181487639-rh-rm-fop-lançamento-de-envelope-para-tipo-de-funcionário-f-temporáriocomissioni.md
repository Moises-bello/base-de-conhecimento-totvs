---
article_id: 4414181487639
category: Funcionários
content_hash: a7f1935626ca5555f215fbe7f1ffcd20d102cdc491de9a4624490f85a5c7a26b
fetched_at: '2026-06-28T22:47:03.369563+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Lançamento de envelope para Tipo de Funcionário F - Temporário/Comissionista
type: support-article
updated_at: '2025-03-13T11:10:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414181487639-RH-RM-FOP-Lan%C3%A7amento-de-envelope-para-Tipo-de-Funcion%C3%A1rio-F-Tempor%C3%A1rio-Comissionista
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Quando o Tipo de Funcionário é cadastrado com o tipo F, o campo do salário não é permitido salvar, com isso ao gerar o envelope o mesmo retorna com o valor zerado.    
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O sistema não irá retornar o valor do campo informado, pois o evento de Código de Cálculo 1 Horas Normais e 2 Dias Trabalhados buscam da tabela **PFUNC** do campo salário.  
  
**Solução**  
O lançamento do envelope será através de um evento de Código de Cálculo 0 composto por fórmula, que deve ser criado pela empresa. A informação do salario pode ser informado no campo **Descrição de salario variável**, mas para que seja lançado no envelope, deve ser criado a fórmula. O evento criado será informado em códigos fixos, dentro do cadastro do funcionário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414211374103/mceclip0.png)

**Importante**O suporte padrão não auxilia na criação de fórmulas, na documentação abaixo em **saiba mais** disponibilizamos algumas orientações e exemplos de fórmulas.   
  
**Saiba mais**  
[Informações Contratuais](https://tdn.totvs.com/pages/releaseview.action?pageId=452719370)  
[Fórmulas - FOP](https://tdn.totvs.com/pages/releaseview.action?pageId=452718597)
