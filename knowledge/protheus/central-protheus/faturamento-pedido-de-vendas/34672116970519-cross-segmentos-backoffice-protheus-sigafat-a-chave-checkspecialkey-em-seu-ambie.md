---
article_id: 34672116970519
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d952fa89e5ee2075615453a4d02a6bb5c6db7089cf91c3e258a0f1cd6e6b112a
fetched_at: '2026-06-28T22:38:39.618033+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - A chave CheckSpecialKey em
  seu ambiente está desligada, você deve liga-la para seu uso da seção [GENERAL]
type: support-article
updated_at: '2025-09-03T17:22:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34672116970519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-A-chave-CheckSpecialKey-em-seu-ambiente-est%C3%A1-desligada-voc%C3%AA-deve-liga-la-para-seu-uso-da-se%C3%A7%C3%A3o-GENERAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34672102013719) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
No módulo de Faturamento, ao tentar preparar o documento de saída e selecionar a numeração da nota, ocorre o seguinte erro:  
"**A chave CheckSpecialKey em seu ambiente está desligada. Você deve ativá-la para utilizar esta funcionalidade na seção [GENERAL], em BACKOFFICE.STOCK.NEWPROXNUM.VALIDSPECIAKEY.**"  
Esse incidente interrompe a execução da aplicação.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.1.2410.  
  
**Causa**  
Esse incidente ocorre porque, na parametrização do **Appserver**, na seção **[GENERAL]**, a chave **CHECKSPECIALKEY** está definida com o valor **"0"**.

**Solução**  
Está sendo implementada na **LIB** uma validação de **Controle de Numeração**, que tem como objetivo verificar se o ambiente está corretamente configurado com a chave **SpecialKey**.

Caso a configuração não esteja adequada, o sistema emitirá uma notificação informando a necessidade de ativação da chave e interromperá a operação em andamento. Essa medida visa garantir a integridade dos dados e prevenir eventuais inconsistências futuras.

Enquanto essa validação não estiver completamente implementada na **LIB**, a ausência da chave **SpecialKey** ou a definição da chave **CheckSpecialKey** com o valor `0` poderá resultar na interrupção da execução da aplicação, com a geração do seguinte erro no **error.log**:

“**A chave CheckSpecialKey em seu ambiente está desligada. Você deve ativá-la para seu uso na seção [GENERAL]**.”

Para garantir o correto funcionamento do sistema até a conclusão da implementação, recomenda-se configurar a chave `CHECKSPECIALKEY` com o valor `1`, ou simplesmente removê-la da seção `[GENERAL]` no arquivo de configuração do Appserver.

Saiba mais:

[**2024 - 31/10 Parâmetro MV\_DOCSEQ**](https://tdn.totvs.com/pages/releaseview.action?pageId=840763998)

[**DT Proxnum | Validação SpecialKey**](https://tdn.totvs.com/pages/releaseview.action?pageId=966221046)
