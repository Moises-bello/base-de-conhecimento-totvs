---
article_id: 360058213814
category: RH - Rescisão
content_hash: 8bd8dc3ab3e4cd86f4186fab3a89c8e290c69b640f29ef4d431c0ca96cad1bf7
fetched_at: '2026-06-28T22:43:48.331785+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Como calcular rescisão com data retroativa
type: support-article
updated_at: '2025-05-07T21:16:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058213814-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-com-data-retroativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19195278608023) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como calcular rescisão com data retroativa?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para calcular rescisão com data retroativa ao período em aberto, siga os passos abaixo:  
  
No Configurador, pelo caminho **>Ambiente >Cadastros >Parâmetros**, altere o parâmetro **MV\_MDDTDEM** para S.  
  
Na rotina de Rescisão, pelo caminho **>Miscelânea >Cálculos >Rescisão**, calcule a rescisão do funcionário com data de demissão dentro do período em aberto conforme exemplo abaixo:

Período em aberto 06/2023  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19436664773911)  
  
Cálculo da rescisão original com data de demissão em 06/2023 calculada e gravada:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19436682283415)  
  
Após gravar a rescisão original, calcule a rescisão **complementar**, e no campo Dt. Demissão altere a data de demissão de acordo com a necessidade de cálculo, no teste abaixo alterei para 04/2023.  
**IMPORTANTE:** O campo Data Geração deve obrigatoriamente ser do período em aberto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19436731904279)  
  
Sistema altera a data de demissão na rotina de Funcionários também:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19436682304791)  
  
**OBSERVAÇÃO**: Se for necessário esse cálculo por decisões judiciais com valores pré determinados que serão lançados manualmente, na rescisão original, utilize um tipo de rescisão com valores zerados.

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Por que não é possível editar data de demissão em rescisão complementar mesmo com o parâmetro MV\_MDDTDEM = S](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411589885335-RH-Linha-Protheus-GPE-Como-alterar-a-data-de-demiss%C3%A3o-na-rescis%C3%A3o-complementar-usando-o-par%C3%A2metro-MV-MDDTDEM-?source=search)

[RH - Linha Protheus - GPE - Como calcular uma rescisão com valores zerados (Acordo Judicial) rescisão indireta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555492)
