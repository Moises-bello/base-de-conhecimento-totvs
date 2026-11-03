---
article_id: 360018301831
category: RH - Folha de Pagamento
content_hash: fe8b540ee9439485129ee3c80c1e0c9d773a3bb41a1359366bb381430fb8a0bb
fetched_at: '2026-06-28T22:44:13.405597+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como e para que pode ser utilizado o Roteiro de
  Cálculo VEX - Valores Extras
type: support-article
updated_at: '2024-09-16T18:55:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018301831-RH-Linha-Protheus-GPE-Como-e-para-que-pode-ser-utilizado-o-Roteiro-de-C%C3%A1lculo-VEX-Valores-Extras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15820110347415) Tempo aproximado para leitura:**00:01:00** min**Dúvida**Como e para que pode ser utilizado o Roteiro de Cálculo VEX - Valores Extras?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Foi disponibilizado um novo **roteiro de cálculo** para **Valores Extras (VEX)**permitindo cálculo e pagamento de verbas **extraordinárias lançadas** para o funcionário, possibilitando ainda a geração do arquivo bancário **separado** da folha através da rotina CNAB.

**Parametrizações**

**Verbas:**

Cadastre uma verba utilizando **identificador** **de cálculo** **1411-Liquido Valores Extras**.  
Esta deve ser do tipo **base provento,** onde o campo **Tipo do Cód. (RV\_TIPOCOD)** com **3-Base (Provento)**.  
  
![](http://tdn.totvs.com/download/attachments/244741676/image2016-8-17%2016%3A10%3A58.png?version=1&modificationDate=1471461058000&api=v2)

Esta verba será gerada **após** a **execução** do roteiro de **Cálculo Valores Extras (VEX)** e será utilizada pelas rotinas de **geração** do **CNAB/SISPAG** e **Relação de líquidos.**

Esse identificador de cálculo é obrigatório para geração do CNAB.

A **integração** dos **cálculos feitos** pelo **VEX** podem ser integrados na **folha de pagamento,** desde que o cadastro do **VEX** esteja **parametrizado.** **Integração de Valores Extras (VEX) na Folha de Pagamento (FOL)**

Como padrão o campo **Integra** (RY\_INTEGRA) retorna a configuração **1-Sim**, sendo obrigatório a integração com o roteiro da **Folha de Pagamento** (FOL).

**![](http://tdn.totvs.com/download/attachments/244741676/image2016-8-18%2015%3A14%3A59.png?version=1&modificationDate=1471544099000&api=v2)**

Caso haja alguma particularidade e a verba paga pelo roteiro Valores Extras (VEX) **não** necessite ser demonstrada na Folha de Pagamento, esta configuração poderá ser alterada em **Atualizações > Definições de Cálculo > Roteiros.**  
  
Com a configuração **ativa** para integração do roteiro de Valores Extras **(VEX)** com a folha de pagamento, as verbas **geradas** neste cálculo **deverão** ser cadastradas com **código de verba correspondente** para que o seu valor entre e saia no roteiro da folha de pagamento sem impacto no liquido.  
  
**Verba de Contrapartida**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26292588805271)

**Configuração do Código Correspondente**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26292588806423)

O cálculo do roteiro VEX trata verbas do tipo **Valor** e **Horas** somente.

Os **encargos não serão calculados** nesse roteiro, portanto o cálculo considera seu **valor original** informado no momento do lançamento. Estes serão calculados no roteiro FOL (folha de pagamento) se forem integrados à ele.

Exemplo de lançamento e cálculo do roteiro VEX

**Cadastro de Verbas:**

|  |  |
| --- | --- |
| **Verbas** | **Código Correspondente** |
| 199-Gratificação | 202-Desc. Valores Extras |
| 200-Gratificação Horas | 202-Desc. Valores Extras |

**Feito lançamento por funcionário destas:**

