---
content_hash: 654996709483761b0289cbbf911eefdc90a3a851b82ee77b9c6dd45f7edf5eee
fetched_at: '2026-06-29T00:10:58.243477+00:00'
page_id: '604529058'
product: rm
source: tdn-rm
title: Exporta Informações para Ministério da Saúde (CIHA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604529058
version: 30
---

## **CONTEÚDO**

1. #### **VISÃO GERAL**
2. #### **PREENCHIMENTO DE INFORMAÇÕES DE CIHA**
3. #### **EXPORTAÇÃO DE INFORMAÇÕES PARA O MINISTÉRIO DA SAÚDE**
4. #### **TABELAS UTILIZADAS**

## **01. VISÃO GERAL**

Após o processo de Alta do paciente é importante que sejam preenchidas as informações que obrigatoriamente devem serem encaminhadas para o Ministério da Saúde (MS) pelo Sistema do próprio MS denominado CIHA – Sistema de **Comunicação de Informação Hospitalar e Ambulatorial.**A Comunicação de Informação Hospitalar e Ambulatorial foi criada para ampliar o processo de planejamento, programação, controle, avaliação e regulação da assistência à saúde permitindo um conhecimento mais abrangente, amplo e profundo dos perfis nosológico e epidemiológico da população brasileira, da capacidade instalada e do potencial de produção de serviços do conjunto de estabelecimentos de saúde do País.

## **02****. PREENCHIMENTO DE INFORMAÇÕES DE CIHA**

**Permissão do Usuário:** Deverá previamente configurar o parâmetro **"Informações Ministério da Saúde - CIHA"**, abaixo informações de como configura-lo:

1. **Cadastros** - **Segurança**e selecione **Perfis**.
2. Selecione o Perfil a ser configurado (Exemplo: DBA).
3. Acessa aba **Acesso a Menus**.
4. Clique na opção "**- Recolher Tudo**" para melhor visualização aos menus.
5. Selecione **Atendimento** -  **Internação** - **Informações p/ o Ministério de Saúde** e clique **Proibir Acesso** para **não permitir liberação para geração do arquivo**.

6. Selecione **Atendimento** -  **Pronto Atendimento / Ambulatório** -**Informações p/ o Ministério da Saúde** e clique **Proibir Acesso** para **não permitir liberação para geração do arquivo**.

7. Acesse o menu **Sistema** e clique em **Selecionar Coligada** para atualizar alterações no sistema.

**Após a configuração do parâmetro no passo anterior, vamos preencher as Informações de CIHA:**

1. Acesse: **RM / Saúde / Hospitais e Clínicas / Atendimento / Recepção / Registro de Atendimento / Informações para o Ministério da Saúde (CIHA)**
2. Será exibida a tela de visão com todos os atendimentos já registrados
3. Crie um filtro para selecionar os registros adequados para o preenchimento / liberação do registro.
4. Dê um duplo clique no paciente/atendimento desejado e será exibida a tela para preenchimento das informações para o ministério da saúde.
5. Selecione o Procedimento principal, o diagnóstico principal e o diagnóstico secundário.
6. Informe o tipo de alta.
7. No menu Anexos, é possível ter acesso aos demais Procedimentos Realizados do CIHA
8. Em seguida determine se as informações registradas serão ou não liberadas para geração do arquivo, que será enviado para o ministério da saúde.
9. Clique em **Salvar/OK**.

Aba Identificação: Informações principais da execução como procedimento principal, CIDs, quantidade e tipo de Alta;

Anexo: Procedimentos Realizados do CIHA

Atenção

O anexo "Procedimentos Realizados do CIHA" somente poderá ser visualizado se o registro selecionado for de um paciente externo.

Caso o registro selecionado não seja de um paciente externo, a opção para abrir o anexo não é exibida, e caso o anexo esteja aberto, o mesmo será fechado.

**Correlação:** Essa opção possibilita a automatização do preenchimento de informações de CIHA, para esse processo, deverá previamente fazer a correlação de itens com a tabela SUS, caso não tenha esse relacionamento, o processo de automatização não irar encontrar o item na tabela SUS, abaixo passos para fazer a correlação:

Acesse a tela de RM / Saúde / Hospitais e Clínicas / Cadastro / Uso Geral / Outros Cadastros / Correlação de Itens com a tabela SUS:

Nesta funcionalidade você poderá vincular o Cod . tabela do Convênio, Cod.Proc. SUS, Cod. Proc Convênio:

## **03.****EXPORTAÇÃO DE INFORMAÇÕES PARA O MINISTÉRIO DA SAÚDE**

1. No RM Saúde Utilitários>Exportar informações para Ministério da Saúde

2. Informe a Unidade de Faturamento, Status do Envio CIHA e Competência.

3. Clique em Consultar para exibir os atendimentos.

4. Ao listar os atendimentos, alguns podem está com o Status liberados, porém com algumas informações pendentes, neste caso o sistema informar na coluna Dados a informação ***incompletos,*** indicando que existem pendências no registro. Expandindo a informação será possível visualizar qual a pendência para ser resolvida.

5. Caso será necessário realizar a exportação, todos os itens com pendência deverão ser corrigidos ou marcado para ***Não Liberar.***Para isso selecione o registro e execute a ação de ***Não Libera.***

6. Caso precise liberar algum atendimento que esteja com o Status Não Liberado, basta executar a consulta informando o Status ***Não Liberado***, na listagem selecione o registro que deseja liberar e execute a ação ***Liberar.***

7. Em algumas situações, se faz necessário exportar algum registro de outra competência que não tenha sido exportado anteriormente. Para isso, o usuário poderá executar a ação Incluir Atendimentos.

8. A consulta poderá ser realizada através do Código do Paciente, Nome do Paciente, CPF. Os campos Data Inicio e Data Final, são obrigatórios para consulta. Após Identificar o atendimento para ser incluído, basca clicar no ícone + para adicionar o registro para exportação.

9. Após adicionar o atendimento, aparecerá na lista para ser exportado. Na imagem abaixo utilizei o campo ***Filtrar*** para identificar o paciente de forma mais rápida.

Com o campo filtrar podemos realizar a busca por CPF, Nome Paciente, Data de Encerramento do Atendimento e Código do Paciente.

10. O arquivo só poderá ser exportado caso não haja nenhuma pendência nos registros que estão com o status Liberado.

Caso algum registro esteja pendente, o sistema emitirá a seguinte mensagem e não será possível realizar a exportação.

11. Após correção dos registros, ao clicar em Exportar CIHA, o arquivo deverá ser gerado no diretório de instalação do RM /Atual/CIHA.

Para exportação não se faz necessário selecionar os registros, TODOS os registros dentro do filtro informado deverão ser exportados.

12. Após exportados, os registros ficarão com o Status Finalizados e poderá ser consultado utilizando o Filtro Status Finalizado.

## **04. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZCADGERAL
* SZPACIENTE
* SZPARCIALATEND

]]>
