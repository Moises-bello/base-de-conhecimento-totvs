---
content_hash: 472c0a7510dcfbb3cb4c2b7e578a75e5f2e596f40a5363c7d2aa97087cfa50e5
fetched_at: '2026-06-29T00:09:32.451772+00:00'
page_id: '425458851'
product: rm
source: tdn-rm
title: Incluir / Excluir Bolsa Retroativa - Alterando o lançamento original
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458851
version: 9
---

---

**Inclusão de Bolsa**Processo automático para fazer os seguintes passos:   
- Cancela a baixa, considerando que a baixa pode ter sido parcial.   
- Insere a bolsa para o aluno.   
- Regera os lançamentos (serão regerados todas as parcelas já geradas anteriormente, inclusive as que não foram baixadas, considerando o novo valor da bolsa)   
- Baixa os lançamentos utilizando o processo padrão de baixa (preenchendo o pagamento a maior com o valor da bolsa). O valor da bolsa estará no valor opcional parametrizado, porém, como o aluno já pagou, este valor a maior também será incluído no campo destinado à conta corrente, pois somente assim conseguiremos incluir este valor na próxima parcela a ser gerada.   
- Insere um registro de crédito na conta corrente do aluno no valor da bolsa.

Observação: se a contabilização já foi exportada para o TOTVS Gestão Contábil, deverá ser feito o estorno antes da execução desse processo. Se o período já foi fechado no RM Saldus, o sistema avisará e não permitirá a execução do processo neste período. Com relação ao período da competência definido no TOTVS Educacional, deverá ser feito um estorno manual de um ou mais meses.

**Exclusão de Bolsa**  
Processo automático para fazer os seguintes passos:   
- Cancela a baixa - Cancela a bolsa do aluno   
- Regera o lançamento   
- Faz uma baixa parcial nos lançamentos ou baixa o lançamentos preenchendo o pagamento a menor com o valor da bolsa. Se o valor opcional de pagamento a menor não for informado, será feita uma baixa parcial, caso contrário será utilizada a conta corrente.   
- Se a opção selecionada for um pagamento a menor, insere um registro de débito na conta corrente do aluno que poderá ser cobrado integralmente no próximo lançamento gerado (pagamento a menor), ou se aluno não tiver mais parcelas não geradas, pode-se usar o processo de aproveitamento de valores em conta corrente.

Observação: se a contabilização já foi exportada para o Totvs Gestão Contábil, deverá ser feito o estorno antes da execução desse processo.

**Atenção:**Ao realizar a inclusão ou exclusão de uma bolsa retroativa o sistema altera o lançamento financeiro no qual a bolsa está sendo incluída ou excluída, regerando-o.

Para os casos em que o status do boleto deste lançamento seja igual a **'Remetido'** ou **'Registrado'**, a inclusão ou exclusão de bolsa retroativa para este lançamento somente será permitida se o parâmetro do sistema **'Cancelar remessa automaticamente ao regerar o lançamento financeiro quando boleto estiver com status Remetido ou Registrado'** estiver marcado, pois como haverá mudança de valores, a remessa do boleto original precisará ser cancelada.

Para os casos em que o lançamento esteja baixado e com extrato agrupado, não será possível a inclusão da bolsa retroativa, pois o sistema não tem autonomia para refazer o agrupamento dos extratos após a inclusão da bolsa retroativa, devido limitações quanto a forma de pagamento e quanto a baixas parciais. Ou seja, para alguns casos, o sistema não conseguiria refazer o agrupamento, mantendo o extrato da forma como o agrupamento foi aplicado originalmente. Para estes casos será necessário que o cancelamento da baixa seja feito manualmente.

Para maiores informações consulte o link com as regras para .  
   
**Importante:** Ao incluir ou excluir uma bolsa retroativa o sistema altera o lançamento financeiro, incluído o valor da respectiva bolsa no campo de **Valor Opcional** ou no campo de **Valor de Integração** parametrizado para armazenar o valor (Bolsa Condicional e Bolsa Incondicional), se o lançamento estiver baixado o valor recebido da bolsa também é lançado no campo parametrizado para registrar Pagamento a menor ou Pagamento a maior (dependendo da operação: inclusão ou exclusão) e dependendo da parametrização este valor vai ser transportado para a conta corrente do aluno.   
É importante observar, então, a parametrização utilizada para armazenar estes valores que pode ser Valor Opcional ou Valor de Integração (*Ambiente | Parâmetros | Educacional | Integração | Financeiro | Educacional)*, mas o controle dos valores, independentemente se lançados em Valor Opcional ou Valor de Integração será feito igualmente.  
 

   Recursos Adicionais

---
