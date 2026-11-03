---
content_hash: 3d60ea6eba74f73f9c01ea5e8fe0105e1d62e7300c437bd4e5024da089be094d
fetched_at: '2026-06-29T00:10:19.608221+00:00'
page_id: '4816710'
product: rm
source: tdn-rm
title: Publicação de Documento no GED Gestão Eletrônica de Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4816710
version: 4
---

BLOCK

Publicação de Documento no GED Gestão Eletrônica de Documentos

FAQ:  **Publicação de Documento no GED (Gestão Eletrônica de Documentos)**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Solução

**TBC integra a Linha RM ao GED (Gestão Eletrônica de Documentos)**

A partir da versão 11.20 o TBC integra a Linha RM ao GED (versão beta). O GED é o aplicativo de Gestão Eletrônica de Documentos da TOTVS, que faz parte do pacote ECM. Nesta primeira versão um novo anexo será apresentado no cadastro de Projetos do TOTVS Obras e Projetos e nos cadastros de Documentos do Aluno e de Professor do TOTVS Educacional. As versões futuras trarão mais novidades e a possibilidade do anexo ser habilitado em qualquer visão da linha RM.

 

**Publicação de Documentos**

Para que um usuário RM consiga postar documentos no GED, primeiramente ele precisa existir na base de dados do GED. O TBC também implementa a função de Sincronizar usuários do RM para o GED, como mostra a figura a seguir  (RM.exe | Segmento Integração | Menu Serviços | Sincronizar Usuários RM com o GED):

![](http://lh3.ggpht.com/_G7KXZLoZDsY/TNP8FzcQwwI/AAAAAAAACrA/ZaXkq7O7FLQ/s1600/image%5B13%5D.png)

Para postar um documento no GED o usuário logado no RM deve acessar a visão RM, selecionar um registro e selecionar o anexo Integração GED.

![](http://lh5.ggpht.com/_G7KXZLoZDsY/TNP8HsALInI/AAAAAAAACrI/HFVJE0AkgyA/s1600/image%5B14%5D.png)

Será exibido o diálogo a seguir, onde o usuário irá informar uma descrição para o documento e localizar o arquivo na sua máquina local ou em qualquer local da rede:

![](http://lh5.ggpht.com/_G7KXZLoZDsY/TNP8I3AO-VI/AAAAAAAACrQ/Ja3DtS61qVY/s1600/image%5B15%5D.png)

Ao clicar em OK o documento será postado no GED.

A estrutura de pastas onde o documento será postado será sempre RM x GED/[Nome da Visão RM de onde o documento se originou], conforme exemplo:

![](http://lh5.ggpht.com/_G7KXZLoZDsY/TNP8K3bmMJI/AAAAAAAACrY/c8gzl1ryhHE/s1600/image%5B16%5D.png)

**Tudo bem simples e intuitivo!**

**Veja o** **filme**.
