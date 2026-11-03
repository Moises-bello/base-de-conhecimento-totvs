---
article_id: 4403360783895
category: NFe - Nota Fiscal Eletrônica
content_hash: 9aa6efde64f969516487b40ff0f2b28e5dbc7dd53b47d5945ff0b37626234946
fetched_at: '2026-06-28T22:40:05.604952+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Campos de Retorno
  da NFe
type: support-article
updated_at: '2025-06-12T14:47:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403360783895-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Campos-de-Retorno-da-NFe
---

**Dúvida**Quais são os campos que carregam os dados de retorno da Sefaz com autorização da nota de produto ou conjugada ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**1- Para voltar a nota no sistema a mesma deve ser incluída em **data base retroativa** ou seja incluída no mesmo dia em que foi **incluída anteriormente.**

2- Após isso, na rotina de transmissão de nota selecione a nota em **Outras ações -> Monitor -> Consulta NF**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17491472697111)

3- **A nota não deve** ser transmitida após isso, será preenchidas a chave e o conteúdo correto nas tabelas do TSS assim a nota estará normal no sistema.

Os campos abaixo existem nas tabelas ***SF2 ou SF1, SFT e SF3.***

1- A **data e hora para NFE** são preenchidos nos campos F2\_DAUTNFE  e F2\_HAUTNFE.

2- O campo **número da NFE**  F2\_DOC.

3- Os campos F2\_CHVNFE ou F1\_CHVNFE, F3\_CHVNFE e FT\_CHVNFE  **gravamos a chave da NFE.**

**Observação:**

A chave possui **44 dígitos da nota autorizada.**

4- O campo  F3\_PROTOC gravamos o **protocolo de autorização da NFE.**

5- O campo F3\_CODRSEF gravamos o **código de retorno da Sefaz.**

* ***Exemplo:***

**100 = Autorizado**

**101= Cancelada**

**102=  Inutilizada**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como identificar o código de retorno da Sefaz do campo F3\_CODRSEF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058980073--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-identificar-o-c%C3%B3digo-de-retorno-da-Sefaz-do-campo-F3-CODRSEF)

6- O campo F2\_FIMP ou F1\_FIMP **a legenda da nota.**

**S=** Verde   
**T=** Azul  
**N=** Preto  
**D=** Denegada  
**Vermelho =**Campo em branco 

O preenchimento dos campos **acontece, após o monitoramento (SPEDNFE -> Monitor -> Faixa)** de uma nota autorizada, cancelada ou inutilizada.

* **Saiba mais:**

Esses campos abaixo são exclusivos da nota fiscal de serviço para a prefeitura:

**\_NFELETR ->** Numero da NFSE gerada na prefeitura  
**\_CODNFE  ->** Numero do protocolo de autorização  
**\_EMINFE   ->** Data de autorização  
**\_HORNFE  ->** Hora de autorização

**Obs:** Na tabela SE1 também é gerado o ***E1\_NFELETR***
