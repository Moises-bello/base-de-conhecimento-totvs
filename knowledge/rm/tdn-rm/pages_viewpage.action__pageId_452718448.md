---
content_hash: ff48571ca15a0ee15866d84127f4bb206b6e1a260e7543b9ac87c178fae45a8b
fetched_at: '2026-06-29T00:09:59.926610+00:00'
page_id: '452718448'
product: rm
source: tdn-rm
title: Controle de faltas para cálculo de avos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718448
version: 7
---

Este cadastrado tem o objetivo de considerar o dia efetivo da falta no cálculo dos avos de férias e 13º salário, tendo como beneficio:

* Calcular os avos de férias verificando as faltas do primeiro ao último dia do período aquisitivo;
* Considerar corretamente a quantidade de dias de faltas para o funcionário que tem jornada diária diferenciada, e o cliente utiliza o evento do tipo hora no desconto da falta no envelope de pagamento;
* Visualizar detalhadamente os dias das faltas de cada funcionário.
* Estornar o dia real da falta indevida.

Através deste anexo será possível incluir/alterar/excluir as faltas. O cálculo dos avos de 13º salário e férias irá considerar estas faltas a partir da data informada no parâmetro 'Utiliza controle de faltas para cálculo de avos' e a desconsiderar os CC8 e CC128.

**Observações:**

1. 1. Este anexo somente estará disponível quando o parâmetro [Controle de Faltas para Cálculo de Avos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020486611) existente em Configurações | Parametrizador | Folha de Pagamento | Folha Normal estiver marcado.
   2. Sempre que for incluída uma falta com a mesma data de uma falta já existente, o sistema irá acrescentar 10 minutos na hora da data, semelhante ao histórico salarial.
   3. Quando a falta não estiver bloqueada, e o usuário fizer alteração manual e processar novamente o lançamento através do Automação de Ponto, às alterações manuais serão perdidas.

**Abonar Falta**

Este flag quando marcado, irá desconsiderar a falta para perda de avos de Férias e 13 Salário.

**Fração Dia de Falta**

Cada dia de falta cadastrado no anexo do funcionário será multiplicado pelo número informado no campo "Fração dia de falta".

Exemplo

Falta registrada nos dias 04 a 08/01 (segunda a sexta) – 5 dias de faltas, mas o funcionário trabalha o sábado nesses dias de semana, ou seja, a cada dia o funcionário trabalha 1,2 dia para compensar o sábado.

No anexo de controle de faltas do cadastro de funcionários, no campo “Fração dia de falta” deve ser cadastrado a fração de falta a que se refere o dia.

No exemplo acima ficaria

04/01 = 1,2 Fração dia de falta

05/01 = 1,2 Fração dia de falta

06/01 = 1,2 Fração dia de falta

07/01 = 1,2 Fração dia de falta

08/01 = 1,2 Fração dia de falta

**Total = 6 dias de faltas (Nesse caso perderia dias de direito de férias de 30 dias para 24 dias)**

Caso o parâmetro seja desmarcado será contado para cada registro 1 dia de falta, mesmo que o cadastro esteja com a fração.

No exemplo acima ficaria

04/01 = 1 dia de falta

05/01 = 1 dia de falta

06/01 = 1 dia de falta

07/01 = 1 dia de falta

08/01 = 1 dia de falta

**Total = 5 dias de faltas (Nesse caso não perderia dias de direito de férias)**

**Desconsidera para Férias**

Este campo ainda não tem funcionalidade, podendo ser utilizado pelos clientes para customizar através de fórmulas visuais caso queira desconsiderar as faltas somente para Férias. Caso queira desconsiderar a falta de forma automática, deve marcar a opção 'Abonar Falta'

**Desconsidera para 13º Salário**

Este campo ainda não tem funcionalidade, podendo ser utilizado pelos clientes para customizar através de fórmulas visuais caso queira desconsiderar as faltas somente para 13º Salário. Caso queira desconsiderar a falta de forma automática, deve marcar a opção 'Abonar Falta'

**Desconta DSR**

Este campo estará disponível quando o parâmetro **C******ontrole de faltas através do Automação de Ponto**** existente em **Configurações | Parametrizador | Folha Normal | Controle Faltas.**

Este campo estará disponível apenas para consulta e será preenchido pelo processo de Lançamento do Movimento do ponto para a Folha. 

Este campo será utilizado na folha agrária para descontar ou não o DSR.

Funcionários
