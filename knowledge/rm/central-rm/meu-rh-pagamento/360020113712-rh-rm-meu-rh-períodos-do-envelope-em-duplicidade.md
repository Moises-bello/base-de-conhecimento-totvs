---
article_id: 360020113712
category: Meu RH - Pagamento
content_hash: 98ed3f3317e9d0ff8a29285440f4b20db7ea844b1f30cbfa99b02b711d0a9a2a
fetched_at: '2026-06-28T22:47:33.906969+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Períodos do envelope em duplicidade
type: support-article
updated_at: '2025-02-03T14:27:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020113712-RH-RM-Meu-RH-Per%C3%ADodos-do-envelope-em-duplicidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:00:22 min**

**Ocorrência**

Ao acessar o aplicativo Meu RH via aplicativo e selecionar o envelope de pagamento, o sistema apresenta a descrição repetida, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016185611/mceclip0.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.20  
  
**Causa**Quando a descrição do período é setada como alguma mês (exemplo: Janeiro), pode ocorrer do usuário esquecer a parametrização e nos meses seguintes o sistema resgatar a informação e continuar usando as informações incorretamente. Também pode ser sua causa na falta do cadastro da descrição do período na tabela dinâmica PDESCPER.  
  
**Solução**Há duas soluções para este caso. Veja abaixo as instruções para solucionar ambos.  
  
**01.** Caso **não** seja utilizado período fixo:   
Se o usuário não utilizar período fixo pelo cadastro da tabela dinâmica PDESCPER, verifique a descrição dos períodos no parametrizadorem **Configurações | Parametrizador | Configurações de Competência** ou durante a liberação da competência.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12133461079063)  
  
**02.** Caso seja utilizado o período fixo, ou a solução acima não tenha surtido efeito:  
Em alguns casos este incidente só é corrigido quando é cadastrado o período na tabela dinâmica e definida uma descrição fixa para o período. Acesse a tabela dinâmica em **Administração de pessoal | Cadastros Globais | Tabelas Dinâmicas** e procure pela tabela **PDESCPER**. Cadastre o período desejado com uma descrição fixa (exemplo: Rescisão). Após realizar este cadastro, a descrição dos períodos deverá ficar correta no aplicativo Meu RH.

O código deve ser o mesmo numero do periodo no qual foi feito o pagamento e então a descrição inserida será apresentada no Meu RH.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12264557824279)
