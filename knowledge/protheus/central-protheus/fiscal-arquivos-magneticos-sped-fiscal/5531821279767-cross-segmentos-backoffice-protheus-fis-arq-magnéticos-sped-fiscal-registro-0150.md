---
article_id: 5531821279767
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d04416880b3d8fcd25c0bf676a13b0e129b42a08f0efc1f0b874353a9989d06c
fetched_at: '2026-06-28T22:42:02.374875+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro 0150-Erro de validação: Campo 08 COD_MUN-Campo obrigatório para contribuintes
  domiciliados no Brasil. Preencher com 9999999, caso contrário.'
type: support-article
updated_at: '2025-02-15T13:28:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5531821279767-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-0150-Erro-de-valida%C3%A7%C3%A3o-Campo-08-COD-MUN-Campo-obrigat%C3%B3rio-para-contribuintes-domiciliados-no-Brasil-Preencher-com-9999999-caso-contr%C3%A1rio
---

**Ocorrência**

Ao validar o arquivo texto do **Sped Fiscal** gerado pelo sistema ocorre o seguinte erro de validação referente ao campo **08-COD\_MUN** do registro **0150-Tabela de Cadastro do Participante**:

**Campo obrigatório para contribuintes contribuintes domiciliados no Brasil. Preencher com 9999999, caso contrário.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**Este incidente ocorre, pois a configuração do sistema está incorreta para o cadastro do participante domiciliado no Brasil.  
  
**Solução**Para que o erro não ocorra, é preciso cadastrar corretamente o código de país nos cadastros de **Cliente** e **Fornecedor.**

O campo **País Bacen - A1\_CODPAIS** no cadastro de **Clientes** e **País Bacen -  A2\_CODPAIS** no cadastro de **Fornecedores** deve ser preenchido 5 dígitos

**Exemplo:** **01058** referente ao **código de país do Brasil**  
  
Tanto no no cadastro de **Clientes** quanto no cadastro de **Fornecedores** o campo fica na aba **Fiscal,** conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5531556086807/mceclip0.png)
