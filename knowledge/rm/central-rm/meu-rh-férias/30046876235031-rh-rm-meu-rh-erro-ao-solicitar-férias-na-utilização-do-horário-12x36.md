---
article_id: 30046876235031
category: Meu RH - Férias
content_hash: 1e04d88efb48cc1350217105a5776ad1f3476e93523f2bf2df572660db7ee750
fetched_at: '2026-06-28T22:47:31.633964+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Erro ao solicitar férias na utilização do horário 12x36
type: support-article
updated_at: '2025-02-21T12:11:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30046876235031-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-na-utiliza%C3%A7%C3%A3o-do-hor%C3%A1rio-12x36
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30046876206871) Tempo aproximado para leitura: **00:01:36 min**

**Ocorrência:**Ao realizar a sugestão de férias, é apresentada a seguinte mensagem de erro: "Início de férias para jornada **12x36** não pode ser em dia de feriado, descanso ou dia compensado."  
  
**Ambiente:**TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões  
  
**Causa:**A mensagem de erro é gerada quando a data solicitada para o início das férias do colaborador coincide com um dia de descanso, compensado ou feriado.  
  
**Solução:**Para solução, deverá conferir as parametrizações necessárias para o correto funcionamento das férias para funcionários no horário 12x36, conforme passos abaixo:

1- Acesse o *parametrizador* no módulo de Folha de Pagamento, no quiosque dos funcionários,

Marque a opção **"Não impedir marcação de férias para jornada 12x36"**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30046876208663)**

2- Em seguida, proceda com as seguintes verificações:

Acesse o *Cadastro de Horário* e, na aba **eSocial**, no campo **Tipo de Jornada e-Social**, certifique-se de que a opção **jornada 12x36** está corretamente selecionada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30046909105047)

3- Após isso, é necessário conferir se a data sugerida de inicio de férias do funcionário, se realmente caiu em um dia trabalhado, para essa conferência, acesse o *Espelho de Ponto* do colaborador e clique no botão **Visualizar Horário**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30046876211351)

Na visualização do horário, insira as datas de início e fim do mês em que o colaborador está solicitando as férias. Selecione o horário desejado e clique em **Atualizar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30046876213015)

Verifique o dia solicitado e certifique-se de que essa data corresponde a um dia de trabalho. Caso a data esteja marcada como feriado, descanso ou dia compensado, será necessário reagendar a solicitação para uma nova data, que seja um dia útil de trabalho.  
  
**Importante**Configura se o cadastro do horário 12x36 foi criado corretamente, conforme orientações da documentação a seguir:  
[RH - RM - PTO - Como criar horário 12x36](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025208432-RH-RM-PTO-Criar-hor%C3%A1rio-12x36)
