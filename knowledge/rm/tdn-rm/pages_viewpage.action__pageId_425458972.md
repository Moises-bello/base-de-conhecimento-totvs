---
content_hash: f9b5aa2cdf5ff5fce937eccdc044314dab0b35fc6a92478cdbcf417da19fa942
fetched_at: '2026-06-29T00:09:33.323404+00:00'
page_id: '425458972'
product: rm
source: tdn-rm
title: Cópia do Plano de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458972
version: 11
---

---

Através deste processo é possível fazer a cópia de planos de pagamento, duplicando-os com a possibilidade de alguns ajustes. Muito utilizado, por exemplo, para copiar o plano de pagamento, com suas parcelas, habilitações e serviços, de um semestre para o outro ou de um período letivo para outro.

O processo de cópia do plano de pagamento está disponível em ***Financeiro/Contábil | Formação de preços | Planos de pagamento | Processos | Cópia de plano de pagamento***.

O processo de cópia será executando considerando o plano de pagamento origem os planos de pagamentos selecionados antes da execução do processo.

No processo de cópia, indique o 'Período destino', para qual o novo plano será copiado e o 'Tipo de vencimento' que deverá ser utilizado para as parcelas.  
  
Em seguida o sistema irá apresentar os dados originais e possibilitará que alguns dados para o destino sejam alterados.  
  
Se desejar, informe na coluna corresponde, novo código, novas datas de validade início e fim, novo nome, nova descrição, nova data de vencimento e nova data de competência para a primeira parcela.

Data de vencimento

A data de vencimento que irá compor o novo plano de pagamento respeitara a informação preenchida no campo “Data de vencimento da primeira parcela”, no entanto para as parcelas seguintes o sistema fara uma correlação com a parcela do plano origem para compor a data de vencimento.

Por exemplo:

**Plano de origem**

Parcela 1 – vencimento 05/01/2017

Parcela 2 – vencimento 10/03/2017

Parcela 3 – vencimento 10/04/2017

Vamos considerar que realizaremos uma cópia do plano de pagamento do exemplo acima, preenchendo a “Data de vencimento da primeira parcela” com “06/01/2018”.

**Teremos após a cópia o novo plano será:**

Parcela 1 – vencimento 06/01/2018

Parcela 2 – vencimento 06/03/2018

Parcela 3 – vencimento 06/04/2018

Observem que o processo de cópia manteve o mês 3 na parcela 2, ou seja, as parcelas seguinte não darão sequência a data inicial informada no processo, mas levará em consideração a data de vencimento da parcela do plano de origem em relação a data inicial, para isso o processo aplicará a seguinte regra ao copiar a parcela 2:

* 1º Identifica quantos meses tem da parcela 1 a 2 no plano de origem

Parcela 2 (10/03/2017) - Parcela 1(05/01/2017) = 2 meses.

* 2º Compõe a data de vencimento da parcela 2, pegando a “Data de vencimento da primeira parcela” informada no processo e acrescenta os 2 meses calculados.

Data de vencimento da primeira parcela = 06/01/2018 + 2 meses = 06/03/2018.

É importante ressaltar que para aplicar a regra acima o sistema considera a ordem por número da parcela e menor data de vencimento entre as parcelas.

Observações

* Se desejar aplicar um reajuste igual para todos os serviços do plano, por exemplo, 10% de acréscimo para todos os serviços, marque a opção 'Replicar reajustes para os serviços' e indique logo em seguida o 'Tipo de reajuste' e o 'Percentual de reajuste'.
* Se desejar aplicar reajustes diferentes para os serviços, deixe a opção 'Replicar reajustes para os serviços' desmarcada. Ao avançar para a próxima etapa do processo, será exibida uma nova tela para que você possa atribuir reajustes distintos para cada serviço do plano.
ATENÇÃO

A partir da **versão 12.1.2506**o processo vai **respeitar o número de casas decimais configurado** no parâmetro "**N° de Casas Decimais**" presente em TOTVS Gestão Educacional → Parâmetros → Integração → Financeiro → Contas a receber → Manutenção de Lançamentos → Lançamento → Opções Gerais.
