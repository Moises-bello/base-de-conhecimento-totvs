---
content_hash: 29c5a0ca4544697db77c0d98af3195362566f27b58a25d6453d986e2932d3c3f
fetched_at: '2026-06-29T00:09:22.537817+00:00'
page_id: '422545993'
product: rm
source: tdn-rm
title: Gerar Movimento com Número da Prefeitura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545993
version: 8
---

## **Conteúdo**

Conteúdo

## **01. Introdução: Diferença entre NF-e e NFS-e**

Diferentemente do processo da **NF-e** (Nota Fiscal Eletrônica), no qual a nota é enviada diretamente à **SEFAZ** para autorização, o processo da **NFS-e** (Nota Fiscal de Serviços Eletrônica) exige que o contribuinte envie um **RPS (Recibo Provisório de Serviço)** à prefeitura. A prefeitura, então, emite a NFS-e com base nesse recibo e retorna as informações autorizadas ao contribuinte.

**Observação:**  
Ao escriturar os movimentos referentes às NFS-e, inicialmente será registrado o **número do RPS** (não o número da NFS-e). Caso o usuário deseje utilizar o **número fornecido pela prefeitura** (NFS-e definitivo), é necessário seguir o processo descrito abaixo.

### **01.1. Características Principais do Processo com RPS**

* O RPS é o documento inicial que antecede a geração da NFS-e.
* A prefeitura autoriza a NFS-e com base no RPS e retorna o número definitivo da nota.

### **01.2. Performance**

Este processo deve ser usado para faturamento de até 50 notas por vez, para o faturamento de um número maior recomenda-se a utilização do processo .

## **02. Configuração do Processo**

### **02.1. Criação do Movimento de RPS (Tipo 2.1.XX)**

* **Tipo de Movimento:** Utilize o movimento **2.1.XX (Pedido)**.
* **Parâmetro Obrigatório:**
  + Em *Compra/Venda > Características*, habilite a opção **"Gerar Movimento de Venda"**.
* **Informações Necessárias:**
  + Preencha todos os dados exigidos pela prefeitura no RPS (ex.: serviços prestados, valores, cliente, etc.).

> **Nota:** A estrutura do movimento é idêntica à de uma NFS-e comum, com exceção do parâmetro acima.

### **02.2. Opções de Faturamento**

Após a criação do RPS, configure como o sistema deve gerar o movimento com o número definitivo da NFS-e:

#### **02.2.1. Faturamento Automático**

* **Funcionamento:**
  + Ao consultar o status da NFS-e na prefeitura, se a nota estiver **autorizada**, o sistema gera automaticamente um novo movimento **2.2.XX** com o número da NFS-e definitivo.
* **Recomendação:**
  + Evite consultar muitos RPS simultaneamente, pois isso pode causar **perda de desempenho** no processo de geração automática.

#### **03.2.2. Faturamento Sem Seleção do Tipo de Movimento**

* **Funcionamento:**
  1. Após consultar o status da NFS-e, o sistema **não gera automaticamente** o movimento 2.2.XX.
  2. Acesse a visão de **NFS-e autorizadas** e selecione os registros desejados.
  3. Clique em **"Gerar movimento com o número da prefeitura"** nos processos.
* **Resultado:**
  + Será criado um novo movimento **2.2.XX** vinculado ao RPS, contendo o número definitivo da NFS-e retornado pela prefeitura.

## **03. Informações Adicionais**

### **03.1. Execução do Job de Geração de Movimentos**

* O Job responsável por converter movimentos **2.1.XX (RPS)** em **2.2.XX (NFS-e definitiva)** segue regras específicas:
  + Executa **apenas para movimentos dentro do período de movimentação** definido nos *Parâmetros Gerais do Módulo de Faturamento*.
  + Aplica-se **somente à coligada corrente** (empresa selecionada no momento da execução).

### **03.2. Tratamento da Data de Competência**

* Caso a **data de competência** esteja **nula** ou com valor mínimo:
  + O sistema utilizará automaticamente a **data de emissão** do RPS durante o processo de geração do movimento com o número da prefeitura.

## **04. Resumo**

1. Crie o RPS (movimento 2.1.XX) com o parâmetro *Gerar Movimento de Venda* habilitado.
2. Consulte o status da NFS-e na prefeitura.
3. Escolha entre:
   * **Geração automática** do movimento 2.2.XX (após autorização) **ou**
   * **Geração manual** via seleção de registros na visão de NFS-e.
4. Valide se o Job está configurado para o período correto e à coligada adequada.
