---
article_id: 20294406847383
category: Escrita Fiscal - Configurador de Tributos
content_hash: 4d181f4973de9603f6fe46b1181efc815d2f104dc8ead9daf1cb6da25af8ceff
fetched_at: '2026-06-28T22:39:17.407068+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  o credito presumido?
type: support-article
updated_at: '2025-11-03T14:49:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20294406847383-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-o-credito-presumido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429161879) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como configurar o credito presumido no FISA170?  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da release 12.1.2210  
  
**Solução**Segue abaixo o passo a passo da configuração do credito presumido no fisa170

ID - tributo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406785431)

Perfis

Perfil do Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429164567)

O produto deve estar devidamente cadastrado no SB1 ( cadastro de produtos )

Perfil de Operação

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429165719)

Perfil de Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406788247)

Perfil Origem / Destino

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406789527)

Regras de Calculo Documento Fiscal

Regra de base de calculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429170839)

Regra de Aliquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406793239)

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429175447)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429176343)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406796951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406803607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406806807)

valor da mercadoria = 1064,00

valor do IPI = 34,58

Base de calculo do icms = 1.098,58\*18% = 197,74

Base de calculo do credito presumido = 1064,00\* 9% = 95,76

Nota fiscal de Venda

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294406808215)

Gravação do credito presumido na SF3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20294429192215)

Verificar no TES o campo

F4\_AGREGCP  
Agr crd Pres = não

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=747332379
