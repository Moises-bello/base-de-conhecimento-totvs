---
article_id: 4402518054039
category: eSocial
content_hash: c14db8d847dc9642b5e42948a3eda82c277cf011503e5da546be18ca9256235f
fetched_at: '2026-06-28T22:47:39.181998+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: RH - RM - SMT - S-2240 - Cadastrar (informar) a ausência risco, quando não
  há exposição mapeada
type: support-article
updated_at: '2025-09-25T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402518054039-RH-RM-SMT-S-2240-Cadastrar-informar-a-aus%C3%AAncia-risco-quando-n%C3%A3o-h%C3%A1-exposi%C3%A7%C3%A3o-mapeada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036494647959) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Quando não há riscos mapeados, como informar a ausência de risco, conforme a tabela 24, item 09.01.001 - Ausência de agente nocivo ou de atividades previstas no Anexo IV do Decreto 3.048/1999 ?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as versões.

**Solução**

Para os casos em que não houver riscos mapeados,  ao gerar o XML do evento S-2240, o sistema irá **informar automaticamente** a ausência de risco código 09.01.001.

**Dessa forma, não deverá criar o tipo de agente e uma avaliação/reconhecimento indicando a ausência de risco.**

Segue o exemplo: Ao gerar o XML, na aba log da geração será emitido o alerta abaixo:

*Não foram encontrados fatores de riscos relacionados a esse funcionário, logo, foi atribuído ao mesmo o código de ausência de risco.*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402517938455)

E ao consultar o XML na tag <codAgNoc> ira aparecer o código 09.01.001 indicando a ausência de risco

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26791866568727)

**Importante**

Atualmente não há como informar o código de **Ausência de Riscos (09.01.001)** no cadastro do Risco. Este código é gerado automaticamente quando não são mapeados nenhum risco ao funcionário. Portanto, para gerar esta ausência não deverá existir nenhum risco associado para o funcionário em questão.

**Saiba mais**Para maiores informações, acesse:

- [S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://tdn.totvs.com/pages/viewpage.action?pageId=469451357)

- [RH - RM - SMT - Gerar o evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007674022)
