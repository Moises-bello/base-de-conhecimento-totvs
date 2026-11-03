---
article_id: 33045059652631
category: eConsignado (Crédito do Trabalhador)
content_hash: 4aed6b49ac0960545e74997ec705f785db3101b0c9ce76c1b304c05a7a990b1c
fetched_at: '2026-06-28T22:43:07.172184+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE -  Verba de Pagamento de Adiantamento é gerada em
  Lançamentos por Funcionário indevidamente com o mesmo valor provisionado do eConsignado
type: support-article
updated_at: '2025-07-24T14:48:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33045059652631-RH-Linha-Protheus-GPE-Verba-de-Pagamento-de-Adiantamento-%C3%A9-gerada-em-Lan%C3%A7amentos-por-Funcion%C3%A1rio-indevidamente-com-o-mesmo-valor-provisionado-do-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33045059620247) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
Após o fechamento do roteiro ADI - Adiantamento, a verba de **provento de adiantamento**, relacionado ao id de cálculo **0006**, é gravada na **RGB - Lançamentos por Funcionário** com o **mesmo** valor de **provisionamento** do eConsignado realizado no Adiantamento indevidamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33045059623959)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - A partir da versão 12  
  
**Causa**  
Este erro pode acontecer devido a **configuração incorreta das verbas** de provisionamento do eConsignado ou quando o **mnemônico P\_PROVADIF** está habilitado.  
  
**Solução**  
Para que o Sistema **não gere o id de cálculo 0006** na RGB quando o roteiro ADI for fechado, as **verbas de provisão relacionadas aos id's de cálculo 1974 e 1975** devem estar com **não** no campo **Ref. Adiant.**, localizado na aba incidências, conforme artigo [RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33045035437847)  
  
E o **mnemônico P\_PROVADIF** deve estar com conteúdo **.F.**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33045035438999)  
  
Para ajuste, será necessário **excluir** a verba com **id 0006 da RGB - Lançamentos por Funcionário**, antes de calcular a folha.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33045035440407)  
  
Cálculo da folha  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33045035441175)

**Para maior conhecimento assista os videos How To abaixo:**

**Saiba Mais**  
[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)
