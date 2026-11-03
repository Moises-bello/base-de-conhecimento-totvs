---
content_hash: 62b7e1d232ab9a9764e005864071fa0118248c73f999923e27163fe16f2177c4
fetched_at: '2026-06-29T00:11:53.852608+00:00'
page_id: '852321747'
product: rm
source: tdn-rm
title: 20406073 DDWMS-13343 - DT MANUTENÇÃO - Rotina 1795 - Expiração de Versão (novas
  versões para 1795, mantendo o funcionamento da versão anterior)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=852321747
version: 2
---

## **01. DADOS GERAIS**

* [Saiba como utilizar](https://tdn.totvs.com/pages/viewpage.action?pageId=846866958#tabs-Saiba%20como%20utilizar)

Favor atualizar rotinas **1795**, **1700** e **3774** para versões descritas abaixo:

* Rotina **1700**:
  + Versão **34.0.04.008**;
  + Versão **36.0.00.006**;

* Rotina **1795**:
  + Versão **34.0.04.008**;
  + Versão **36.0.00.008**;
* Rotina **3774**:
  + Versão **36.0.00.009**;

**Passo a passo:**

* Abra a rotina **1700**;
* Selecione a aba **Objetos do Banco**;
* Escolha a opção "Cadastro de parâmetros WMS (PCPARAMETROWMS)";
* Clique em **Confirmar**:

* Abra a rotina **1795**;
* Selecione a aba "03 - Expedição";
* Entre no modo de edição de parâmetros, pressionando o botão **Editar**;
* Efetue o comando **Ctrl** + **F** ou clique no botão "Localizar (Ctrl+F)":

* Pesquise pelo os parâmetros: **SOLICITARENDERECOS3774**, **VALIDACAIXABIPE3774** e **TIPOSEPARACAO3774**:

* Parametrize os parâmetros localizados conforme a necessidade;
* Clique em **Confirmar**:

* Siga o fluxo na rotina **3774**, conforme a necessidade;

**Observações:**

* Não foi realizado nenhum ajuste ou modificação, apenas atualizações dos parâmetros já existentes que funcionavam na versão anterior.

## **04. DEMAIS INFORMAÇÕES**

        Não se aplica

## **05. ASSUNTOS RELACIONADOS**

        Documentação de como utilizar a rotina **3774**:
