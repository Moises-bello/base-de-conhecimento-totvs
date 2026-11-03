---
content_hash: 3e18663227ec2d3b265354f1d486069d56c29725c10b44f3b9a1d2d8f8727013
fetched_at: '2026-06-29T00:12:15.437183+00:00'
page_id: '979020035'
product: rm
source: tdn-rm
title: Nova Gestão de Abono - Parâmetro Trabalhar com base no próximo período mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979020035
version: 64
---

## **01. DADOS GERAIS**

| **Produto:** | RM |
| --- | --- |
| **Linha de Produto:** | Linha RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Automação de Ponto |
| **Função:** | Parâmetros do Quiosque |
| **País:** | Brasil |
| **Requisito/Story/Issue:** | [DRHJORNRM-4355](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-4355), [DRHJORNRM-8384](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8384) |

## **02. VERSÕES**

 A partir da versão 12.1.2510 e superiores.

## **03.** **SITUAÇÃO/REQUISITO**

Parametrizada a solicitação de abonos para "**Trabalhar com base no próximo período mensal"** e a Gestão por escala "**A partir do período ativo" ,** porém,  o sistema está permitindo inserir abonos no Período Atual e Futuro. 

## **04. SOLUÇÃO**

Quando no grupo de quiosque estiver parametrizado para "**Trabalhar com base no próximo período mensal"** e a Gestão por escala estiver "**A partir do período ativo" ,** será permitida a inclusão de abonos somente no Período Futuro.

## **05.****EXEMPLO DE UTILIZAÇÃO**

11Período Futuro e Gestão - Sim

O usuário definiu a seguinte parametrização: "**Trabalhar com base no próximo período mensal" e "Gestão por escala 'A partir do período ativo' =Sim".** Será permitido inserir abonos somente no período futuro, caso seja inserida data de início anterior, será demonstrada a mensagem para o usuário " **É possível realizar alterações somente a partir do dia "XX/XX/XXXX**'.

**Exemplo:**

Período Atual e Ativo: 01/08/2025 a 31/08/2025

Período Futuro: 01/09/2025 a 30/09/2025

Solicitado abono com data de início anterior ao período futuro- 25/08/2025

2Período Futuro e Gestão - Não

O usuário definiu a seguinte parametrização: **"Trabalhar com base no próximo período mensal" e "Gestão por escala 'A partir do período ativo' =Não"**.

O sistema irá permitir inserir abonos em qualquer período Atual ou Futuro.

**Exemplo1:**

Período Atual e Ativo: 01/08/2025 a 31/08/2025

Período Futuro: 01/09/2025 a 30/09/2025

Solicitado abono com data de início anterior ao período futuro- 21/08/2025

Solicitado abono com data de início dentro período futuro- 17/09/2025

**Exemplo 2:**

Período Atual e Ativo: 01/08/2025 a 31/08/2025

Período Futuro: 01/09/2025 a 30/09/2025

Solicitado abono com data de início anterior ao período atual e ativo- 10/07/2025

3Não utiliza período futuro e Gestão - Sim

O usuário definiu a seguinte parametrização: **"Não Trabalhar com base no próximo período mensal" e "Gestão por escala 'A partir do período ativo' =Sim"**.

O sistema irá permitir inserir abonos apartir do período atual.

**Exemplo:**

Período Atual e Ativo: 01/08/2025 a 31/08/2025

Período Futuro: Não esta parametrizado

Solicitado abono com data de início anterior ao período futuro- 21/08/2025

Solicitado abono com data futura- 19/09/2025

## **06. ASSUNTOS RELACIONADOS**

**[Nova Gestão de Abono](https://tdn.totvs.com.br/pages/viewpage.action?pageId=349184213)**
