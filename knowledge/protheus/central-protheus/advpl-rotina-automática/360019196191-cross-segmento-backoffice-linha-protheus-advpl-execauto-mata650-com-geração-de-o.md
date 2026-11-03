---
article_id: 360019196191
category: ADVPL - Rotina Automática
content_hash: ae570c9d5df55d779f0f2fc2ca86d8b4e519612a8f36c019f6d4fe1d89d2609f
fetched_at: '2026-06-28T22:40:24.025579+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - EXECAUTO MATA650 com Geração
  de Ops Interm. / Empenhos
type: support-article
updated_at: '2021-12-29T14:52:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019196191-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-EXECAUTO-MATA650-com-Gera%C3%A7%C3%A3o-de-Ops-Interm-Empenhos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Estou criando um fonte para gerar automaticamente a ordem de produção chamando o EXECAUTO da rotina MATA650.

Existe alguma informação adicional que deve ser passada?   
É possível o sistema trazer a tela do empenho onde o usuário poderia alterar alguma informação?

Pois no padrão é possível

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014963451/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014929532/mceclip0.png)  
  
**Ambiente**Protheus – PCP – A partir da versão 11.80  
  
  
**Solução**Essa tela é executada após a inclusão do OP não sendo possível ser executada via execauto, sendo assim será necessário criar uma condição para verificar se o produto tem estrutura e utilizar a rotina automática mata380 com a opção 4 (Alteração)

[**MATA380**](http://tdn.totvs.com/display/PROT/MATA380+-+Ajuste+de+Empenhos)
