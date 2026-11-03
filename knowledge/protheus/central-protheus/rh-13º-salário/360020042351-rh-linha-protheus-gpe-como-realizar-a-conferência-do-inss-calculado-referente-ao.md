---
article_id: 360020042351
category: RH - 13º salário
content_hash: 467912469156d21db90eef10ce423528eebfec8709165e3e5fd57635f3ca9694
fetched_at: '2026-06-28T22:44:00.718421+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a conferência do INSS calculado referente
  ao Complemento da 2ª parcela de 13º na folha de dezembro
type: support-article
updated_at: '2025-08-13T13:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020042351-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-INSS-calculado-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29275238264855) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**Como realizar a conferência do **INSS** calculado referente ao **Complemento da 2ª parcela de 13º** na folha de dezembro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para calcular o valor do **INSS referente ao Complemento da 2ª parcela do 13º** precisamos primeiro identificar como foi composto o valor do **complemento da 2ª parcela 13º (id 0028)** que é utilizado como **Base do INSS de 13º (id 0019)**:  
  
A partir da verba lançada com incidência para média de 13º após o cálculo e fechamento da 2ª parcela do 13º, este valor será dividido por 12 para se chegar ao valor da média. O resultado desta divisão irá compor os id's 0028 (Diferença 2ª parcela 13º) e 0019 (Base INSS 13º).

Com o valor da base de inss 13º calculado na folha determinado, precisamos localizar o percentual que será utilizado para desconto de INSS 13º. Deve ser utilizado a seguinte fórmula de cálculo:

Valor da verba com id 0019 do cálculo da 2ª parcela do 13º + Valor da verba com id 0019 do cálculo da folha referente ao período de dezembro;  
  
Com o valor obtido no cálculo acima, verificar em qual faixa de INSS se encontra e aplicar o percentual de desconto. Sobre este resultado, subtrair o valor do INSS do 13º que já foi descontado no cálculo da 2ª parcela. A diferença será o valor gravado na verba de INSS 13º (id 0070) na folha.

**Exemplo (verificar a explicação e os valores nos prints):**  
Valor da verba de H.E + Adic Not +DSR (que possui incidência para média de 13º) lançado após o cálculo e fechamento da 2ª parcela do 13º no roteiro FOL: R$ 2.213,09  
Com isso as médias é recalculada e apurado um novo valor de media para pagamento **(este valor será gravado na verba de id 0028 e id 0019)**

**Médias consideradas no calculo da 2° parcela R$ 220,88   
Médias recalculadas na Folha R$ 469,13  
Diferença 13° salario pago na folha R$ 248,25 (469,13 - 220,88)**

* Base INSS 13° + Diferença (4.037,88 + 248,25) = 4.286,13 \* Aliquota = 436,23   
  Inss Atual - Inss 13° = 436,23 - 401,47 = **R$ 34,76 INSS 13°**

 Cálculo da 2ª parcela do 13º

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11117135604119)  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11116650097815)

Cálculo da folha referente ao período de dezembro  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11117263735703)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11117363777943)

**Saiba Mais**  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>

[RH - Linha Protheus - GPE - Cálculo de Complemento de 13º salário na Folha de Dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019750511-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Complemento-de-13%C2%BA-sal%C3%A1rio-na-Folha-de-Dezembro?source=search)  
[RH - Linha Protheus - GPE - É possível calcular a diferença de 13° (id 0028) em outros meses, além do pagamento da folha referente a dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019905131-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-calcular-a-diferen%C3%A7a-de-13-id-0028-em-outros-meses-al%C3%A9m-do-pagamento-da-folha-referente-a-dezembro?source=search)  
[RH - Linha Protheus - GPE - Como realizar a conferência do FGTS calculado referente ao Complemento da 2ª parcela de 13º na folha de dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019820072-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-FGTS-calculado-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro?source=search)  
[RH - Linha Protheus - GPE - Como realizar a conferência do IRRF referente ao Complemento da 2ª parcela de 13º na folha de dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019827572-RH-Linha-Protheus-GPE-Como-realizar-a-confer%C3%AAncia-do-IRRF-referente-ao-Complemento-da-2%C2%AA-parcela-de-13%C2%BA-na-folha-de-dezembro?source=search)
