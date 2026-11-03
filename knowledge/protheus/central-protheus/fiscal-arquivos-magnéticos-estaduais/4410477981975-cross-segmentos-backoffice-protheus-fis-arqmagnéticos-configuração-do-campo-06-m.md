---
article_id: 4410477981975
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1442a9ba735e540dc31218f4f8201f02459a4f95bc1d874d116456f3fd523fd0
fetched_at: '2026-06-28T22:42:10.362198+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  do Campo "06 Modelo do Documento Fiscal" Serviços Tomados de prestadores de outros
  municípios para São José dos Campos (Fisa305)
type: support-article
updated_at: '2022-08-17T19:39:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410477981975-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-do-Campo-06-Modelo-do-Documento-Fiscal-Servi%C3%A7os-Tomados-de-prestadores-de-outros-munic%C3%ADpios-para-S%C3%A3o-Jos%C3%A9-dos-Campos-Fisa305
---

**Dúvida**  
Como preencher o campo "06 Modelo do Documento Fiscal" na rotina Serviços Tomados de prestadores de outros municípios para São José dos Campos (Fisa305)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Para preencher o campo **"06 Modelo do Documento Fiscal"**é necessário realizar a seguinte configuração:

1. Acesse o **configurador** e crie o **Parâmetro:**

**Nome do Parâmetro =** MV\_CRTMDNT

**Tipo =**Caráter;

**Descrição:** No caso em que se utiliza espécies de documentos não reconhecidas pela rotina (Espécies reconhecidas pela rotina: NFS, ECF, ESAT,RPS, OT e OM), definir nesse parâmetro qual o modelo de documento, no formato solicitado pelo layout no Campo 06 - Modelo do documento fiscal, que essa espécie é referente.

Ex.: {{'NFPS','A'},{'RPS','RP'}}

Obs.: É importante que o conteúdo seja organizado como consta no exemplo:

Mais informações no link abaixo:

https://tdn.totvs.com/pages/releaseview.action?pageId=578632139
