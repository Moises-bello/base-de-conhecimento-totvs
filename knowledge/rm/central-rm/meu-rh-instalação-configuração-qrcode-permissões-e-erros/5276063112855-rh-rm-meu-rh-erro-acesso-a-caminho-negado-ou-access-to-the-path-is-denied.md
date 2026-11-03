---
article_id: 5276063112855
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 523a4102f291a1c4a9195f0dabba4859052a9f6182f2fc79f9fb29b6e84f2c04
fetched_at: '2026-06-28T22:47:29.525326+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Erro Acesso a caminho negado ou access to the path is denied
type: support-article
updated_at: '2025-02-03T13:10:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5276063112855-RH-RM-Meu-RH-Erro-Acesso-a-caminho-negado-ou-access-to-the-path-is-denied
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24076990392599) Tempo aproximado para leitura: **00:02:02 min****Ocorrência**No Meu RH ao tentar acessar algum menu é apresentado o erro **Access to the path is danied (acesso a caminho negado).****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**Esse incidente ocorre por falta de permissão de escrita\leitura no caminho de rede utilizado nas tags FileServerPath e LogPath, essas tag's ficam localizadas dentro dos arquivos Hosts do RM, pasta rm.net.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5275210170903)  
  
**Solução**  
Para solucionar essa ocorrência, realize o seguinte passo:  
  
1. Acesse a pasta  do caminho que é apresentado no erro , por exemplo cujo o nome seja **ARQUIVOS** (esta pasta deverá ter o compartilhamento TODOS);  
![](https://tdn.totvs.com/download/attachments/203754419/image2017-1-17%2011%3A42%3A49.png?version=1&modificationDate=1484664253000&api=v2)  
  
**Importante** :  
1- Utilizar apenas uma única pasta compartilhada na rede em todos os arquivos de configuração.  
  
2- Utilizar somente pastas compartilhadas na rede.  
  
3- Não é possível o uso de pastas "MAPEADAS" sejam elas localmente ou via TS por problemas de incompatibilidade dos serviços do Windows conforme informado no link [Serviços e Unidades Redirecionadas](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685143(v=vs.85).aspx).

**Saiba Mais****[CLIQUE AQUI para mais informações sobre configuração das Tags FileServerPath e LogPath](https://tdn.totvs.com/display/public/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)**
