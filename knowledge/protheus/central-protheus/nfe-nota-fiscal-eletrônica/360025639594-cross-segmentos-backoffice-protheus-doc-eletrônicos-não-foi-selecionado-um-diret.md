---
article_id: 360025639594
category: NFe - Nota Fiscal Eletrônica
content_hash: 40db403ad2094e8008ca93a4f88473a54ba49e8178be9cd27b2746b478eec2fc
fetched_at: '2026-06-28T22:40:00.346682+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Não foi selecionado
  um diretório válido para impressão. on FWMSPRINTER:NEW(FWMSPRINTER.PRW)'
type: support-article
updated_at: '2021-06-16T19:54:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025639594--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-N%C3%A3o-foi-selecionado-um-diret%C3%B3rio-v%C3%A1lido-para-impress%C3%A3o-on-FWMSPRINTER-NEW-FWMSPRINTER-PRW
---

**Dúvida**

Como corrigir o seguinte error.log abaixo:

Não foi selecionado um diretório válido para impressão. on FWMSPRINTER:NEW(FWMSPRINTER.PRW) ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Erro  ocorre no momento da impressão do DANFE, este incidente costuma ocorrer quando o diretório/pasta informado no parâmetro MV\_RELT não existe.  
Para correção do erro, crie o diretório informado no parâmetro ou informe um diretório existente.  
O respectivo parâmetro pertence ao Protheus, poderá acessá-lo pelo Configurador (SIGACFG).

**THREAD ERROR** Não foi selecionado um diretório válido para impressão. on FWMSPRINTER:NEW**(FWMSPRINTER.PRW)** ?
