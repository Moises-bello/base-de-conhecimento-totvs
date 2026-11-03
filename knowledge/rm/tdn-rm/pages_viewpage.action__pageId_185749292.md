---
content_hash: bac095edd386854f4cae9152dfe67f0f9b842cdbd31ab4b02fc280a2ba3b4bc7
fetched_at: '2026-06-29T00:05:58.335240+00:00'
page_id: '185749292'
product: rm
source: tdn-rm
title: Metadados com Action Anexas - Funcionário II
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185749292
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de pagamento |
| **Processo** | **:** | Metadados |
| **Subprocesso** | **:** | Incluir um anexo em funcionário |
| **Versão** | **:** | 12.1.3 |

Este documento possui o objetivo de auxiliar o usuário no processo de criação de um anexo em funcionários, que tem a finalidade de armazenar   
informações relativas a funções gratificadas e cargos comissionados, gerando um histórico por período de datas.

Possibilitando ainda informar um nível de carreira para estes funcionários.

O documento será dividido em 2 Partes, sendo a primeira a criação de um Metadados com o nome de Nível que servirá de "Lookup" para o segundo Metadados.

# 

# **Processo de Criação - Parte 1 - Tabela de Nível (Lookup)**

## **Passo 1 – Criação da Tabela**

---

Para acessar a criação de tabelas, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Tabela

**Foto 1-1**

1. Coloque o nome da tabela de "NIVEL" e o rótulo de "Nível".
2. A aplicação da tabela será no "RM LABORE".
3. Execute os seguintes passos:
   1. Crie as colunas "CODIGO" e "DESCRICAO".
   2. Coloque "CODIGO" como chave primária.
   3. No campo "DESCRICAO" marque a opção "Descrição para Lookup?".
   4. Para as colunas "CODIGO" e "DESCRICAO" informe respectivamente no campo "Tamanho" 10 e 20.

## **Passo 2 – Criação do Modelo de Negócio**

---

Para acessar a criação do Modelo de Negócio, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Modelo de Negócio

 

### **Criação do Modelo de Negócio - Parte 1-1.**

**Foto 1-2**

1. Dê um nome e rótulo para o Modelo de Negócio.
2. A aplicação do "Modelo de Negócio" será no "RM LABORE".
3. Clique na aba “Estrutura de Dados”.
4. Acesse a opção Novo > Tabela. (Foto 1-3)
5. Selecione a tabela criada no passo 1. (Foto 1-4)
6. Clique na aba “Controles” e clique em salvar para liberar o acesso aos campos. (Foto 1-3)

**Foto 1-3**

**Foto 1-4**

### 

### **Criação do Modelo de Negócio -****Parte 1-2 – Configurando os campos.**

**Foto 1-5**

1. Modifique o campo “Rótulo”, para alterar a informação que fica em cima do mesmo

* + Exemplo:
  + Realize esta operação para todas as colunas, conforme demostra a imagem acima. (Foto 1-5)

## **Passo 3 – Criação de Formulários.**

---

Para acessar a criação de Formulários, siga o seguinte caminho: Serviços Globais > Metadados (Beta) >Formulários

1. Dê um nome e rótulo para o Formulário.
2. Escolha onde o Formulário será aplicado.
3. Selecione o “Modelo de Negócio” criado no passo anterior.
4. Clique na aba “Apresentação” e em seguida clique em “Salvar”. Revise o que foi feita na "Criação do Modelo de Negócio - Parte 1-2 – Configurando os campos" e faça as correções necessárias.

## 

## **Passo 4 – Criação do Projeto.**

---

Para acessar a criação de Projeto, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Projeto

**Foto 1-6**

1. Dê um nome para o Projeto.
2. Informe a versão.
3. Escolha onde o Metadados será aplicado.
4. Selecione o formulário criado no passo 3
5. Selecione o Segmento.
6. Gere um ID de Segurança.
7. Selecione onde este Metadados será disponibilizado.
8. Marque a checkbox do projeto criado e vá em Processos -> Gerar Projeto de Metadados para finalizar a criação

# **Processo de Criação - Parte 2 - Tabela Principal (Cargo Comissionado e Função Gratificada)**

## **Passo 1 – Criação da Tabela**

---

Para acessar a criação de tabelas, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Tabela

**Foto 2-1**

1. Dê um nome e rótulo para a tabela.
2. Escolha onde esta tabela será aplicada.
3. Execute os seguintes passos:
   1. Crie as colunas: CODCOLIGADA, CHAPA, CODIGO, NIVEL, OPCAO, DATAINICIO, DATAFIM conforme a "Foto 2-1".
   2. Coloque as colunas CODCOLIGADA, CHAPA, CODIGO como chave primária.
   3. Para as colunas NIVEL E OPCAO informe no campo “Tamanho” 50.
   4. Deixe as colunas CODCOLIGADA e CHAPA invisíveis, ou seja, desmarque as seguintes checkboxes:

