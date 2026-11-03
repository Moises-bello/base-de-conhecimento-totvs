---
article_id: 4421537813399
category: SIGAEST - CUSTOS
content_hash: 168d6800466448359d34edcf0473be20e204fa787459ffd2c59748b02874e4dd
fetched_at: '2026-06-28T22:39:00.594709+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao executar o Custo
  Médio ocorre HELP A330NVL. Como corrigir?
type: support-article
updated_at: '2022-06-28T17:43:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421537813399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-executar-o-Custo-M%C3%A9dio-ocorre-HELP-A330NVL-Como-corrigir
---

**Dúvida**Ao executar a rotina de Custo Médio gera o help de A330NVL na tabela de processamento CV8, como corrigir?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421528623255/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Esse help é apresentado quando os campos **G1\_NIV** e **G1\_NIVINV** não estão preenchidos. 

Os campos G1\_NIV e G1\_NIVINV são atualizados automaticamente ao sair da rotina de Estrutura dos Produtos (MATA200) quando se é criado uma nova estrutura.

Neste caso é necessário validar na estrutura se esses campos estão preenchidos corretamente. 

Referente ao campo **G1\_NIV** é o nível em que o produto se encontra dentro da estrutura em contagem crescente.  
E o **G1\_NIVINV** se trata do nível invertido, de forma decrescente, partindo de 99.

Caso tiver dúvidas de como preencher corretamente, favor validar juntamente ao time Suporte Protheus de Manufatura para que o time auxilie corretamente.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
