---
article_id: 37277760630807
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 640c1fe19ff77e219b6bdaca66ec66096065381b16ee9855297dd55cd4a7d5fb
fetched_at: '2026-06-28T22:37:22.951191+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help F7QCOMP ao tentar
  Excluir ou Alterar na Manutenção de Contrato no Gestão de Contratos
type: support-article
updated_at: '2025-12-26T19:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37277760630807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-F7QCOMP-ao-tentar-Excluir-ou-Alterar-na-Manuten%C3%A7%C3%A3o-de-Contrato-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37277760627351) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao tentar Excluir ou manipular um Adiantamento do contrato do Gestão de Contrato corre o Help " F7QCOMP - Inconsistência no Dicionário de Dados " :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37277760627607)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Verificando os fontes padrões do Protheus quanto ao help F7QCOMP, observa-se a sua ocorrência nos processos do Módulo Financeiro, onde ele ocorre quando no ambiente em questão existe diferença de compartilhamento entre as tabelas FK7 e F7Q, relativas ao módulo Financeiro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37277760627863)

Dessa forma, um analise que pode ser realizada é essa de comparação dos compartilhamentos dessas tabelas, e o devido ajuste de compartilhamento caso estejam de fato diferentes.  
   
   
Caso persista, ou necessite de apoio referente a essas tabelas do módulo Financeiro. orientamos o contato junto ao suporte ao SIGAFIN, que é a equipe que da apoio a elas e fontes no qual ocorre o help em questão.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
