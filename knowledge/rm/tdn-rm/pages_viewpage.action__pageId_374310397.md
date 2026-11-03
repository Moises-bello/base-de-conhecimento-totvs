---
content_hash: 86a4b62a6818fee38c7e585525138b75bfc6c3757422ade205cca145a147355a
fetched_at: '2026-06-29T00:09:01.615233+00:00'
page_id: '374310397'
product: rm
source: tdn-rm
title: Utilizando Atividade "Iniciar Processo Clássico"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374310397
version: 44
---

## **CONTEÚDO**

1. **Objetivo**
2. **Configuração**

## **01. OBJETIVO**

Este documento tem como finalidade, demonstrar o uso da atividade **"**Iniciar Processo Clássico**"**.

## **02. CONFIGURAÇÃO**

**Informações Gerais - Atividade Iniciar Processo Clássico**

**Objetivo:** A finalidade da atividade "Iniciar Processo Clássico" é permitir que um Colaborador crie uma solicitação de um **Processo** informando quem será o solicitante e o responsável pela tarefa.  
**Passo a Passo:** Primeiramente é necessário arrastar a atividade **"Iniciar Processo Clássico"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Caso queira enviar um **CardData (Dados do formulário vinculado à uma solicitação)**, basta vinculá-lo, ou a uma atividade **Recuperar Campos do Formulário da Solicitação (RMSFluigGetInstanceCardData)** ou à qualquer outra atividade com uma propriedade do tipo **string[][]**

Caso queira enviar um **Anexo**, preencha as propriedades da sessão **Dados do Anexo**

Atenção

Lembrando que apenas um anexo por vez poderá ser enviado.

Caso queira realizar um **Apontamento**, preencha as propriedades da sessão **Dados do Apontamento**

Atenção

Lembrando que apenas um apontamento poderá ser realizado por vez.

Após preencher as propriedades, salve e execute a **Fórmula Visual**. Verifique o resultado do processo. A **Fórmula Visual** deverá executar com sucesso.

**Dados do Anexo**

* **Description (Opcional)**

**Descrição:** Descrição do anexo.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que a descrição do arquivo anexado à solicitação do **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer descrição)

* **FileContent (Opcional)**

**Descrição:**Conteúdo do Arquivo em Data64, caso queira que o arquivo seja transferido por stream.  
**Tipo:**Array de Bytes (byte[])  
**Como Usar:**Esse parâmetro é do tipo**Array de Bytes**, ou seja, deve-se utilizar um array de bytes que representem o arquivo à ser anexado à solicitação do**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer arquivo, sendo ele um Array de Bytes (byte[]))

* **Filename (Opcional)**

**Descrição:** Nome do arquivo físico.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o nome do arquivo físico do anexo vinculado a solicitação do **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer nome)

**Dados do Apontamento**

* **AppointmentDate (Opcional)**

**Descrição:**Data para o apontamento.  
**Tipo:**Data  
**Como Usar:**Esse parâmetro é do tipo**Data**, ou seja, deve-se utilizar uma data para o apontamento da tarefa vinculada à solicitação do**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer data)

* **AppointmentSeconds (Opcional)**

**Descrição:**Segundos para o apontamento.  
**Tipo:**Inteiro  
**Como Usar:**Esse parâmetro é do tipo**Inteiro**, ou seja, deve-se utilizar um valor numérico que represente os segundos para o apontamento da tarefa vinculada à solicitação do**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer valor numérico)

* **AppointmentSequence (Opcional)**

**Descrição:**Sequência de Apontamento  
**Tipo:**Inteiro  
**Como Usar:**Esse parâmetro é do tipo**Inteiro**, ou seja, deve-se utilizar um valor numérico que represente a sequência de apontamento da tarefa vinculada à uma solicitação de **Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer valor numérico)

* **ColleagueName (Opcional)**

**Descrição:** Nome do usuário para o apontamento.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o Nome do Usuário que irá apontar na tarefa vinculada a solicitação do**Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Nome de qualquer usuário ativo cadastrado no FLUIG)

* **MovementSequence (Opcional)**

