---
article_id: 29443879168407
category: LOGIN
content_hash: bf163e8b8b4c4b469abf6e5692242c99fb702e84ef89c037579e85ef452e2a84
fetched_at: '2026-06-28T22:44:40.393788+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH -  Erro de Sistema Indisponível no acesso ao app
  Meu RH
type: support-article
updated_at: '2025-11-06T20:28:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29443879168407-RH-Linha-Protheus-MEU-RH-Erro-de-Sistema-Indispon%C3%ADvel-no-acesso-ao-app-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29443879162647) Tempo aproximado para leitura: **00:03:30 min** **Ocorrência**  
No App MEU RH não aparece a tela de login, é apresentado o erro Sistema indisponível no momento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29443879163543)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
O incidente ocorre quando o sistema apresenta falta de atualizações.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

**1** - atualização de todos os RPO's com o último pacote de expedição contínua do GPE <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>  
  
**2** - atualização dos arquivos de portal na pasta \web, conforme instruções abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034>  
  
\*\*\* Dica de atualização:  
Dentro do diretório Path / WEB , delete todos os arquivos existentes, menos o properties.json, assim a pasta terá somente os arquivos atualizados.  
[RH - Linha Protheus - Meu RH - Quais as atualizações necessárias para o App Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21524187944215-RH-Linha-Protheus-Meu-RH-Quais-as-atualiza%C3%A7%C3%B5es-necess%C3%A1rias-para-o-App-Meu-RH?source=search)  
  
**3** - Além do RPO e dos Arquivos de Portal, **orientamos sempre estar com a LIB e os Binários atualizados, por conta das aplicações em *REST*.**  
<https://suporte.totvs.com/portal/p/10098/download#000006/368/> 

**4** - Após Atualização, a orientação será:  
[RH - Linha Protheus - MEU RH - Como limpar o Cache do MEU RH no Navegador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058395633-RH-Linha-Protheus-MEU-RH-Como-limpar-o-Cache-do-MEU-RH-no-Navegador)  
[RH - Linha Protheus - MEU RH - Como limpar o Cache do MEU RH no APP em smartphones com Android](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058394613-RH-Linha-Protheus-MEU-RH-Como-limpar-o-Cache-do-MEU-RH-no-APP-em-smartphones-com-Android)   
[RH - Linha Protheus - MEU RH - Como limpar o Cache do MEU RH no APP em smartphones com iOS (iPhone)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058394333-RH-Linha-Protheus-MEU-RH-Como-limpar-o-Cache-do-MEU-RH-no-APP-em-smartphones-com-iOS-iPhone)  
  
**5** - Verificar se os arquivos de certificado SSL de segurança, estão exatamente na pasta que foi declarada no appserver.ini:  
  
Pasta declarada no appserver.ini:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29799071308823)  
  
Arquivos efetivamente na pasta:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29799071310359)  
  
**6** - reiniciar todos os serviços do ambiente

**Saiba Mais**  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
