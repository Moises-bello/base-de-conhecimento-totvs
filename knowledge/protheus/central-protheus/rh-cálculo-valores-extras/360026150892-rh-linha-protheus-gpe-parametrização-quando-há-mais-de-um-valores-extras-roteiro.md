---
article_id: 360026150892
category: RH - Cálculo Valores Extras
content_hash: 33c5f3ed16ceba9529ee4e6f1ef9d553d7539e2007f3e8b81048c512f902938c
fetched_at: '2026-06-28T22:43:12.231391+00:00'
product: protheus
section_id: 360011983433
source: central-protheus
title: RH - Linha Protheus - GPE - Parametrização quando há mais de um Valores Extras
  - Roteiro VEX no mês
type: support-article
updated_at: '2025-10-17T11:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026150892-RH-Linha-Protheus-GPE-Parametriza%C3%A7%C3%A3o-quando-h%C3%A1-mais-de-um-Valores-Extras-Roteiro-VEX-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676702336023)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Parametrização quando existe o cálculo de mais de um roteiro VEX com integração no mês  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - A partir da versão 12  
  
**Solução**Hoje já possuímos um documento explicando como parametrizar as verbas para cálculo de valores extras e integração com a folha de pagamento.

Descrito no link: [Roteiro Valores Extras](http://tdn.totvs.com/display/PROT/TVVSDA_DT_Roteiro_Valores_Extras)

Mas caso tenha a necessidade de ser calculado mais de um VEX no mês deve-se seguir as orientações abaixo para que todos os números de pagamentos criados com o Roteiro VEX integrem para o roteiro FOL cujo cadastro está no número de pagamento 01.

- Cadastro de verbas utilizadas no processo já com suas verbas de descontos amarradas no campo Cod. Corresp. das verbas de proventos que deseja lançar no Roteiro VEX em **Atualizações > Definições de verbas > Verbas (GPEA040)**;![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625111)

- Criar o Período no cadastro de períodos normalmente apenas se atentando na data de pagamento informada no Roteiro VEX que no caso é o dia que irá efetuar o pagamento do mesmo, em **Atualizações > Definições de Cálculos > Períodos (GPEA400)**;![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025610232)

- Na RGB em **Atualizações > Lançamentos > Por Funcionários (GPEA580)** lance a verba que deseja efetuar o pagamento no Roteiro VEX e calcule:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625391)

- Após conferido os valores, efetue o procedimento de Integração com o Roteiro FOL. Em **Miscelânea > Cálculos > Integrações (GPEM019)**. (Observe que sempre será integrado com o FOL do número de pagamento 01):![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625551)

- RGB após integração do Roteiro VEX os valores serão apresentados no roteiro FOL, em **Atualizações > Lançamentos > Por Funcionários (GPEA580)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025610632)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025610712)

- Após conferência e integrada para a folha foi executado o fechamento do Roteiro VEX e criado um novo período em **Atualizações > Definições de Cálculos > Períodos (GPEA400)** com diferente número de pagamento para o roteiro VEX com data de pagamento diferente.

**OBSERVAÇÃO: Todo número de pagamento criado do Roteiro VEX independente da quantidade no mês, sempre deverá ser cadastrado no cabeçalho do cadastro de período - Data Inicial e Final o primeiro dia do mês e o ultimo dia do mês, o que mudará é somente a data de pagamento do roteiro VEX:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025610832)

- Lance a Verba desejada no Roteiro VEX – 02 em **Atualizações > Lançamentos > Por Funcionários (GPEA580)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625851)

- Após lançamento efetue o calculo do roteiro VEX, faça a conferência, integre e feche o roteiro normalmente.  
- RGB após integração VEX – 02 visualizado em **Atualizações > Lançamentos > Por Funcionários (GPEA580)**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025611492)

-Realizado mais um cadastro de Roteiro VEX no período para demonstração, agora com o número de pagamento 03 em **Atualizações > Definições de Cálculos > Períodos (GPEA400)**;![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025611552)

- Lançada a verba no Roteiro VEX para cálculo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025626391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025611612)

-Após efetuado o cálculo, e integrado para o roteiro FOL, a RGB será apresentada todas as verbas lançadas e integradas conforme exemplo abaixo:![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025611792)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025611812)

Observe que toda vez que é utilizado o pagamento da mesma verba em número de pagamentos diferentes na RGB é gerado Sequencia de Verba para distinguir os lançamentos;

- Efetue então o cálculo da Folha de pagamento 03/2019 em **Miscelânea > Cálculos > Por Roteiro (GPEM020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025612012)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025626571)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025626651)

As verbas são apresentadas separadamente na folha, somente as que tem mais de um lançamento são somadas, tanto nos proventos quanto nos descontos, porém na verba de líquido  (ID 1411) é a somatória de todas as verbas do Roteiro VEX.

**OBS.: A verba utilizada como contrapartida do VEX, não pode ser utilizada no calculo da Folha quando nessa mesma competência ocorrer calculo do Roteiro VEX, pois o sistema prioriza a verba com origem I, sendo assim, a verba do VEX com origem C será sobreposta caso a mesma verba seja informada com um valor diferente.   
<https://tdn.totvs.com/pages/releaseview.action?pageId=447094830>**

**Saiba Mais:**

[Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)
