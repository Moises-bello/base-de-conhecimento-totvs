---
article_id: 360026673272
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: a98a2eba9701107841386ef2d8d4cf4168c9a89650ab8ab7b6775b8c7167fb62
fetched_at: '2026-06-28T22:36:58.129186+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Movimento no exterior
type: support-article
updated_at: '2022-06-21T18:31:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Movimento-no-exterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como incluir um Câmbio tipo Movimento no Exterior no SIGAEEC e realizar a Baixa/Estorno do título?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 11.80  
  
**Solução**Para realizar o Movimento no Exterior, a premissa é possuir uma Embarque com Data de Embarque vinculada:  
1. Acesse SIGAEEC>Atualizações>Financeiro>Cambio;  
2. Selecione o Processo que deseja realizar o Procedimento e Clique em Alterar;  
3. Selecione a Parcela de Cambio>Outras Ações>Alterar;  
4. Altere o campo Modalidade para 2 - Movimento no Exterior, Salve a tela da Manutenção do Cambio e depois Salve o Cambio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026325132/mceclip0.png)

5. Para realizar a ação de Liquidação do Movimento no Exterior, altere a Parcela de Cambio, agora com a Modalidade Movimento no Exterior, e preencha o Campo Dt. Cred. Ext:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026315871/mceclip1.png)

Na Aba Movimento no Exterior, preencha a informação com o Banco no Exterior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026325572/mceclip2.png)

Clique em Salvar, e depois em Salvar novamente. Note que neste momento, será enviado a Liquidação do Título ao Financeiro.  
6. Para realizar o Estorno da Baixa, selecione a Parcela e clique em Alterar;  
7. Retire a Data de Crédito no Exterior, campo Dt. Cred. Ext:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026316311/mceclip3.png)

Clique em Salvar, e depois novamente em Salvar. Neste momento será enviado a Ação de Estorno da Liquidação ao Financeiro.