![](http://tdn.totvs.com/download/attachments/244741676/image2016-8-17%2016%3A12%3A5.png?version=1&modificationDate=1471461125000&api=v2)

Cálculo do Roteiro de Cálculo de Valores Extras:

|  |  |  |  |
| --- | --- | --- | --- |
| **Verbas** | **Provento** | **Desconto** | **Base** |
| 199-Gratificação | R$ 100,00 |  |  |
| 200-Gratificação Horas | R$ 169,09 |  |  |
| 325-Líquido Valores Extras |  |  | R$ 269,09 |

![](http://tdn.totvs.com/download/attachments/244741676/image2016-10-13%208%3A44%3A19.png?version=1&modificationDate=1476359057000&api=v2)

**Roteiro de Cálculo da Folha de Pagamento**

|  |  |  |  |
| --- | --- | --- | --- |
| **Verbas** | **Provento** | **Desconto** | **Base** |
| 001-Salário | R$ 1.200,00 |  |  |
| 199-Gratificação | R$ 100,00 |  |  |
| 200-Gratificação Horas | R$ 169,09 |  |  |
| 202-Desc. Valores Extras |  | R$ 269,09 |  |
| 326-Líquido Folha |  |  | R$ 1.200,00 |

\* Não foram considerados bases e impostos. Os valores acima são apenas para demonstrar os valores de proventos e descontos gerados a partir da integração com o cálculo de Valores Extras (VEX)

Verba 202(desconto) foi gerada no cálculo da Folha.

![](http://tdn.totvs.com/download/attachments/244741676/image2016-8-17%2010%3A52%3A21.png?version=1&modificationDate=1471442493000&api=v2)

Quando **integrado** roteiro **VEX** com o roteiro **FOL,** as verbas **pagas** no roteiro **VEX** irão **duas vezes** para os **acumulados (SRD)** após o fechamento.   
Uma por conta do **fechamento** do roteiro **VEX** e outra em virtude do **fechamento** do roteiro **FOL,** sendo essa uma **situação natural.**

**Saiba Mais**

[RH - Linha Protheus - GPE - Como gerar arquivo líquido CNAB do roteiro VEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028792131-RH-Linha-Protheus-GPE-Como-gerar-arquivo-l%C3%ADquido-CNAB-do-roteiro-VEX?source=search)

[RH - Linha Protheus - GPE - Sistema não realiza contabilização do roteiro VEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000127341-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-realiza-contabiliza%C3%A7%C3%A3o-do-roteiro-VEX?source=search)

[RH - Linha Protheus - GPE - Como configurar e conferir um título do Roteiro VEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058130654-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-do-Roteiro-VEX?source=search)

[RH - Linha Protheus - GPE - Roteiro VEX não gera cálculo dos lançamentos fixos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050399114-RH-Linha-Protheus-GPE-Roteiro-VEX-n%C3%A3o-gera-c%C3%A1lculo-dos-lan%C3%A7amentos-fixos?source=search)

[RH - Linha Protheus - GPE - Parametrização quando há mais de um Valores Extras - VEX no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026150892-RH-Linha-Protheus-GPE-Parametriza%C3%A7%C3%A3o-quando-h%C3%A1-mais-de-um-Valores-Extras-VEX-no-m%C3%AAs?source=search)

[RH - Linha Protheus - GPE - Roteiro VEX não é calculado quando lançamento é realizado Por Verba](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060045833-RH-Linha-Protheus-GPE-Roteiro-VEX-n%C3%A3o-%C3%A9-calculado-quando-lan%C3%A7amento-%C3%A9-realizado-Por-Verba?source=search)

[RH - Linha Protheus - GPE - Dissídio retroativo - Roteiro VEX não foi integrado com a folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053219094-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-Roteiro-VEX-n%C3%A3o-foi-integrado-com-a-folha-de-pagamento?source=search)

[RH - Linha Protheus - GPE - É possível calcular separadamente o IRRF de uma verba informada no roteiro VEX e IRRF de folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051442194-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-calcular-separadamente-o-IRRF-de-uma-verba-informada-no-roteiro-VEX-e-IRRF-de-folha?source=search)

[RH - Linha Protheus - GPE - Registros não são gerados na folha de pagamento após a realização da integração do roteiro VEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025549632-RH-Linha-Protheus-GPE-Registros-n%C3%A3o-s%C3%A3o-gerados-na-folha-de-pagamento-ap%C3%B3s-a-realiza%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o-do-roteiro-VEX?source=search)
