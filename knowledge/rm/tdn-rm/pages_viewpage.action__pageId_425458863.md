---
content_hash: 9c53bc5a7e3c8c9c38f3f0cef86337dea7877e04530c0aebe3aef288486fde82
fetched_at: '2026-06-29T00:09:32.495677+00:00'
page_id: '425458863'
product: rm
source: tdn-rm
title: Gerar Atendimentos a partir de uma Sentença SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458863
version: 2
---

**Gerar Atendimentos a partir de uma Setença SQL**   
A funcionalidade de Gerar atendimento a partir de uma sentença SQL é para gerar atendimentos de acordo com os registros retornados de uma sentença SQL.

Estes atendimentos terão alguns campos preenchidos de acordo com uma parametrização inicial do processo e tais atendimentos terão como opções de repasse para um atendente fixo, para um grupo de atendentes e ainda definido no avanço da primeira etapa do fluxo.

Para execução deste serviço a sentença SQL deve ser previamente cadastrada, e caso possua parâmetros os mesmos devem ser informados criando a associação.

Os tipos de valores permitidos para sentença são (Valor fixo, Data Atual, Coligada Atual, Usuário logado), onde valor fixo irá permitir definir um valor ou as colunas da sentença.

O assunto e a solicitação irão preencher os respectivos campos no atendimento, sendo possível utilizar o esquema de de {0} {1}, onde os valores entre chaves poderão ser substituídos por campos retornados da sentença SQL + o default, que é Coligada Atual, Data Atual, Usuário logado.

O assunto mostra de forma resumida o pedido da solicitação e a solicitação por sua vez detalha e documenta o que pedido.

Os atendimentos podem seguir um fluxo de trabalho (Workflow) mas, os campos grupo e tipo do atendimento devem ser preenchidos.

Após a seleção destes campos os parâmetros do tipo de atendimento podem ser visualizados (caso possua parâmetros) e informados.

A classificação do atendimento auxilia na verificação das solicitações prioritárias, elas são de grande importância e permitem agilidade em problemas de relevância alta.

Atendente responsável: Permite que seja escolhida a forma de repasse dos atendimentos gerados.  
Atendente Fixo | Grupo de Atendentes | Definido no avanço da primeira etapa.

Coligada do Cliente  
Selecione a coligada do cliente para que o atendimento gerado pelo processo tenha o campo cliente preenchido corretamente.

Cliente do Atendimento  
Para valor este campo de maneira correta é necessário que a sentença SQL retorne o valor do campo que representa o código do cliente lembrando que o cliente pode ser registros dos cadastros de pessoa, aluno, professor, prospect e cliente/fornecedor.

Tipo do Cliente  
Um atendimento pode ter como cliente qualquer registro dos seguintes cadastros: Cliente / Fornecedor, Prospect / Suspect, Pessoa, Aluno ou Professor. Este campo deve estar preenchido em sintonia com o campo cliente do atendimento. Caso seja selecionado um tipo de cliente diferente do cliente selecionado, o cliente do atendimento não será salvo.

Coligada do Produto  
Selecione a coligada do produto para que o atendimento gerado pelo processo tenha o campo produto preenchido corretamente.

Produto do Atendimento  
Para valor este campo de maneira correta é necessário que a sentença SQL retorne o valor do campo que representa o código do produto.

**Regras de Funcionamento:**

* Caso a sentença SQL possua parâmetros os mesmos devem ser definidos.
* Os parâmetros possuem relação direta ao tipo:  
  Parâmetro do Tipo Inteiro: Aceita apenas valores inteiros ou decimais.  
  Parâmetro do Tipo Real: Aceita apenas valores inteiros, reais ou decimais.  
  Parâmetro do Tipo Data: Aceita apenas valores data.  
  Parâmetro do Tipo String: Aceita qualquer valor.  
  Parâmetro do Tipo Texto: Aceita qualquer valor.
* Para cada registro o sistema abre um novo atendimento, caso a sentença não retorne nenhum valor, nenhum atendimento será criado.
* Para definir o tipo de atendimento será obrigatório definir o grupo de atendimento.
* Para valorar os parâmetros do tipo de atendimento será necessário ter um tipo de atendimento definido.
* Para que o atendimento avance para  primeira etapa será necessário ter um tipo de atendimento definido.
* Para definir como atendente fixo deverá ser selecionado um atendente.
* Para definir com o grupo de atendente deverá ser selecionado um grupo de atendente.
* Nos campos de texto livre (Assunto, Solicitação), o esquema utilizado para parâmetros é {0},{1},{2}, respeita a ordem seqüencial de 0,1,2 assim sucessivamente, pois não será possível inserir parâmetros que não respeitem essa sequência . Caso seja inserido neste campo parâmetros de forma incorreta (seja ela com os números não sequenciais ou com chaves abertas sem fechar, ou fechadas sem abrir, ou até mesmo aberta e fechada sem possuir valor dentro, será apresentado uma mensagem e o processo não irá prosseguir.

  **Hora de execução (1ª execução)**  
  Executar o processo uma única vez e imediatamente na data corrente.  
  Executar o processo uma única vez em uma data e hora especifica de acordo com a data e hora escolhida. Essa opção vem com a data corrente do dia como padrão, sendo possível alterá-la.  
  Sob demanda  
  Repetir a execução  
  Para habilitar esta opção é necessário informar a data e hora para 1ª execução.  
  Deseja executar o processo de forma recorrente onde serão apresentados as seguintes opções de recorrência:  
  • Semanal - Todas as semanas no mesmo horário e no(s) dia(s) definido(s) pelo usuário.   
  • Mensal - Todos os meses, no mesmo horário e no dia definido pelo usuário.  
  • Diária - Diariamente, a cada intervalo (em horas) definido pelo usuário.

  |  |  |
  | --- | --- |
  |  | Recursos Adicionais |

  [  
  Blog - Gerar Atendimentos por Consultas SQL|http://totvsconnect.blogspot.com/2011/02/como-fazer-gerar-atendimento-via]
