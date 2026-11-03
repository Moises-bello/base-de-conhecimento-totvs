---
article_id: 360023380572
category: Financeiro - Contas a Pagar
content_hash: ff8fca65978d809032e6c3d59a21fd80492adcf38a1a23208c1285020a29ed1b
fetched_at: '2026-06-28T22:38:08.497715+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como faz para diferenciar
  o vencimento do imposto ISS por estado/município
type: support-article
updated_at: '2022-08-05T11:30:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023380572-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-faz-para-diferenciar-o-vencimento-do-imposto-ISS-por-estado-munic%C3%ADpio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como faz para diferenciar o vencimento do imposto ISS por estado/município?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**1. Cadastre o Município na rotina **"FISA010"**, insira o dia de vencimento no campo **Dia de recolhimento ISS**(CC2\_DTRECO);  
2. Cadastre o **fornecedor** com o código IBGE, de acordo ao Município cadastrado;  
3. Cadastre o múltiplo vínculo **ISS** na rotina **FINA270** com o registro do **cód. estado** e **município** e a **alíquota**, vinculando o **fornecedor** junto ao **cadastro**;  
4. Insira o título no **Contas a Pagar** (FINA050), informando a **natureza** , **fornecedor** e o **código de ISS**(E2\_CODISS).
