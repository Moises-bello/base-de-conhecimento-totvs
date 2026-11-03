---
content_hash: fecb8467d8bd9e77488827c38a31544fef4e568695054be79e6702a4bc5e89bb
fetched_at: '2026-06-29T00:10:31.934764+00:00'
page_id: '525013171'
product: rm
source: tdn-rm
title: Receita PEP
type: documentation
url: https://tdn.totvs.com/display/LRM/Receita+PEP
version: 15
---

##### **O receituário do PEP RM possui integração com a MEMED.**

##### **MEMED => Para manual de usuário ou maiores informações, segue link: <https://ajuda.memed.com.br/>**

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração Receituário Digital**
3. **Exemplo de utilização**
4. **Telas utilizadas**
5. **Checagem de dados RM x MEMED**

Receita PEPVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo mostrar as receitas médicas emitidas para o paciente através da Memed

Configuração Receituário Digital 

## **02. CONFIGURAÇÃO RECEITUÁRIO DIGITAL**

No RM acesse o menu ambiente → Parâmetros → Gestão Hospitalar acessa a opção de Prontuário  Eletrônico → Receituário digital - realize a configuração do tipo de receituário digital utilizado por usuário.

Exemplo de utilização

## **03. EXEMPLO DE UTILIZAÇÃO**

1. Ao acessar a tela, serão carregadas as 10 primeiras receitas do paciente, agrupadas por mês/ano e dia;
2. Botão **"Ver mais"** carrega mais 10 registros na *timeline* de receitas;
3. Botão **"+ Novo"** direciona para a tela de criação de uma nova receita para o profissional logado;

Só é possível acessar uma receita como edição caso o item editado esteja no status de "Rascunho" e que tenha sido criado pelo profissional logado.

Telas utilizadas 

## **04. TELAS UTILIZADAS**

Checagem de dados RM x MEMED

## **05. CHECAGEM DE DADOS RM x MEMED**

Ao entrar no menu de receitas, o sistema realizará a checagem dos dados entre RM e Memed. Ao encontrar qualquer distinção de dados, será aberto um modal para que essas informações sejam confirmadas e ou alteradas.  
Caso os dados da Memed estejam corretos, a alteração deve ser feita pelo RM, caso contrário, ao confirmar os dados serão alterados na Memed automaticamente.

Integração MEVO

## **06. INTEGRAÇÃO MEVO**

## Visão geral

A integração com Mevo é um sistema de receituário digital que permite aos profissionais de saúde criar prescrições (medicamentos, exames, atestados, encaminhamentos e relatórios) através de um modal integrado ao sistema PEP. A comunicação acontece via iframe e mensagens, onde a Mevo processa a prescrição e retorna os documentos gerados para serem salvos no banco de dados RM.

## Configuração

### Pré-requisitos

1. **Configuração no RM**
   * Tipo de integração, Memed ou Mevo
2. **Configuração do Usuário**
   * Usuário deve possuir conselho profissional cadastrado
   * Usuário deve ter UF do conselho profissional
   * Usuário deve ter configuração de receituário digital habilitada

## Exemplo de Utilização

### Fluxo Completo: Criar Receita Mevo

#### 1. Usuário Clica no Botão “Criar Receita”

* Botão localizado na timeline de receitas

#### 2. Interação no Modal Mevo

* Profissional preenche prescrição no sistema Mevo
* Mevo valida dados e gera documentos
* Sistema pode gerar múltiplos documentos:
  + RECEITAS (medicamentos)
  + EXAMES (solicitações)
  + ATESTADOS
  + ENCAMINHAMENTOS
  + RELATORIOS
  + LME (Laudo para Medicação Especial)

#### 3. Receita Aparece na listagem do PEP

* Timeline recarrega
* Nova receita aparece no topo
* Badges indicam documentos disponíveis (LME, PDF)
* Ações disponíveis: visualizar, imprimir

## Telas Utilizadas

### 1. Tela Principal Receita

* **Descrição**: Lista histórica de receitas do paciente configurado para MEVO
* **Elementos principais**:
  + Botão “Criar Receita”
  + Lista de receitas em formato timeline
  + Filtros e paginação
  + Indicadores de tipo de receita (Mevo ou Memed)

### 2. Modal Mevo

* **Descrição**: Modal tela cheia que carrega interface Mevo
* **Características**:
  + Sem botão de fechar

### 3. Item da Timeline

* **Descrição**: Exibição individual de cada receita
* **Elementos principais**:
  + Categorias de documentos (Medicamentos, Exames, Atestados, etc.)
  + Botões para visualizar PDFs
  + Badge LME quando disponível
  + Informações do atendimento e profissional

## Tratamento de Erros e Validações

### Erros Comuns e Mensagens

| Cenário | Mensagem | Tratamento |
| --- | --- | --- |
| Usuário sem conselho | “O usuário não possui conselho profissional cadastrado” | Bloqueia criação |
| Usuário sem UF | “O usuário não possui cadastro de UF para o conselho profissional” | Bloqueia criação |
| Credenciais inválidas | “Credenciais da MEVO inválidas ou não configuradas” | Bloqueia criação |
| Integração não habilitada | “Seu usuário não está habilitado para emissão de receita digital” | Bloqueia criação |
| Erro na API Mevo | “Ocorreu um erro ao integrar com a Mevo. Tente novamente mais tarde” | Permite retry |
| Documento não encontrado | “Documento não encontrado” | Informa usuário |
| Erro ao processar PDF | “Erro ao processar o documento. Tente novamente” | Permite retry |