* + - Visível na Visão?
    - Visível na Edição?

## **Passo 2 – Criação do Modelo de Negócio**

---

Para acessar a criação do Modelo de Negócio, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Modelo de Negócio

 

### **Criação do Modelo de Negócio - Parte 2-1.**

**Foto 2-2**

1. Dê um nome e rótulo para o Modelo de Negócio.
2. Escolha onde o Modelo de Negócio será aplicado.
3. Clique na aba “Estrutura de Dados”.
4. Acesse o menu Novo -> Tabela. (Foto 2-3)
5. Selecione a tabela criada no passo 1. (Foto 2-4)
6. Clique na aba “Controles” e clique em salvar para liberar o acesso aos campos. (Foto 2-3)

**Foto 2-3**

**Foto 2-4**

### **Criação do Modelo de Negócio -****Parte 2-2 – Configurando os campos.**

**Foto 2-5**

1. Modifique o campo “Rótulo”, para alterar a informação que fica em cima do mesmo

* + Exemplo:
  + Realize esta operação para todas as colunas, conforme demostra a imagem acima. (Foto 2-5)

2. No campo “Tipo de Controle” realize as seguintes modificações.

* + Coloque o tipo “Data” para as colunas DATAFIM E DATAINICIO, com essa modificação o usuário terá a opção de abrir o calendário e selecionar a data.
  + Em OPCAO coloque o tipo "Caixa de opção" e coloque as seguintes informações:
  + Na coluna NIVEL vamos realizar a seguinte operação:

Em “Action fonte de dados” pesquise e selecione a tabela de Nível criada no início do documento.  
> Faça o relacionamento, igual é demonstrado na Foto 2-6.  
> Informe que a “descrição da fonte de dados” será o campo Descrição.

## 

## **Passo 3 – Criação de Formulários**

---

Para acessar a criação de Formulários, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Formulários

1. Dê um nome e rótulo para o Formulário.
2. Escolha onde o Formulário será aplicado.
3. Selecione o “Modelo de Negócio” criado no passo anterior.
4. Clique na aba “Apresentação” e em seguida clique em “Salvar”. Revise o que foi feita na "Criação do Modelo de Negócio - Parte 2-2 – Configurando os campos" e faça as correções necessárias.

## **Passo 4 – Criação do Projeto.**

---

Para acessar a criação de Projeto, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Projeto

1. Dê um nome para o Projeto.
2. Informe a versão.
3. Escolha onde o Metadados será aplicado.
4. Selecione o formulário criado no passo 3
5. Selecione o Segmento.
6. Gere um ID de Segurança.
7. Selecione onde este Metadados será disponibilizado.
8. Marque a checkbox do projeto criado e vá em Processos -> Gerar Projeto de Metadados para finalizar a criação.

## **Passo 5**

---

Após a criação do Metadados, recrie o ".broker” e então vá em Serviços Globais -> Serviços -> Actions do sistema -> Processos -> Atualização de actions cadastradas.

Lembre-se de dar permissão aos perfis desejados, para que os mesmos tenham acesso aos Metadados criados.

## **Passo 6 – Configurando o anexo.**

---

Acesse RH -> Folha de pagamento -> Funcionários -> Anexo -> Configurar Anexo.

1. Selecione o último campo da treeview "Folha de Pagamento", como demonstra a foto abaixo e então clique em adicionar Action (+Action).
2. Procure o Metadados criado e selecione o mesmo.
3. Selecione a action adicionada.
4. Faça o relacionamento da tabela criada com a tabela de Funcionários.
5. Entre novamente em "Funcionários" para atualizar.  
     
   Pronto !  O anexo já está disponível no cadastro do funcionário conforme imagem abaixo.

Agora precisamos melhorar a visualização do formulário, pois alguns campos ficam com tamanhos desproporcionais aos valores.

Siga o passo 7 para configurar os campos.

# **Passo 7 – Configurando o Leiaute do formulário**

---

1. Acesse o anexo criado Funcionários -> Anexo -> Folha de pagamento -> .
2. Crie um novo filtro e em seguida clique em “INCLUIR”.
3. Clique em "definir Leiaute".
4. Utilizaremos o recurso “Item Vazio” como demostra a foto a baixo para customizar o formulário.
5. Arraste o “item vazio”  para o lado do campo "Código".
6. Agora terá liberdade de aumentar ou diminuir o tamanho do campo.

Agora que compreendeu um pouco melhor o assunto, personalize os formulários criados pelo metadados do jeito que melhor lhe convém.

### **Exemplo de Leiaute da tabela principal:**

### **Exemplo de Leiaute da tabela de Nível:**

O formulário está pronto para ser utilizado.
