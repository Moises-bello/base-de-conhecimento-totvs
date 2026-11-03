---
article_id: 11469310117143
category: PCO - Integrações
content_hash: c978455cbd7a7a1ff40d6423fbbf9ce3115f61933b42d10d10aebeeee130e5ec
fetched_at: '2026-06-28T22:37:10.184876+00:00'
product: protheus
section_id: 1500001550902
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA500 - Envio de
  E-mail na geração e Aprovação da Contingencia '
type: support-article
updated_at: '2023-01-10T13:38:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11469310117143-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA500-Envio-de-E-mail-na-gera%C3%A7%C3%A3o-e-Aprova%C3%A7%C3%A3o-da-Contingencia
---

**Dúvida**Como Configurar o ambiente para Envio de E-mail no momento da geração e aprovação da contingencia.

**Ambiente**Cross Segmento - Backoffice Linha Protheus -Planejamento e Controle Orçamentário.

#### **Solução:**

No sistema existe o parâmetro MV\_PCOEMCT que permite enviar E-mails informativos no momento da geração e aprovação da Contingencia..  
  
Configurar o parametro MV\_PCOEMCT com .T.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11468925774743)

Após configuração do parametro é necessário realizar a configuração do E-mail Proxy pelo configurador conforme a documentação:

[Configurar o SMTP para envio de relatórios por e-mail](https://tdn.totvs.com.br/pages/releaseview.action?pageId=271166884)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11469029319831)

**OBS:** Esta configuração é tratada pelo time de Framework caso tenha alguma duvida poderá contata-los que irão lhe auxiliar na configuração.

Após as configurações acima será apresentado a tela para envido do E-mail informativo na geração e Aprovação da Contingencia:

**Geração:**

Exemplo de Inclusão de Pedido de Compras (MATA121):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11469153097239)

**Aprovação:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11469214590999)

Ao apresentar esta tela basta selecionar enviar e o E-mail será enviado.

**Saiba mais:**

[Parâmetros PCO Planejamento e Controle Orçamentario](https://tdn.totvs.com/pages/releaseview.action?pageId=312175430)

[Parametro MV-PCOEMCT](https://tdn.totvs.com/pages/releaseview.action?pageId=6073482)
