---
content_hash: 8cb392f423564ef0c1456f6f0d0f8cb4d5cb73ebe6832599e866f741d947cd14
fetched_at: '2026-06-29T00:09:33.878726+00:00'
page_id: '425459072'
product: rm
source: tdn-rm
title: Criar estrutura de oferta a partir das turmas/disciplinas importadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459072
version: 3
---

---

O processo de "Criar estrutura de oferta a partir das turmas/disciplinas sugeridas" busca as informações das turmas/disciplinas sugeridas e com base nesta cria/atualiza:

* Cadastro horário da turma/disciplina
* Cadastro professores da turma/disciplina
* Cadastro dos horários dos professores da turma/disciplina
* Geração do plano de aula

Quando uma turma/disciplina é atualizada todos os seus anexos (horários, professores, horários dos professores e planos de aula) são excluídos e depois são recriados com base nas informações da turma/disciplina sugerida.  
 Na primeira etapa do processo é selecionado as turmas/disciplinas que vieram do Urânia que serão importadas a oferta para o TOTVS Educacional. No filtro de turmas/disciplinas irá retornar apenas turmas/disciplinas que não possuem log pendente.  
    
 Na segunda etapa do processo o usuário poderá optar por gerar plano de aula ou não. Caso opte em gerar plano de aula é preciso informar os parâmetros da geração do plano de aula para avançar para o próximo passo.  
    
 Na terceira etapa o usuário poderá definir as permissões e os valores para a associação do professor.  
  Os parâmetros estarão habilitados caso o usuário tenha permissão no perfil de usuários ou esteja habilitado nos parâmetros do sistema, na integração Urânia.  
    
 Parâmetros  
 Sobre gravar a estrutura da turma/disciplina mesmo que contenha alunos matriculados   
 Atualizar turma/disciplina com dados de pagamento de professores aprovado  
 Atualizar turma/disciplina que contenha plano de aula gerado com conteúdo previsto preenchido  
 Permitir super alocação de alunos, de salas e de professores  
    
 Nesta etapa é informado também os valores para a inclusão dos professores das turmas/disciplinas.  
    
 **Importante**

Caso as turmas/disciplinas selecionadas não possuam alunos matriculados o processo será executado e irá:

* Atualizar as informações de horários dos professores, professores e horários da turma/disciplina que já estejam cadastrados e estejam sendo reimportados pelo Urânia.
* Adicionar as informações de horários dos professores, professores e horários da turma/disciplina que não existam na oferta e que estejam sendo enviados pelo Urânia.
* Excluir as informações de horários dos professores, professores e horários da turma/disciplina que já estejam cadastrados e não mais estejam sendo enviados pelo Urânia.

Quando existir alunos matriculados nas turmas/disciplinas selecionadas e o usuário não possuir a permissão ou não irá sobregravar as informações da turma/disciplina, será exibido um novo passo no processo para que sejam informadas as datas de início e término que serão utilizadas para criação de horários modulares e definição dos períodos de início e fim de participação dos professores nas turmas/disciplinas.
