---
article_id: 360050356433
category: NFe - Nota Fiscal Eletrônica
content_hash: 0c354c48e4c57a4c789c323a06fbd47fc61a57cb5aef16aa1400ca6b668a4681
fetched_at: '2026-06-28T22:40:00.458079+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 206 Rejeição:
  Numeração da NF-e já está inutilizada na Base de dados da SEFAZ'
type: support-article
updated_at: '2021-09-09T15:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050356433--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-206-Rejei%C3%A7%C3%A3o-Numera%C3%A7%C3%A3o-da-NF-e-j%C3%A1-est%C3%A1-inutilizada-na-Base-de-dados-da-SEFAZ
---

**Dúvida**Como solucionar a rejeição abaixo:

206 Rejeição: NF-e já está inutilizada na Base de dados da SEFAZ ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Se Tipo de Emissão da NF-e for 1 **(Emissão normal), 6 (Contingência SVC-AN) ou 7 (Contingência SVC-RS): • Acesso BD de Inutilização (Chave: Modelo, UF, CNPJ/CPF, Série, Número)**: o Numeração da NF-e está inutilizada (NT 2011/004) (NT 2018.001)   
  
Observação: Se cUF(B02) for igual 35(SP) validar também se Tipo de Emissão da **NF-e for 2 (Contingência FS-IA)**

Quando emitida uma NF-e com uma numeração **que já foi inutilizada,** será retornado a **rejeição "206** - NF-e já está inutilizada na Base de dados da SEFAZ"

2. É possível consultar a Inutilização da nota através **do site da Sefaz no link abaixo:**

*[Clique aqui](https://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=YG1QjUXR4PY=)*

3.  Se inutilizada **não****é possível reutilizar mais essa numeração.** Deve-se, nessa situação, emitir a NF-e com uma nova numeração, ainda não utilizada.

4. Caso esse número **NF-e não esteja inutilizado,** entre em contato com o nosso suporte para correção.

* **Saiba mais:**

Conforme a Nota Técnica 2020.005 :

2.2.10. Fim da Validação de Inutilização da Numeração nas Emissões em Contingência A regra 3B08-100, que não permite autorização de NF-e com numeração que tenha sido inutilizada, deixa de ser aplicada nas hipóteses de emissão em contingência **2 (Contingência FS-IA), 4 (Contingência EPEC) ou 5 (Contingência FS-DA).**

Observação: Se cUF(B02) for igual 35(SP) validar também se Tipo de Emissão da NF-e **for 2 (Contingência FS-IA), 4(Contingência EPEC) ou 5(Contingência FS-DA).**

* **Validação da Sefaz:**

![206_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408134941975/206_rejei__o.JPG)
