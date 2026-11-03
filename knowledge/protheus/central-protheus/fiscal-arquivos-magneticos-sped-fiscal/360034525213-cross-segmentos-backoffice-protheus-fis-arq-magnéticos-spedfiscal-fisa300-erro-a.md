---
article_id: 360034525213
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 1f2013aee0a738af82fd728a72ddbcb55e05b2cad833ce3f6a555263e1a83aa5
fetched_at: '2026-06-28T22:42:02.598196+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL_FISA300
  Erro ao tentar processar a apuração do ISS "FISA300ASERVICO F1O_CODISS REGNOIS Não
  existe registro relacionado a este código".
type: support-article
updated_at: '2025-02-11T22:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034525213-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-FISA300-Erro-ao-tentar-processar-a-apura%C3%A7%C3%A3o-do-ISS-FISA300ASERVICO-F1O-CODISS-REGNOIS-N%C3%A3o-existe-registro-relacionado-a-este-c%C3%B3digo
---

**Ocorrência**Ao tentar processar a **Apuração de ISS** pela Rotina **FISA300** ocorre o seguinte erro:

**"Ocorreram erros durante a gravação:**  
**FISA300ASERVICO**  
**F1O\_CODISS**  
**REGNOIS**  
**Não existe registro relacionado a este código.**  
**1) Informe um código que exista no cadastro.**  
**2) Efetue o cadastro no programa de manutenção do respectivo cadastro.**  
**3) Escolha um registro válido."**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043853274/mceclip0.png)  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**   
 Esse incidente ocorre, pois o(s) código(s) utilizado(s) não está(ão) configurado(s) pela rotina **MATA963** ou existe algum código de Serviço existe na tabela **SFT** que não está na **tabela 60** da **SX5.**

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Análise os códigos de Serviço que estão sendo apresentados na Tabela **SFT**, se também estão existentes na **Tabela 60** da **SX5**. Se não estiver deve ser inserido na **SX5** todos os códigos utilizados.  
 2. Acesse a rotina de Relacionamento código de serviço - **MATA963**,que foi disponibilizada no **Protheus** para que seja realizada a amarração dos códigos de serviço, códigos da **Lei Complementar 116/03**;  
 3. Preencha as informações nos campos;  
4. Importante utilizar no campo **CDN\_CODLST** o código de serviço segundo **Lei Complementar 116/03**;  
 5. Após, verifique que as informações foram gravadas na tabela **CDN**.
