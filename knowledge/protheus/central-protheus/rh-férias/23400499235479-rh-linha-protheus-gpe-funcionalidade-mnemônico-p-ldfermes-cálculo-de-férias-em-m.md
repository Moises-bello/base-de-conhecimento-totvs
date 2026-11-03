---
article_id: 23400499235479
category: RH - Férias
content_hash: 6a748e41f31b4d70d124218930435a9efb98690b2c9575b35969c3c18d3c6b53
fetched_at: '2026-06-28T22:43:58.280150+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade mnemônico P_LDFERMES (Cálculo de
  Férias em meses de 31 dias)
type: support-article
updated_at: '2025-09-02T18:02:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23400499235479-RH-Linha-Protheus-GPE-Funcionalidade-mnem%C3%B4nico-P-LDFERMES-C%C3%A1lculo-de-F%C3%A9rias-em-meses-de-31-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23400499219991) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Funcionalidade do mnemônico **P\_LDFERMES** para o cálculo de Férias em meses de 31 dias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Foi criado o mnemônico **P\_LDFERMES**, cujo **conteúdo padrão é .F.,** o que mantém o sistema **respeitando o cadastro de períodos,** ou seja, caso o período esteja definido para **calcular sempre por 30 dias** (MV\_DIASPER = 2), todos os cálculos de Férias irão utilizar como base 30 dias, e caso o Funcionário fique 30 dias de Férias dentro do mês, **todo o salário será pago como Férias**, não gerando a verba de salário da Folha.  
  
Caso o mnemônico seja alterado para **.T.**, em meses com 31 dias, o cálculo de Férias, bem como o de Folha, **serão efetuados considerando a quantidade de dias do mês.****Importante:**Quando o mnemônico for alterado para .T., todas as **Férias** que já tenham sido calculadas **deverão ser recalculadas**, do contrário, a Folha irá gerar um dia de salário indevido.  
No caso de férias partidas que foram calculadas com o mnemônico desativado, **recomenda-se a desativação do mnemônico** para calcular a Folha do Funcionário, para que o salário seja calculado com o mesmo divisor das Férias.  
  
  
**Saiba Mais:**[Cálculo de férias em meses com 31 dias](https://tdn.totvs.com/pages/viewpage.action?pageId=825319706)[RH - Linha Protheus - GPE - Como configurar o parâmetro MV\_DIASPER para definir regra de calculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059317953-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-DIASPER-para-definir-regra-de-calculo)  
[RH - Linha Protheus - GPE - Férias Proporcionais dividindo por 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003366622-RH-Linha-Protheus-GPE-F%C3%A9rias-Proporcionais-dividindo-por-31-dias)  
[RH - Linha Protheus - GPE- A verba de média das férias está calculando por 30 dias em meses com 31 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410815803287-RH-Linha-Protheus-GPE-A-verba-de-m%C3%A9dia-das-f%C3%A9rias-est%C3%A1-calculando-por-30-dias-em-meses-com-31-dias)
