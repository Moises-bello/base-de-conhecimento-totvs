---
article_id: 9550768064919
category: Evento S-2240
content_hash: 4c31b01db2c8ed8a04dd670aeae89eb9987ea152fa57d537baf328b10ac684dc
fetched_at: '2026-06-28T22:45:23.750924+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Quando um funcionário é exposto
  a dois ou mais riscos e um é eliminado, como é comunicado este evento ao Governo
type: support-article
updated_at: '2025-03-11T19:09:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9550768064919-RH-Linha-Protheus-MDT-eSocial-S-2240-Quando-um-funcion%C3%A1rio-%C3%A9-exposto-a-dois-ou-mais-riscos-e-um-%C3%A9-eliminado-como-%C3%A9-comunicado-este-evento-ao-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24789100014871) Tempo aproximado para leitura: **00:08:00 min** **Dúvida**Quando um funcionário é exposto a dois ou mais riscos e um é eliminado, como é comunicado o evento S-2240 ao Governo?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**No momento da eliminação do risco é gerado um novo evento no TAF com a data de eliminação, onde, dentro desse novo evento é possível verificar que um dos riscos permanece ativo. Desta forma é realizado a comunicação da nova condição do Funcionário relacionado ao evento S-2240.  
  
Exemplo:  
Funcionário exposto a dois riscos sendo o Ruído e Radiações.  
  
Demonstração da exposição do Risco - Agente Ruído.  
  
![](https://totvssuporte.zendesk.com/attachments/token/So2NMDsN36DcCXI3rbW8k5szZ/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/wJRUXfk4lOIcDGrUbvERVjugu/?name=image.png)  
  
Demonstração da exposição do Risco - Agente radiação.

![](https://totvssuporte.zendesk.com/attachments/token/sDn51L7vU1iTG5rLtrUvobO5B/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/J4U3aKI1iKmJobSIe3ia1yzRt/?name=image.png)

Visualização dos riscos no TAF. Neste exemplo leve em consideração que, Centralizou no mesmo evento devido a data de ambos riscos serem a mesma.

![](https://totvssuporte.zendesk.com/attachments/token/rwhvMFoV6GpZ038AuFUZcgs8N/?name=image.png)  
  
Será eliminado o Risco - Agente Ruído com data de eliminação (14/10/2022).

![](https://totvssuporte.zendesk.com/attachments/token/7NPXpJ31ueYrQ2SkeG5VY1PeE/?name=image.png)  
  
Neste momento é gerado a informação do evento S-2240 integrado ao TAF.

![](https://totvssuporte.zendesk.com/attachments/token/Ym0xYSbPaTxa0WL5uG3qC98BG/?name=image.png)

Visualização do Risco através do MDT demonstra a legenda (vermelha), ou seja Risco Eliminado.

![](https://totvssuporte.zendesk.com/attachments/token/CwXz1CbvSFvDDvrBBIoS5sjBs/?name=image.png)  
  
Ao conferir a informação no TAF note:  
Gerou um novo evento com a mesma data da eliminação, e neste evento apresenta a nova condição de exposição do funcionário demonstrando apenas o(s) risco ativo. Atendendo assim o cumprimento do MOS.

![](https://totvssuporte.zendesk.com/attachments/token/gr2OuLxwwivkLFI7CcSzRrbSf/?name=image.png)

![](https://totvssuporte.zendesk.com/attachments/token/iywrIFKDkkFr3sioOIDFHc5rc/?name=image.png)

O cenário demonstrado acima é o esperado para comportamento do ERP seguindo as determinações do Governo.  
  
**Saiba Mais**[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Eventos SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
