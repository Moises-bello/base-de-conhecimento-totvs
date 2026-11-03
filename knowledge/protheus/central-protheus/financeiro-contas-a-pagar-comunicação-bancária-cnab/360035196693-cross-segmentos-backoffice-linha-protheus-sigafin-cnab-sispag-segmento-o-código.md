---
article_id: 360035196693
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 87b7605dea0c76c3d910aaece504742d5723881563fa647196495b27b58ffa59
fetched_at: '2026-06-28T22:37:55.374913+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB SISPAG - Segmento
  O - Código de Barras de Tributos
type: support-article
updated_at: '2022-11-23T21:54:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035196693-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-SISPAG-Segmento-O-C%C3%B3digo-de-Barras-de-Tributos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00min**  
**Dúvida**Como gerar tributos no **SISPAG** com código de barras?  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
**Solução**Será necessário utilizar o ponto de entrada abaixo para gerar o segmento desejado:

[F240ALMOD - Alteração de conteúdo](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6070983)

**Modelo 13** - pagamento a concessionárias" que é padrão do sistema faz gerar o segmento O, através do ponto de entrada você conseguirá fazer com que modelo referente ao **GNRE (Modelo 91)** se comporte igual ao modelo 13, com isso esse também irá gerar o segmento O.

Utilização do tipo de modelos para geração dos segmentos

[Modelo de bordero para geração de CNAB por segmentos](http://tdn.totvs.com/pages/viewpage.action?pageId=233743712)

**Exemplo:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045047114/mceclip0.png)

**Saiba Mais:**

Segue um artigo que também poderá ajudar quanto a outras configurações que possa querer utilizar.

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - SISPAG - Existem variáveis e funções que possam ser utilizadas na configuração de CNAB/SISPAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004894128-MP-SIGAFIN-CNAB-SISPAG-Existem-vari%C3%A1veis-e-fun%C3%A7%C3%B5es-que-possam-ser-utilizadas-na-configura%C3%A7%C3%A3o-de-CNAB-SISPAG?source=search)

Segue link referente a configurações do SISPAG

[Financeiro - SISPAG](http://tdn.totvs.com/display/public/PROT/SISPAG)
