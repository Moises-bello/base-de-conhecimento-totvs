---
content_hash: d856fda915f370a783a7e4c1154603b879bfc284c2a7c10e4a1ee2a66514ef62
fetched_at: '2026-06-29T00:09:17.725493+00:00'
page_id: '421388631'
product: rm
source: tdn-rm
title: Gerenciar Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciar+Acordo
version: 4
---

Desenvolvido com o objetivo de permitir gerenciar as negociações realizadas nos Lançamentos Financeiros, gerando novos Acordos utilizando o Template de Acordo.

A opção está disponível no Menu: Contas a Pagar - Receber | Operações Financeiras | Acordo | Gerenciar Acordo

Serão apresentados na Visão os Acordos gerados pelo Totvs Gestão Financeira e pelo Portal do Educacional, onde será possível visualizar informações como : Referência do Acordo , Data do Acordo , Usuário Aprovação, Cliente/Fornecedor, Quantidade de Parcelas, Data do primeiro Vencimento , Situação entre outros.  
    
**Aprovação do Acordo**

Existem duas formas de aprovação do Acordo que são parametrizadas no template: a "Simples", executada via processo na Visão de Acordo pelo usuário que tenha permissões no menu, e a aprovação via Work Flow que gera, de acordo com os parâmetros definidos no template um atendimento para o Módulo CRM. O processo será controlado por um campo de Status, e também serão armazenados o usuário e data de aprovação.

Somente será apresentado as opções de Aprovar ou Reprovar Acordo no Menu- Processos, se o Template estiver parametrizado para Efetivar Ao Aprovar.

A aprovação de Acordo com opção de Efetivação com aprovação via Work Flow será realizada na visão de Acordo, editando o registro desejado. Na aba Dados do Acordo deverá clicar no campo de Atendimento Aprovação para que seja iniciada as etapas do processo e assim concluido o processo de geração do mesmo.

**Rastreabilidade Lançamentos do Acordo**

Os Lançamentos Financeiros do Acordo serão gerados conforme a opção de Efetivação parametrizada no Template de Acordo. Até que a Efetivação ocorra existirá somente registros de Lançamentos não efetivados que poderão ser visualizados na tela do menu Anexos: Lançamentos Gerados por Acordo não Efetivados.

Ao efetivar um Acordo a cobrança será realizada nas parcelas geradas do mesmo. Alterações no Lançamento de origem do Acordo somente poderão ocorrer caso o mesmo esteja com status de Efetivado ou Cancelado. No caso de Acordo reprovado os Lançamentos não serão gerados ficando apenas como consulta na tela de Lançamentos Gerados por Acordo não Efetivados.

Se habilitada a opção Efetivação do Acordo do Template como "Ao Criar" os Lançamentos serão gerados automaticamente na criação do Acordo, sendo apresentados na *Visão de Lançamentos* e Lançamentos Gerados por Acordo.

Se habilitada a opção de "Ao aprovar", os Lançamentos serão apresentados na tela de *Lançamentos* Gerados por Acordo não Efetivados, após a execução do processo de aprovação os registros ficarão disponíveis em  Lançamentos Gerados por Acordo.

Com a opção de "Após pagamento 1ª parcela" somente o Lançamento da primeira parcela é criado junto com o Acordo, para as demais parcelas, serão geradas na baixa ou emissão de cheque desse lançamento, sendo apresentadas em  Lançamentos Gerados por Acordo.

**Cancelamento do Acordo**

Para cancelar um Acordo selecione o registro que deseja realizar o processo. Será possível realizar o cancelamento de duas formas:

Varredura de Lançamentos

Será utilizada quando a primeira parcela do Acordo já estiver vencida em um número de dias maior que o prazo definido na execução, sendo assim o sistema varrerá os Lançamentos Financeiros identificando o Acordo e cancelando o mesmo.

Cancelamento pela visão de Acordo

Será utilizado para um ou mais registros independente se vencidos ou não.

Em ambos os casos a regra para cancelamento será a mesma: Lançamentos gerados pelo Acordo não podem estar baixados nem cancelados. O cancelamento do Acordo irá disparar um processo para que o Módulo que fez o Acordo faça validações e também execute as regras de cancelamento em suas entidades (caso exista alguma).

O cancelamento somente será possível se todos os Lançamentos gerados por Acordo atenderem a condição de cancelamento, do contrário o sistema não permitirá a conclusão do processo.

Para Lançamento gerado via acordo com boleto atrelado é necessário cancelar o Acordo para que o (s) Lançamento (s) e Boleto (s) também seja cancelado (s).

**Exclusão de Acordo**

Para excluir um Acordo, este que deverá estar com Status de cancelado, utilize o botão "Excluir".
