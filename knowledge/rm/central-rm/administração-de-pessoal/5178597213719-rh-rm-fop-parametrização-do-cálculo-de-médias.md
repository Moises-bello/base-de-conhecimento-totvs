---
article_id: 5178597213719
category: Administração de Pessoal
content_hash: 6b4c3e14c8cd28a6e6971ca1114498a0d73cc3c7ba8f1fa19d37b583a48f05f3
fetched_at: '2026-06-28T22:47:01.370144+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Parametrização do Cálculo de Médias
type: support-article
updated_at: '2024-01-29T18:33:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5178597213719-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-do-C%C3%A1lculo-de-M%C3%A9dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:14:26 min  
  
Dúvida**  
Como realizar parametrização para calculo médias no sindicato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar parametrização de calculo das médias verifique as orientações abaixo.  
  
1. Acesse: **Administração de Pessoal | Sindicatos** e edite o sindicato desejado.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5217182419735/mceclip0.png)  
 **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5178498298007/mceclip1.png)**Os parâmetros **Tipo de Cálculo**, **Corrige Valores, Habitualidade** e **Parâmetros relacionados à afastamento** estão disponíveis em todas as abas de Média, e as definições destes campos seguem abaixo:

* **Tipo de cálculo:** Selecione o tipo de cálculo dos eventos para média de 13º salário na Rescisão.  
  São três as opções:

**0 - sem média:** não considerará média  
**1 - média por valor:** considerará valores dos eventos  
**2 - média por hora:** considerará número de horas dos eventos

* **Número de meses:**

**--> Tipo de Cálculo = Hora****Meses p/ evento Valor:** Informe o número de meses, até três períodos, para o cálculo da média dos eventos do tipo valor.  
**Meses p/ evento Hora:** Informe o número de meses, até três períodos, para o cálculo da média dos eventos do tipo hora.  
**Meses p/ evento. Ref:** Informe o número de meses, até três períodos, para o cálculo da média dos eventos do tipo referência.  
  
**--> Tipo de Cálculo = Valor****Meses p/ evento Valor:** Informe o número de meses até três períodos para o cálculo da média dos eventos do tipo valor.  
**Meses p/ evento Hora:** Informe o número de meses, até três períodos, para o cálculo da média dos eventos do tipo hora.  
**Meses p/ evento. Ref:** Informe o número de meses, até três períodos, para o cálculo da média dos eventos do tipo referência.  
  
**Importante**  
Na primeira coluna, informando o número de meses igual a 0, zero, o sistema calculará a média de 13º salário sobre o Período Aquisitivo. Se o usuário informar um determinado número de meses, o sistema irá considerar esse número para cálculo da média.  
A segunda e terceira colunas, caso estejam preenchidas com 0, zero, serão desconsideradas pelo sistema. Se o usuário lançar quaisquer números de meses em uma dessas colunas ou em ambas, esses números serão considerados para cálculos das médias.  
O maior valor encontrado, considerando os três períodos informados, é que será assumido pelo sistema.  
Ver Comparação de Média em até 3 períodos distintos.

* **Maiores Valores:** Informe o número de meses para que o sistema busque os maiores valores, dentro dos meses indicados para o cálculo da média, dos eventos do tipo valor.

**Exemplo:**  
O número de meses indicado para a média foi 3, três. O sistema buscará nos últimos 3, três, meses da Ficha Financeira os eventos que participarão do cálculo da média de férias, incidem férias.  
No campo **Maiores Valores** foi informado 2, dois, meses. Neste caso, o sistema irá verificar quais os 2, dois, meses dentre os 3, três, informados para a média, que possuem os eventos com maiores valores, para utilizá-los no cálculo da média.  
 **Importante**  
O sistema tratará da seguinte forma as informações dos campos Nro. Meses p/ análise, Nro. Meses para habitualidade, Meses p/ ev. Valor, Meses p/ ev. Hora e Maiores Valores:  
  
- Antes de mais nada, será necessário verificar se determinado evento é habitual ou não. Para isso, o sistema irá verificar nos N meses anteriores ao atual, onde N é o número de meses para análise, quantas ocorrências existem.  
- Se existir pelo menos o número especificado como mínimo para se considerar habitual, o evento entrará para a média.  
- O sistema irá, então, procurar os eventos selecionados nos últimos N meses anteriores ao atual, onde N, agora, é o número de Meses p/ Ev. Valor e Meses/ Ev. Hora, selecionando e somando os Maiores Valores.  
O resultado será dividido pelo número de Meses p/ Ev. Valor e Meses p/ ev. Hora, conforme o tipo do evento.

* **Considera maiores valores para soma:** Este parâmetro configura o sistema, de modo que, durante o cálculo de média, o usuário pode escolher dentre os valores obtidos para média de valor e hora, os dois maiores de cada tipo.
* **Habitualidade**

**Número de meses para análise:** Informe o número de meses que deverão ser considerados pelo sistema para verificar a Habitualidade, frequência, do evento, isto é, o número de vezes em que o evento foi habitual. Este campo está diretamente associado ao seguinte:  
   
**Número de Meses para habitualidade:** Informe um número mínimo de meses que os eventos, que entrarão para o cálculo das médias, deverão constar na ficha financeira do funcionário para ser considerado pelo sistema para o cálculo da média.  
Essa habitualidade será verificada dentro do período, número de meses para análise, informado no campo anterior.  
Caso o usuário não deseje que esta consistência seja feita, deverá informar 0, zero.  
Informando um número de meses de habitualidade diferente de 0, zero, o sistema irá proceder da seguinte maneira:  
  
