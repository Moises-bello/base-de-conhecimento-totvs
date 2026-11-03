---
article_id: 360024732031
category: Financeiro - Contas a Pagar
content_hash: d57e6645a39e533a4db87a04f0c8a4426839299eb5f8de9815fd9a405804284a
fetched_at: '2026-06-28T22:38:07.023672+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento BackOffice Linha Protheus - Como parametrizar os cadastros para
  que os títulos a pagar necessite de aprovação
type: support-article
updated_at: '2025-08-12T20:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024732031-Cross-Segmento-BackOffice-Linha-Protheus-Como-parametrizar-os-cadastros-para-que-os-t%C3%ADtulos-a-pagar-necessite-de-aprova%C3%A7%C3%A3o
---

**Dúvida**  
Como parametrizar os cadastros para que os títulos a pagar necessite de aprovação?  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**

**Parâmetros que influenciam no controle de alçada de aprovação**

1. **MV\_CTLIPAG**  
   Responsável por controlar as baixas a pagar mediante o preenchimento da *Data de Liberação*.

* Quando habilitado, o sistema verifica se o campo **E2\_DATALIB** está preenchido.
* Caso não esteja, o controle não é aplicado.

2. **MV\_FINCTAL**  
   Determina a forma de liberação dos movimentos:

* **1** – Liberação simples
* **2** – Controle por alçada

Quando o parâmetro **MV\_FINCTAL** está configurado para *Controle por Alçada* (valor **2**), a rotina de manutenção de títulos a pagar exigirá:

* O preenchimento do campo **E2\_CODAPRO** (Aprovador).
* O registro do status do título (**E2\_STATLIB**) como *Aguardando Aprovação*.

**Rotinas necessárias para o correto funcionamento do controle de alçada**  
Para que o processo de inclusão e aprovação dos títulos funcione adequadamente, é necessário cadastrar as seguintes rotinas:

* **FINA002** – Cadastro de Analista Financeiro
* **FINA004** – Cadastro de Grupo de Analistas
* **FINA003** – Cadastro de Gestor Financeiro
* **FINA005** – Cadastro de Grupo de Gestores
* **FINA006** – Cadastro de Aprovador x Superior

**Saiba mais**[Liberação para Baixa - FINA580 - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=312165854)

[Liberação de despesas FINA581](https://tdn.totvs.com/pages/viewpage.action?pageId=312166026)  
[Liberação de Fundos](https://tdn.totvs.com/pages/viewpage.action?pageId=392502351)
