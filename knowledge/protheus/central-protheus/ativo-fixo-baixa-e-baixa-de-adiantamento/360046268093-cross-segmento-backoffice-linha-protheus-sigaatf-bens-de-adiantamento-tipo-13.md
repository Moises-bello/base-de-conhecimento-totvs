---
article_id: 360046268093
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: dfabb7ea437da2c7e2ebfa836332a1eaa70b2f02ddbc6c26d96c844c6061bf73
fetched_at: '2026-06-28T22:41:55.557486+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - BENS DE ADIANTAMENTO
  TIPO 13
type: support-article
updated_at: '2023-11-20T16:19:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046268093-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-BENS-DE-ADIANTAMENTO-TIPO-13
---

**Ocorrência**

Na rotina de baixa de adiantamento (ATFA040) não considera bens do tipo 13 - Adiantamento Gerencial

**Ambiente**  
Protheus – Sigaatf – A partir da versão 12  
   
 **Causa**

Para bens do tipo 13 não será possível efetuar essa operação através da rotina Baixa de adiantamento (ATFA040), pois é necessário utilizar rotina de **Aquisição por Transferência (ATFA251)**.

**Solução**

 **Tipo de Bem 13 – Adiantamento Gerencial** aplicam-se as seguintes regras:

* Este será o controle gerencial de um Bem em formação, sendo que o seu controle fiscal é efetuado através do **Bem do Tipo 03 – Adiantamento**.
* Este tipo de bem permite que tenha mais de um tipo de saldo, mas apenas um registro para a combinação **Tipo de Bem + Tipo de Saldo.**

Na inclusão do ativo deve informar uma linha com o tipo 03 - Adiantamento e outra linha com o tipo 13 - Adiantamento gerencial.

Segue link com detalhes sobre a baixa do ativo tipo 13  e sua inclusão

<https://tdn.totvs.com/pages/releaseview.action?pageId=385857587>
