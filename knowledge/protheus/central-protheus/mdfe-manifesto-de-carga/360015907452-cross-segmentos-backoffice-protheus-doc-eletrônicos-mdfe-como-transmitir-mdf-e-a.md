---
article_id: 360015907452
category: MDFe - Manifesto de Carga
content_hash: 4d470f7d6778cf15e4afa55cb0da5e03f62404e01ab742b5f6bba813fe1c2a5f
fetched_at: '2026-06-28T22:40:08.263985+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Como transmitir
  MDF-e a partir de um documento de entrada sem atualizar estoque, fiscal, etc ?
type: support-article
updated_at: '2025-06-17T17:23:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015907452-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Como-transmitir-MDF-e-a-partir-de-um-documento-de-entrada-sem-atualizar-estoque-fiscal-etc
---

**Dúvida**Como transmitir MDF-e a partir de um documento de entrada sem atualizar estoque, fiscal, etc ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

1. Foi realizado ajuste na rotina de documento de entrada **MATA103** com a validação do parâmetro **MV\_BLOQ103.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410731745815)**

2. Este parâmetro funciona em conjunto com o pergunte **"Bloq. Movimento" dos parâmetros F12 do documento de entrada** e permite que seja incluída uma nota de entrada com formulário próprio igual a "Não" com bloqueio de movimentos (legenda roxa)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410719386391)

* **Saiba mais:**Devem ser realizados os **procedimentos dos links abaixo:**Boletim Inclusão de nota com bloqueio de movimentos e form. próprio = Não  
    
  <http://tdn.totvs.com/pages/releaseview.action?pageId=325848537>

* Para verificar as **correções realizadas pelo desenvolvimento**  e baixar o pacote atualizado dos fontes a **expedição** continua dos **documentos eletrônicos MDFe**  será liberado através do link abaixo:  
    
  <https://tdn.totvs.com/pages/releaseview.action?pageId=525010692>

**Caso o link acima não abra copie e cole em outra aba do Navegador.**

* Nesse **link acima** para baixar clique na versão, conforme o print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32682863528471)

* Para aplicar o **RDMAKE da rotina do MDF-e deve estar compilado,  *MDFesefaz e o DAMDFe* baixar o fonte pelo link abaixo:**

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download?e=1152113)
