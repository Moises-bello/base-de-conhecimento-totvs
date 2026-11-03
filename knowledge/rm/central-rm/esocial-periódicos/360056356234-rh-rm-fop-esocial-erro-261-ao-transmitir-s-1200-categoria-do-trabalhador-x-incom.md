---
article_id: 360056356234
category: esocial - Periódicos
content_hash: 47a09a2f773a12f87a1314d60f6660d62cfe91303d34efab1fd8bb84880bdc70
fetched_at: '2026-06-28T22:47:09.272971+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 261 ao transmitir S-1200: Categoria do trabalhador
  "X" incompatível com a lotação do tipo "Y" e classificação tributária do empregador
  "Z"'
type: support-article
updated_at: '2024-02-20T17:37:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056356234-RH-RM-FOP-eSocial-Erro-261-ao-transmitir-S-1200-Categoria-do-trabalhador-X-incompat%C3%ADvel-com-a-lota%C3%A7%C3%A3o-do-tipo-Y-e-classifica%C3%A7%C3%A3o-tribut%C3%A1ria-do-empregador-Z
---

**Ocorrência**Ao transmitir o evento **S-1200** ocorre o erro **261** com descrição **Categoria do trabalhador "X" incompatível com a lotação do tipo "Y" e classificação tributária do empregador "Z"** conforme exemplo abaixo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097952913)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**​No exemplo da **Ocorrência** temos um trabalhador categoria 731, Tipo da lotação tributária 01 e classificação tributária do empregador 99. Será necessário validar a compatibilidade dos dados diante da **Tabela 11 - Compatibilidade entre Categoria de Trabalhadores, Classif. Tributária e Tipos de** **Lotação**. Para validar os dados realize os passos abaixo:

**1**. Acesse **Folha de Pagamento | eSocial | Eventos Periódicos** selecione o evento com erro e identifique as tag **codLotacao**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095653614)

**2**. Acesse **Folha de Pagamento | eSocial | Lotação Tributária** filtre pelo código de lotação localizado no passo 1 conforme exemplo abaixo;

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095654994)

**3.** Acesse a **Tabela 11** e valide a compatibilidade entre categoria de trabalhadores, classificação tributária e tipos de lotação. A categoria **731**, por exemplo, será compatível com lotações tributárias dos tipos 01, 02, 03, 04, 05, 06, 07, 10 e 91 e a classificação tributária é compatível com todas classificações desde que o indicativo de cooperativa seja igual a 1 (cooperativa de trabalho);

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097953133)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097953193)

Considerando ainda o exemplo utilizado em Ocorrência e a compatibilidade de categoria, classificação tributária e tipo de lotação, veja que a categoria apresentada no erro é compatível com o tipo de lotação porém, o indCoop do evento S-1000 não é igual a 1, tornando assim a classificação tributária incompatível.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098041293)

**Saiba mais**Segue link para download da documentação técnica eSocial contendo as tabelas e regras:   
      • [LEIAUTES DO ESOCIAL](https://www.gov.br/esocial/pt-br/documentacao-tecnica)
