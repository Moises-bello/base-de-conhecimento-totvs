---
content_hash: 68cef9c72b0ad8c3fc0ebed79d201f6bcde7b02140a0102e7d4adc356dbff5da
fetched_at: '2026-06-29T00:10:52.439415+00:00'
page_id: '572511039'
product: rm
source: tdn-rm
title: 5- Central de avisos do professor
type: documentation
url: https://tdn.totvs.com/display/LRM/5-+Central+de+avisos+do+professor
version: 34
---

A **Central de Avisos** do professor tem como objetivo alertá-lo sobre os prazos das suas atividades diárias.

Permissão de acesso

Para que essa funcionalidade esteja disponível ao professor, é necessário conceder a permissão em: **Serviços Globais | Seg****urança | Perfis | Educacional | Portal | Educacional (Portal) | Professor | Central de Avisos**

Parametrização dos eventos

Para visualizar os eventos, é necessário selecionar os **tipos de alerta** que deseja exibir. Cada tipo de alerta possui um **parâmetro** que define com quantos dias de antecedência ele será exibido no portal.

Atenção

Para otimizar a performance, as informações da **Central de Avisos** são armazenadas em **cache** por 60 minutos. Portanto, caso algum dado seja alterado — como a **data de uma avaliação**, as **datas de início e fim da etapa**, as **datas de início e fim do limite de digitação da etapa** ou os **parâmetros de alerta** —, será necessário que o professor faça **logout e login** novamente no portal, ou **atualize a página** após a expiração do cache, para que as informações sejam atualizadas.

Lista de turma/disciplina disponíveis

Para que as turmas e disciplinas sejam exibidas no portal, elas devem atender aos seguintes critérios:

* A **data limite de digitação** deve ser maior ou igual à data atual;
* A **turma/disciplina** deve estar ativa;
* O **período letivo** não pode estar encerrado;
* O **período letivo** deve ter o parâmetro **“Exibir no portal do professor”** habilitado;
* No **cadastro da etapa**, o parâmetro **“Exibe no portal e na central do aluno”** deve estar habilitado;
* A turma/disciplina **não pode ser uma Turma GERENCIADA**;
* A **frequência diária** não pode estar liberada aos alunos (**FREQUENCIADISPWEB**).
Lista de eventos disponíveis

A lista de eventos disponíveis é a seguinte:

* **Digitação de notas**
* **Digitação de faltas**
* **Digitação de conteúdo previsto**
* **Digitação de conteúdo realizado**
* **Digitação de notas de avaliação**
* **Digitação de frequência diária**

Ao acessar os eventos no diário, o professor poderá ser redirecionado automaticamente para a **funcionalidade correspondente**, bastando clicar no **link** disponível em cada evento.

Ao clicar no link, os **filtros e parâmetros não serão transferidos** para o menu correspondente. Nesse caso, o professor precisará **ajustar os filtros manualmente** para selecionar o período desejado e realizar a ação necessária no diário de classe.

Período de digitação de notas de avaliação

A exibição do aviso referente ao evento **“Período de digitação de notas de avaliação”** considera dois campos de data:

* **Data limite de digitação** (Cadastro da etapa de notas)
* **Data de devolução** (Cadastro da avaliação)

O evento será exibido apenas se estiver dentro do **prazo de digitação**, ou seja, aparecerá com o status **VENCERÁ EM BREVE**, considerando a data que ocorrer primeiro.

* Se a **data limite de digitação da etapa** tiver expirado, o aviso **não será apresentado**, pois não é possível inserir notas após o prazo da etapa.
* Se, no cadastro da etapa, o campo **data limite** estiver em branco, o aviso será exibido apenas se a **data de devolução** estiver dentro do período; caso essa data tenha expirado, o aviso **não será exibido**.

**Exemplo:**

> * **Data atual:** 26/02
> * **Data limite de digitação da Etapa 1:** 26/02
> * **Data de devolução da Avaliação 1:** 27/02
> * **Data de devolução da Avaliação 2:** 24/02
>
> **Resultado esperado ao acessar a Central de Avisos:**
>
> * **Avaliação 1:** Será exibida, considerando a **data de devolução da etapa**, pois essa data ainda não expirou.
> * **Avaliação 2:** Não será exibida, pois o prazo informado na avaliação já expirou.
