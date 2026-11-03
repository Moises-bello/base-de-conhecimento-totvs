---
article_id: 9915830910231
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 59283567ca476271f635758a431e6405c4617344ce2ef2923c3a8a33cb8e7278
fetched_at: '2026-06-28T22:39:56.337906+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Campinas:
  Motivo do cancelamento'
type: support-article
updated_at: '2025-05-29T12:36:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9915830910231-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Campinas-Motivo-do-cancelamento
---

**Dúvida**A prefeitura de Campinas-SP começou a validar em Outubro de 2022 o motivo de cancelamento da NFSE, como enviar esse motivo?

Rejeição Apresentada:

![Rejei__o_Campinas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9916075702935)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Habilite no Protheus o parâmetro **MV\_INFXJUS.**  
Reinicie o serviço e acesse a rotina FISA022 para transmissão do cancelamento.  
Será apresentado a **tela abaixo** ao clicar em cancelamento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9915673780631)

Informe uma das 3 opções aceitas pela prefeitura: 

"**Servico Nao Prestado**” ou  
“**Nota Fiscal Emitida em Duplicidade**” ou  
“**CPF ou CNPJ do Tomador do Servico Incorreto**”

Obs.: Informe apenas o texto sem as "" (Aspas Duplas).

Caso utilize a mesma filial para envio de NFSE e NFE foi criado o parâmetro **MV\_MODXJUS** (Habilita tela de justificativa de cancelamento 1-NFSE, 2-NFE, 3-Ambos. Trabalha em conjunto com o parâmetro MV\_INFXJUS)

Para que ao habilitar o parâmetro MV\_INFXJUS seja possível definir se a tela de digitação da justificativa será apresenta apenas em um dos tipos de notas (NF-e e NFS-e). 

O parâmetro **MV\_MODXJUS** deve ser criado da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18371983332631)

Caso o parâmetro MV\_MODXJUS não exista no sistema, será respeitado o legado. Ou seja, respeitará apenas o conteúdo do parâmetro MV\_INFXJUS

Para que funcione os fontes das rotinas FISA022 e SPEDNFE  devem ter data igual ou superior a 09/03/2023.
