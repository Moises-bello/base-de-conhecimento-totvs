---
content_hash: 409237701c480d2ad436ad7a78331a9cc8b152180f32bffcf4f8978ec0524e8a
fetched_at: '2026-06-29T00:11:25.464068+00:00'
page_id: '708888910'
product: rm
source: tdn-rm
title: Fórmulas Visuais SCAE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708888910
version: 11
---

# **1 - Síntese**

As fórmulas visuais desenvolvidas para atender as melhorias do SGE serão responsáveis por bloquear o preenchimento de informações no processo de matrícula e dos campos complementares que possam invalidar o envio da produção SCAE de acordo com as regras definidas na MIT021.

# **2** - **Processo para importação das Fórmulas Visuais**

Ao realizar a importação de uma Fórmula Visual que já exista no SGE, ou seja, ao executar uma atualização, é preciso excluir ou desativar as Fórmulas Visuais já existentes, para que elas e suas consultas SQL associadas sejam atualizadas em Gestão / Visões de Dados.

## 2.1 - Download Fórmulas Visuais

## 2.2 - Importação

Para realizar a importação, acione o menu “Gestão | Fórmula visual | Fórmula visual” (Figura 1), selecione o submenu ”Processos | Importação de Fórmula Visual” (Figura 2), onde será apresentado um Wizard nativo do SGE.

*Figura 1 – Menu para o cadastro da Fórmula visual*

*Figura 2 - Processo para Importação de Fórmula Visual*

Na tela apresentada, selecione a opção “Adicionar Objetos” e selecione todas as Fórmulas Visuais da coligada corrente (SESI) a serem importadas (Figura 3) e em seguida, selecione a opção “Abrir”.

*Figura 3 - Seleção dos objetos para Importação de Fórmula Visual*

Após a seleção dos arquivos, certifique-se que todos os objetos da Fórmula Visual estejam selecionados, adicione a “Categoria”, marque a opção “Importar Gatilhos”. Esse processo se repete para cada uma das Fórmulas Visuais importadas.

Após abrir os arquivos, selecione a Fórmula Visual, clique na aba “Parâmetros”, adicione a “Categoria”, e marque a opção “Importar Gatilhos”. Esse processo se repete para cada uma das Formulas Visuais importadas.

Após realizar o procedimento acima em todas as Fórmulas Visuais importadas clique em “Executar” e aguarde o fim da execução do processo.

*Figura 4 - Seleção dos objetos para Importação de Fórmula Visual*

*Figura 5 – Fim da execução do Processo*

*Figura 6 - Visualização das fórmulas importadas*

# **3 - Fórmula Visual**

## 3.1 - Fórmula Visual: SESI - Para Categoria igual a 3 - Dependente da Indústria, é obrigatório preencher o Tipo de Documento, CNPJ ou CEI

Pré-Requisito

Executar o processo de importação (Item 2) na coligada SESI.

**Descrição:**

A fórmula visual será acionada antes de salvar o cadastro de matrícula no período letivo. Se o campo complementar “Categoria” for igual a 3 - Dependente da Indústria, será disparado uma exceção se o campo Tipo de Documento for vazio e os campos CNPJ da Empresa ou CEI da Empresa forem vazios. Se o Tipo de Documento estiver preenchido com CEI ou CNPJ a fórmula também dispara uma exceção caso um desses documentos não esteja informado nos seus respectivos campos.

Figura 7 – Cadastro de campos complementares da matrícula no período letivo

**Fluxo:**

1. Verifica se a categoria é igual a 3 - Dependente da Indústria.

1.1 **Sim**: Verifica se o campo Tipo de Documento é vazio.

1.1.1 **Sim**: É lançada uma exceção informando que o Tipo de Documento e CNPJ ou CEI da empresa deve ser preenchido.

1.2 **Não**: O fluxo avança para a próxima atividade.

1.2.1 Verifica se o tipo de documento é CEI

1.2.1.1 **Sim:** Verifica se o CEI da Empresa está preenchido

1.2.1.2 **Não:** É lançada uma exceção informando que o CEI da empresa deve ser preenchido.

