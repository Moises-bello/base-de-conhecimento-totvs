---
article_id: 36323502116631
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: aa9ad491aea4ee82242db02e037df4c4f04631328f15c0e1d1a664647a31966d
fetched_at: '2026-06-28T22:40:34.121260+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA080 - Experessão
  ADVPL ultrapassa o limite caracteres do campo no Lançamento Padrão.
type: support-article
updated_at: '2025-11-14T18:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36323502116631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Experess%C3%A3o-ADVPL-ultrapassa-o-limite-caracteres-do-campo-no-Lan%C3%A7amento-Padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36323506813463) Tempo aproximado para leitura: 00**:05 min**  
  
**Dúvida**  
Expressão ADVPL ultrapassa o limite máximo dos campos do Lançamento Padrão.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Contabilidade Gerencial - Todas as versões

**Solução**

Quando a expressão **ADVPL** ultrapassa o limite do campo do Lançamento Padrão (LP), poderá efetuar a chamada de uma função de usuário, e nesta função efetue os tratamentos necessários retornando o conteúdo conforme a sua regra.   
   
Conforme exemplo abaixo, pode criar a ***User Function***, compilar no ambiente e acionar a chamada da mesma no campo do Lançamento Padrão (LP) que receberá o retorno:  
![](https://totvssuporte.zendesk.com/attachments/token/yhWRXek8fBrk6Kxm7pCqMq2v2/?name=image.png)

**Observação**: O suporte padrão não avalia regras específicas criadas, somente o funcionamento básico da rotina padrão e se ela cumpre seu objetivo.

**Dicas sobre desenvolvimento nas plataformas TOTVS acesse:**  
<https://developers.totvs.com/>   
[https://devforum.totvs.com.br](https://devforum.totvs.com.br/)
