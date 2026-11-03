---
content_hash: 8aac9c82b13177d47053e74f5307c2d473603c264f90a928760f0f8c059a7c44
fetched_at: '2026-06-29T00:11:28.452893+00:00'
page_id: '731215184'
product: rm
source: tdn-rm
title: 05 - Visualizar planejamento
type: documentation
url: https://tdn.totvs.com/display/LRM/05+-+Visualizar+planejamento
version: 29
---

## Visão geral

Esta etapa é responsável por apresentar o progresso do planejamento de oferta que está sendo desenvolvido, permitindo o acompanhamento do planejamento.

Os filtros **curso**, **habilitação**, **matriz**e **turno** são de preenchimento obrigatório nesta etapa, onde o botão de **Selecionar** somente será habilitado, após a seleção destes filtros.  
O filtro **Período** não é obrigatório, podendo ser selecionado como **Todos** ou sendo selecionado algum período específico. Caso este filtro seja selecionado com a opção **Todos**, será exibido um quadro de horário para cada período que possuam turmas/disciplinas planejadas geradas.  
  
**OBS**. Ao selecionar uma matriz aplicada que já tem oferta gerada, o quadro de horário não será exibido e emitirá validação.

## Permissionamento

Para ter acesso a etapa de visualizar planejamento no processo de planejamento de oferta, o usuário autenticado deve possuir a seguinte permissão de usuário no seu Perfil:

**Acessar RM.exe I Menu | Serviços Globais | Perfil | Educacional | Acesso ao Menus | Educacional | Educacional (Portal) | Gestão Educacional | Gestão de ofertas | Visualizar planejamento**

## Exibição dos alertas

Após clicar em **Selecionar**, abaixo da área de filtro será(ão) exibido(s) o(s) quadro(s) de horários (de acordo com o filtro realizado na tela) que possua(m) turmas/disciplinas planejadas geradas:

Será exibido também o botão **Selecionar alertas dos quadros** para que o usuário habilite/desabilite os tipos de alertas que ele deseja que sejam exibido no(s) quadro(s) de horários. Por padrão, no primeiro carregamento da página, todos os alertas estarão habilitados. Para desmarcar um tipo de alerta basta clicar no respectivo botão do alerta e clicar no botão **Aplicar filtro** para que a nova configuração de alertas seja aplicada nos quadros:

As áreas coloridas em tons de laranja claro e escuro no quadro indicam a presença de algum alerta a ser verificado. Ao clicar no ícone de exclamação de alguma área dentro do quadro, os detalhes do alerta existente naquela região serão exibidos conforme abaixo:

No final da descrição detalhada de cada alerta haverá um link para a respectiva etapa onde o usuário poderá atuar para resolver o problema apontado pelo alerta.

Na parte superior do quadro será exibido juntamente com a descrição do período, um ícone para indicar se aquele período possui alertas de validação ou não, de acordo com os tipos de alertas selecionados para serem validados. No caso em que o período possuir alertas, será apresentado o ícone . Caso o período não possua alertas de validações, será exibido o ícone .

Na parte inferior do quadro serão exibidos os nomes das disciplinas das turmas/disciplinas não alocadas no quadro.

A partir da versão **12.1.2510**, foi implementado um novo recurso na etapa de visualização do planejamento, denominado “**Corpo Docente**”, que possibilita a exibição dos professores vinculados à oferta selecionada e de todas as suas turmas/disciplinas em que estão alocados.

Será possível consultar os dados cadastrais do docente, incluindo nome, matrícula, e-mail institucional e a da foto, quando disponível. No quadro de alocação, serão exibidas as informações das disciplinas com a distribuição da carga horária e os totalizadores.

Para que a busca seja realizada, é obrigatório o preenchimento do campo “Nome do Professor”, que serve como parâmetro para localizar o docente desejado.

Importante destacar que o sistema permite a visualização de apenas um professor por vez, não sendo possível consultar múltiplos docentes simultaneamente.

Ao realizar a busca o Professor é exibido da seguinte forma:

**Observação:** Para as colunas de Carga Horária e Quantidade de Aulas, exceto CH total da disciplina, os valores apresentados são aproximados, considerando o padrão de 20 semanas letivas para um semestre.

Portanto, se:

* a disciplina tem 80 horas no semestre;
* e são 4 aulas por semana;
* um semestre letivo no Brasil geralmente tem cerca de 20 semanas.

Então:

Carga horária semanal = 80 horas / 20 semanas = 4 horas (por semana).
