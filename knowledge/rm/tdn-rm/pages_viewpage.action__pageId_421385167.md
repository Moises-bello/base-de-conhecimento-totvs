---
content_hash: f72899504b5cd85744f79e5efe912eba8bd215a591bebfeaf8b5acfafea445ce
fetched_at: '2026-06-29T00:09:14.245854+00:00'
page_id: '421385167'
product: rm
source: tdn-rm
title: Preencher cronograma da planilha de serviços
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385167
version: 3
---

---

Na planilha de serviços é permitida a edição dos cronogramas Previsto, Realizado e Medido, a edição pode ser realizada manualmente onde os usuários podem inserir valor, quantidade e percentual para o cronograma ou utilizar o processo "Preencher cronograma da planilha de serviços".

O processo "Preencher cronograma da planilha de serviços" realiza as seguintes atividades:

Preenche os cronogramas das tarefas da planilha de serviço, levando em consideração as atividades associadas ao serviço, ou seja, as informações do cronograma das atividades associadas ao serviço serão utilizados para preenchimento do cronograma do serviço. Na tela apresentada quando selecionado o processo é possível definir qual cronograma será o preenchido e solicitar ou não o recalculo do cronograma na realização do processo.

Não é necessário que tenha um serviço selecionado para realização do processo. Nesta situação todos os serviços que possuem atividades associadas serão atualizados, portanto as informações que constavam antes no cronograma destes serviços serão deletados e substituídos pelas novas informações. Se algum serviço for selecionado para execução do processo somente este serviço será afetado, os outros serviços não sofrerão alterações.

**Observações:**

Somente o cronograma previsto é marcado como padrão para execução do processo.

O processo verifica todos os períodos independente do período estar bloqueado ou não, ou seja, mesmo que o período esteja bloqueado o preenchimento do cronograma de serviço é realizado.

Se um serviço sem vínculo com atividades possuir um cronograma, este será ignorado pelo processo e não serão realizadas alterações.

O cálculo da proporção que incide no percentual do cronograma selecionado depende do tipo de grandeza definido nos parâmetros de projeto:

Se a quantidade do Serviço for diferente de zero o cálculo acontece da seguinte forma:

* Parâmetro de "Tipo de vínculo entre Serviço e Atividade" estiver como Percentual:  
    
  Quantidade Vinculada = (Quantidade do Serviço X Percentual Vinculado) / 100;

**Proporção** = Quantidade Vinculada / Quantidade do Serviço

* Parâmetro de "Tipo de vínculo entre Serviço e Atividade" estiver como Quantidade:  
    
  **Proporção** = Quantidade Vinculada / Quantidade do Serviço

---
