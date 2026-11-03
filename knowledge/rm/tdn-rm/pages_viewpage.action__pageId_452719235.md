---
content_hash: 1886d477a935005fa0989b5202d37204eadebf4cb9445248c4820577c71e9de7
fetched_at: '2026-06-29T00:10:04.695310+00:00'
page_id: '452719235'
product: rm
source: tdn-rm
title: Assistente de Lançamento de Benefícios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719235
version: 2
---

**Assistente de Lançamento de Benefícios**

---

Este assistente permite a manutenção (inclusão, edição, consulta e exclusão) dos benefícios de Funcionários e seus Dependentes. Apenas benefícios vinculados pelo Assistente de Vinculação de Benefícios poderão ser lançados. O assistente realiza o lançamento dos benefícios vinculados direta ou indiretamente para o funcionário e seus dependentes.

**Passos para executar o Lançamento de Benefícios:**

1)Selecionar os funcionários e dependentes desejados;

2)Selecionar os benefícios a serem lançados na grid Benefícios não Lançados;

3)Acionar o botão "Lançar Benefício" e informar os dados do lançamento.

**Importante:**

O Totvs Gestão de Pessoas não realizará a validação dos benefícios obrigatórios, essa informação será usada na integração com o sistema Totvs Folha de Pagamento.

**Lançamento de benefícios com controle de pontuação:**

Quando o sistema Totvs Gestão de Pessoas estiver parametrizado para trabalhar com Controle de Benefício por Pontuação deverá ser apresentado para cada funcionário o saldo de pontos disponível. Este saldo será resultado da soma das fontes (cargos, funções, seções e funcionários).

Neste caso ao lançar benefícios ao funcionário o sistema realizará a validação do saldo disponível pelo funcionário, porém:

- Os pontos consumidos pelos benefícios adicionados aos dependentes do funcionário serão somados ao total de pontos utilizado pelo funcionário.

- Os pontos utilizados pelo funcionário ou seus dependentes serão subtraídos ao saldo disponível pelo funcionário. Ao realizar um lançamento obrigatório ou não obrigatório e o saldo não for suficiente o sistema emitirá uma mensagem informando ao RH que o funcionário não tem saldo disponível, mas permitirá o lançamento. Sendo assim, caso este beneficio tenha pontos para aquisição o valor do mesmo será debitado do saldo de pontos mesmo que deixando o saldo negativo.

- Apenas no Totvs RM Portal o funcionário não conseguirá solicitar um beneficio quando o saldo de pontos disponível não for suficiente para adquirir o beneficio solicitado.

- Assim também caso um benefício seja removido do lançamento do funcionário e/ou seus dependentes os respectivos pontos dos mesmos serão creditados no saldo de pontos do funcionário.

**Lançamento de períodos para os benefícios:**

Para um benefício é possível realizar um ou mais lançamentos separados por período, porém: - Não será possível lançar um benefício para um período ao qual a data de início seja menor ao mês/ano de competência; - Não será possível lançar mais de um período para o benefício com a mesma data de início; Todo período que for gerado pelo usuário e apresentar alguma intercessão deverá ser tratado conforme os casos: O período informado é menor que os demais períodos salvos:

* Será disponibilizado como um subperíodo subscrevendo o intervalo informado sobre o período já salvo; - Sua data de inicio menos um dia será a data de termino do período anterior; - Sua data de termino mais um dia (caso esta seja informada) será a data inicio do próximo período; - A data de termino dos períodos já salvos serão mantidos caso estas não sejam iguais a data termino do novo período; - Todos os períodos que foram subscritos serão salvos na tabela de histórico dos lançamentos. O período informado é maior que os demais períodos salvos:
* Será disponibilizado como um novo período sobrescrevendo o intervalo informado sobre o período já salvo; - Sua data de inicio menos um dia será a data de termino do período anterior; - Sua data de termino mais um dia (caso esta seja informada) será a data inicio do próximo período; - Qualquer data término dos períodos já salvos que forem menor igual a data de termino do período lançado, serão sobrescritas e salvas na tabela de histórico dos lançamentos; - Caso o período informado não possua data de termino, qualquer período já salvo que tenha interseção com a data de inicio, será sobrescrita e salva na tabela de histórico dos lançamentos. Todos os períodos que foram subscritos serão salvos na tabela de histórico dos lançamentos. **Importante:** - O cálculo dos benefícios lançados no Totvs Gestão de Pessoas será feito no Totvs Folha de Pagamento através do Cálculo de Benefícios dos Funcionários disponível no Menu Rotinas - Cálculo de Benefícios dos Funcionários. - Para lançar os benefícios para o envelope do funcionário, o usuário deverá acessar a tela de Grupo de Eventos disponível no Menu Movimento – Folha de Pagamento – Lançamentos Automáticos – Grupo de Eventos.  
     
     
  **Cópia de** **Benefício**  
     
  Para realizar a cópia de benefícios lançados a um funcionário para outro, há a opção *Copiar* no Assistente de Lançamento de Benefícios.  
   Para isso, é preciso selecionar o funcionário de quem se deseja copiar os benefícios e em seguida clicar na opção.  
   No mesmo é possível escolher os funcionários destino, sendo possível realizar filtro.  
    É possível selecionar os tipos de benefício origem que serão lançados e a ação para o lançamento, que são:  
    
  **Origem dos Benefícios (Lançamentos)**  
     
   - Selecionados: Somente os benefícios lançados e selecionados do Funcionário serão copiados.  
   - Benefícios Obrigatórios: Todos os benefícios marcados como obrigatórios através da hierarquia (Seção, Cargo, Função, Funcionário e Dependente) serão copiados com os valores de referência do cadastro de benefícios.  
   - Todos: Copiar todos os benefícios disponíveis da origem selecionada.  
     
  **Ação para o(s) Lançamento(s)**  
     
   - Ignorar: Ao lançar o benefício caso este já esteja lançado ao Funcionário selecionado, a cópia do benefício será ignorada.  
   - Sobrescrever: Ao lançar o benefício caso este já esteja lançado ao Funcionário selecionado, seu valor será sobrescrito.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cálculo de Benefícios do Funcionário  Benefícios gerenciados através do RM Portal
