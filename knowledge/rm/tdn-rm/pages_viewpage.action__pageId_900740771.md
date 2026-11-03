---
content_hash: ed6fc47e3081941be339bf49b59789fb049696bc9d988c14e29175ecaba42d9a
fetched_at: '2026-06-29T00:12:02.377959+00:00'
page_id: '900740771'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900740771
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastro RM**
3. **Telas utilizadas no PEP**
4. **Marca d'água em relatórios**

TOTVS Assinatura Eletrônica1. Visão geral

## **01. VISÃO GERAL**

O PEP RM apresenta a integração com a TOTVS Assinatura Eletrônica, trazendo a possibilidade de realização de assinatura digital de documentos através do prontuário eletrônico. As assinaturas possuem certificado digital e é possível consultar e gerenciar os documentos assinados via PEP ou TAE.

2. Cadastro RM

## **02.** **CADASTRO NO RM**

O primeiro passo para realização da configuração dos parâmetros é  realizar o acesso aos parâmetros gerais do RM (RM → Ambiente → Parâmetros → Gestão Hospitalar → Prontuário Eletrônico → Assinatura Digital PEP) . Ao acessar o parâmetro descrito, o usuário deve selecionar a utilização da assinatura digital e a opção TAE

**Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Assinar documentos digitalmente | * Indica se o Prontuário Eletrônico não irá usar ou não assinatura digital. |
| Tipo de Assinatura | * Permite ao usuário, escolher entre as opções de assinatura digital **EVAL** e **TAE.** Essa opção só é válida com a flag **Assinar Documentos Digitais** marcada. |

**ATENÇÃO**: Não é permitido usar os dois tipos de integração com assinatura digital.

Também é necessário configurar as informações referentes aos dados para comunicação com a TAE através dos parâmetros gerais (RM → Ambiente → Parâmetros → Gestão Hospitalar → Assinatura Digital).

**Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| **EVAL** - Url do Web Service para assinatura | * Campo da url do web service de assinatura da **EVAL**. |
| **EVAL** - Id da Eval | * Identificador da **EVAL**. |
| **TAE** - Url do Web Service para assinatura | * Campo da url do web service de assinatura da **TAE** (Totvs Assinatura Eletrônica). |
| **TAE** - Usuário para geração de token | * Campo de e-mail referente ao usuário cadastrado para geração de token da integração com a **TAE** (Totvs Assinatura Eletrônica). |
| **TAE** - Senha de usuário para geração de token | * Campo de senha do usuário de geração de token da integração com a **TAE** (Totvs Assinatura Eletrônica). |

O PEP permite a utilização da assinatura digital de acordo com o perfil e necessidade de cada unidade de atendimento, o cliente pode cadastrar quais unidade de atendimento será utilizado a assinatura digital. Uma vez optado pela utilização da TAE, todas as unidades parametrização para assinatura digital deverá utilizar a TAE. A parametrização é realizada dentro da unidade de atendimento (RM → Unidade de Atendimento → Prontuário Eletrônico → Geral)

Quando alguma parametrização não estiver preenchido, o usuário final receberá um alerta em tela relacionado ao motivo da falha na tentativa de realizar a assinatura pela TAE. A finalização do registro no PEP não está vinculado ao sucesso da assinatura portanto, o usuário final visualiza o seu registro finalizado porém com a pendencia da assinatura.

Em caso de falha na assinatura digital, será possível prosseguir com a finalização do registro. Nesse cenário, será exibida uma mensagem informando que não foi possível realizar a assinatura, uma vez que ela foi ignorada.

3. Telas utilizadas no PEP

## **03. TELAS UTILIZADAS NO PEP**

Após cadastro das parametrizações realizadas o PEP deve apresentar ao usuário a opção de realizar autenticação.

Ao selecionar a opção de abrir autenticador o usuário deve preencher o campo com o seu CPF e selecionar a opção "VIDaaS - VALID". 

Na sequência o QrCode será aberto para leitura e validação

O processo de assinatura não concorre com a finalização do registro pelo profissional.  Caso ocorra falha na assinatura o documento será finalizado e o status de assinado se mantém como pendente com a mensagem "Falha ao realizar assinatura".

Quando assinatura foi finalizada será exibido a mensagem em tela

4. Marca D'água em Relatórios

## **04. MARCA D'ÁGUA EM RELATÓRIOS**

Foi implementada uma nova marca d’água fixa para identificação de assinaturas digitais em todos os relatórios que contenham documentos assinados eletronicamente, conforme requisito da SBIS para Prontuário Eletrônico de Saúde (PES).

A marca d’água é posicionada automaticamente no final da página (formato A4) do relatório e contém o texto:

> **Documento assinado digitalmente de acordo com a ICP-Brasil, MP 2.200-2/2001, Resolução CFM 1821/2007, no sistema *[Nome da Empresa]*, por *[Nome do Profissional]* CPF *[XXX.XXX.XXX-XX]*, às *[data atual]* *[hora atual]*. Estado da assinatura: Válida.**

**Comportamento e restrições:**

* A marca d’água é gerada via código, com posicionamento fixo no final da folha.
* Não é mais possível mover, editar ou reposicionar o texto da assinatura manualmente dentro do relatório, como ocorria em versões anteriores.
* Ao configurar relatórios personalizados, o cliente deve reservar um espaço em branco ao final da página para permitir o carimbo automático da assinatura.
* Essa implementação garante conformidade com a legislação vigente e as exigências da SBIS referentes à autenticidade e integridade de documentos eletrônicos de saúde.
