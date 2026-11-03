---
article_id: 32480529848087
category: eConsignado (Crédito do Trabalhador)
content_hash: 1ebc71580279430135f5575171f0f296a5a920362f6646db44164c07696d9c4e
fetched_at: '2026-06-28T22:43:07.363892+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Provisionamento nas Férias referente ao eConsignado
  (Programa Crédito do Trabalhador)
type: support-article
updated_at: '2026-06-03T16:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32480529848087-RH-Linha-Protheus-GPE-Provisionamento-nas-F%C3%A9rias-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32480537419415)  Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como é feito o provisionamento nas férias referente ao eConsignado.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para realizar o cálculo de férias com o **provisionamento** do empréstimo consignado referente ao programa de Crédito do Trabalhador, siga os passos abaixo:

**1.** Realize a importação da parcela ou realizar o cadastro manual da verba de eConsignado na rotina de valores futuros.   
Exemplo: parcela de R$ 408,60 importada para valores futuros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984157750039)

**2.** Cadastre as verbas de provisionamento de férias, [conforme esta documentação.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34174866521751)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130160279)

3. Durante o cálculo de férias, o sistema **verifica se existe empréstimo consignado** (verba com natureza 9253) lançado para o mês nos valores futuros (SRK). Caso não encontre, será verificado **se existe empréstimo na tabela de Histórico de Importações (RUO)**, com a competência do cálculo de férias.  
  
**Importante:** Foi realizado ajuste na rotina para contemplar os seguintes cenários:

**1. Existência de importação para período futuro na RUO**  
              A rotina passa a verificar se existe recorrência de eConsignado na RUO para o período do cálculo das férias.  
**Caso exista recorrência:**  
                O provisionamento considerará apenas os contratos existentes na RUO.   
                Quando houver importação para período futuro **e esta não for referente ao funcionário**, o empréstimo da tabela **SRK** não será considerado no provisionamento.

**2. Ausência de importação na RUO para período futuro**  
O provisionamento será realizado com base nos contratos ativos da **SRK** (mantendo o comportamento atual).

Se o sistema encontrar o empréstimo em uma das duas tabelas, ele irá gerar o valor como desconto nas verbas de ID **1971** e **1972**, de forma **proporcional à quantidade de dias de férias no mês atual e no mês seguinte.**

O valor descontado será sempre proporcional aos dias de férias. Por exemplo, se a parcela do empréstimo é de R$408,60 (total dos dois emprestimos) e o funcionário tirar 20 dias de férias (de 25/08 a 13/09), será gerado:

* R$95,34 no ID **1971** (referente a Agosto)
* R$177,06 no ID **1972** (referente a Setembro)

**Observação:** A verba de mês seguinte é **opcional**, podendo ser feito todo o processo apenas com a verba do mês.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984157753367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130165271)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130167063)

4. Após integrar o roteiro FER com a folha, são geradas as verbas de férias, 1972 (provisionamento mês seguinte) e 1973 (devolução do provisionamento), sendo valor integral da parcela.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130168343)

A verba de ID 1971 (desconto) será gravada na RGB na verba de ID 1973 (provento), **devolvendo o provisionado nas férias** (valor integral) e possibilitando o desconto do empréstimo na folha, via verba cadastrada nos lançamentos futuros.

O valor da verba 1972 será somado na 1973, mas a 1972 também será enviada para a RGB para conferência, **anulando-se mutuamente.**  
  
**"**No caso de ocorrência simultânea de férias e adiantamento no mesmo período, o valor total provisionado não deve ultrapassar o valor da parcela. Ou seja, se a provisão for realizada integralmente nas férias, não haverá provisão no adiantamento. Caso a provisão nas férias seja parcial, o valor restante será provisionado no adiantamento.  
Importante ressaltar que a provisão deve ser calculada com base nos dias de férias e no percentual do adiantamento, podendo resultar em valores menores que a parcela, mas nunca superiores."  
  
**Com o Novo Id 1979 o Liquido de férias não sofre alteração de valor após ser integrado para a folha de pagamento.**  
**"**A verba 1979 foi criada para possibilitar a contrapartida do provisionamento das férias na folha, sem alteração do liquido. Se ela for criada, será gerada na folha com o valor total do provisionamento, sem alteração do liquido. Caso ela não exista, o sistema continuará ajustando o liquido para realizar a contrapartida."  
  
**5.** No cálculo da folha, será devolvido o valor provisionado nas férias e calculado o desconto, limitado conforme mnemônicos **P\_LIMECONS** e **P\_PERECONS**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130168983)

**Observação:**  
Após o fechamento da folha, a verba 1972 é enviada para o próximo período como provento 1973, efetivando a devolução provisionada para o mês seguinte.

6. Cálculo após o fechamento do período, é gerado o ID 1973 sendo a devolução do valor mês seguinte descontado nas férias;   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34984130171159)  
  
  
No cálculo da folha de pagamento o Sistema utilizará a seguinte fórmula de cálculo para margem:

Verbas de provento com **sim para INSS** + verbas informadas no **P\_ADICONS** - **INSS** - **IR** - verbas de desconto com sim para INSS - verbas informadas no **P\_DEDCONS** \* **percentual** informado no **P\_PERECONS** (se o **P\_LIMECONS = .T.**)  
  
Caso as verbas de férias não estejam nesta composição é necessário adicioná-las no mnemônico **P\_ADICONS conforme documentação:** [RH - Linha Protheus - GPE - Como Incluir outras verbas de Provento na margem de consignação do Programa Crédito Trabalhador eConsignado (MP 1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34816119834519-RH-Linha-Protheus-GPE-Como-Incluir-outras-verbas-de-Provento-na-margem-de-consigna%C3%A7%C3%A3o-do-Programa-Cr%C3%A9dito-Trabalhador-eConsignado-MP-1-292-2025)

**Importante**  
No caso de funcionários que tiveram a migração de empréstimos Consignados para o Crédito do Trabalhador após o cálculo das férias, será necessário **recalcular** as **férias** depois de cadastrar as verbas conforme orientado acima, pois no caso do eConsignado, o desconto **nas férias** não é diretamente realizado como no empréstimo consignado comum: o sistema trabalha com provisionamento nas férias e depois desconto na folha.  
  
Desta forma, os valores descontados serão referente ao provisionamento do eConsignado (verbas com id 1971 e 1972) e o desconto em si será realizado na Folha de Pagamento, conforme previsto na MP 1.292/2025.  
  
**Para um melhor entendimento do processo assista nossos videos HOW TO abaixo:**

**Saiba Mais**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
[Calculo provisionamento deve considerar somente dados da RUO quando o cálculo das férias é referente a períodos seguintes ao da folha em aberto](https://tdn.totvs.com/pages/releaseview.action?pageId=1061159947)
