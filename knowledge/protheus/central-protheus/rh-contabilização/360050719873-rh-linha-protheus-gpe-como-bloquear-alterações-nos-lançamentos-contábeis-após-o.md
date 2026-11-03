---
article_id: 360050719873
category: RH - Contabilização
content_hash: c77c3ca5ffdd1ebc3e83f0e48848180830b942983a65adf7f3885c58dc4a4bc0
fetched_at: '2026-06-28T22:43:46.068072+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como bloquear alterações nos lançamentos contábeis
  após o processamento da contabilização no GPE
type: support-article
updated_at: '2021-06-07T13:27:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050719873-RH-Linha-Protheus-GPE-Como-bloquear-altera%C3%A7%C3%B5es-nos-lan%C3%A7amentos-cont%C3%A1beis-ap%C3%B3s-o-processamento-da-contabiliza%C3%A7%C3%A3o-no-GPE
---

**Dúvida**Como bloquear alterações nos lançamentos contábeis após o processamento da contabilização no GPE  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução:**Acesse Configurador->Base de Dados->Dicionário->Base de Dados->Parâmetros:

1) Faça a busca do parâmetro MV\_ALTLCTO:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076898313/mceclip3.png)

2) Altere o conteúdo do parâmetro para "N":  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076895573/mceclip2.png)

3) Efetue o processamento da contabilização através da rotina GPEM110:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076899013/mceclip4.png)

4)  Verifique que não é possível alterar os lançamentos contábeis apresentados em tela: ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075782834/mceclip5.png)
