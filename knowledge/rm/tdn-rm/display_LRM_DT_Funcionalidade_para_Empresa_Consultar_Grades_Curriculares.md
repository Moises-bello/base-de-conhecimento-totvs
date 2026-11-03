---
content_hash: 711ea64ef357d6ef5e9074577fe725d0ca087480058d52e433b852a90b638150
fetched_at: '2026-06-29T00:08:03.956365+00:00'
page_id: '235330815'
product: rm
source: tdn-rm
title: DT_Funcionalidade_para_Empresa_Consultar_Grades_Curriculares
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Funcionalidade_para_Empresa_Consultar_Grades_Curriculares
version: 126
---

# Funcionalidades para a empresa (Consultar grades curriculares)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Consultar grades curriculares | Consultar grades curriculares |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Requisito (ISSUE):** | PCREQ-10643 |
| **País(es):** | Todos |

## Descrição

Disponibilizar para as empresas as informações a respeito das matrizes curriculares da instituição de ensino.

## Procedimento para Utilização

* Acessar o cadastro de perfil e liberar o acesso para a nova funcionalidade (**Serviços Globais | Segurança | Perfis**), alterar o sistema para "Educacional" e conceder a permissão para a funcionalidade Cursos da instituição (**Educacional - Outras permissões - RM Portal - Empresa - Cursos da instituição**)
* Gerar usuário para um ou mais funcionários da empresa e vincular ao perfil adequado (**Atividades acadêmicas | Empresas | Geração de usuários (Funcionários)**)
* Acessar o menu "**Empresa | Cursos da instituição**" pelo Portal Acadêmico (esta funcionalidade só poderá ser acessada entrando como Empresa)

1. Serão listadas as matrizes curriculares que obedeçam as seguintes regras:  
   * O campo status do cadastro da matriz curricular deve ser diferente de inativo. (**Currículo e Oferta | Matrizes curriculares**)
   * Usuário deve ter permissão de acesso ao Portal para o contexto da matriz curricular. (**Serviços Globais | Segurança | Usuários | Usuário / Filial**)
2. As informações exibidas para o usuário são:
   * Informações do Curso
   * Lista das disciplinas obrigatórias
     + Informações das disciplinas
     + Lista dos complementos da disciplina
   * Lista das disciplinas optativas e eletivas
     + Informações das disciplinas
     + Lista dos complementos da disciplina
3. Algumas disciplinas da matriz curricular podem não ser exibidas no contexto de ensino básico dependendo da definição do parâmetro "**Exibir as disciplinas para o aluno de acordo com o campo ‘Imprime no Boletim' do cadastro de disciplinas da matriz curricular**".
4. A exibição do resultado será pelo agrupamento em dois níveis, sendo o primeiro a coligada e o segundo representado pelo nível de ensino.
5. A exibição da lista com os complementos da disciplina seguirá a seguinte regra:  
   1. Parâmetro "**Manter histórico de complemento de disciplina por período letivo**" estiver desmarcado todos os complementos serão listados.
   2. Parâmetro  "**Manter histórico de complemento de disciplina por período letivo**" marcado é listado os complementos do período letivo corrente que é definido no parâmetro do educacional "**Período letivo"**. Caso este não esteja parametrizado nenhum complemento de disciplina será exibido.

Localização dos parâmetros:

* Exibir as disciplinas para o aluno de acordo com o campo ‘Imprime no Boletim' do cadastro de disciplinas da matriz curricular ****- Configurações | Parâmetros - RM Portal - "RM Portal - Gerais" - "Portal - Geral 5/7"****
* Manter histórico de complemento de disciplina por período letivo **- ****Configurações | Parâmetros - Secretária - Geral 3/5******
* Período letivo********- Configurações | Parâmetros - Secretária - Período letivo********

divs
