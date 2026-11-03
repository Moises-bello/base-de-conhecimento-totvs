---
article_id: 35268005267735
category: NFe - Nota Fiscal Eletrônica
content_hash: c0b345a5511deb11cf32655e5b96f450607563c0c30b2640d660d89b8ffb1e26
fetched_at: '2026-06-28T22:40:06.921854+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Rejeição 865 ocorre
  quando o somatório do valor dos pagamentos Tag vPag
type: support-article
updated_at: '2025-09-29T13:41:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35268005267735-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Rejei%C3%A7%C3%A3o-865-ocorre-quando-o-somat%C3%B3rio-do-valor-dos-pagamentos-Tag-vPag
---

**Dúvida**  
Como realizar todas as atualizações e configurações para de adequar a **Nota Técnica 2024.003 v1.06?**  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
A rejeição **865** ocorre quando o somatório do valor dos pagamentos *Tag* **vPag - id:YA03 é menor**que o total da nota *Tag***- vNF - id:W16.**

Esta regra não se aplica para Nota Fiscal de Ajuste, *Tag* **finnfe = 3 - id:B25**e para Nota Fiscal de Devolução **finnfe=4.**  
  
**Solução**

Conforme publicação da NT2025.001\_v1.02 no dia de 02/09/2025, a validação/rejeição abaixo **foi adiadas:**  
  
 

* Alterada RV YA03-10 (**Rejeição 865**) para “Implementação futura” no modelo 55;

  <https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=3NLMgy80wTE=>  
     
     
  Caso você esteja com essa rejeição acima, **basta retransmitir e monitorar a nota**.  
  Se a rejeição persistir, acione a SEFAZ para questionar a normalização.

**Saiba mais**  
Para mais detalhes sobre a adequação das *tags* do grupo de **Cobrança**, acesse o documento: [DT NT2025.001 - NF-e](https://tdn.totvs.com.br/display/public/LDT/DT+NT2025.001+-+NF-e)
