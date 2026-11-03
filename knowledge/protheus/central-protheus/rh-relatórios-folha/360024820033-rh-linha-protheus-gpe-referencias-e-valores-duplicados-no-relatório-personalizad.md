---
article_id: 360024820033
category: RH - Relatórios Folha
content_hash: d28f3a218f1b966c66e7b9427a75a5fa2359072612ca858e2371ad01971125a1
fetched_at: '2026-06-28T22:43:17.569798+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Referencias e valores duplicados no Relatório Personalizado
  GPER106
type: support-article
updated_at: '2024-08-23T01:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024820033-RH-Linha-Protheus-GPE-Referencias-e-valores-duplicados-no-Relat%C3%B3rio-Personalizado-GPER106
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25840352992791) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Referencias e valores duplicados no Relatório Personalizado GPER106.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**O relatório personalizado GPER106 estava trazendo as referencias e valores duplicados:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038888873)  
  
**Solução**Para solução deve ser verificado o **compartilhamento** da Tabela SRV (cadastro de verbas), SQB (cadastro de departamento) e CTT (cadastro de centro de custo), pois caso esteja como **compartilhada** não deve possuir o campo FILIAL preenchida e se estiver como **exclusiva**, o campo FILIAL deve estar preenchido.  
Abaixo um exemplo com erro na tabela SRV:

SRV - Cadastro de verbas  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038889153)  
Compartilhamento da tabela SRV:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039230153)

Se a tabela é compartilhada não deve conter verbas com FILIAL preenchida, isso gera impacto neste relatório especificamente.  
No caso deixar somente as verbas da FILIAL em branco.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038889353)

**Sabia mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
