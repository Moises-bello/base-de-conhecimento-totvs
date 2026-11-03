---
article_id: 360028524272
category: RH - Rescisão
content_hash: e6101e8d6649bf34ad8f793ebe58934ebfa7bbdc3a30fd408aed3ad1bca587fb
fetched_at: '2026-06-28T22:43:52.090851+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer demissão para um sócio que recebe pro-labore
type: support-article
updated_at: '2025-06-16T17:31:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028524272-RH-Linha-Protheus-GPE-Como-fazer-demiss%C3%A3o-para-um-s%C3%B3cio-que-recebe-pro-labore
---

**Dúvida**Como fazer demissão para um sócio que recebe pro-labore?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Se foi enviado na carga inicial os dados do pró-labore no evento **S2300,** no seu desligamento é necessário enviar o evento **S2399**.  
Para isso basta informar na **SRA** a **data do desligamento** e a **situação da folha = D**

Ao salvar é gerado automaticamente o evento **S2399** e enviado para o **TAF**.

Mas mesmo não sendo usual pelo Protheus, há a possibilidade de efetuar a rescisão do sócio, e assim após a integração do roteiro RES para a folha de Autônomo, os campos na SRA serão preenchidos automaticamente.

Para isso deverá seguir os passos abaixo:  
- Criar um novo **Tipo de Rescisão** para o Pro-labore na **Tabela S043**, com os todos os campos com **N** pois o pro-labore não possui os direitos do celetistas;  
- Efetue a rescisão, caso o mesmo não possua salario fixo na SRA, deve informar o valor na RGB antes do cálculo.  
- Após conferencia, efetue a integração com o roteiro AUT e feche o roteiro RES.
