---
article_id: 360059188733
category: RH - Períodos de Apontamento
content_hash: 16d596505bbfed0c79447184a14b06a4b2ef94cb00cb49b866390e2c221bdc71
fetched_at: '2026-06-28T22:44:45.130866+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290
type: support-article
updated_at: '2025-06-02T14:20:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290
---

**Dúvida**Rotina Período de Apontamento - PONA290 - Período de Apontamento  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No módulo Ponto Eletrônico, em Atualizações -> Cadastro de Ponto -> **Período de Apontamento**, temos uma rotina que podemos alterar o **período em aberto** que estamos trabalhando naquele momento.  
  
Ao acessar a rotina, clique em **Modificar Período de Apontamento**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26270233535767)  
  
Com exceção de períodos que precisem ser maiores ou menores que 30/31 dias, deve ser utilizada a opção **Dia Inicial/Final,** pois desta forma, o parâmetro **MV\_PAPONTA** ficará preenchido de forma que possibilite ao usuário alternar entre os períodos e trabalhar em mais de um período de apontamento. Para isto, basta ir alterando a data base do sistema de acordo com o último dia do período que deseja trabalhar. Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099507613)  
  
Informe o **Dia Inicial/Final conforme seu Período de Apontamento**, por exemplo: 01/31 (nos casos em que o período é do mês completo. Deve ficar desta forma mesmo para os meses que tem 30, 29 ou 28 dias, pois o sistema conseguirá interpretar a quantidade de dias corretamente para a montagem do calendário), 26/25, 16/15, etc:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28627541357975)  
  
Após **Salvar,** informe o **último dia do período** que ficará como aberto/principal para o sistema:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28627605030423)  
  
Após concluir e clicar em **Apenas Visualizar**, ficará conforme exemplo abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097201474)  
  
**IMPORTANTE:**  
Nesta rotina ficarão **apenas os períodos já fechados pela rotina de** **Fechamento Mensal, e os registros terão legenda em cor vermelha.** **Não recomendamos a inclusão do Período de Apontamento manualmente,** pois pode acarretar problemas nas rotinas do módulo de forma geral.Caso existam registros com legenda em **cor verde**, significa que foram criados indevidamente pelo usuário, portanto, **devem ser excluídos.  
  
\*\*\***Se o Espelho de Ponto for impresso com **datas parciais** do Período de Apontamento, o rodapé com as Verbas dos Resultados **não será impresso**, pois o Cálculo Mensal processado com o último dia do   
Período gera as verbas nos Resultados com a Data de Pagamento neste mesmo dia, portanto, é feito este vínculo diretamente com o calendário do Período do Ponto.  
Em casos de desligamentos dirante o período, onde é necessária a impressão do Espelho de Ponto parcial e exibindo o rodapé com as Verbas, o **Cálculo Mensal** deve ser feito com a **database** no dia do desligamento do funcionário, para que as Verbas sejam geradas com esta data.  
  
**Saiba Mais:**[RH - Linha Protheus - Como trabalhar com um período de apontamento menor ou maior que 30 dias no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011060231-RH-Linha-Protheus-Como-trabalhar-com-um-per%C3%ADodo-de-apontamento-menor-ou-maior-que-30-dias-no-Ponto-Eletr%C3%B4nico)
