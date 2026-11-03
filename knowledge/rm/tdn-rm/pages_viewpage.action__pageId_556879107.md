---
content_hash: 804c0942be800789902cc7128b6ee23678047c0f6dc52fa25cdec92d6b33fc54
fetched_at: '2026-06-29T00:10:47.027936+00:00'
page_id: '556879107'
product: rm
source: tdn-rm
title: Afastamento 2/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556879107
version: 6
---

Evento para atestado médico (mensalista)  
Neste campo deve informar um evento para lançar os dias de atestado de forma global e não queira lançar o evento de atestado via grupo de eventos. É necessário cadastrar um evento de provento do tipo dia ou valor, com o código de cálculo 145.   
Este campo só lista os eventos com o código de cálculo 145.  
   
Evento para atestado médico (horista)  
Neste campo deve informar um evento para lançar os dias de atestado de forma global e não queira lançar o evento de atestado via grupo de eventos. É necessário cadastrar um evento de provento do tipo hora, com o código de cálculo 145.   
Este campo só lista os eventos com o código de cálculo 145.   
**Observação**  
Com o parâmetro 'Lança evento de atestado via grupo de eventos' marcado, é ignorado os eventos informados nos campos acima, mesmo que não seja informado nenhum evento no grupo de eventos com o código de cálculo 145.  
O evento com o código de cálculo 145 não será lançado para os diretores (Tipo de Funcionário = 'D' e Categoria SFIPE = 5 ou 11).

Motivo de afastamento por COVID-19  
Nesse campo deve ser informado um motivo de afastamento por COVID-19. E quando for feito o afastamento, o motivo deve ser o mesmo informado no campo referente ao motivo, para que seja lançado no envelope de pagamento o “código de cálculo 436 – Atestado Médico de Afastamento por COVID-19”. Esse evento será considerado para eSocial, GPS e SEFIP.   
**Exemplo**  
Informado no campo o motivo 01 - Afastamento por COVID-19  
Funcionário afastado pelo Tipo ‘P' e motivo 01 - Afastamento por COVID-19  
No envelope de pagamento será lançado o evento tipo base código de cálculo 436 – Atestado Médico de Afastamento por COVID-19, criado previamente.

Contrato Suspenso

Afastamento por Contrato Suspenso mantém período aquisitivo de férias

Quando o funcionário for afastado por contrato suspenso, o sistema fará o acerto do período aquisitivo de férias de acordo com este parâmetro e o motivo selecionado para que não haja perda do período aquisitivo gerado por esse afastamento. O acerto do período aquisitivo deve ser executado no retorno do afastamento.

Afastamento por Contrato Suspenso mantém avos de 13º salário

Quando o funcionário for afastado por contrato suspenso, o sistema fará o cálculo dos avos de 13º salário de acordo com este parâmetro e o motivo selecionado para que não haja perda dos avos gerado por esse afastamento.

Motivo do afastamento por Contrato Suspenso sem perda de avos

Quando for marcado um dos parâmetros acima será necessário informar neste campo o motivo de afastamento que será considerado para não computar a perda de avos referentes ao afastamento por Contrato Suspenso. Para que esta parametrização seja considerada é necessário que este motivo seja igual ao motivo cadastrado no afastamento do funcionário.

**Observação:** Caso estes parâmetros não estejam selecionados todos os afastamentos serão considerados para a perda de avos nos processos de acerto de período aquisitivo, rescisão, histórico de provisões e lançamento de 13º salário. Para o cálculo da rescisão com a perda dos avos do período aquisitivo deve ser executado o acerto do período aquisitivo.

**Exemplo:** Mês competência 05/2020 – Parâmetros marcados e motivo preenchido com 1 – Sem perda de avos

Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 1 – Sem perda de avos

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 2 – Com perda de avos

Executando o acerto de período aquisitivo:

Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Período não foi estendido porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – Período aquisitivo de 02/01/2020 a 02/03/2021 – Período foi estendido porque o motivo de afastamento não era o mesmo do parametrizador.

Calculando 13º salário em dezembro/2020:

Funcionário 1 – 12 avos – Avos completos porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – 10 avos – Perda de 2 avos porque o motivo de afastamento não era o mesmo do parametrizador.

Para a rescisão contratual e histórico de provisões deverá ser executado o acerto de período aquisitivo primeiro pois assim o período aquisitivo estará correto no momento do cálculo. E o cálculo do 13º salário rescisão e histórico de provisões do 13º salário seguirá do mesmo jeito do 13º salário normal.
