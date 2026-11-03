---
content_hash: 2eb9ec46a0fe262be90f733e0ac61ff33e10b62d3ff31113daa1edf7acd26d09
fetched_at: '2026-06-29T00:09:47.698220+00:00'
page_id: '435105049'
product: rm
source: tdn-rm
title: Incluindo uma Medição do Tipo TOTVS Obras e Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105049
version: 16
---

O avanço da obra  do tipo TOTVS Obras e Projetos tem o objetivo de preencher automaticamente os avanços da obra  de acordo com o cronograma das tarefas de um projeto. Ao vincular o cadastro da tarefa e executar o processo  automaticamente  os avanços serão  informados, podendo ou não sofrer alteração.

Pré-Condições

1. Ter incluído um projeto
2. Ter configurado os parâmetros do projeto (tecla F6 ou Projetos/Parâmetros/Construção e Projetos/Projetos)

   * **Cronograma/Períodos:** Defina o período do projeto
   * **Cronograma/Lançamentos:** Selecione o radio button Percentual
   * **Integração/Financeiro/Geral:** Informe as naturezas financeiras
   * **Exibição/Máscaras:** Estabeleça uma máscara para cada um dos itens e selecione o auto incremento
3. Ter incluído um empreendimento, suas unidades e tabela de preços
4. Ter incluído a obra, etapa e tarefa em Orçamento/Planilha/Planilha de atividades (F10)

   Obra - Obrigatório preencher apenas:
   * Código
   * Nome
   * DescriçãoEtapa - Obrigatório preencher apenas:
   * Código
   * Nome
   * DescriçãoTarefa - Obrigatório preencher apenas:

   **Código:** Informe um sequencial da obra e da tarefa, de acordo com a máscara estabelecida na pré-condição 2.

   Exemplo:Obra: 01; Etapa: 01.01; Tarefa: 01.01.001
5. Ter incluído o cronograma previsto, acessando Anexos/Cronograma, pedir para calcular e depois salvar
Incluindo o Andamento da Obra

**Passo 1** - Clique em incluir andamento da obra

**Passo 2** - Preencha os campos conforme parametrização abaixo e clique no botão Salvar

**Tipo de Medição:** TOTVS Obras e Projetos

**Empreendimento:** Informe o Código do Empreendimento a executar o andamento da obra. Se  a unidade e subunidade não forem informados, o andamento da obra será aplicado para todas as unidades e subunidades deste empreendimento

**Unidade:** Informe o código da unidade  se deseja  direcionar o andamento da obra para a  todas as subunidades  desta unidade

**Subunidade:** Informe o código da subunidade se deseja direcionar o andamento da obra para  uma subunidade específica

**Tipo de Planilha:** Atividade selecionado

**Projeto:** Informe o projeto cadastrado nas pré-condições

**Obra:**Informe a obra cadastrada nas pré-condições 

**Etapa:** Informe a etapa cadastrada nas pré-condições 

**Tarefa:** Informe a tarefa cadastrada nas pré-condições 

**Passo 3** - Acesse Processos/Calcular Avanço da Obra (POC)

O sistema irá inserir os avanços de acordo com o percentual informado em cada período do cronograma cadastrado para a tarefa do TOTVS Obras e Projetos
