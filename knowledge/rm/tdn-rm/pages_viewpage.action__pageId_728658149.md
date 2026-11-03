---
content_hash: db1d44b32c5f04f5eccc4705ecd588fe2b92d99717114a8138af08f4eb6ae355
fetched_at: '2026-06-29T00:11:27.686514+00:00'
page_id: '728658149'
product: rm
source: tdn-rm
title: Contrato de Locação - Contabilidade Através do Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728658149
version: 2
---

O passo a passo abaixo deve ser seguido para realizar a contabilização dos lançamentos de aluguel gerados. Essa parametrização é a recomendada para realizar a contabilização de todos os processos que geram lançamentos dentro de contratos de aluguel.

### **1) Precisamos desabilitar a integração contábil do contrato de aluguel no parâmetro abaixo:**

*Ambiente / Parâmetros / Gestão de Imóveis / Aluguel / Contabilidade*

### **2) Configurar o parâmetro de Integração Financeira para que contabilize os lançamentos financeiros na inclusão:**

Essa etapa é feita diretamente no parâmetro de integração financeira do contrato:

### **3) Neste exemplo, dentro do parâmetro "Padrão Aluguel" definimos o tipo de documento e o efeito contábil foi parametrizado para "Efeito Contábil":**

Dessa forma a contabilidade será gerada no momento da geração dos lançamentos financeiros.  
A definição do tipo de documento é importante pois é neste documento que iremos parametrizar o evento financeiro para a contabilização de inclusão.

### **4) Vamos no parametrizador do financeiro onde iremos definir um default de tabelas para que o TCGI faça a contabilização:**

Use o default "Tipo de Documento" que deve ser cadastrado em *Ambiente / Parâmetros / Gestão Financeira / Contas a Receber / Contab. Financeiro*

### **5) Estando esse parâmetro salvo no financeiro, vamos agora alterar o cadastro de tipo de documento:**

Devemos alterar o mesmo tipo de documento que usamos no parâmetro de integração associado aos contratos.  
Neste exemplo é o de código 37 e devemos consultar a aba de **Evento Contábil:**

### **6) E aqui definir o Evento Contábil para contabilização de inclusão:**

Desta forma **todos os lançamentos gerados** a partir dos processos de aluguel que utilizam o parâmetro de integração financeira serão gerados com o tipo "**Contábil**" e contabilizados com o evento acima parametrizado:  
Exemplo com a parametrização acima:

Gerando lançamento para a **C****ompetência do mês 09/22**

Contabilização de inclusão **preenchida**no lançamento gerado com o evento do tipo de documento:
