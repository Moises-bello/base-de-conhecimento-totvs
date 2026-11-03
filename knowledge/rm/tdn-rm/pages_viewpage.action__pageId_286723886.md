---
content_hash: 07d7b3cd9275f587d3cc14028375ee4eb4ea852ac0ab8577119e2d090bb4f2d4
fetched_at: '2026-06-29T00:08:41.367907+00:00'
page_id: '286723886'
product: rm
source: tdn-rm
title: RMCTB00003_Cópia/Atualização do Plano de Contas Paralelo entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286723886
version: 15
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | **Cópia/Atualização do Plano de Contas Paralelo entre Coligadas** |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Este processo tem por objetivo reduzir o trabalho repetitivo de inserção do plano paralelo, bem como realização do mapeamento das contas contábeis com as paralelas, centros de custos e/ou contas gerenciais. Informamos que este processo é uma cópia especificamente entre coligadas e somente irá ter êxito, se forem repeitadas as regras impostas pelo sistema.  ****DESENVOLVIMENTO/PROCEDIMENTO****  1 - Selecione o plano de contas a ser copiado e acesse o processo.  Acesse o Cadastros / Paralelo / Selecione o Plano Paralelo / Processos / Cópia/Atualização do Plano de Contas Paralelo entre Coligadas:  2 - Selecione as opções de acordo com a necessidade da empresa, bem como insira a coligada destino e execute o processo.  Atente-se para as opções que serão marcadas, pois para cada opção marcada deverá respeitar as regras que o próprio sistema informa:  Veja que ao marcar determinadas opções a empresa deverá repeitar determinados quesitos:   * Ao marcar a opção: Copiar mapeamento da Conta Paralela com a Conta Contábil?   A coligada de destino tem que estar parametrizada para visualizar conta global.  Serão copiados somente mapeamentos realizados para as contas contábeis globais.   * Ao marcar a opção: Atualizar Conta(s) Paralela(s) e mapeamento(s) das Contas Contábeis na(s) Coligada(s) de destino?   A coligada de destino tem que estar parametrizada para visualizar conta global.  Serão copiados somente mapeamentos realizados para as contas contábeis globais.  Para atualizar o Plano de Contas Paralelo, o código do Plano de Contas da coligada de origem deve ser deve ser igual ao código do Plano Contas da coligada destino.  As Contas paralelas que existirem na coligada de origem e não existirem na coligada de destino serão removidas no Plano de Contas paralelo da coligada de origem.   * Ao marcar a opção: Copiar/Atualizar mapeamento para o Centro de Custo ou Conta Gerencial?   Poderão ocorrer erros caso o Centro de Custo mapeado não exista na coligada de destino.  3 - Ao final do processo consulte o Log do processo para conferir as alterações efetuadas: |
| **Observações:** |  |
