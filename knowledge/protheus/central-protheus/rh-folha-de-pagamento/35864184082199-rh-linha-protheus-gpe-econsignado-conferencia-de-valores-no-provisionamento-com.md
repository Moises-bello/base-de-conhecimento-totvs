---
article_id: 35864184082199
category: RH - Folha de Pagamento
content_hash: 366e92f46661e4aeb136cc918e6fbab8fdd4e86774bdf342f2867ff7862922f6
fetched_at: '2026-06-28T22:44:17.142283+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - eConsignado - Conferencia de Valores no Provisionamento
  com Férias Partidas
type: support-article
updated_at: '2025-11-12T19:02:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35864184082199-RH-Linha-Protheus-GPE-eConsignado-Conferencia-de-Valores-no-Provisionamento-com-F%C3%A9rias-Partidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35864199992599) Tempo aproximado para leitura: 00**:10:00 min**  
  
**Dúvida**  
Como conferir os valores do eConsignado com e sem o ID 1972 (Provisionamento Férias Mês Seguinte) em casos de Férias Partidas  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**

1ª cenário com ID 1972 (Prov Mes Seguinte)

**Valores SRK (Valores Futuros)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865016422295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865016424599)

Verbas utilizadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865016426263)

 Realizar o Calculo de Férias Partidas com o ID 1972 (Opcional) - Provisionamento Férias Mês Seguinte

Foi gerado a A02 (Reserva)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35864994134679)

2.  Após integrar o roteiro FER com a folha, será possível antes do calculo visualizar as verbas que foram levadas para RGB e será mostrado em folha, destaque para a origem delas e a verba A16 - ID 1979 mantendo o liquido das férias intacto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865650869399)

3. Recibo de Pagamento calculo de folha 10/2025. Note que de fato o único desconto que esta tendo em folha é da verba 432 - Empréstimo Consignado enquanto a A16 traz o que foi provisionado nas férias como demonstrativo para não mexer mais no liquido e gera a A03 (Provisionamento Mês Seguinte) que será devolvido no próximo periodo

No calculo da folha a A02 vira a A16 e gera a A04 como provento, se anulando para assim no calculo conseguir descontar a verba principal 432 e dessa forma não gerar insuficiência de saldo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865650872215)

**Importante**

Note que, embora essas verbas sejam de desconto e provento, na prática nenhum desconto é efetivamente efetuado. O que é feito é uma reserva de valor, que será descontado no cálculo de férias, e posteriormente este valor é devolvido no cálculo de folha, unicamente para viabilizar o desconto efetivo do empréstimo.

**Explicação do funcionamento da verba de ID 1972(Provisão eConsignado Férias Mês Seguinte)**  
  
No caso de férias partidas quando existe o ID 1972(Provisão eConsignado Férias Mês Seguinte), após realizar a integração das férias com a folha será gerado para RGB(Lançamentos do Funcionário) este mesmo ID e no cálculo da folha calculado como desconto.  
  
Entretanto, o ID 1972 NÃO será descontado duas vezes, observe no exemplo dos prints acima que este não é descontado novamente do líquido das férias e nem devolvido o valor para o líquido, conforme é feito com a verba de provisionamento mês ID 1971, ficando pendente APENAS a devolução descontado no ID 1972 nas férias, essa que será calculada como provento no mês seguinte.

**OBS: A verba de mês seguinte é opcional, podendo ser feito todo o processo apenas com a verba do mês.**

4. Recibo do pagamento do calculo folha periodo seguinte 11/2025 devolvendo o valor do mês seguinte e descontando na 432 a parcela atual do empréstimo consignado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865818914327)

2ª Cenário sem ID 1972 (Prov. Mês Seguinte)

1.Realizado calculo de férias partidas sem o ID 1972 de Provisionamento de Mês Seguinte

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36064051471383)

2.  Após integrar o roteiro FER com a folha, será possível antes do calculo visualizar as verbas que foram levadas para RGB e será mostrado em folha, destaque para a origem delas (K) e a verba A16 - ID 1979 mantendo o liquido das férias intacto e nesse caso sem a verba com ID 1972(Provisionamento de Férias), ou seja, tudo será provisionado no periodo "atual"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36064051474455)

3. Recibo de Pagamento do calculo de folha 11/2025 - Note que de fato o único desconto que esta tendo em folha é da verba 432 - Empréstimo Consignado enquanto a A16 traz o que foi provisionado nas férias como demonstrativo para não mexer mais no liquido e gera a A04 que é o provento do provisionamento de férias.

Verbas A04 e A16 se anulam, gerando apenas o desconto do consignado 432.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36064513377687)

Obs: Origem das verbas para um melhor entendimento das origens que transitam entre férias e folha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36064303133847)

Documento explicando origem das verbas: [RH - Linha Protheus - GPE - Como identificar a origem das verbas no cálculo mensal do funcionário – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026973572-RH-Linha-Protheus-GPE-Como-identificar-a-origem-das-verbas-no-c%C3%A1lculo-mensal-do-funcion%C3%A1rio)

Documento sobre o ID 1979 para manter o liquido gerado nas férias: [DT Programa Crédito do Trabalhador - Provisionamento nas Férias e Adiantamento - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=940305598)
