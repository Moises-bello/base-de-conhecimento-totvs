---
content_hash: 0f0c17ab63d3ed1daa24b3d42e19bcbcd7a726c3fbe2274bed7a298261ad4fde
fetched_at: '2026-06-29T00:05:58.308911+00:00'
page_id: '185748574'
product: rm
source: tdn-rm
title: Metadados com Action Anexas - Funcionário I
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185748574
version: 19
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de pagamento |
| **Processo** | **:** | Metadados |
| **Subprocesso** | **:** | Incluir um anexo em funcionário |
| **Versão** | **:** | 12.1.3 |

Este documento possui o objetivo de auxiliar o usuário no processo de criação de um anexo em funcionários, que tem a finalidade de informar um "Substituto Padrão" para um determinado funcionário, será utilizado o Metadados para a criação deste anexo.

Substituto padrão é o substituto "natural" de um funcionário, na ausência do funcionário, quem responderá por ele será o substituto padrão.

**Processo de criação**

## **Passo 1 – Criação da Tabela**

---

Para acessar a criação de tabelas, siga o seguinte caminho: Serviços Globais > Metadados (Beta) >Tabela

**Foto 1**

1. Dê um nome e rótulo para a tabela.
2. Escolha onde esta tabela será aplicada.
3. Execute os seguintes passos:
   1. Crie as colunas: CODCOLIGADA, CHAPASUBSTITUIDO, CODCOLSUBSTITUTO, CHAPASUBSTITUTO, DATAINICIO, DATAFIM E MOTIVO conforme a foto "Foto 1-1".
   2. Coloque as colunas CODCOLIGADA, CHAPASUBSTITUIDO, CHAPASUBSTITUTO, DATAINICIO como chave primaráa.
   3. Para as colunas CHAPASUBSTITUIDO, CHAPASUBSTITUTO E MOTIVO informe respectivamente no campo “Tamanho” 100,100,200.
   4. Deixe as colunas CODCOLIGADA, CHAPASUBSTITUIDO E CODCOLSUBSTITUTO invisíveis, ou seja, desmarque as seguintes checkboxes:

* + - Visível na Visão?
    - Visível na Edição?

## **Passo 2 – Criação do Modelo de Negócio**

---

Para acessar a criação do Modelo de Negócio, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Modelo de Negócio 

### 

### **Parte 1.**

### **Foto 2**

1. Dê um nome e rótulo para o Modelo de Negócio.
2. Escolha onde o Modelo de Negócio será aplicado.
3. Clique na aba “Estrutura de Dados”.
4. Acesse o menu Novo -> Tabela. (Foto 3)
5. Selecione a tabela criada no passo 1. (Foto 4)
6. Clique na aba “Controles” e clique em salvar para liberar o acesso aos campos. (Foto 3)

**Foto 3**

**Foto 4**

### **Parte 2 – Configurando os campos.**

**Foto 5**

1. Modifique o campo “Rótulo”, para alterar a informação que fica em cima do mesmo

·         Exemplo:

·         Realize esta operação para todas as colunas, fazendo com que fique mais agradável.

2. No campo “Tipo de Controle” realize as seguintes modificações.

·         Coloque o tipo “Data” para as colunas DATAFIM E DATAINICIO, com essa modificação o usuário terá a opção de abrir o calendário e selecionar a data.

·         No campo “CHAPASUBSTITUTO” realize a seguinte operação para a criação de um Lookup:

Ø Em “Action fonte de dados” selecione Funcionário.

Ø Faça o relacionamento, igual é demonstrado na Foto 6.

Ø Informe que a “descrição da fonte de dados” será o campo Nome.

**Foto 6**

## **Passo 3 – Criação de Formulários.**

---

Para acessar a criação de Formulários, siga o seguinte caminho: Serviços Globais > Metadados (Beta) >Formulários

**Foto 7**

1. Dê um nome e rótulo para o Formulário.
2. Escolha onde o Formulário será aplicado.
3. Selecione o “Modelo de Negócio” criado no passo anterior.
4. Clique na aba “Apresentação” e em seguida clique em “Salvar”. Revise o que foi feita na Parte 2 do Passo 2 e faça as correções necessárias.

## **Passo 4 – Criação do Projeto.**

---

Para acessar a criação de Projeto, siga o seguinte caminho: Serviços Globais > Metadados (Beta) > Projeto

**Foto 8**

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

Acesse RH -> Folha de pagamento -> Funcionário -> Anexo -> Configurar Anexo.

1. Clique em adicionar Action (+Action).

2. Procure o metadados criado e selecione o mesmo.

3. Selecione a action adicionada.

4. Faça o relacionamento da tabela criada com a tabela de funcionário.

Pronto !  O anexo já está disponível no cadastro do funcionário conforme imagem abaixo.

Agora precisamos melhorar a visualização do formulário, pois alguns campos ficam com tamanhos desproporcionais aos valores.

Siga o passo 7 para configurar os campos.

# **Passo 7 – Configurando o Leiaute do Formulário**

---

1. Acesse Funcionário novamente par atualizar e então entre no Anexo criado.
2. Crie um novo filtro e em seguida clique em “INCLUIR”.
3. Clique em "definir Leiaute".
4. Utilizaremos o recurso “Item Vazio” como demostra a foto a baixo para customizar o formulário.

Arraste o “item vazio” para o fim do formulário, ficando embaixo de todos os campos.

Arraste o campo “Data Início” para cima.

Adicione um “Item Vazio” na frente do campo “Chapa Substituto”, fazendo com que o ganhe liberdade para aumentar ou diminuir o tamanho do campo.

Agora que compreendeu um pouco melhor o assunto, personalize os formulários criados pelo metadados do jeito que melhor lhe convém.

Exemplo de Leiaute:

O formulário está pronto para ser utilizado.
