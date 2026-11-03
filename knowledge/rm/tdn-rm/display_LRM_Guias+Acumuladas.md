---
content_hash: 5180db0b8bf3bd2f7d2ec7440b76f9e049ff68bdcc9b8701afd37e90ccc5a419
fetched_at: '2026-06-29T00:09:19.561743+00:00'
page_id: '422545612'
product: rm
source: tdn-rm
title: Guias Acumuladas
type: documentation
url: https://tdn.totvs.com/display/LRM/Guias+Acumuladas
version: 7
---

O controle de guias de recolhimento acumuladas estará disponível para tributos dos seguintes tipos: CIDE, COFINS, COFINS IMPORTAÇÃO, CSLL, PIS, PIS IMPORTAÇÃO, INSS, IRPJ, IRRF PJ, OUTROS, IOF, COSIRF, CPMF e SIMPLES NACIONAL.  
Definido o campo no cadastro de tributos, pasta Outros Dados, **Valor mínimo Guia**. Este campo recebe o valor mínimo para geração de guias de recolhimento. Esse campo será visível somente para os tributos de tipos listados acima e receberá como default zero. Se o Valor Mínimo Guia for maior que zero, o sistema passará a controlar guias acumuladas para o tributo, caso contrário o controle não existirá.   
Para todos os tipos de guias foi criado o campo Valor Apurado, onde estará definindo o valor apurado para a guia no período selecionado. É este campo que receberá o valor calculado para a guia, que somado à multa e aos juros, estarão compondo o Valor Pago.  
Nas guias onde existe o controle de valor acumulado, ou seja, cujo tributo possui Valor Mínimo Guia maior que zero, além do Valor Apurado, serão visíveis os campos Valor Acumulado e Valor Guia. Valor Acumulado estará recebendo o valor acumulado de guias anteriores que não atingiram o valor mínimo para o tributo e o Valor Guia estará recebendo o Valor Apurado + Valor Acumulado.   
   
***Atenção!***Se o usuário decidir trabalhar com o valor mínimo de R$ 10,00 para o tributo IRPJ, por exemplo, ao abrir um período de maio de 2011 para IRPJ, todas as guias cadastradas estarão como Guia Processada e Não Acumulada. Até mesmo as guias que não atingiram o valor de R$ 10,00, visto que antes da alteração, o valor mínimo guia era 0 (zero). Para que o sistema passe a reconhecer estas guias como acumuladas, o estorno do processo de utilização de guias acumuladas deverá ser executado. A partir daí, as guias estarão como Guia Não Processadas. Neste momento o processo poderá ser executado e o sistema passará a considerar tanto guias acumuladas como não acumuladas.

***Atenção:*** Antes de efetuar o processo de Guias Acumuladas é necessário verificar se o **código da receita** foi carregado na guia DARF.  O mesmo é necessário para que as guias possam ser acumuladas.  
   
**Inclusão das Guias (Controle de Valor Mínimo)**

Na inclusão de guias com controle de valor acumulado, o Valor Acumulado será preenchido automaticamente com o valor zero.   
Este será preenchido somente na rotina de processamento de guias acumuladas, disparada em Processos | Processar Guias acumuladas.   
Inicialmente as guias serão adicionadas como processadas, ou seja, para o sistema não será importante se a guia atingiu o valor mínimo ou não.  
***Observação:***Não será permitida a inclusão de uma guia se existir guias posteriores com mesmas características, para as quais o processo de utilização de guias acumuladas já foi executado.   
   
**Edição das Guias (Controle de Valor Mínimo)**

Se o processo de utilização de guias acumuladas já foi executado para a guia, esta não poderá ser editada, somente consultada. Mesmo que a guia não tenha utilizado guias acumuladas anteriormente.  
   
**Exclusão das Guias (Controle de Valor Mínimo)**

Também não será permitido excluir guias para as quais o processo de utilização de guias acumuladas já foi executado. Tal processo deverá ser estornado primeiro.  
   
**Processo Guias Acumuladas**

