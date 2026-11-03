---
article_id: 360060656094
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4b513dcf72acbf891308b7e6268a78ef2c656bfd72adcb4301d0f6bccb94a89b
fetched_at: '2026-06-28T22:39:11.064251+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus)  - SIGAACD - Falha ao comunicar
  com o Servidor/Sem conexão com o servidor
type: support-article
updated_at: '2026-05-27T14:32:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060656094-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Falha-ao-comunicar-com-o-Servidor-Sem-conex%C3%A3o-com-o-servidor
---

O erro "Falha ao comunicar com o Servidor/ Sem conexão com o servidor" no App Meu Coletor de Dados ocorre devido a configurações incorretas. Para resolver, configure a tag *Security* como 1 no appserver.ini, verifique todas as chaves necessárias no ambiente REST e preencha o campo "EndPoint" como "REST" no app. Em ambiente Cloud, problemas de acesso podem exigir suporte técnico.

**Dúvida**  
Ao tentar realizar conexão no App Meu Coletor de Dados ocorre "Falha ao comunicar com o Servidor/ Sem conexão com o servidor". Como resolver?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001950762)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para solucionar este problema, siga os passos abaixo:

**1°** - Via AppServer.ini, configure as tag *Security*com conteúdo **1**conforme a imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001951002)

2° - Validar se possui todas ás chaves no appserver.ini do ambiente REST pois pode gerar erro de Bloqueio conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40769484962199)

Pode consultar se possui todas ás chaves na documentação abaixo:

[Configuração do REST](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)

**3°** -Para o correto funcionamento, o campo "EndPoint" na tela do Meu Coletor deve estar preenchida como "***REST***"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103008633)

Desta forma, o coletor comunicará normalmente com o servidor.

**Observação:** Se o usuário utilizar ambiente Cloud, e se por algum motivo estiver sem acesso ao Cloud, este erro poderá ser disparado ao tentar acessar o Coletor. Desta forma deve-se avaliar a possibilidade de abertura de chamado junto ao time de Suporte Cloud para avaliação da configuração e conexão com o servidor.

**Saiba mais:**

[*Configuração REST Protheus para uso com aplicativos mobile*](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360002469152-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
