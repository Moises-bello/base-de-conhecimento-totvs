---
article_id: 36943120614679
category: Financeiro - Novo Gestor Financeiro
content_hash: 70cd615443b3365edb68549ba775626683be76ddf3d26e70b444513b1832d724
fetched_at: '2026-06-28T22:37:41.590181+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Linha Backoffice Protheus - SIGAFIN - Cadastros JOB FINA892
  e FINA892A
type: support-article
updated_at: '2025-12-11T14:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36943120614679-Cross-Segmentos-Linha-Backoffice-Protheus-SIGAFIN-Cadastros-JOB-FINA892-e-FINA892A
---

**Dúvida**  
Qual a configuração ideal para o JOB FINA892  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução:**  
O **JOB FINA892** tem como objetivo realizar a **transmissão dos títulos** que estão em situação de **cobrança PIX**.  
Já o **JOB FINA892A** é responsável por realizar a **baixa desses títulos**, desde que já tenham sido transmitidos previamente, considerando as informações retornadas pelo banco.

A configuração do agendamento (schedule) de ambos os jobs deve ser feita diretamente pelo **módulo Configurador**.

**Exemplo de cadastro JOB FINA892:**  
*![](https://centraldeatendimento.totvs.com/hc/article_attachments/36943093485207)*

#### **Importante:**

A configuração do JOB deve ser **única por Grupo de Empresas**, ou seja, **deve existir apenas um agendamento** para uma única filial dentro do grupo. Isso garante que apenas **uma chamada** seja realizada pelo schedule, deixando a execução para o próprio job, que processará **todas as empresas do grupo**.

####
