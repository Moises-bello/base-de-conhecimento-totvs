---
article_id: 360020836831
category: MDe - Manifesto do Destinatario
content_hash: 7f6fb35898a04f6bc8185526677845e42a9adb4113161269f3c990d63f71d7bd
fetched_at: '2026-06-28T22:40:09.259514+00:00'
product: protheus
section_id: 1500001549162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDE - Exportar XML  na
  rotina de MDe
type: support-article
updated_at: '2026-01-12T22:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020836831-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDE-Exportar-XML-na-rotina-de-MDe
---

**Dúvida**  
Como exportar XML das notas pela rotina SPEDMANIFE?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**  
1. Acessar no browser da Manifestação do Destinatário ( SPEDMANIFE ) Em outras ações -> **Exportar**

Para exportação serão consideradas **somente** as notas com status de "**Confirmação**" e "**Ciência**" da Operação.

**Importante:**

Para exportação do MDe é necessário verificar as informações abaixo:

 - Notas com ***registro na SPED156***

 - Notas com ***registro na SPED150 e SPED154*** ( Com evento registro e vinculado a NF-e) Apenas de ciência da operação e confirmação da operação.

 - Notas incluídas manualmente ou manifestadas pela rotina MATA103 não geram registro na SPED156 por isso não exporta o XML

**Notas incluídas manualmente na SPEDMANIFE e notas manifestadas na rotina MATA103 geram registro apenas na C00 do Protheus**

 - Exportação apenas na versão da ***manifestação 1.01***

**-** Para a exportação as notas devem ter ***até 90 dias***

* **Rejeição 632:**  
  Verificar se NF-e está no prazo de download, 90 dias da data de recebimento da NF-e no Ambiente Nacional

**Notas Canceladas e denegadas não são exportadas:**

* **Rejeição 653:**  
  NF-e Cancelada, arquivo NF-e indisponível para download

* **Rejeição 654:**  
  NF-e Denegada, arquivo NF-e indisponível para download

**Na rotina tem um campo de Sit. NFe:**  
Autorizado = 1  
Denegada = 2  
Cancelado = 3

* **Saiba mais:**  
  Caso seja exportação de NFe, temos a **documentação do link abaixo:**  
  [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Exportação de XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052081154)

Obs: A exportação do xml manifestado não fica no Protheus, sistema apenas faz um solicitação para a Sefaz, é ela que libera o arquivo para ser baixado.
