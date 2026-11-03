---
article_id: 24575959302807
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 02838ba7785dc0ae17dec85856f907f344ee946b915174c4abce37cb22596926
fetched_at: '2026-06-28T22:37:56.522894+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA811
  - Falha na visualização nos dados dos titulos enviados por e-mail
type: support-article
updated_at: '2024-07-08T18:31:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24575959302807-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-FINA811-Falha-na-visualiza%C3%A7%C3%A3o-nos-dados-dos-titulos-enviados-por-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24575936681111) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao enviar um e-mail via **Carta de Cobrança FINA811,** os dados do título não são apresentados.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24575936689815)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o compartilhamento das tabelas **FWP, FWS** estão divergentes rotina **FINA810 - Layout da Carta de Cobrança**  
  
**Solução**1. Ajustar o compartilhamento das tabelas, ambas devem ser iguais  
2. Criar um novo layout, ou ajustar o layout e filiais envolvidas  
3. Enviar novamente o e-mail via **FINA811**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24575936691351)

**Saiba mais**  
**[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)**
