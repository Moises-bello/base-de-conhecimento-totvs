---
article_id: 360036651774
category: RH - Provisão
content_hash: 17e98dffb7107a3527174e2fd967df371ce194e618a833a2d6f7a29600fb830e
fetched_at: '2026-06-28T22:43:56.830006+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Provisão de Férias e 13º Salário emitido
  por Níveis de Centro de Custo
type: support-article
updated_at: '2024-11-05T15:11:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036651774-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Provis%C3%A3o-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-emitido-por-N%C3%ADveis-de-Centro-de-Custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27571732715415) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como Funciona o Relatório de Provisão de Férias e 13º Salário emitido por Níveis de Centro de Custo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Os Relatórios de Provisão Por Níveis de Centro de Custo são impressos respeitando o conteúdo do parâmetro **MV\_MASCCUS.**No parâmetro deverá ser informado o número de dígitos para cada nível, por padrão está configurado com 1111. Este parâmetro trata-se apenas da máscara contábil de Centro de Custo, influenciando apenas na impressão dos relatórios e consultas.

Exemplo de Emissão do Relatório:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047965174)

Neste exemplo, o relatório será impresso com 5 totais :   
1 - o centro de custo completo        - 001  
2 - centro de custo com 4 posições - 001   
3 - centro de custo com 3 posições - 001  
4 - centro de custo com 2 posições - 00  
5 - centro de custo com 1 posições - 0

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048838833)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047965094)

**Importante***:* Caso a empresa não utilize o preenchimento dos Níveis por Centro de Custo, basta deixar o conteúdo do parâmetro **MV\_MASCCUS** em branco, e a pergunta "Impr.Níveis C. Custo?" preenchida com Não, que o centro de custo será emitido apenas uma vez no relatório de provisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27571756727191)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
