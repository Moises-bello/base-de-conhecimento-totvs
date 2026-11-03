---
article_id: 40104472104983
category: Férias
content_hash: 9af9da9ec56a060948905a419f97f7c5b2dc65709c257b2333b7945d83c97c95
fetched_at: '2026-06-28T22:46:56.122579+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Cálculo e conferência de médias nas férias'
type: support-article
updated_at: '2026-04-29T19:18:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40104472104983-RH-RM-FOP-F%C3%A9rias-C%C3%A1lculo-e-confer%C3%AAncia-de-m%C3%A9dias-nas-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40104493862935) Tempo aproximado para leitura: 00**:02:31 min**  
  
**Dúvida:**  
Como realizar a conferência e entender o cálculo de médias de férias no sistema RM Folha de Pagamento?  
  
**Ambiente:**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução:**

O cálculo de médias de férias é realizado com base nas configurações do Sindicato do funcionário e nos valores/horas acumulados no período aquisitivo ou conforme o período de médias definido nos parâmetros. No log de processo de médias, o sistema detalha os valores encontrados mês a mês para cada evento configurado para compor a média.

Para a conferência, deve-se observar:  
  
**Parâmetros do Sindicato**: O sistema valida o tipo de média (Valor, Hora ou Referência), se considera o mês atual e se há correções salariais.

**Período de Apuração**: Geralmente compreende os meses do período aquisitivo, conforme demonstrado no log.

**Composição por Grupos**: Os eventos são separados por grupos (Ex: Grupo 2 para Comissões).

**Cálculo Aritmético**: Soma-se o total acumulado do evento no período e divide-se pelo número de meses (divisor) configurado ou correspondente ao período.  
  
**Passos:**  
  
1. Acesse o cadastro do Sindicato em **Administração de Pessoal |** **Sindicatos** e verifique na aba **Férias | Média de Férias** as regras de cálculo para Férias;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104493864471)

2. No Log de Médias, identifique o **Período a ser considerado** (ex: 03/2025 a 02/2026);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104493866263)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104493866903)

3. Verifique o **Grupo** e o **Evento** (ex: 0084 - COMISSAO) que está sendo apurado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104493869591)

4. Confirme a soma dos valores mensais listados no log e a divisão efetuada (ex: Total 2.400,00 / 12 meses = 200,00).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104472063255)

5. O resultado final da média será somado ao Salário Base para compor a remuneração de férias do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40104472064791)

**Saiba Mais:**  
  
[RH - RM - FOP - Médias: cálculo e discriminação de médias de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015334532-RH-RM-FOP-M%C3%A9dias-c%C3%A1lculo-e-discrimina%C3%A7%C3%A3o-de-m%C3%A9dias-de-f%C3%A9rias)  
[RH - RM - FOP - Parametrização: Média Férias discriminado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5819565371287-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-M%C3%A9dia-F%C3%A9rias-discriminado?source=search)
