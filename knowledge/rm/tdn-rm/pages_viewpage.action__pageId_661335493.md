---
content_hash: b3b5944395df363fe56081676aa7017c24c1974808785af0f117c54076af6c44
fetched_at: '2026-06-29T00:11:13.518546+00:00'
page_id: '661335493'
product: rm
source: tdn-rm
title: CRIAÇÃO FÓRMULA VISUAL - Automatização do preenchimento descrição de ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661335493
version: 10
---

## **Objetivo**

Este documento visa demonstrar como implementar uma fórmula visual no RM Gestão Fiscal para automatizar o preenchimento da descrição de ajuste na Situação Tributária do Lançamento Fiscal (campo necessário para a Reinf 2060).

## **Necessidade**

Criar uma documentação explicando como automatizar o preenchimento do campo complementar que foi criado para levar a descrição do ajuste.

Na formula deve ter um filtro para testa se a CFOP é de devolução e neste caso a descrição no campo deve ser "Devolução + Numero do Lançamento" Exemplo:

**"Devolução: 000100123"**

## **Solução**

Foi criada uma Fórmula Visual buscando facilitar o processo citado, de forma que a manipulação dos dados sem necessidade de realizar ações repetitivas.

## **Passo-a-passo de como criar a Fórmula Visual**

falseFormulas1º Passo

Para se criar uma Fórmula Visual basta acessar o módulo de **Serviços Globais** - aba **Gestão | Ferramentas de Análise | Fórmula Visual | Fórmula Visual**

Imagem

Uma aba se abrirá. Clique em Incluir.

Imagem

Escolha um nome e a categoria da Fórmula, marque-a como Ativo, e se quiser coloque uma descrição e clique em OK.

Imagem2º Passo

Dê um duplo clique na Fórmula criada para abrir sua edição.

Imagem

A seguinte aba irá se abrir, e é aqui que iremos iniciar o desenho de nossa fórmula.

Imagem3º Passo

Adicionando a consulta SQL que irá selecionar os dados do Lançamento Fiscal que foi salvo.

Selecione uma nova atividade de Consulta SQL e arraste para o Fluxo da Fórmula Visual.

Imagem

Clique com o botão direito do mouse em cima da atividade de Consulta SQL e selecione a opção "Selecionar Consulta SQL".

Imagem

Clique no ícone para incluir uma nova consulta e adicione uma consulta SQL que retorne os campos que deseja copiar. Exemplo:

**SELECT DLAF.\*,DLAFCOMPL.\***  
**FROM DLAF (NOLOCK)**  
**INNER JOIN DCFOP (NOLOCK) ON (DCFOP.CODCOLIGADA = DLAF.CODCOLIGADA AND DCFOP.IDNAT = DLAF.IDNAT)**  
**LEFT JOIN DLAFCOMPL (NOLOCK) ON (DLAFCOMPL.CODCOLIGADA = DLAF.CODCOLIGADA AND DLAFCOMPL.IDLAF = DLAF.IDLAF)**  
**WHERE DCFOP.TIPODEVOLUCAO = 'D' AND DLAF.CODCOLIGADA = :CODCOLIGADA AND DLAF.IDLAFAGRUP = :IDLAFAGRUP**

Imagem

Selecione a consulta SQL criada anteriormente.

Imagem

Selecione a Atividade de Consulta SQL adicionada e preencha os parâmetros nas Propriedades.

**CODCOLIGADA:**

**Activity=RMSWorkflow, Path=ConvertedParametersOfContext.CodColigada.AsShort**

**IDLAFAGRUP:**

**Activity=RMSWorkflow, Path=Tables[0].Item["IDLAFAGRUP"].AsInteger**

Imagem4º Passo

Como pode encontrar várias situações tributárias em um único lançamento fiscal, será necessário percorrê-las para executar o preenchimento do campo Complementar de cada situação tributária.

Selecione uma nova atividade de ForEach e arraste para o Fluxo da Fórmula Visual. (Abaixo da atividade SQL)

Imagem

Selecione a atividade de ForEach adicionada, acesse a aba Propriedades e clique no ícone **Ligações**.

