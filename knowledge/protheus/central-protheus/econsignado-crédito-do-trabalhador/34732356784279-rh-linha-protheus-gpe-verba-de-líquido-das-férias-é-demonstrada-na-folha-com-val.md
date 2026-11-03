---
article_id: 34732356784279
category: eConsignado (Crédito do Trabalhador)
content_hash: ec911df8f1952cbc2c5a7c127695a72662e878c9a1e0ef289cfb534d9307da9f
fetched_at: '2026-06-28T22:43:07.408680+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Verba de líquido das férias é demonstrada na folha
  com valor maior que o calculado no recibo de férias para funcionários que tiveram
  provisão do eConsignado
type: support-article
updated_at: '2025-09-05T19:23:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34732356784279-RH-Linha-Protheus-GPE-Verba-de-l%C3%ADquido-das-f%C3%A9rias-%C3%A9-demonstrada-na-folha-com-valor-maior-que-o-calculado-no-recibo-de-f%C3%A9rias-para-funcion%C3%A1rios-que-tiveram-provis%C3%A3o-do-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34732356762519) Tempo aproximado para leitura: **00:02:30 min**  
  
**Ocorrência**  
Após integração das férias na folha, a verba de líquido das férias é demonstrada com valor maior que o calculado no recibo de férias para funcionários que tiveram provisão do eConsignado  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - A partir da versão 12.1.2210  
  
**Causa**  
O valor do eConsignado provisionado no cálculo das férias, nas verbas com id **1971 - Provisão eConsigado Férias** e **1972 - Provisão eConsignado Férias Mês Seguinte** são somadas na verba de líquido (com i**d 0102**) após a integração do roteiro FER pois **não existe** verba cadastrada com Id de cálculo **1979 - Dev. eConsignado Férias.**  
  
**Solução**  
Para que, no momento da integração do roteiro FER a verba de líquido de férias seja apresentada na folha com o mesmo valor do recibo de férias, será necessário:

1. Ter o **Sistema atualizado** com a **Expedição Contínua do RH** com data **igual ou superior a 05/09/2025**
   1. Versão 12.1.2210 **COM GARANTIA ESTENDIDA SOMENTE**: <https://suporte.totvs.com/portal/p/10098/download?e=1080347>
   2. Versão 12.1.2310 **COM GARANTIA ESTENDIDA SOMENTE**: <https://suporte.totvs.com/portal/p/10098/download#detail/1123885>
   3. Versão 12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>
2. Criar uma nova verba relacionada ao Id de cálculo **1979** - **Dev. eConsignado Férias, sem incidências, não para Emp. Cons., do tipo Desconto / Valor.**
   1. Aba Geral:![](https://centraldeatendimento.totvs.com/hc/article_attachments/34732356763543)
   2. Aba Incidências:  
      ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34732356763927)
3. Cancelar a integração do roteiro FER
   1. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34734304370583)
4. Integrar novamente o roteiro FER
   1. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34734381497239)

Desta forma, o Sistema vai levar para RGB - Lançamentos por funcionário - a verba de líquido das férias (com id 0102) com o mesmo valor calculado nas férias e também apresentará a nova verba relacionada ao id de cálculo 1979 - **Dev. eConsignado Férias com o mesmo valor provisionado nas férias.**

**Exemplo:**

**Cálculo das férias**

* **Provisão do eConsignado** (verba com id 1971 - tipo desconto)**: R$ 4.968,69**
* **Líquido pago nas férias** (verba com id 0102)**: R$ 27.049,30**  
    
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/34734304373527)**

**RGB - Lançamentos por funcionário após integração do roteiro FER**

* **Devolução** da **Provisão do eConsignado nas férias** (verba com id 1973 - tipo provento):R$ 49.68,69
* **Gera** verba de **Contra partida da provisão nas férias** (verba com id 1979 - tipo desconto): R$ 49.68,69
* Demonstra **verba de líquido pago nas férias** (verba com id 0102 - tipo desconto) com **valor igual ao das férias**: **R$ 27.049,30**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34734332952471)

**Saiba Mais**

[Manual Crédito do Trabalhador Protheus - SIGAGPE](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)

[Programa Crédito do Trabalhador - Provisionamento nas Férias e Adiantamento](https://tdn.totvs.com/pages/viewpage.action?pageId=940305598)

[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)

[RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)
