---
content_hash: baa9a18e6510edd7681f44424e7f959e920b513d87d97d4a7ffd87fc1568dad8
fetched_at: '2026-06-29T00:08:09.932905+00:00'
page_id: '240295765'
product: rm
source: tdn-rm
title: DT_Ativar_Desativar_Usuario_Fluig_Integracao_EDU_LMS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Ativar_Desativar_Usuario_Fluig_Integracao_EDU_LMS
version: 116
---

# Ativar/Desativar usuário FLUIG - Integração EDUxLMS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | **TOTVS Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Alterar Situação de Matrícula.* | *Alterar Situação de Matrícula.* | | Cadastro de Filiais do Professor | Cadastro de Filiais do Professor | |
| **Cadastros Iniciais:** | *Cadastro de Professor; Matrícula em Período Letivo; Situação de Matrícula* |
| **Requisito (ISSUE):** | *EDUEDU001-6* |
| **País(es):** | *Todos* |

## Descrição

O objetivo é possibilitar que o usuário do FLUIG LMS, quando integrado ao RM, seja ativado/desativado de acordo com informações do status de matrícula do aluno, ou de acordo com o campo ativo informado nas filiais do professor.

## Procedimento para Utilização

Para o comportamento abaixo, o RM deve estar integrado com o Fluig LMS, **sem IDENTITY**, mais detalhes em [TOTVS EDUCACIONAL & LMS - FLUIG](http://tdn.totvs.com/pages/viewpage.action?pageId=219698498)

* Aluno
  + Configurações  
    Caso a situação de matrícula esteja configurada para "cancelar usuário" ou "ativar usuário" na aba Status no Período Letivo, e ocorra alguma alteração no status de matrícula do aluno, o sistema executará mensagem única da integração para alterar também a situação do usuário no Fluig LMS.  
    Acesso ao menu: "Currículo e Oferta | Acadêmico | Situação de Matrícula"  
    Acesso ao menu: "Currículo e Oferta | Aluno e Professor | Alunos | Anexo - Matrículas no Período Letivo | Processos - Alterar Situação de Matrícula"
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
    Acesso ao menu: "Currículo e Oferta | Aluno e Professor | Professores | Anexo - Filiais do Professor"
  + Restrições
    - O sistema deve estar integrado com o Fluig LMS.
    - Caso esse usuário esteja vinculado a um professor ativo em mais de uma filial, o mesmo não poderá ter sua situação alterada no Fluig LMS. Para que a alteração aconteça, esse professor deve estar inativo em todas as filiais a ele vinculado  e não ser um aluno com matrícula ativa.

Existe a possibilidade do usuário estar vinculado a um aluno e também a um professor. Nessa situação, as duas restrições acima descritas se aplicam.

Caso exista integração com o IDENTITY, toda a regra de ativação/desativação de usuário fica a cargo dessa integração.

divs
