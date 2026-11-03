---
content_hash: db78e26da185a08b92614363b90e206ace9d06e39bd3463e15073a400fc54069
fetched_at: '2026-06-29T00:08:48.610976+00:00'
page_id: '327324727'
product: rm
source: tdn-rm
title: Utilizando a Atividade "Assumir Tarefa"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327324727
version: 42
---

## **CONTEÚDO**

1. **Objetivo**
2. **Configuração**

## **01. OBJETIVO**

Este documento tem como finalidade, demonstrar o uso da atividade "Assumir Tarefa".

## **02. CONFIGURAÇÃO**

**Informações Gerais - Atividade Assumir Tarefa**

**Objetivo:** A finalidade da atividade "Assumir Tarefa" é permitir que um Colaborador assuma uma tarefa e consequentemente dê prosseguimento ao fluxo do **Processo**.  
**Passo a Passo:** Primeiramente é necessário arrastar a atividade **"Assumir Tarefa"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Após preencher as propriedades, salve e execute a **Fórmula Visual**. Verifique o resultado do processo. A **Fórmula Visual** deverá executar com sucesso.

Resultado: A Solicitação 40 que estava com Carlos Philippe Farias Marques agora foi assumida por Stella Vilaca.

**Parâmetros do Método TakeProcessTask**

* **CompanyId****(Opcional)**

**Descrição:** Código da Empresa.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer valor numérico que represente o Código da Empresa)

* **ProcessInstanceId****(Obrigatório)**

**Descrição:** Número da Solicitação.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Número da Solicitação do **Processo**.  
**Valor Utilizado na Requisição:** 40

* **ThreadSequence****(Obrigatório)**

**Descrição:**Indica se existe atividade paralela no processo. Se não existir o valor é 0 (zero), caso exista, este valor pode ser de 1 a infinito dependendo da quantidade de atividade paralelas existentes no processo.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo Inteiro, ou seja, deve-se utilizar um valor numérico que represente o valor da existência de uma atividade paralela no Processo.  
**Valor Utilizado na Requisição:**0

* **UserId****(Opcional)**

**Descrição:**Matrícula do usuário que vai executar a tarefa.  
**Tipo:**Cadeia de Caracteres (String)  
**Como Usar:**Esse parâmetro é do tipo Cadeia de Caracteres, ou seja, deve-se utilizar um valor alfanumérico que represente a Matrícula do Usuário que vai executar a tarefa vinculada ao Processo.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer usuário ativo cadastrado no FLUIG)

**Retorno do Método TakeProcessTask**

****Descrição:****Retorno do método TakeProcessTask. ****Tipo:****Cadeia de Caracteres (String)

**Estrutura de retorno com sucesso (Webservice):**

**Estrutura de retorno com erro (Webservice):**
