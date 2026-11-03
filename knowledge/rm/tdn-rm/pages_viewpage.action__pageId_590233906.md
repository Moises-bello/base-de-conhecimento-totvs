---
content_hash: 21041659f7b93073792d7fcc77e2a1d47f5dfcc53a43b0357613026302b0a7d9
fetched_at: '2026-06-29T00:10:56.049761+00:00'
page_id: '590233906'
product: rm
source: tdn-rm
title: Importação de Prontuário em PDF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590233906
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-Requisitos**
3. **Passo a passo do processo**
4. **Conferência**

SumárioVisão Geral

## **01. VISÃO GERAL**

Essa funcionalidade consiste no processo de importação de arquivos em PDF, que serão adicionados ao cadastro Arquivos do Paciente (**RM Gestão Hospitalar > Cuidados com o Paciente > Arquivos do Paciente**).

Pré-Requisitos

## **02. PRÉ-REQUISITOS**

1. Os arquivos de importação devem estar no formato PDF;
2. O nome do arquivo deverá ser o código do prontuário do paciente existente no RM Gestão Hospitalar. Exemplo: 153412.pdf. O código do prontuário consta no cadastro do paciente (**RM Gestão Hospitalar > Atendimento > Dados de um Paciente**);
3. Os arquivos devem estar em uma mesma pasta, aqueles que estiverem em subpastas não serão considerados.
Passo a passo

## **03. PASSO A PASSO DO PROCESSO**

Acesse **RM Gestão Hospitalar > Utilitários > Assistente de Importação de Prontuário em PDF**:

No campo **Diretório dos arquivos PDF** informe o local em que estão os arquivos que serão importados.

Se a opção **Ignorar arquivos já importados** estiver **marcada**, a rotina de importação não irá processar novamente arquivos já existentes. Essa opção deve ser utilizada caso seja necessário realizar o processo em mais de uma etapa.

Se a opção **Ignorar arquivos já importados** estiver **desmarcada**, a rotina irá processar todos os arquivos contidos no diretório informado, sem verificar se o arquivo já existe.

Após selecionar os opções, clicar em **Executar**:

Após o final do processamento será exibida uma tela com os logs de importação:

Conferência

## **04. CONFERÊNCIA**

Para realizar a conferência dos arquivos importados, acesse o cadastro Arquivos do Paciente (**RM Gestão Hospitalar > Cuidados com o Paciente > Arquivos do Paciente**).

Ao abrir um registro, acesse o processo **Visualizar arquivo selecionado** para visualizar o PDF vinculado ao paciente.
