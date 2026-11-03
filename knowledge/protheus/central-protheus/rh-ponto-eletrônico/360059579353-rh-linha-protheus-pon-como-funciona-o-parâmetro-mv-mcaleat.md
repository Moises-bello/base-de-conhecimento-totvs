---
article_id: 360059579353
category: RH - Ponto Eletrônico
content_hash: 3f47b4f7e885d54566daa17cbb75de0dd7e21d717a2c19e8881684935ee9d5ff
fetched_at: '2026-06-28T22:44:58.296461+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona o parâmetro MV_ MCALEAT
type: support-article
updated_at: '2021-09-13T19:03:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059579353-RH-Linha-Protheus-PON-Como-funciona-o-par%C3%A2metro-MV-MCALEAT
---

**Dúvida**Como funciona o parâmetro MV\_MCALEAT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

O Sistema permite que a geração das Marcações Automáticas seja feita com minutos aleatórios. Para isso, é necessário que o parâmetro MV\_MCALEAT esteja com o conteúdo preenchido com valor superior a zero. Este parâmetro irá definir a quantidade máxima de minutos que poderão ser utilizados para gerar as marcações de forma aleatória, exemplo: 05, 10.  
  
Para isso, realize os seguintes passos:  
1 - Informar no Parâmetro MV\_MCALEAT, o limite de minutos para gerar as marcações aleatórias:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097965454/mceclip0.png)

2 - Na rotina de Marcações (PONA040), ao aplicar o comando F7, o sistema gerou as marcações aleatórias, considerando o limite de 05 minutos apontados no parâmetro MV\_MCALEAT, e respeitando o horário informado na Tabela de Horário Padrão:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097965694/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097966114/mceclip2.png)

**Saiba mais:**[MP - PON - Funcionalidade da rotina Marcações por Centro de Custo - PONA230](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050356233-MP-PON-Funcionalidade-da-rotina-Marca%C3%A7%C3%B5es-por-Centro-de-Custo-PONA230?source=search)  
[MP - PON - Atalhos das teclas na rotina PONA040 - Marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058393533-MP-PON-Atalhos-das-teclas-na-rotina-PONA040-Marca%C3%A7%C3%B5es-?source=search)