Imagem

No campo **Lista de Items**, apague a informação (nenhum) e preencha o campo com o valor abaixo:

Activity=Activity=rmsConsSQLActivity1, Path=Tables[0].Rows

Imagem

Selecione uma nova atividade de Sequência e arraste para dentro do ForEach adicionada anteriormente.

Imagem5º Passo

Selecione uma nova atividade de Ler Registro e arraste para dentro da atividade de Sequência adicionada no passo anterior.

Imagem

Selecione a atividade de Ler Registro adicionada, na aba Propriedades preencha o Nome do DataServer = **FisLanFiscalData** e aperte Tab no teclado.

Imagem

Preencha os campos abaixo com as seguintes informações:

**COLIGADA:**

Activity=rmsForEachActivity1, Path=Fields["CODCOLIGADA"].AsShort

**IDLAFAGRUP:**

Activity=rmsForEachActivity1, Path=Fields["IDLAFAGRUP"].AsInteger

Imagem6º Passo

Preenchendo o campo complementar descrição do código de ajuste.

Selecione uma nova atividade de Expressão e arraste para dentro da atividade de Sequência, abaixo da atividade de Ler Registro.

Imagem

Selecione a atividade de Expressão adicionada, na aba Propriedades preencha os campos abaixo:

**Expressões:** Valor Original - Ex:

**'Devolução: ' + rmsForEachActivity1.DOCINI**

**Valor Calculado:** Campo de Destino - Ex:

**Activity=rmsReadRecordActivity1, Path=Tables["DLAFCOMPL"].Item["DESCCODAJUSTE"].AsString**

Imagem

Selecione uma nova atividade Salvar Registro e arraste para dentro da atividade de Sequência, abaixo de Expressão.

Imagem

Selecione a atividade de Salvar Registro adicionada, na aba Propriedades preencha o campo abaixo:

**Atividade Ler Registro:** rmsReadRecordActivity1

Imagem7º Passo

Salvando a Fórmula Visual.

Clique no ícone Salvar para que a fórmula visual criada seja salva.

Imagem

## **Passo-a-passo para associar a Fórmula Visual em Salvar um Lançamento Fiscal**

A fórmula visual será associada na tela de Lançamentos Fiscais (Entrada ou Saída) na ação de salvar um registro de lançamento fiscal.

falseConfigurando1 Passo

Após criado/importado a Fórmula Visual devemos acessar: **Gestão Fiscal | Obrigações Principais | Lançamento Fiscal Saída (ou Lançamento Fiscal Entrada) | Processos | Fórmula Visual | Gerenciar**

Imagem2 Passo

A seguinte janela de Gerenciamento de Fórmula Visual se abrirá.

Na aba **Gatilhos**, selecionar Após Salvar o Registro

Imagem

Clique no botão verde na parte superior "Adicionar Fórmula Visual", e pesquise o nome da fórmula:

Imagem

Após adicionado a fórmula visual no gatilho, clique em OK.

Imagem

## **Criando o campo complementar**

false

Este  deve ser criado na Situação Tributária. Podendo ser acessado no módulo Fiscal pelo seguinte caminho:

ImagemDetalhes do Campo Complementar

Criar com o nome de coluna: DESCCODAJUSTE

Tipo de Campo: texto ou alfanumérico

Tamanho 20 (Conforme é utilizado no SPED)

Imagem

****Executando a fórmula visual****

false

Ao criar um lançamento fiscal cujo a Natureza for de devolução, o campo complementar Descrição do Código de Ajuste irá ser preenchido: "Devolução: XXXXXXX" onde o X representa o número do documento do lançamento.

Imagem

**Observação:**

As fórmulas Visuais podem ser importadas e exportadas entre as bases (Por exemplo criar em homologação e depois importa-la para o ambiente de Produção).

Para isto, basta seguir procedimento de Importação disponível no link abaixo:

[Importar/Exportar Fórmula Visual](https://tdn.totvs.com/x/34vFAw)

Disponível a partir da biblioteca 12.1.33
