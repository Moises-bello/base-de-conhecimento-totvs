---
article_id: 16110041641623
category: RH - Férias
content_hash: 3e1cf04f9e54785ce7f6bc601e1c7696602aaed07bbc8de04551c8c79ee8c248
fetched_at: '2026-06-28T22:43:57.959794+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Atualização dos períodos aquisitivos quando há
  afastamento sem data de retorno
type: support-article
updated_at: '2025-08-28T14:41:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16110041641623-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-dos-per%C3%ADodos-aquisitivos-quando-h%C3%A1-afastamento-sem-data-de-retorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16110050080279) Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Como o Protheus atualiza os Períodos Aquisitivos quando há Afastamento sem data de Retorno?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Caso o afastamento do funcionário não possua data de retorno, ao realizar o fechamento mensal da Folha:

>Períodos Ativos: Será mantida a contagem dos avos de direito de Férias, de Acordo com a Configuração do campo "Tip. Aus. Feri" (RCM\_FERIAS) no Cadastro do Tipo de Ausência (GPEA430).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31726213582743)

**1 - Perde Após 180 dias:** ao atingir a contagem de 180 dias de afastamento desconsiderando os dias que são pagos pela empresa, o Período Aquisitivo Ativo será atualizado como Prescrito.

**2 - Suspensão do Período:** O Período Aquisitivo fica Congelado, e ao informar a data Fim, os dias de Afastamento serão somados ao Final do Período Aquisitivo.

**3 - Perde Após 30 dias:** Ao atingir a contagem de 30 dias de afastamento, o Período Aquisitivo Ativo será atualizado como Prescrito.

**4 - Não Perde:** O Funcionário garante direito ao período Aquisitivo de Férias e o afastamento não terá impacto

Nos casos de afastamentos por Doença/Acidente superiores a 180 dias, o novo período aquisitivo se inicia no dia seguinte ao retorno do afastamento, portanto somente serão criados novos períodos aquisitivos após a inclusão da Data Fim do Afastamento do Funcionário.  
  
**Exemplo**:  
Funcionário Afastado por Doença à partir de 25/09/2022 sem data de Retorno.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109546895255)

Desconsiderando os 15 primeiros dias de afastamento que foram pagos pela empresa, do início do afastamento até o último dia do período aquisitivo (06/04/2023), são 179 dias de afastamento, portanto o Período Aquisitivo fica Ativo, e o próximo período será criado apenas quando for informada a data de retorno do afastamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16109632708247)

**Saiba Mais**[Como o sistema efetua a atualização de períodos no fechamento quando há afastamento sem data de retorno?](https://tdn.totvs.com/pages/viewpage.action?pageId=721016068)  
[RH - Linha Protheus - GPE - Como Funciona a Rotina Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015671131-RH-Linha-Protheus-GPE-Como-Funciona-a-Rotina-Controle-de-Dias-de-Direito)  
[RH - Linha Protheus - GPE - Tolerância de afastamento informada através do campo RCM\_DIASFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016555092-RH-Linha-Protheus-GPE-Toler%C3%A2ncia-de-afastamento-informada-atrav%C3%A9s-do-campo-RCM-DIASFE)  
[RH - Linha Protheus - GPE - Após fechamento da folha, sistema gera período aquisitivo desde admissão do funcionário com status Ativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015471312-RH-Linha-Protheus-GPE-Ap%C3%B3s-fechamento-da-folha-sistema-gera-per%C3%ADodo-aquisitivo-desde-admiss%C3%A3o-do-funcion%C3%A1rio-com-status-Ativo)
