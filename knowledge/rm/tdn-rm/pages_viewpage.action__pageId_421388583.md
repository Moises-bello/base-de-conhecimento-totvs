---
content_hash: 0e36d6e44c9967f61c8f3ebb0b12ea4a371b7cbc167d38339528924c354bd915
fetched_at: '2026-06-29T00:09:17.406776+00:00'
page_id: '421388583'
product: rm
source: tdn-rm
title: Liberação de período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388583
version: 6
---

O processo de liberação de período está disponível no Menu: Utilitários | Liberação de período.

**Período Contábil**

Para realizar o processo, o exercício contábil da data definida no Wizard de Liberação deverá estar liberado. O processo será através do Gestão Contábil em Escrituração Contábil | .

Ao executar o processo deverão ser informados os seguintes parâmetros:

"Liberar registros até"

Define até qual data serão liberados os registros. Essa data deverá estar compreendida dentro de um período contábil e o mesmo deverá ter o status = Liberado.

"Somente Autorizados"

Se marcado, só serão liberados os registros que anteriormente forem autorizados pelo processo: Autorizar | Desautorizar liberação nos cadastros de Lançamentos e Extratos de Caixa.

**Observação:** Apenas registros oriundos dos Sistemas: Gestão Financeira, Gestão de Estoque, Compras e Faturamento e Educacional serão liberados. Sendo que os Lançamentos provenientes do Gestão de Estoque, Compras e Faturamento só serão liberados após ser realizada a liberação do movimento.

**Registros**

A liberação dos registros irá ocorrer por processo conforme sequência abaixo, quando atenderem os pré-requisitos:

Faturas e Vencimentos de Fatura:

Faturas de Lançamentos de duplicata baixadas até a data de liberação, sem vínculo com movimento, ou que estejam canceladas.

Acordo Financeiro:

Serão selecionados os lançamentos origem e os gerados pelo acordo. Acordos com os Lançamentos baixados até a data de liberação, sem vínculo com movimento, ou lançamentos cancelados.

Lançamentos que não sejam relacionados a fatura ou acordo:

Lançamentos baixados até a data de liberação, sem vínculo com movimento e/ou fatura, ou cancelados.

Extratos de caixa e registros relacionados:

Extratos compensados ou cancelados. Caso extrato tenha sofrido conciliação bancária, estes registros também deverão ser liberados.

Extratos conciliados com cartão:

Só serão liberados/excluídos os registros cujo os extratos estiverem liberados no período informado no processo.

* Extrato conciliado com cartão;
* Extrato de transferência conta caixa cartão;
* Extrato de depósito no banco;
* Extrato de saque de taxa.

Condições para liberação:

Todos os registros de conciliação devem estar relacionados à extratos que estão sendo liberados.

Extratos relacionados a conciliação que ainda não foi finalizada, ou seja, não tem os respectivos extratos de 'Depósito no banco', 'Transferência conta caixa cartão' e 'Saque de taxa', não devem ser liberados pois a conciliação do cartão ainda está pendente.

**Obs**.: Não é permitido excluir o extrato já conciliado ou gerado por conciliação que não esteja no período liberado.

**Da Liberação**

Registros que possuem data de Contabilização posterior à data de Liberação não serão liberados.

No momento da execução da Liberação do Período será validado em cada processo se todos os registros foram liberados, caso não ocorra a liberação de algum registro não será realizado por completo. Para aquele processo os demais registros liberados com sucesso não serão liberados até a correção da pendência do registro com divergência.

Será apresentado log separado por processo e as operações realizadas.