O processo de utilização de guias acumuladas poderá ser disparado do menu Processos | Processar Guias acumuladas, localizado na edição das Guias em Anexos do período. Este botão será visível somente se existir o controle de valor mínimo para o tributo.  
Todas as guias do período selecionado serão percorridas e o processo será executado para cada uma delas. Se existirem erros, será exibido um arquivo de LOG armazenado no diretório temporário do Sistema de Gestão Fiscal com as informações necessárias.   
Se a guia não gerou nenhum dos LOG's acima, o sistema estará executando as seguintes tarefas:  
Seleciona guias anteriores com mesmas características acumuladas. Serão selecionadas somente guias acumuladas, ainda não utilizadas para apuração de períodos posteriores. Além disso, as guias selecionadas já deverão se encontrar processadas, ou seja, a rotina de utilização de guias acumuladas já deverá ter sido executada para elas.  
Soma o Valor Apurado destas guias anteriores acumuladas  
Se a soma do Valor Apurado das guias acumuladas anteriormente com o Valor Apurado da guia para a qual o processo está sendo executado atingir o valor mínimo para geração de guias, o Valor Acumulado da guia receberá a soma do Valor Apurado das guias acumuladas anteriormente, o Valor Guia receberá o Valor Apurado + Valor Acumulado. Se o valor mínimo não foi atingido, o Valor Acumulado não será preenchido e as guias acumuladas anteriormente continuarão acumuladas. Neste caso, a guia para qual o processo está sendo executado. Se o sistema não selecionou nenhuma guia acumulada anteriormente, o Valor Apurado da guia para qual o processo está sendo executado será comparado ao Valor Mínimo para geração de guias.

**Estornar Guias Acumuladas**

O estorno das Guias acumuladas poderá ser disparado através do menu Processos | Estornar Guias acumuladas, localizado na edição das Guias em Anexos do período. Este botão será visível somente se existir o controle de valor mínimo para o tributo.  
Todas as guias do período selecionado serão percorridas e o processo será executado para cada uma delas. Se existirem erros, será exibido um arquivo de LOG armazenado no diretório temporário do Sistema de Gestão Fiscal com as informações necessárias.  
As guias acumuladas anteriormente, utilizadas pela guia a ser estornada, passarão a se tratar de guias acumuladas que poderão ser utilizadas por guias posteriores para apuração a qualquer momento. Mesmo que o Valor Mínimo Guia do tributo tenha sido alterado, estas guias que tinham sido utilizadas continuarão acumuladas, até que o processo para elas também seja estornado.  
              
**Integração das Guias Acumuladas com TOTVS Gestão Financeira**

O sistema estará integrando ao TOTVS Gestão Fiscal somente as guias de recolhimento não acumuladas e já processadas, ou seja, aquelas em que a rotina de utilização de guias acumuladas já foi executada.   
   
**Rotinas Legais**

Nas rotinas legais que utilizam guias de recolhimento, serão selecionadas somente guias de recolhimento não acumuladas, ou seja, aquelas que atingiram o valor mínimo para geração de guias ou aquelas que não possuem controle de guias acumuladas. São exemplos de rotinas legais que selecionam guias de recolhimento: GIA ST, SISIF CE, Apuração de ICMS ES, GIA RS, DCTF e SINTEGRA.  
Para uma correta geração dos registros baseados nas guias de recolhimento, será necessário processar as guias acumuladas para todas as guias pertencentes ao período para o qual a rotina será gerada.   
   
**Geração **Automática**das Guias Acumuladas**

Se existir alguma guia de recolhimento já processada, ou seja, guia para a qual a rotina de utilização de guias acumuladas já foi executada, a geração automática de guias não será permitida. Caso contrário, as guias continuarão sendo geradas normalmente desde que não existam guias posteriores com mesmas características já processadas. Lembrando que inicialmente todas as guias serão consideradas PROCESSADAS e NÃO ACUMULADAS.   
Se o tributo não possuir controle de guias acumuladas, estas consistências não serão realizadas na geração automática de guias.  
  
**Exemplo de Controle de Guias Acumuladas:**

|  |  |
| --- | --- |
| Valor Mínimo | 30,00 |

| Janeiro / 2011 | |
| --- | --- |
| Valor acumulado | 0,00 |
| Valor apurado | 5,00 |
| Valor da guia | 5,00 |
| Acumula? | Sim |

| Fevereiro / 2011 | |
| --- | --- |
| Valor acumulado | 0,00 |
| Valor apurado | 10,00 |
| Valor da guia | 10,00 |
| Acumula? | Sim |

| Março/ 2011 | |
| --- | --- |
| Valor acumulado | 0,00 |
| Valor apurado | 5,00 |
| Valor da guia | 5,00 |
| Acumula? | Sim |

| Abril / 2011 | |
| --- | --- |
| Valor acumulado | 20,00 (guias de Janeiro e Março) |
| Valor apurado | 15,00 (valor apurado em Abril) |
| Valor da guia | 35,00 |
| Acumula? | Não acumula |
