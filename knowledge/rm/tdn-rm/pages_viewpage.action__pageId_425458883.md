---
content_hash: dbe384d335e07b6041399790b6ea2671b848b39032cef278540f41aef5120437
fetched_at: '2026-06-29T00:09:32.600993+00:00'
page_id: '425458883'
product: rm
source: tdn-rm
title: Matrícula no Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458883
version: 35
---

## Tela de cadastro

Este serviço deve informar se um determinado aluno está matriculado em algum período letivo e cursando normalmente uma habilitação/filial. É possível visualizar se este aluno está aprovado ou não em no curso atual por período letivo na aba Resultado.

Para que os ícones de impressão seja exibidos na tela conforme abaixo, é necessário parametrizar os relatórios 1 e/ou 2 em Configurações | Parâmetros | Secretaria | Relatórios | Grupo: Secretaria.

**Importante**

* O campo data de matrícula poderá ser editado. Para isto, é necessário habilitar o parâmetro "Permitir alterar data de matrícula no período letivo" em parâmetros educacionais que está em Serviços Globais, perfil do usuário.

* Se existir notas/faltas de etapas e/ou frequência diária lançada para alguma da(s) disciplina(s) não será permitido a exclusão do registro.

É possível definir no  no perfil do usuário a opção "Permitir excluir matrícula no período letivo com movimentação em notas e frequência"

## Enade

Neste cadastro também é possível visualizar se este aluno foi selecionado pelo ENADE, se é do tipo Ingressante ou Concluinte, se compareceu ou não para a prova.

Para atender o novo layout 1.05 do Mec referente ao diploma/Histórico digital, foi incluído um novo campo Ano Referência.

Além da alteração no campo Situação do Enade - Diploma Digital para **Motivos de não habilitação no ENADE - Diploma digital,** passando este a ser habilitado somente se o aluno foi dispensado da realização da prova. As opções do campo foram modificadas de acordo com a imagem abaixo:

Alterações disponíveis a partir das versões: 12.1.2205.278, 12.1.2209.235, 12.1.2302.158, 12.1.2306.103.

**Novidades!!!** Foi incluído o campo Não Habilitado, na situação para a prova do MEC.  A opção de justificativa , "Motivos de não habilitação no Enade - Diploma digital", passa a ser visualizada, se o campo Não habilitado, estiver preenchido. 

Aluno habilitado:

* Ingressante ou Concluinte que compareceu.
* Ingressante ou Concluinte dispensado.

Aluno irregular:

* Ingressante ou Concluinte selecionado que não compareceu.

Aluno não habilitado:

* Ingressante ou Concluinte Não habilitado.

Alterações realizadas para atender o novo layout 1.05 do MEC referente ao diploma/Histórico digital. Versões disponíveis: 12.1.2209.265,12.1.2302.198 e 12.1.2306.139

## Competência contábil: inicial e final

* Se o sistema estiver parametrizado para "Utilizar contabilização por competência"
* Data contábil estiver parametrizada para "Data contábil do contrato e plano de pagamento" (Parâmetros > Integrações > Contabilidade -> Data contábil)
* Usuário tiver permissão de perfil Educacional > Financeiro / Contábil >Contratos > Contratos > Permite alteração de data contábil do contrato marcada e a aba de lançamentos estiver habilitada,

O sistema exibirá os campos de competência inicial e competência final que conterão os valores a serem preenchidos nos contratos que serão gerados, se um dos campos for preenchido o outro será obrigatório e a data inicial não poderá ser menor que a data final.

Preenchendo ambos os campos, o sistema considerará o período de competência informado no processo para todos os contratos a serem gerados.

Caso não seja informado nenhum valor para os campos de competência, o sistema buscará os valores preenchidos no plano de pagamento utilizado como modelo para a criação das parcelas do contrato.

Para que a aba de lançamentos esteja habilitada é necessário que a situação de matrícula no período letivo esteja parametrizada para "Exige contrato financeiro"

Anexo - Monitor de documentos para assinatura eletrônica

Para acessar o anexo "Monitor de documentos para assinatura eletrônica", o perfil do usuário deverá ter a seguinte permissão:

* **Educacional | Matrícula e Avaliação | Matrícula | Matrículas | Monitor de documentos enviados para assinatura**

Informações Complementares

---

Como Fazer

---

Recursos Adicionais

---

[Boletim técnico - Permitir alterar data de matrícula no período letivo](http://tdn.totvs.com/pages/viewpage.action?pageId=189312813)
