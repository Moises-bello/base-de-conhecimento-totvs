---
article_id: 12267100072727
category: Rescisão
content_hash: d343ae28ea0d6d95b76009d0a32b29122d0e8f9f6625cf8338d0befac4f580ac
fetched_at: '2026-06-28T22:46:54.285418+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: FGTS mês anterior'
type: support-article
updated_at: '2024-06-20T22:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12267100072727-RH-RM-FOP-GRRF-FGTS-m%C3%AAs-anterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:30 min****Ocorrência**  
Ao realizar a geração da GRRF, o FGTS do mês anterior está sendo levado para o arquivo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Este processo ocorre pois ao calcular a rescisão a seguinte flag está marcada:  
  
![](https://totvssuporte.zendesk.com/attachments/token/FPc0lnPj5btWL8ueLZs0CXoYU/?name=image.png)

Nos casos em que o funcionário é demitido e o FGTS do mês anterior à rescisão será recolhido via GRFC junto com o FGTS rescisório é necessário utilizar o parâmetro "FGTS mês anterior recolhido na GRFC" no momento do cálculo da rescisão.  
  
O parâmetro não ficará visível para demissões com tipo de dispensa igual a:

* 1 - justa causa
* 4 - pedido de demissão
* 8 - falecimento

Normalmente esta situação ocorre em demissões do mês seguinte à folha, entre os dias 01 e 07 do próximo mês.  
Nestas datas (01 a 07) normalmente o FGTS da folha ainda não foi gerado pelo arquivo SEFIP.RE, e as vezes o usuário opta por recolher o FGTS do mês da folha na própria GRFC, juntamente com o FGTS rescisório.  
Ao gerar o arquivo SEFIP.RE do mês da folha dos funcionários com demissão no mês seguinte e que terão o FGTS mês anterior recolhido na GRFC, sairão no arquivo com um registro 32 de movimentação de demissão, porém com o indicativo de recolhimento em GRFC com o status = 'S' - Sim. Onde o 'S' significa que o recolhimento do FGTS da folha ou do mês anterior à data de demissão foi recolhido pela GRFC.  
  
Homolognet é um sistema do Ministério do Trabalho e Emprego que visa a conferência da rescisão contratual do funcionário que está se desligando da empresa. No cadastro de itens para a rescisão existem parâmetros que devem ou não serem marcados de acordo com a situação do desligamento do funcionário.  
  
**Saiba Mais**  
[Rescisão - RHU](https://tdn.totvs.com/pages/viewpage.action?pageId=452719347)
