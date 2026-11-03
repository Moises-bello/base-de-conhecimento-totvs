---
content_hash: 165e9c8f9de4fef3b61d8ccea9194ab050b71fc01a011a0172b7c867ef47244e
fetched_at: '2026-06-29T00:08:09.211784+00:00'
page_id: '239029413'
product: rm
source: tdn-rm
title: ER_EDUEDU001-37_Ativar_Desativar_Usuario_Fluig_Integracao_EDU_LMS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUEDU001-37_Ativar_Desativar_Usuario_Fluig_Integracao_EDU_LMS
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | EDUEDU001 | **IRM1** | EDUEDU001-6 |
| **Requisito1** | EDUEDU001-37 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O objetivo da nova funcionalidade é possibilitar que o usuário do FLUIG LMS, quando integrado ao RM, seja ativado/desativado de acordo com informações do status de matrícula do aluno, ou de acordo com o campo ativo informado nas filiais do professor.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Alterar Situação de Matrícula | [Alteração] | [Currículo e Oferta | Aluno e Professor | Alunos | Anexo: Matrículas no Período Letivo | Processo: Alterar Situação de Matrícula] | - |
| Cadastro de Professor | [Alteração] | [Currículo e Oferta | Aluno e Professor | Professores | Anexo: Filiais do Professor] | - |

Para o comportamento abaixo, o RM deve estar integrado com o Fluig LMS, **sem IDENTITY**, mais detalhes em 

* Aluno
  + Configurações  
    Caso o status de matrícula esteja configurado para "cancelar usuário" ou "ativar usuário" na aba Status no Período Letivo, e ocorra alguma alteração no status de matrícula do aluno, o sistema executará mensagem única da integração para alterar também a situação do usuário no Fluig LMS.
  + Restrições
    - O sistema deve estar integrado com o Fluig LMS.
    - O envio da mensagem seguirá as regras já existentes para ativar/desativar o usuário do Corpore:
      * Ativar  
        Os usuários do Corpore e do LMS sempre serão ativados caso a situação de matrícula escolhida possua o campo "Ação usuário aluno", da aba "Status no período letivo", configurado para "Ativar usuário".
      * Desativar  
        Caso exista alguma outra matrícula ativa em período letivo e/ou o aluno também seja um professor ativo em uma ou mais filiais, não será permitido desativar os usuários do Corpore e LMS. Matrícula "Ativa" é aquela cuja situação de matrícula "Ativa o usuário", através do campo "Ação usuário aluno", da aba "Status no período letivo".
* Professor
  + Configurações  
    Caso o usuário altere o campo "ativo" do cadastro de "Filiais do Professor", o sistema executará mensagem única da integração para alterar também a situação do usuário no Fluig LMS.
  + Restrições
    - O sistema deve estar integrado com o Fluig LMS.
    - Caso esse usuário esteja vinculado a um professor ativo em mais de uma filial, o mesmo não poderá ter sua situação alterada no Fluig LMS. Para que a alteração aconteça, esse professor deve estar inativo em todas as filiais a ele vinculado e não ser um aluno com matrícula ativa.

Existe a possibilidade do usuário estar vinculado a um aluno e também a um professor. Nessa situação, as duas restrições acima descritas se aplicam.

Caso exista integração com o IDENTITY, toda a regra de ativação/desativação de usuário fica a cargo dessa integração.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
