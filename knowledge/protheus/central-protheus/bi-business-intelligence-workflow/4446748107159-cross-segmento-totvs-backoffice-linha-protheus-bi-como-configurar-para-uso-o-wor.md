---
article_id: 4446748107159
category: BI - Business- Intelligence - Workflow
content_hash: dac216a0c4f0045f687ff1571e1a9c65c4ab269b6f16e93b48c0d5d09b7b9b0f
fetched_at: '2026-06-28T22:37:03.097255+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Como configurar para
  uso o Workflow via Configurador
type: support-article
updated_at: '2025-08-05T14:17:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4446748107159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Como-configurar-para-uso-o-Workflow-via-Configurador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28220016535831)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como configurar para uso o *Workflow* via Configurador (SIGACFG) ?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – BI – Workflow - Todas as versões.  
  
**Solução**  
1- Configure a caixa de saída do e-mail dentro de **"Contas de e-mail"** no Configurador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28220016540311)

2- Deixe também o processo funcional dentro de **"Parâmetros do *Workflow*"** no Configurador. Copie também os dois arquivos **Html**que lhe enviaremos para dentro da Pasta **"*Workflow*"** na **Protheus Data**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28220016543255)  
  
3- É importante validar o "**appserver.ini**" conforme a imagem abaixo:  
  
**Exemplo do appserver.ini para parametrização do *Workflow*:**  
**![](https://totvssuporte.zendesk.com/attachments/token/RfA3cmCRJR363DN2HhLB64mZI/?name=inline-271514886.png)**

```
​Neste exemplo deixamos o [Schedulerwf] comentado, pois nossos testes são manuais e não via job.   
Veja também por gentileza a chave do [HTTP] em seu AppServer.ini
```

**Importante:**

A **TOTVS** permite customizar o processo de **WorkFlow** da maneira que o cliente desejar, ou seja, com as regras estabelecidas pela própria organização, existem muitas formas de customização dos processos.

Nosso suporte atua com a validação de envio, processamento e retorno do **WorkFlow**.  
O desenvolvimento específico da regra fica a critério do cliente.

Disponibilizamos neste artigo fonte com exemplo Padrão da **TOTVS**, para validação da ferramenta dentro do ambiente; neste exemplo, será possível confirmar as configurações de envio e processamento de seu sistema.  
Resumidamente, trata-se de um código de exemplo, com o objetivo apenas de testar o envio e recebimento da mensagem. O fonte também pode servir como base para as customizações do processo.  
Para também o auxiliar, disponibilizamos neste artigo além dos arquivos e fonte, vídeo explicativo.

**Contas de e-mail:**
