---
article_id: 23820899683351
category: Gestão de Transportes (TMS)
content_hash: f6bc642ab875c079d8b2b4410e4e992a2541e26d5bce23d3fb1dafc6830684ba
fetched_at: '2026-06-28T22:45:27.552801+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Configuração do cadastro da Pamcard em várias
  filiais
type: support-article
updated_at: '2025-05-23T12:08:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23820899683351-Log%C3%ADstica-Linha-Protheus-TMS-Configura%C3%A7%C3%A3o-do-cadastro-da-Pamcard-em-v%C3%A1rias-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23820906583319) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Como realizar a configuração do cadastro da **Pamcard** para várias filiais no **TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Em **Atualizações/ Operadoras Frota/ Operadoras Frota - TMSAE60**, tabela **DEG**, altere o cadastro relacionado a operadora de frota **Pamcard**. Na aba **Outros,** preencha o campo **DEG\_FILCTR**, com a filial que possui o contrato com a **Pamcard**.

![pamcard.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23821774042775)

Abaixo um exemplo de **XML** de transmissão para a **Pamcard** de uma filial que não é a contratante.

![xml.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23821823062935)

**Importante**

* Se a tabela **DEG** for compartilhada, deve entrar na rotina de cadastro em cada filial e **Alterar / Salvar** para que o Sistema crie o arquivo **.PEM** de cada filial na *system*.
* Se a tabela **DEG** for exclusiva, deve realizar o cadastro completo em cada filial.
