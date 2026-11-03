---
content_hash: 657d0273c50c35e710a820e321087caddafa9e9e7ecdbad6dab06403cc70f305
fetched_at: '2026-06-29T00:05:49.035775+00:00'
page_id: '1035866203'
product: rm
source: tdn-rm
title: 'TOTVS Educacional - Reforma Tributária: Parametrizações para Geração de Movimentos'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1035866203
version: 9
---

Este guia orienta sobre as configurações e processos necessários no **TOTVS Educacional** para atender às novas exigências da **Reforma Tributária.** 

**Vigência:** 01/01/2026 | **Tributos: IBS** e **CBS****(****EC 132/2023)**

As alterações e validações abaixo são exclusivas para documentos emitidos a partir de **01/01/2026**. Verifique se seu ambiente está atualizado antes de prosseguir:

VERSÕES HOMOLOGADAS

* + - **12.1.2502.271** ou superior
    - **12.1.2506.232** ou superior
    - **12.1.2510.160** ou superior

* **Configurações Estruturais**

* + Para garantir a conformidade fiscal e o correto funcionamento da integração **TOTVS Educacional x BackOffice,** realize os cadastros fiscais conforme detalhado na documentação técnica de referência, abaixo:
    - 📄 **[Guia de Cadastros Base - Reforma Tributária](https://tdn.totvs.com/pages/viewpage.action?pageId=925352283)**

* + Ajuste o vinculo do cadastro de **Regra tributária** no módulo Educacional, siga a hierarquia de parametrização:
    - *[Prioridade1]:***Cadastro de Serviço**, acesse: **Financeiro/Contábil > Serviço.**
      * Vincule o cadastro de *Regra tributária* ao serviço para a geração do movimento.

* + - *[Prioridade2]:***Parâmetros de Integração**, acesse: **Ambientes | Parâmetros | Educacional | Integração | Fiscal | Fiscal 2/2.**
      * Vincule, no contexto, o cadastro de *Regra Tributária*vigente para geração do movimento.

 Se não houver o vinculo da regra definida em nenhum dos níveis, o sistema bloqueará a geração do movimento.

* **Cadastro do Alunos**

* + Campos Obrigatórios: **CPF, Logradouro, Número, Bairro, Município, UF**e **CEP**para identificar o **Local da Operação**.

 Se não houver o preenchimento completo do endereço do aluno, o sistema bloqueará a geração do movimento.

***[Regra temporária]*** 

**Alunos Estrangeiros:** 1.O NIF será enviado automaticamente como **"0 - Não informada na nota de origem".**

                                    2. Ocadastro **CPF** não é obrigatório se a nacionalidade do estudante for diferente de "*Brasileira*".

* **Cadastro do Curso: Ensino superior**
  + A modalidade do curso define a incidência tributária na nova lei, selecione uma das opções:

 Quando selecionado, Semipresencial, seleciona a regra de emissão da NF-e:
