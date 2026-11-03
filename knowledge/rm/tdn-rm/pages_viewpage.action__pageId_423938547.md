---
content_hash: 271b5d2ef3938f015b5df318717236bd605fffca30eabd90de22151699ed800a
fetched_at: '2026-06-29T00:09:27.866919+00:00'
page_id: '423938547'
product: rm
source: tdn-rm
title: Lançamentos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938547
version: 6
---

Dica

A funcionalidade é multicoligada a partir da versão 12.1.2310.

A rotina de Lançamentos Periódicos auxilia na criação de lançamentos que se repetem periodicamente (mês a mês, ou mesmo diariamente), variando de um período para o outro apenas algumas informações, como a data, número de documento ou mesmo a filial, mas onde a maioria dos dados do lançamento se repete periodicamente. O pagamento de algumas despesas como Aluguel, Água e Luz, Telefone são alguns exemplos de lançamentos que se repetem periodicamente, usando sempre as mesmas contas contábeis e no caso de Aluguel, por exemplo, usando também o mesmo valor, variando de um período para o outro apenas algumas informações como data, número do documento e em alguns outros casos também o valor.   
   
Para facilitar a execução de rotinas contábeis como estas, ao invés de incluir os lançamentos, um a um, através da Inclusão de Lançamentos, podem-se criar *estruturas* que permitam a geração automática de lançamentos semelhantes aos referidos acima. É interessante que se crie uma estrutura para cada tipo de lançamento, como nos exemplos acima, uma para Pagamento de Aluguel outra para Pagamento de Água, etc. Em cada uma das estruturas crie seus respectivos moldes com as informações comuns que se repetirão a cada período (tais como as contas contábeis), assim como as definições das variáveis que serão informadas e alteradas à cada execução do processo de geração dos lançamentos (tais como data e número do documento). Uma vez criadas as estruturas, quando for necessário incluir os lançamentos, que neste caso não serão mais cadastrados um a um e sim gerados automaticamente, basta executar o processo de Geração de Lançamentos Periódicos.  
   
Quem trabalha com o *JobServer* configurado para executar em modo 3 Camadas, pode contar ainda com o recurso de Agendamento de Processos, possibilitando então **Agendar** a Geração dos Lançamentos Periódicos para um determinado dia/horário, podendo ainda se desejar, criar recorrências ou repetições para estes agendamentos.   
   
**Atenção**  
Não é possível Alterar ou Excluir estruturas que tenham agendamentos pendentes, para isto, primeiro desabilite o agendamento para a estrutura desejada.  
Para ter acesso aos agendamentos, selecione a estrutura desejada e em *Anexos*, selecione a opção *Agendamentos*. Através desta opção você poderá consultar, acompanhar e gerenciar todas as gerações executadas por estrutura.

Clique nos itens abaixo para obter informações sobre:

* Criação de Estruturas
* Criação de Variáveis
* Criação de Moldes
Processos

* Geração de Lançamentos Periódicos
* Cópia de Estrutura de Lançamentos Periódicos
