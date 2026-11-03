---
content_hash: d54321e1e4f435261c98dff846d7b86153ba9a8fc22538a5631a5a8c2f3d412d
fetched_at: '2026-06-29T00:09:32.436074+00:00'
page_id: '425458848'
product: rm
source: tdn-rm
title: Cadastro de Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458848
version: 14
---

O cadastro do período letivo é usado para identificar os ciclos 'períodos' definidos pelas instituições. Geralmente, as Instituições trabalham com cursos semestrais ou anuais.

A tela de cadastro permite definir a descrição do período letivo; o numero de dias letivos; a carga horária; as datas de inicio, previsão de termino e termino; o calendário que será aplicado; período letivo anterior e as datas de competência e movimento.   
   
**Entenda como os dados inseridos no cadastro do período letivo refletem nas demais rotinas do sistema:**

* Os valores inseridos nos campos "Data inicial" e "Data para previsão do término" podem ser utilizados na [geração do plano de aula](http://tdn.totvs.com/x/IfxbGQ) para as turmas/disciplinas vinculadas ao período.
* O campo "Período Letivo anterior" é usado em toda , caso essa informação não esteja preenchida o processo de rematrícula não será processado.
* As datas de Contabilização e Movimento influenciam diretamente nos processos de [geração de nota fiscal eletrônica](http://tdn.totvs.com/x/SP9bGQ) e [contabilidade](http://tdn.totvs.com/x/PPxbGQ).
* Os campos Descrição, Nº de Dias Letivos e Carga Horária são meramente informativos. Ajudam o usuário a identificar cada período cadastrado, más, não impactam em nenhum processo do sistema.
* O calendário permite definir os feriados 'dias não letivos' ao longo do período que esta sendo cadastrado.
* Ao marcar o Parâmetro: , irá determinar que o Período Letivo selecionado está encerrado.
* Período Letivo encerrado para Geração de Lançamentos: Este parâmetro tem como objetivo, permitir a Geração de  de contratos onde os Períodos Letivos estão encerrados.

=> Parâmetro Habilitado: Quando o parâmetro tiver habilitado, o sistema **não** permitirá gerar os lançamentos financeiros vinculados ao período letivo que esteja com o status encerrado.  
=> Parâmetro desabilitado: Quando o parâmetro tiver habilitado, o sistema permitirá gerar os lançamentos financeiros vinculados ao Período Letivo que esteja com o status encerrado.  
Foi criado também, o Parâmetro: *Permitir Gerar lançamentos para Períodos Letivos Encerrados para geração financeira*, no cadastro de parâmetros Educacionais no Perfil de Usuário. Este perfil tem como objetivo, permitir aos usuários gerar lançamentos financeiros para Períodos Letivos Encerrados.  
Caminho: Totvs Serviços Globais | Segurança | Perfis | Anexo | Parâmetros Educacionais | "Geral" | Permitir Gerar lançamentos para Períodos Letivos Encerrados para geração financeira.

**A partir** da versão release **12.1.2205** o campo **data de início** passa a ser **obrigatório** e além disso, será necessário preencher **obrigatoriamente** o campo de **previsão de término** e/ou **data de término**. Estas regras passam a valer para qualquer atualização feita no cadastro de um período letivo existe ou inclusão de um novo período letivo.

**A partir** da versão release **12.1.2406** o parâmetro **Exibir no portal** foi dividido em dois parâmetros: **Exibir no portal do aluno** e **Exibir no portal do professor**. Flexibilizamos a parametrização de exibição do período letivo para o Portal. Teremos um parâmetro para tratar a exibição do período letivo para cada portal, um para o Portal do Aluno e outro para o Portal do Professor.

**A partir** da versão release **12.1.2502** foi adicionada a aba **Disponibilidade do Professor** com os o parâmetros **Data de Inicial** e **Data Final** responsáveis por delimitar o . A disponibilidade dos períodos letivos cadastrados no portal estará atrelada as datas Inicial e Final e somente será possível realizar inclusões de novas disponibilidades se a data corrente estiver dentro do intervalo início/fim ou se as datas forem nulas, o cadastro de disponibilidades no executável do RM não considera essa regra **(é exclusiva para o Portal do Professor)**

Informações Complementares

---

[Bolsa por Período Letivo](http://tdn.totvs.com/x/aPxbGQ)

[Modelo de Etapa por Período Letivo](http://tdn.totvs.com/x/2-tbGQ)

[Documento Técnico - Período letivo Encerrado para Geração de Lançamentos](http://tdn.totvs.com/display/LRM/DT_Periodo_letivo_encerrado_geracao_lancamento)

 

Como Fazer

---

[Atualizar Etapas de Turma/Disciplinas](http://tdn.totvs.com/x/2fxbGQ)
