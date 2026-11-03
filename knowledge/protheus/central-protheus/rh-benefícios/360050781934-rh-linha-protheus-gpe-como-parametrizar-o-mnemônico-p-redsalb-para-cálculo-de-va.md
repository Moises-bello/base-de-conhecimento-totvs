---
article_id: 360050781934
category: RH - Benefícios
content_hash: beef252a6b776a5ba39b211fa26a0443b4d7401e6777fde1bfe484df8983d11b
fetched_at: '2026-06-28T22:44:03.848308+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o mnemônico P_REDSALB para cálculo
  de Vale Transporte
type: support-article
updated_at: '2025-09-26T14:05:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050781934-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-REDSALB-para-c%C3%A1lculo-de-Vale-Transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32696046684183) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como parametrizar o mnemônico P\_REDSALB para cálculo de Vale Transporte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Foi criado o mnemônico **P\_REDSALB** (Considera redução salarial MP 936 p/ cálculo de benefícios?).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11652058776599)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11652122258327)

Ao alterar sua configuração para **.T.**, ou seja, verdadeiro, o sistema irá pesquisar no histórico de contrato do funcionário e na tabela S061 pela redução salarial e irá descontar o valor da redução do salário base do funcionário.

**Exemplo de cálculo**:

* O salário base do funcionário é R$ 2.500,00 e o funcionário está com redução salarial de 50% no mês todo.
* O sistema irá apurar a redução, que no caso é de R$ 1.250,00. O salário base terá os R$ 1.250,00 deduzidos, resultando numa base de R$ 1.250,00.
* Sobre a base reduzida, R$ 1.250,00, será aplicado o percentual de 6% (valor padrão) e então ficará definido que o teto de desconto da parte do funcionário é de R$ 75,00.

**Saiba Mais**[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406270401047-RH-Linha-Protheus-GPE-Como-descontar-valor-Fixo-de-Vale-Transporte?source=search)  
[RH - Linha Protheus - GPE - Pagamento Vale transporte em folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051969333-RH-Linha-Protheus-GPE-Pagamento-Vale-transporte-em-folha-?source=search)  
[RH - Linha Protheus - GPE - Desconto de Vale Transporte para Estagiários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036282453-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-para-Estagi%C3%A1rios?source=search)  
[RH - Linha Protheus - GPE - Como calcular percentual de desconto de Vale transporte inferior a 6% para todos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059488853-RH-Linha-Protheus-GPE-Como-calcular-percentual-de-desconto-de-Vale-transporte-inferior-a-6-para-todos-funcion%C3%A1rios?source=search)
