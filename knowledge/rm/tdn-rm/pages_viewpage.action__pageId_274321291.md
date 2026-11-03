---
content_hash: 06c85c5061173f81d00bac4eb2f2e3209985e3369a12d5a081f33110fc19840f
fetched_at: '2026-06-29T00:08:33.472004+00:00'
page_id: '274321291'
product: rm
source: tdn-rm
title: 811591 EDUCACIONAL01-716 DT Cadastro de funcionário pelo aluno na solicitação
  de estágio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274321291
version: 106
---

# Solicitação de Estágio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Cadastro de funcionário na solicitação de estágio. |
| **Situação/Requisito:** | O aluno realizando o cadastro da solicitação de estágio pelo portal, poderá realizar o cadastro do funcionário da empresa. Caso o aluno cadastre um representante legal pelo portal não está exigindo o RG, CPF endereço, esses campos devem ser obrigatórios. |
|  |  |
|  |  |
| **Solução/Implementação:** | Melhoria nos procedimentos da gestão de estágio adicionando o novo parâmetro “Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário “Responsável Legal" na solicitação de estágio.”   Adequações:  * **Parâmetros de estagio**  Adicionado um novo parâmetro que determina que os documentos e endereço do funcionário informados na solicitação de estágio sejam obrigatórios.  Parâmetro:Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário “Responsável Legal" na solicitação de estágio.  * **Cadastro de Funcionário da solicitação de estágio (Anexo solicitação de estágio)**  Disponibilizado nos campos  CPF, RG, Estado emissão, órgão expedição, data expedição,  CEP, Rua, Numero, Bairro, Complemento, UF, município , pais.  Regra 1:    Se o parâmetro "Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário “Responsável Legal" estiver marcado, ao cadastrar um funcionário com a função igual "Responsável Legal/Supervisor" ou "Responsável Legal " os campos CPF, RG,  CEP, Rua, Numero, Bairro, Complemento, UF, município , pais serão obrigatórios:    Regra 2:    No cadastro de funcionário da solicitação de estágio se o funcionário (lookup) estiver preenchido os novos campos acima ficarão desabilitados.  * **Solicitação de estágio**  Ao alterar o status da solicitação de estágio para "Aprovado" o sistema cópias as informações do funcionário da solicitação de estágio para o cadastro de funcionário da empresa e para este procedimento o sistema passa a cópiar informações dos novos campos.    * **Portal**   Se o parâmetro "Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário “Responsável Legal" estiver marcado ao silicitar o estágio pelo portal e informar um represetante legal os novos campos serão obrigatórios. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 811591 |
| **Requisito:** |  |

divs
