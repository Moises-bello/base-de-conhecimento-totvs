---
article_id: 360025443851
category: eSocial - Gerar XML/ Integração Evento
content_hash: 1d22ee7e83224f8f537446dd277c2e8afbc405962b68a844db2e7cedf651d190
fetched_at: '2026-06-28T22:47:12.993092+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro no S-1200 para funcionários com Múltiplos Vínculos:
  Verificação de chave duplicada. Tabela C9K- Grupo da Tag'
type: support-article
updated_at: '2024-06-12T11:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025443851-RH-RM-FOP-eSocial-Erro-no-S-1200-para-funcion%C3%A1rios-com-M%C3%BAltiplos-V%C3%ADnculos-Verifica%C3%A7%C3%A3o-de-chave-duplicada-Tabela-C9K-Grupo-da-Tag
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19195737042711)**Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Ao realizar a integração dos eventos periódicos com o TAF, após executar o processamento de Jobs, o sistema apresenta no **Gerenciador de Integração** o erro **Verificação de chave duplicada. Erro de chave duplicada, favor verificar as informações que estão sendo integradas. Tabela: C9K - Grupo da Tag:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12490276953751)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões

**Causa**O erro geralmente ocorre para funcionário com mais de um vínculo, pois a tag **ideDmDev**deverá conter um identificador único para cada um dos demonstrativos de pagamento do trabalhador dentro da mesma competência, conforme descrito no layout do e-Social.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024000472)

Assim, no caso de funcionários que possuem múltiplos vínculos na mesma coligada e que tenham pagamentos no mesmo período, o sistema irá gerar o **ideDmDev** igual para os vínculos, gerando o erro supracitado na integração.

**Solução**No cadastro do funcionário, aba **Parâmetros**, foi implementado o campo **Prefixo Período (eSocial)**. O valor preenchido neste campo será agregado ao valor do período na tag**ideDmdev**, evitando assim sua duplicidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024533972)

**Saiba mais**  
Para mais informações acesse:  
      • [Como discriminar nos eventos S-1200 e S-1210 a Tag <ideDmDev> para funcionários com categorias diferentes?](http://tdn.totvs.com/pages/viewpage.action?pageId=388236245)
