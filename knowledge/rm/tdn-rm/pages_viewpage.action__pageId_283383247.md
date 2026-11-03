---
content_hash: 5964eb902af0617db0e7e63913b7fbb08dc8cc9cb1b969df08f919cbaf0d5966
fetched_at: '2026-06-29T00:08:35.938056+00:00'
page_id: '283383247'
product: rm
source: tdn-rm
title: 934547 EDUCACIONAL01-1054 DT Lista de Excedentes Não Atualizada após Desmatricular
  aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=283383247
version: 104
---

# Desmatricular aluno do processo seletivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Desmatricular aluno do processo seletivo |
| **Situação/Requisito:** | Ao desfazer a matricula de um processo seletivo é disponibilizado uma nova vaga no processo seletivo e se existir algum candidato inscrito como excedente o sistema não estava atualizando a lista de inscrito e alterando o candidato excedente para inscrito.  E se o usuário do sistema cadastrasse um novo candidato o mesmo estava entrando como inscrito e não como excedente. |
| **Solução/Implementação:** | Evoluído o processo de cancelamento de matricula do processo seletivo para que a lista de excedentes seja atualizada.  Foi disponibilizado a opção "Atualizar lista de candidatos inscritos excedentes", que se for marcada o sistema ao desfazer a matricula analisa a lista de candidatos inscritos e verifica se tem algum candidato "excedente" que pode ficar como inscrito em função da liberação da vaga.    Observação:  A opção "Atualizar lista de candidatos inscritos excedentes" ficará disponível somente se o processo seletivo estiver parametrizado  para "Utilizar controle de vagas" e o tipo de controle de vagas seja "Permitir novas inscrições, mas os candidatos dicarão como excedentes". |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
