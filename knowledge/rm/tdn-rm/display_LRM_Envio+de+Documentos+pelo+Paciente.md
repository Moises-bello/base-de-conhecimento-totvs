---
content_hash: 1e4fad3f92cbb99b3acc48b4093519476a2b54fe35cafe4ba72de5d92a9e8495
fetched_at: '2026-06-29T00:11:55.987430+00:00'
page_id: '865008015'
product: rm
source: tdn-rm
title: Envio de Documentos pelo Paciente
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+Documentos+pelo+Paciente
version: 6
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela de Campos do Paciente**
4. **Tela de Seleção/Cadastro de Convênio**
5. **Tela de Seleção de procedimento**
6. **Tela de Concluir agendamento**
7. **Tabelas utilizadas**
8. **Parâmetros Gerais**

sumarioVisão Geral

## **01. VISÃO GERAL**

A opção de envio de arquivos, permite ao paciente, anexar seus documentos ao agendamento online para que a clínica médica possa validar/analisar antecipadamente todas as informações de identificação, elegibilidade de carteirinha e procedimento, evitando imprevistos no dia da consulta/exame.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

O paciente deve anexar os documentos referentes a cada passo do agendamento de consultas/exames, clicando em "**selecione arquivos do computador**", ou arrastando os arquivos para a área de upload.

Os arquivos de anexos são dos tipos:

1. Documentos de identificação (frente e verso) ao iniciar o agendamento de uma consulta/exames - RG ou CNH
2. Documentos de carteirinha do convênio (frente e verso) ao incluir um novo convênio no portal do paciente
3. Documentos documentos de procedimentos médicos (guias, pedidos médicos, encaminhamentos);

A obrigatoriedade do anexo deve configuradas nos parâmetros gerais do portal do paciente no RM.

Tela de Campos do Paciente

## **03. TELA DE CAMPOS DO PACIENTE**

Na tela de "**Informações pessoais**" o paciente deve inserir documentos de identificação, como RG ou CNH (frente e verso). Essas informações são gravadas na base no momento de conclusão do agendamento.

Os arquivos de anexo serão carregados para outras consultas.

Limitações do envio de anexos:

* Limite de arquivos: 2 arquivos (frente e verso);
* Limite de tamanho dos arquivos: 5MB;
* Formatos válidos: JPG, JPEG, PNG e PDF;
Tela de Seleção/Cadastro de Convênio

## **04. TELA DE SELEÇÃO/CADASTRO DE CONVÊNIO**

Na tela de seleção/cadastro de convênio, o paciente deve cadastrar um novo convênio, anexando os documentos referentes a carteira do convênio a ser utilizada no agendamento.

Ao concluir o cadastro de convênio, a previa do arquivo será mostrada dentro do cartão do convênio, logo abaixo das informações de Plano, SubPlano e Número de carteirinha.

Observação: As informações de anexos serão apresentadas no convênio para próximos agendamentos de consultas/exames.

| Ação | Descrição |
| --- | --- |
| Incluir Convênio | Os anexos de imagem serão mostrados na tela, mas só serão gravados se o paciente concluir o agendamento |
| Apagar Convênio | Ao apagar um convênio que possui anexos, as imagens são removidas instantaneamente |

Tela de Seleção de procedimento

## **05.** **TELA DE SELEÇÃO DE PROCEDIMENTO**

Na tela de seleção de procedimento, o paciente deve anexar os arquivos referentes a guias, pedidos médicos, encaminhamentos e tec...

Tela de Concluir agendamento

## **06. TELA DE CONCLUSÃO DE AGENDAMENTO**

Na tela de conclusão do agendamento, é apresentado o resumo das informações do agendamento. Nessa tela também serão apresentados os anexos de documentos pessoais, convênio e procedimento conforme mostrado na imagem a seguir:

Observação: Todos os anexos só serão salvos caso o paciente conclua o agendamento.

Tabelas utilizadas

## **07. T****ABELAS UTILIZADAS**

Para gravar os dados de arquivos do portal do paciente, foi necessário a criação da tabela intermediária SZPORTALARQUIVO, contendo os campos adicionais referentes ao Paciente, convênio e procedimento relacionado ao arquivo de anexo.

* CODPORTALCADASTRO: Refere ao paciente que anexou o arquivo no portal;
* CODCADGERAL: Refere ao código do convênio ao qual foram anexados arquivos de imagem;
* CODAGENDAMENTO: Refere ao agendamento ao qual os arquivos foram anexados. Em especial, esse campo grava informações referentes aos anexos relacionados aos procedimentos realizados.
* CODARQUIVO: referente ao campo IDARQUIVO da tabela SZARQUIVO, onde os arquivo será gravado;
* TIPOARQUIVO: referente ao tipo do arquivo de anexo, sendo 1 para arquivo pessoal, 2 para arquivo de convênio e 3 para arquivo de procedimento;
* COD e CODCOLIGADA: chave primária da tabela;
Parâmetros Gerais

## **08. PARÂMETROS GERAIS**

Os parâmetros gerais configurados para envio de documentos de agendamento são:

| Parâmetro | Descrição |
| --- | --- |
| Obrigatoriedade - Documentos Pessoais | Essa opção marcada obriga o paciente a anexar arquivos de identificação no portal do paciente |
| Obrigatoriedade - Carteira do convênio | Essa opção marcada obriga o paciente a anexar arquivos de carteira convênio no portal do paciente |
| Obrigatoriedade - Documentos relacionados ao procedimento | Essa opção marcada obriga o paciente a anexar arquivos relacionados a procedimento no portal do paciente |
| Tipo de Documento - Documentos Pessoais | O valor selecionado nessa opção será usado no campo CODTIPODOC da tabela de SZARQUIVO para gravar arquivos do tipo documento pessoal |
| Tipo de Documento - Documentos de Carteira de Convênio | O valor selecionado nessa opção será usado no campo CODTIPODOC da tabela de SZARQUIVO para gravar arquivos do tipo documento de carteira de convênio |
| Tipo de Documento - Documentos relacionados a procedimentos | O valor selecionado nessa opção será usado no campo CODTIPODOC da tabela de SZARQUIVO para gravar arquivos do tipo documento relacionado a procedimento |

As configuração de envio de arquivos podem ser encontradas na terceira parte das configurações gerais do portal do paciente:
