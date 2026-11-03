---
article_id: 35969881319575
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: dccf3b86ebd6eadd9b936f7a9cf98445b2bbf41b940d9b111807165ad20fa107
fetched_at: '2026-06-28T22:39:55.111230+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Configuração
  de Logotipo no DANFECOM
type: support-article
updated_at: '2025-10-29T19:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35969881319575-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Configura%C3%A7%C3%A3o-de-Logotipo-no-DANFECOM
---

**Dúvida**  
Como realizar a configuração de logotipo para a impressão da DANFECOM?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Primeiramente, as dimensões da imagem devem respeitar as seguintes regras:  
**Tamanho**: 90 x 90  
**Formato**: BMP de 256 cores  
  
Após isso, a imagem deve estar na pasta \System do Protheus e seguir a seguinte regra de nomenclatura:  
  
**Opção 1 - Caso queira diferenciar entre as filiais:**  
**LGRL+Código da Empresa+Filial.bmp**, como o exemplo abaixo:

**LGRL010101.bmp** (caso o servidor seja linux a extensão deve ser maiúscula)  
  
**Opção 2 - Caso queira usar o mesmo logo entre as filiais:**  
**LGRL+Código da Empresa.bmp**, como o exemplo abaixo:

**LGRL99.bmp** (caso o servidor seja linux a extensão deve ser maiúscula)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35969892945687)
