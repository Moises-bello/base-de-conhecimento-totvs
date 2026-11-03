---
article_id: 8605993329047
category: TAF - GIA
content_hash: 57cad9dfc5b006859a77895cd17b525a7f509c2188d38e2bc42a7ff87fe84864
fetched_at: '2026-06-28T22:41:32.342888+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - TAF - Nova GIA -
  Erro Tamanho do registro inválido CR = 28
type: support-article
updated_at: '2022-09-02T16:40:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8605993329047-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-TAF-Nova-GIA-Erro-Tamanho-do-registro-inv%C3%A1lido-CR-28
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Na validação da **GIA** ocorre o erro de validação: **Erro Tamanho do registro inválido CR = 28**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - A partir da versão P12.1.25  
  
**Causa**Esse incidente ocorre porque a descrição do subitem está incorreta na **Apuração do ICMS**  
  
**Solução**Este registro é gerado conforme o código **ECREDAC** informado na **Apuração do ICMS** (r**otina MATA953) no Protheus.**

Para que o dado seja apresentada corretamente na **GIA**, deve ser informado **Código de Subitem** válido e **Código do Visto eletrônico de 12 dígitos** no campo **Descrição**.

De acordo com o manual da **GIA,** a informação que deve ser gerada no código de subitem é o código de autorização de ressarcimento:  
  
![](https://totvssuporte.zendesk.com/attachments/token/8uqpopS1oW6FSZJN1rnEapLlB/?name=inline42036384.png)​  
​<https://portal.fazenda.sp.gov.br/servicos/gia/Downloads/pre_formatado_ngia_v0210_gia0801.pdf>

Dessa forma realize o seguinte processo:

1. Acesse a rotina **MATA953 (Apuração do ICMS)**

2. Informe o **Código de Subitem, Código de Lançamento** e no campo **Descrição** informe o Código correspondente ao **Visto Eletrônico,** conforme exemplo abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8608561978775/mceclip3.png)

3. Caso exista mais de um código que precise ser inserido, informe o **Código de Subitem** na **Apuração de ICMS** da seguinte forma:  
  
007.40 1

007.40 2

007.40 3

4 -Após realizar este processo, refaça a **Apuração do ICMS**,  extração e integração para o **TAF** e gere novamente o arquivo da **GIA**.
