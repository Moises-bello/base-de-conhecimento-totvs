---
content_hash: a727e0a046ab8960b5af5bc54ab171ef1f1a2fae3c3ade339934893debe6c6e4
fetched_at: '2026-06-29T00:08:10.169892+00:00'
page_id: '240302622'
product: rm
source: tdn-rm
title: ER_EDUEDU001-69_Verificar_Inadimplencia_Transferencia_Interna
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUEDU001-69_Verificar_Inadimplencia_Transferencia_Interna
version: 129
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [EDU 2016/2017](http://jiraproducao.totvs.com.br/browse/EDUEDU001) | **IRM1** | EDUEDU001-68 |
| **Requisito1** | EDUEDU001-69 | **Subtarefa1** | EDUEDU001-75 |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   ( ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que a instituição de ensino defina se a validação de inadimplência deverá ser executada durante a transferência interna de alunos.

## Definição da Regra de Negócio

**RN\_01** - Criação de um novo parâmetro no perfil do usuário: "**Permitir transferência de alunos inadimplentes**"

**RN\_02** - Criação de um novo parâmetro no processo de transferência interna e transferência interna entre coligadas: "**Transferir alunos inadimplentes**"

* Este novo campo só ficará disponível para alteração quando o parâmetro do TOTVS Educacional "**Bloquear matrícula de inadimplentes**" e o parâmetro do perfil do usuário **"Permitir transferência de alunos inadimplentes**" estiverem marcados. Neste cenário o usuário poderá decidir se verifica ou não a inadimplência na transferência do aluno.

**RN\_03 -** Transferências internas - regras de validação de matrícula

As transferências internas sem a alteração proposta possuem o seguinte comportamento:

* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver desmarcado a transferência é realizada com sucesso mesmo o aluno estando inadimplente.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Matricular alunos inadimplentes**” marcada, a transferência é realizada com sucesso mesmo o aluno estando inadimplente.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Matricular alunos inadimplentes**” desmarcada, a transferência não é realizada e o sistema exibe ao final do processo a informação de inadimplência do aluno.

Com a implementação do novo parâmetro no perfil do usuário do TOTVS Educacional “**Permitir transferência de alunos inadimplentes**” e o parâmetro "**Transferir alunos inadimplentes**" no processo, o sistema passa a ter o seguinte comportamento:

* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver desmarcado a transferência é realizada com sucesso mesmo o aluno estando inadimplente. Neste cenário o parâmetro "**Transferir alunos inadimplentes****"**  é apresentado desabilitado nos processos de transferência interna.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” marcada, neste cenário é exibido nos processos de transferência interna o parâmetro "**Transferir alunos inadimplentes****":**
  + Se estiver desmarcado a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada.
  + Se estiver marcado a transferência é realizada mesmo o aluno estando inadimplente.
* Parâmetro do TOTVS Educacional “**Bloquear matrícula de inadimplentes**” estiver marcado e o usuário possuir em seu perfil a opção “**Permitir transferência de alunos inadimplentes**” desmarcada, a inadimplência é verificada e se o aluno estiver inadimplente a transferência não é realizada. Neste cenário o parâmetro "**Transferir alunos inadimplentes****"**é apresentado desabilitado nos processos de transferência interna.

**Importante:**

* O comportamento de verificação de inadimplência continuará o mesmo para as matrículas presenciais, via portal e processos seletivos.
* A transferência interna entre coligadas deverá na avaliação de inadimplência verificar o parâmetro de tesouraria “**Verificar débitos do aluno em outras coligadas**”. Exemplo: o aluno possui débitos na coligada origem e na coligada destino foi feita parametrização para não verificar débitos em outras coligadas, desta forma a transferência sempre será realizada, pois na coligada destino não existe débito para o aluno.
* Quando houver uma transferência de um aluno de **A (período letivo 2016/1) para B (período letivo 2016/1)** e em outro momento for realizada a **operação inversa** o parâmetro do TOTVS Educacional a ser avaliado não mais será o “**Bloquear matrícula de inadimplentes**” e sim o "**Bloquear mudança de situação de matrícula para inadimplentes**".  O motivo da utilização do parâmetro "**Bloquear mudança de situação de matrícula para inadimplentes**" é que neste cenário não está sendo realizada uma matrícula e sim uma alteração de situação de matrícula.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Transferência Interna | Alteração | Atividades acadêmicas -> Transferência interna -> Transferência interna | - |
| Transferência interna entre coligadas | Alteração | Atividades acadêmicas -> Transferência interna -> Transferência interna entre coligadas | - |
| Perfil do usuário | Alteração | Módulo: Serviços Globais -> Segurança -> Perfis -> Parâmetros educacionais | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
