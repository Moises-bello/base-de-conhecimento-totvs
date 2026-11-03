---
article_id: 360061700714
category: Inspeção de Processos (SIGAQIP)
content_hash: b81194c695066be9b20b1cc89ee4c373429886ce1d36adf805a25e7d1d0b086e
fetched_at: '2026-06-28T22:42:25.927473+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - QIPA215 não permite retroceder ou avançar
  a data base
type: support-article
updated_at: '2021-10-01T13:08:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061700714-Manufatura-Linha-Protheus-SIGAQIP-QIPA215-n%C3%A3o-permite-retroceder-ou-avan%C3%A7ar-a-data-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:35 min**  
**Dúvida**Por quê a **data base** retorna para a data atual quando é alterada na rotina **QIPA215 - Resultados**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Esse comportamento é padrão da rotina, ou seja, a **data base** é alterada a para a data atual.  
Para que a rotina permita retroceder ou avançar a **data base**, deve-se utilizar o **PE - Ponto de Entrada** **QP215DAT** para um comportamento diferente.  
  
**Saiba mais**  
A documentação para utilização do **PE QP215DAT** está disponível no *link* [QP215DAT - Alteração de database](https://tdn.totvs.com/pages/releaseview.action?pageId=6803667).
