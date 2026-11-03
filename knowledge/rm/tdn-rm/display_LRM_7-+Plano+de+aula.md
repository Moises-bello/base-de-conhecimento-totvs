---
content_hash: 2164a79e7018d1f4b7fb4d06afbbda8e0675b5bcf9f0d4f789051425c0d2362d
fetched_at: '2026-06-29T00:10:52.175632+00:00'
page_id: '570372128'
product: rm
source: tdn-rm
title: 7- Plano de aula
type: documentation
url: https://tdn.totvs.com/display/LRM/7-+Plano+de+aula
version: 60
---

Nesta tela, o professor **visualiza e gerencia** o Plano de Aula vinculado a uma turma/disciplina específica.

Permissão de acesso

Para acessar essa funcionalidade, o perfil do professor deve possuir a seguinte permissão: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de Classe | Plano de Aula**.

Filtros

Esta seção descreve os filtros disponíveis e a lógica de preenchimento automático aplicada ao acessar a tela pela primeira vez.

### 1. Regras de Preenchimento Automático (Primeiro Acesso)

O sistema aplica uma lógica de pré-seleção para agilizar o fluxo de trabalho do docente:

* **Data:** \* Prioriza a data da aula já cadastrada e exibida no campo "Data da Aula" do Diário de Classe.

  + Caso não haja aula registrada, o campo é preenchido com a **data atual**.
* **Etapa:**

  + O sistema seleciona a etapa automaticamente se houver apenas uma cujo período de digitação englobe a data definida no filtro acima.
  + Havendo duplicidade de etapas para o mesmo período, o campo permanecerá vazio para seleção manual.

### 2. Filtros Disponíveis

Os filtros podem ser combinados para refinar a busca:

| **Filtro** | **Descrição** |
| --- | --- |
| **Etapa** | Ciclo ou período acadêmico correspondente. |
| **Subturma** | Segmentação específica da turma (se aplicável). |
| **Data** | Data específica da aula para a qual o plano será consultado/editado. |

falseFiltro Subturma

A seleção de uma **Subturma** refina a exibição para apenas os Planos de Aula de seus respectivos horários. **Caso o campo permaneça vazio, o sistema listará todos os planos disponíveis para a disciplina**.

Subturmas vinculadas à turma/disciplina.

**Horários** da Subturma 1

Após selecionar a Subturma 1, serão exibidos apenas os Planos de Aula correspondentes aos horários previamente cadastrados para essa Subturma.

**Horários** da Subturma 2

Após selecionado a **Subturma 2** ,foi retornado apenas os Planos de Aula que representam os horários previamente cadastrados na **Subturma 2**:

Lista de planos de aulas disponíveis

O sistema listará os Planos de Aula vinculados à combinação de turma e disciplina, observando os seguintes critérios de exibição:

falsePeríodo do professor na turma/disciplina

A listagem é filtrada pela vigência do vínculo do professor. Caso existam as datas de **Início** e **Término**, apenas os Planos de Aula compreendidos nesse intervalo serão exibidos. Na ausência dessas datas, o critério de período de atuação é desconsiderado.

Parâmetro "Permitir ao professor alterar Plano de aula/Frequência fora do período de datas do professor na turma/disciplina"

Caso o parâmetro **"Permitir ao professor alterar Plano de Aula/Frequência fora do período de datas do professor na turma/disciplina"** esteja **marcado**, a regra acima será desconsiderada. O parâmetro está disponível em: **Configurações | Parâmetros | RM Portal | Portal Geral 1/18**.

falsePeríodo informado da etapa

O sistema valida a **Etapa** apenas se o intervalo entre a 'Data de Início' e a 'Data de Término' contemplar a data atual. Na ausência dessas informações ou se o período for inválido, a regra de preenchimento automático não será executada.

Editar plano de aula

Para realizar o cadastro ou a edição de um Plano de Aula, localize o item desejado e **expanda-o**. Após inserir ou atualizar as informações, clique em **Salvar** para confirmar as alterações.

Tipo de aula

A opção **'Extensão'**, dentro do campo Tipo de Aula, é habilitada exclusivamente para o contexto do **Ensino Superior**. Em outros níveis de ensino, esta modalidade não será exibida ou estará indisponível.

Listar todos os horários

O filtro de horários opera, por padrão, de forma restrita ao **turno e dia** selecionados. Para expandir essa visualização, utilize a opção **'Listar todos os horários'**, que exibirá todos os horários cadastrados para o dia, independentemente do turno.

Campos da lista de horários

As informações exibidas no combo de horários são as seguintes: **Código do Horário – Turno – Dia – Horário Inicial – Horário Final**.

Professor substituto

A seleção de um docente substituto é condicionada à ativação do campo **'Professor Substituto'**. Somente após marcar esta opção, o sistema carregará a listagem de professores disponíveis para substituição.

Copiar o conteúdo previsto para o conteúdo realizado

Para agilizar o preenchimento, o sistema permite replicar o **Conteúdo Previsto** no campo **Conteúdo Realizado**. Para isso, utilize o botão de transferência localizado entre os dois campos de texto.  

Professor associado ao horário

O sistema exibe todas as aulas do dia corrente cadastradas para a disciplina, independentemente de o professor estar associado ao horário, desde que o parâmetro **“Configurações | Parâmetros | RM Portal | Portal Geral 1/15 | Permitir ao professor visualizar/alterar Plano de Aula, frequência e quadro de horário sem que o professor esteja cadastrado no horário da turma”** esteja marcado.

Caso o parâmetro esteja desmarcado, serão exibidas apenas as aulas do dia corrente nas quais o professor esteja associado ao respectivo horário.

Para o preenchimento das informações em **“Prevista”**, o sistema seguirá as regras abaixo para habilitar ou bloquear os campos:

**1.**  O campo **“Previsto”** será bloqueado caso o parâmetro **“Configurações | Parâmetros | RM Portal | Portal Geral 1/15 | Permitir alterar conteúdo previsto”** esteja desmarcado.

Alteração dos campos "Previsto"

**2.**  Todos os campos serão bloqueados caso a data atual seja posterior à **“Dt. limite de conteúdo previsto”** cadastrada na etapa.

**3.** O campo **“Tipo de Aula”** será bloqueado caso o perfil do professor não possua a permissão **“Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de Classe | Plano de Aula – Permite ao professor a alteração do Tipo da Aula”**.  
Alteração dos campos "Realizado"

Para o preenchimento das informações em **“Realizado”**, o sistema seguirá as regras abaixo para habilitar ou bloquear os campos:

**1.** A cópia para o campo **“Realizado”** será bloqueada caso a data atual seja posterior à **“Data do Plano de Aula”** e o parâmetro **“Configurações | Parâmetros | RM Portal | Portal Geral 1/15 | Permitir lançamento de conteúdo efetivo (realizado) de dias posteriores ao atual”** esteja desmarcado.

****2.**** Todos os campos serão bloqueados caso a data atual seja posterior à **“Dt. limite de conteúdo efetivo”** cadastrada na etapa.

Desassociar material da turma/disciplina

Para remover o compartilhamento, o professor terá duas opções:

**1.** **Desassociar** um Plano de Aula de um material.

**2º**-Desassociar um Plano de Aula de um ou mais materiais.

Para acessar outras opções:
