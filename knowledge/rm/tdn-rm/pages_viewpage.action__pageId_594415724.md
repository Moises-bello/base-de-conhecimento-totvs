---
content_hash: 5e75da8262ad3901964fd87f9686b59e763761ecb9619d783aecf54c907afd68
fetched_at: '2026-06-29T00:10:57.128823+00:00'
page_id: '594415724'
product: rm
source: tdn-rm
title: FISCAL01-14802 - DT NF-e NT 2020.006 - Intermediador da Transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=594415724
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14802 |

## **02. SITUAÇÃO/REQUISITO**

Gerar NF-e com o preenchimento e com as informações do intermediador da transação: CNPJ do Intermediador da Transação, Identificador Cadastro Intermediador.

## **03. SOLUÇÃO**

Conforme "Nota Técnica 2020.006" foi realizada implementação que contempla o novo grupo da NF-e.

**Grupo B** - Identificação da NF-e

Grupo B

**Grupo YB** - Informações do Intermediador da Transação.

Grupo YBRegras no Movimento

**Para as Operações:**

**2** = Operação não presencial, pela Internet;  
**3** = Operação não presencial, Tele atendimento;  
**4** = NFC-e em operação com entrega a domicílio;  
**9** = Operação não presencial, outros.

* Se Informado indicativo de presença (TAG: **indPres**) ***IGUAL**a**:* **2, 3, 4** ou **9**
  + Obrigatório o preenchimento do campo indicativo do **Intermediador** (TAG: **indIntermed**).

* Se Informado indicativo de presença (TAG: **indPres**) ***DIFERENTE** de:* **2, 3, 4** ou **9**
  + Proibido o preenchimento do campo Indicativo do **Intermediador** (TAG: **indIntermed**).

Obs.: [Identificador do Intermediador](https://tdn.totvs.com/x/SABcIw)

Regras no Envio da NF-e

* Se informado indicador do **Intermediador** ***IGUAL*** a **1 - Operação em site ou plataforma de terceiros (intermediadores/marketplace)**
  1. TAG **indIntermed** do XML será igual a **1** (Um)
  2. Obrigatório o preenchimento das informações do Intermediador da Transação (TAG: **infIntermed**) - (Incluída na NT 2020.006)

* Se informado indicador de presença do comprador no estabelecimento comercial no momento da operação ***DIFERENTE*** de **1 - Operação em site ou plataforma de terceiros (intermediadores/marketplace)**
  1. TAG **indIntermed do XML**será diferente de **1** (Um)
  2. Não é permitido o preenchimento das Informações do Intermediador da Transação (TAG: **infIntermed**) - (Incluída na NT 2020.006)