**Descrição:** Sequência da Movimentação  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente a sequência de movimentação da tarefa vinculada à uma solicitação de **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer valor numérico)

* **TransferenceSequence (Opcional)**

**Descrição:** Sequência da transferência da atividade (histórico de movimentações).  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente a sequência de transferência da tarefa vinculada à uma solicitação de **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer valor numérico)

**Dados dos registros do formulário**

* **CardData****(Opcional)**

**Descrição:** Itens de um Formulário de uma Solicitação  
**Tipo:** Array de Array de Cadeia de Caracteres (String[][])  
**Como Usar:** Esse parâmetro é do tipo **Array de Array de Cadeia de Caracteres**, ou seja, deve-se utilizar um conjunto de valores alfanuméricos que represente os campos do formulário da solicitação do **Processo**.  
**Valor Utilizado na Requisição:** Activity=rmsFluigGetInstanceCardDataActivity1, Path=Retorno (Associação)

**Parâmetros do Método StartProcessClassic**

* **ChoosedState (Obrigatório)**

**Descrição:** Número da Atividade.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Número da Atividade vinculada a solicitação do **Processo**.  
**Valor Utilizado na Requisição:** 0

* **ColleagueId (Obrigatório)**

**Descrição:** Usuário que receberá a tarefa.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que indicará qual Colaborador assumirá a atividade vinculada à uma solicitação de **Processo**.  
**Valor Utilizado na Requisição:** japa

* **Comments (Obrigatório)**

**Descrição:** Comentários.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico para acrescentar comentários à atividade vinculada a solicitação do **Processo**.  
**Valor Utilizado na Requisição:** Teste

* **CompanyId (Obrigatório)**

**Descrição:** Código da Empresa.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao **Processo**.  
**obs:** Caso não seja informado o valor receberá o código da empresa configurado na integração.  
**Valor Utilizado na Requisição:**1  
**Exemplo de Utilização:** (Qualquer valor numérico que represente o Código da Empresa)

* **CompleteTask (Opcional)**

**Descrição:** Indica se deve completar a tarefa (true) ou somente salvar (false).  
**Tipo:** Lógico (Booleano)  
**Como Usar:** Esse parâmetro é do tipo **Lógico**, ou seja, deve-se utilizar um valor lógico (Sim ou Não / Falso ou Verdadeiro) que indique a vontade de Completar a tarefa ou de somente Salvar a tarefa.  
**Valor Utilizado na Requisição:**True  
**obs:** Quando o parâmetro estiver como false, a tarefa não é direcionada ao usuário configurado no campo "ColleagueId".

* **ManagerMode (Opcional)**

**Descrição:** Indica se o usuário está executando a tarefa como gestor do processo.  
**Tipo:** Lógico (Booleano)  
**Como Usar:** Esse parâmetro é do tipo **Lógico**, ou seja, deve-se utilizar um valor lógico (Sim ou Não / Falso ou Verdadeiro) que indique se o usuário está executando a tarefa como gestor do Processo.  
**Valor Utilizado na Requisição:** False

* **ProcessID(Obrigatório)**

**Descrição:** Código do processo.  
**Tipo:** Inteiro  
**Como Usar:** Esse parâmetro é do tipo **Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Número da Solicitação do **Processo**.  
**Valor Utilizado na Requisição:** Activity=rmsFluigGetInstanceCardDataActivity1, Path=ProcessInstanceId (Associação)

* **UserId (Obrigatório)**

**Descrição:** Usuário que vai executar a tarefa.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente a Matrícula do Usuário que vai executar a tarefa vinculada ao **Processo**.  
**Valor Utilizado na Requisição:** mestre  
**Exemplo de Utilização:** CodUsuário (RM) ou Matricula (Fluig).

**Retorno do Método StartProcessClassic**

**Descrição:** Retorno do método StartProcessClassic.  
**Tipo**: Array de Array de Cadeia de caracteres (String[][])

**Estrutura de retorno com sucesso (Webservice):**

**Estrutura de retorno com erro (Webservice):**
