---
article_id: 360040942454
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 48c3d28e4f4708c1f66706c00c1c452a3ce6c097e2d4af8fa743bd987f8c3868
fetched_at: '2026-06-28T22:42:04.887053+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Ajuste de Credito
  ou Debito na apuração da EFD Contribuições
type: support-article
updated_at: '2023-04-20T13:57:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040942454-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Ajuste-de-Credito-ou-Debito-na-apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Ajuste de Credito ou Debito na apuração da EFD Contribuições?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

#### **Ajustes de Crédito de PIS e COFINS**

Para realizar ajustes de Crédito no PIS e COFINS e gerar os Registros M110 e M510 é necessário o cadastro manual dos ajustes através da rotina **Ajuste de Crédito PIS e COFINS (FISA042)**, preenchendo os campos:

* **Indicador do Ajuste**: Indicador do tipo de ajuste. 0- Ajuste de redução e 1- Ajuste de acréscimo.
* **Ajuste de PIS/COFINS:**0 = Ajuste de PIS ou 1 = Ajuste de COFINS.
* **Valor Ajuste:**Valor a ser ajustado nos Créditos. (não ultrapassar o total de créditos do período).
* **Código do Ajuste:**Código do ajuste, conforme a Tabela indicada no item 4.3.8. 01 = Ação Judicial, 02 = Processo Administrativo, 03 = Legislação Tributária, 04 = Regime Especial do RTT, 05 = Outras Situações e 06 = Estorno.
* **Número do Documento:**Número do processo, documento ou ato concessório ao qual o ajuste está vinculado, se houver.
* **Descrição do Ajuste**: Descrição resumida do ajuste.
* **Data de Referência:**Data de referência do ajuste (ddmmaaaa).
* **Tipo Crédito:**Código do tipo do crédito.
* **Código do Ajuste:**Código sequencial do Ajuste.

**Importante:**

Para que ajuste seja considerado na apuração campos de **Código do tipo do crédito**deve ser compatível com tipo de credito existente na apuração conforme tabela 4.3.6 – Tabela Código de Tipo de Crédito

#### **Campos necessários para Ajuste de CPRB**

* **Tp.Atividade:** Tipo de Atividade CPRB - Este campo é imprescindível para que o ajuste de CPRB na apuração seja executado corretamente.
* **CST:**  Código da Situação Tributaria
* **Base Cálculo:** Base Cálculo
* **Alíquota:** Alíquota do Ajuste
* **Conta Contábil:** Conta Contábil
* **Inf. Compl.**: Informação Complementar

#### **Campos necessário para Ajuste de Debito**

**Para realizar ajustes de Debito no PIS e COFINS e gerar os Registros M220, M225, M620 e M625 é necessário o cadastro manual dos ajustes através da rotina Ajuste de Crédito PIS e COFINS (FISA042), preenchendo os campos:**

* **Créd/Debito:** Ajuste de Credito/Débito
* **Cod. Contrib:** Código da Contribuição conforme tabela (4.3.5)

**Importante:** 

Para que ajuste seja considerado na apuração campo de **Cod. Contrib**deve ser compatível com código da contribuição existente na apuração conforme tabela 4.3.5 - Código da Contribuição

**Registros afetados.**

REGISTRO M220: AJUSTES DA CONTRIBUIÇÃO PARA O PIS/PASEP APURADA

REGISTRO M225: DETALHAMENTO DOS AJUSTES DA CONTRIBUIÇÃO PARA O PIS/PASEP APURADA

REGISTRO M620: AJUSTES DA COFINS APURADA

REGISTRO M625: DETALHAMENTO DOS AJUSTES DA COFINS APURADA

**Importante:** Para Determinar regime do ajuste é utilizado campo CF5\_CODCON.

Para não cumulatividade são utilizados códigos: "01|02|03|04|71"

Para que ajuste tenha efeito é necessário que exista nota de saída para composição do debito de PIS e COFINS.

Serão preenchidos ajustes na tabela CLA e CL4

CL4 Detalhamento do Ajuste

CLA Ajuste PIS/COFINS

CKS verificar campos CKS\_AJAC e CKS\_AJRD

Informações adicionais:

**Manual da apuração do EFD Contribuições**

<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>

**Manual da geração do arquivo do EFD Contribuições**

<https://tdn.totvs.com/pages/releaseview.action?pageId=715144991>
