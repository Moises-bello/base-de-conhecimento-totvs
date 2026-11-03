---
content_hash: b14838a003b10baaef7fd7e578a8b822db307b8dee9988acae10273cd5f0c1aa
fetched_at: '2026-06-29T00:08:48.784549+00:00'
page_id: '327331755'
product: rm
source: tdn-rm
title: Utilizando Atividade "Iniciar Solicitação Simples"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327331755
version: 27
---

## **CONTEÚDO**

1. **Objetivo**
2. **Configuração**

## **01. OBJETIVO**

     Este documento tem como finalidade, demonstrar o uso da atividade **"**Iniciar Solicitação Simples**"**.

## **02. CONFIGURAÇÃO**

Atenção

A Atividade "**Iniciar Solicitação Simples**" utiliza como padrão o usuário e senha configurados nos parâmetros globais do sistema.

**Todas as solicitações serão criadas pelo usuário Administrador**, para criar uma solicitação utilizando um outro usuário é necessário utilizar a atividade Iniciar Solicitação Clássica.

**Informações Gerais - Atividade Iniciar S****olicitação Simples**

**Objetivo:** A finalidade da atividade "Iniciar Solicitação Simples" é permitir que um Colaborador crie uma solicitação de um **Processo**.  
**Passo a Passo:** Primeiramente é necessário arrastar a atividade **"Iniciar Solicitação Simples"** para o **"Fluxo de Trabalho Sequencial"** em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira:

Caso queira enviar um **CardData (Dados do formulário vinculado à um processo)**, basta vinculá-lo, ou a uma atividade **Recuperar Campos do Formulário do Processo (RMSFluigGetProcessFormFields)** ou à qualquer outra atividade com uma propriedade do tipo **string[][]**

Caso queira enviar um **Anexo**, preencha as propriedades da sessão **Dados do Anexo**

Atenção

Lembrando que apenas um anexo por vez poderá ser enviado.

Após preencher as propriedades, salve e execute a **Fórmula Visual**. Verifique o resultado do processo. A **Fórmula Visual** deverá executar com sucesso.

Resultado: Primeiramente vamos relembrar a Atividade **"Recuperar Campos do Formulário do Processo (RMSFluigGetProcessFormFields)"**: Observe os dados preenchidos.

No Fluig perceberemos que uma nova Solicitação de **Processo** foi criada.

**Dados do Anexo**

* **Description (Opcional)**

**Descrição:**Descrição do anexo.  
**Tipo:**Cadeia de Caracteres (String)  
**Como Usar:**Esse parâmetro é do tipo**Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que a descrição do arquivo anexado ao **Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer descrição)

* **FileContent (Opcional)**

**Descrição:**Conteúdo do Arquivo em Data64, caso queira que o arquivo seja transferido por stream.  
**Tipo:**Array de Bytes (byte[])  
**Como Usar:**Esse parâmetro é do tipo**Array de Bytes**, ou seja, deve-se utilizar um array de bytes que representem o arquivo à ser anexado ao**Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer arquivo, sendo ele um Array de Bytes (byte[]))

* **Filename (Opcional)**

**Descrição:** Nome do arquivo físico.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o nome do arquivo físico do anexo vinculado ao **Processo**.  
**Valor Utilizado na Requisição:** N/A  
**Exemplo de Utilização:** (Qualquer nome)

**Dados dos Registros dos Formulários**

* **CardData****(Opcional)**

**Descrição:**Itens de um Formulário de um Processo  
**Tipo:**Array de Array de Cadeia de Caracteres (String[][])  
**Como Usar:**Esse parâmetro é do tipo**Array de Array de Cadeia de Caracteres**, ou seja, deve-se utilizar um conjunto de valores alfanuméricos que represente os campos do formulário do**Processo**.  
**Valor Utilizado na Requisição:**Activity=rmsFluigGetProcessFormFieldsActivity1, Path=Retorno (Associação)

**Parâmetros do Método SimpleStartProcess**

* **Comments (Obrigatório)**

**Descrição:** Comentários.  
**Tipo:** Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico para acrescentar comentários ao **Processo**.  
**Valor Utilizado na Requisição:** Teste

* **CompanyId (Opcional)**

**Descrição:**Código da Empresa.  
**Tipo:**Inteiro  
**Como Usar:**Esse parâmetro é do tipo**Inteiro**, ou seja, deve-se utilizar um valor numérico que represente o Código da Empresa vinculada ao **Processo**.  
**Valor Utilizado na Requisição:**N/A  
**Exemplo de Utilização:**(Qualquer valor numérico que represente o Código da Empresa)

* **ProcessId (Obrigatório)**

**Descrição:**Código do Processo  
**Tipo:**Cadeia de Caracteres (String)  
**Como Usar:** Esse parâmetro é do tipo**Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o Código do**Processo**.  
**Valor Utilizado na Requisição:**Activity=rmsFluigGetProcessFormFieldsActivity1, Path=ProcessId (Associação)

**Retorno do Método SimpleStartProcess**

**Descrição:** Retorno do método SimpleStartProcess.  
**Tipo:** Array de uma Cadeia de caracteres (String[])

**Estrutura de retorno com sucesso (Webservice):**

**Estrutura de retorno com erro (Webservice):**