**Exemplo:**  
No cálculo da média de férias foram consideradas as informações:  
Meses para ev. Valor: 6  
Meses para ev. Hora: 6  
Número. Meses para análise: 12  
Número. Meses para Habitualidade: 5  
   
- Os eventos Comissão e Hora Extra incidem férias e serão pesquisados para o cálculo da média de férias.  
- O sistema pesquisará nos últimos 12, doze, meses a habitualidade desses eventos.  
- Como o número de meses informado para o cálculo da média foi 0, zero, serão considerados os eventos constantes em todo o período aquisitivo do funcionário.  
- O evento Comissão somente consta em 2, dois, meses do período aquisitivo, logo não será considerado para o cálculo da média, mesmo estando incidindo férias, pois o número de meses de habitualidade, Nr. Meses Hab., é 5, cinco.  
- O evento Hora Extra 50% está presente em 7, sete, meses do período aquisitivo, logo será considerado para o cálculo da média.  
- Embora o evento Hora Extra 50% tenha ocorrido 7, sete, vezes, não serão considerados 7, sete, meses para cálculo da média, uma vez que, no campo Meses p/ ev. Hora, foi informado 6, seis, meses.  
  
**Importante**  
O sistema não irá considerar os eventos para média, caso o número de meses da habitualidade seja superior ao número de meses para o cálculo da média, Meses p/ ev. Valor,Meses p/ ev. Hora.  
Informando um número de meses, valor, diferente de 0, zero, o usuário deverá também preencher o campo **Maiores Valores**.

* **Correção de Valores**

**Corrige valores pelo salário da época:** Marque este parâmetro caso deseje que os eventos do Tipo Valor, os eventos do Tipo hora e os eventos do Dipo dia sejam corrigidos de acordo com o histórico salarial do funcionário para o cálculo da média.  
  
**Corrige valores por tabela de correção:** Confirmando este campo, o sistema atualizará os valores dos eventos que participarão da média de férias, de acordo com a Tabela de Correção.  
  
**Importante  
- Média por Hora:** O sistema corrigirá somente os valores dos eventos tipo valor que participarão da média. Os eventos tipo hora terão seus valores atualizados de acordo com o valor hora do salário atual.   
**- Média por Valor:** O sistema corrigirá os valores dos tipo valor e dos eventos tipo hora. 

* **Tabela de Correção:** Através deste campo o usuário poderá atualizar a unidade monetária. Selecione a tabela de correção de valores, índice, moeda, etc., a ser considerada. O ícone abaixo, localizado na extremidade do campo, acessa a Janela de edição Moeda, para inclusão, caso haja necessidade:

O cálculo da correção do valor é feito pela divisão do índice na data do pagamento do evento, ou data imediatamente anterior, multiplicado pelo índice na data do último dia do mês da competência atual, ou data imediatamente anterior.  
  
Sugerimos a impressão do debug do cálculo e das médias com tipo da fonte *Courier New* e Tamanho 8.

* **Parâmetros relacionados à afastamentos:** Marque os afastamentos que os meses não serão contados para cálculo de médias.

**Exemplo:** Marcando o afastamento Af.Ac.Trabalho, durante o período de afastamento os meses não serão considerados para cálculo de média.

* **Desconsidera o mês em que o funcionário ficar XX dias ou mais afastado para contagem de meses:** Cadastre no campo o número de dias para que o mês não seja considerado para contagem de tempo para cálculo de médias.

**Exemplo:**  
Se for cadastrado o número 31, o mês em que o funcionário estiver afastado por período inferior a 31 dias será considerado para cálculo das médias e no mês em que o funcionário estiver afastado por período superior ou igual a 31 dias não será considerado.

* **Desconsidera também p/soma dos valores:** Marque este parâmetro caso queira desconsiderar também os valores dos meses de afastamentos parametrizados acima. Este botão, , permite copiar registros entre coligadas de tabelas de uma coligada para outra.

O usuário deverá também seguir uma ordem, para evitar inconsistências no momento da operação. Veja detalhes no Roteiro para Cópia dos Registros entre Coligadas.  
  
Clique neste ícone que o Folha de Pagamento disponibilizará a janela de Cópia de Registro onde o usuário poderá marcar os valores dos campos que serão copiados para o próximo registro.  
Utilize este ícone para colar os valores que selecionados do registro anterior.

* **Substitui período de afastamento por meses anteriores:** Com este parâmetro marcado, o período a ser desconsiderado para o cálculo de média é substituído por meses respectivamente anteriores em quantidade referente ao período do afastamento. Este parâmetro não é válido para empresas que realizam o cálculo da média de acordo com o Período Aquisitivo, somente para últimos N meses.

**Exemplo:**  
Considere que a apuração de média do funcionário é realizada nos últimos 6 meses, e que dentro deste período o funcionário ficou 2 meses afastados:  
   
Meses para a apuração de média: 01/2010 a 06/2010  
Período do afastamento: de 01/04/2010 a 01/06/2010  
   
Caso o parâmetro **Substitui período de afastamento por meses anteriores** esteja marcado, o sistema automaticamente aumenta o número de meses em igual quantidade do afastamento. No caso do exemplo o sistema considera os meses de Nov/09 e Dez/09 para o cálculo das médias. Caso nestes meses também existam afastamentos o sistema desconsidera, trazendo sempre o anterior.