1.2.2 Verifica se o tipo de documento é CNPJ

1.2.2.1 **Sim:** Verifica se o CNPJ da Empresa está preenchido

1.2.2.2 **Não:** É lançada uma exceção informando que o CNPJ da empresa deve ser preenchido.

1.2.3 Se Tipo de documento CEI ou CNPJ da empresa estiver preenchido o processo finaliza sem exibir exceção.

**Consulta SQL:**

Essa fórmula não utiliza consulta no fluxo.

## 3.2 - Fórmula Visual: SESI - Para Gratuidade igual a 1 -Sim, impedir o salvamento se código do financiamento igual a 1 - pago

Pré-Requisito

Executar o processo de importação (Item 2) na coligada SESI.

**Descrição:**

A fórmula visual será acionada antes de salvar o cadastro de matrícula no período letivo. Se o campo complementar Gratuidade da matrícula no período letivo for igual a 1 - Sim e o Código do financiamento igual a 1 - Pago será disparado uma exceção.

Figura 8 – Cadastro de campos complementares da matrícula no período letivo

**Fluxo:**

1. Verifica se a Gratuidade é igual a 1 - Sim e Código do Financiamento é igual a 1 - Pago.

1.1 **Sim**: É lançada uma exceção informando que o Código de Financiamento não pode ser 1 - Pago.

1.2 **Não**: O processo finaliza sem exibir exceção.

**Consulta SQL:**

Essa fórmula não utiliza consulta no fluxo.

## 3.3 - Fórmula Visual: SESI - Impedir matricular nas modalidades Nova EJA e EJA Profissionalizante, caso a situação de matrícula seja diferente de Reconhecimento de Saberes (Alunos)

Pré-Requisito

Executar o processo de importação (Item 2) na coligada SESI.

**Descrição:**

A fórmula visual será acionada antes de concluir o processo de matricular aluno através do Menu: **Currículo e Oferta | Alunos | Processos | Matricular Aluno**. Se a matrícula do aluno for realizada em um curso com as modalidades Nova EJA ou EJA Profissionalizante e a situação de matrícula for diferente de Reconhecimento de Saberes será disparado uma exceção.

Figura 9 – Processo Matricular Aluno

**Fluxo:**

1. Verifica se o curso é das modalidades Nova EJA ou EJA Profissionalizante e a situação de matrícula é diferente de Reconhecimento de Saberes.

1.1 **Sim**: É lançada uma exceção informando que para as Nova EJA e EJA Profissionalizante a situação de matrícula deve ser Reconhecimento de Saberes.

1.2 **Não**: O processo finaliza sem exibir exceção.

**Consulta SQL:**

TOTVS.MLSESI.001 - Retorna Modalidade do Curso - Melhoria SESI

## 3.4 - Fórmula Visual: SESI - Impedir matricular nas modalidades Nova EJA e EJA Profissionalizante, caso a situação de matrícula seja diferente de Reconhecimento de Saberes (Processo Seletivo)

Pré-Requisito

Executar o processo de importação (Item 2) na coligada SESI.

**Descrição:**

A fórmula visual será acionada antes de o assistente de matrícula de candidatos aprovados em processo seletivo através do Menu: **Matrícula e Avaliação | Processo Seletivo (RM) | Matricular**. Se a matrícula do aluno for realizada em um curso com as modalidades Nova EJA ou EJA Profissionalizante e a situação de matrícula for diferente de Reconhecimento de Saberes será disparado uma exceção.

Figura 10 – Assistente de matrícula de candidatos aprovados em processo seletivo

**Fluxo:**

1. Verifica se o curso é das modalidades Nova EJA ou EJA Profissionalizante e a situação de matrícula é diferente de Reconhecimento de Saberes.

1.1 **Sim**: É lançada uma exceção informando que para as Nova EJA e EJA Profissionalizante a situação de matrícula deve ser Reconhecimento de Saberes.

1.2 **Não**: O processo finaliza sem exibir exceção.

**Consulta SQL:**

TOTVS.MLSESI.002 - Retorna Modalidade do Curso - Melhoria SESI
