---
article_id: 360020283311
category: Banco de talentos
content_hash: c1c1d81a58aa36f820537162ea22a22b69dd72054ef535d3197bf4b436dba603
fetched_at: '2026-06-28T22:47:16.102481+00:00'
product: rm
section_id: 1500000834901
source: central-rm
title: RH - RM - RHU - Validação das configurações de conexão entre banco de dados
  e banco de talentos quando este apresentar problemas de acesso ao clicar nos botões
  (hiperlinks) da página
type: support-article
updated_at: '2025-09-25T14:50:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020283311-RH-RM-RHU-Valida%C3%A7%C3%A3o-das-configura%C3%A7%C3%B5es-de-conex%C3%A3o-entre-banco-de-dados-e-banco-de-talentos-quando-este-apresentar-problemas-de-acesso-ao-clicar-nos-bot%C3%B5es-hiperlinks-da-p%C3%A1gina
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034645036439) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Fiz a instalação do TOTVS RM Portal - 12.1.XX.msi e BibliotecaRM - 12.1.XX.msi, apliquei os patches (BibliotecaRM (Patch) 12.1.XX.XXX.exe e TOTVSRMPortal (Patch) 12.1.XX.XXX.exe) mas ao acessar o Banco de Talentos quando clico em qualquer botão (hiperlink) ou tento realizar um cadastro de candidato, não acontece nada, ou apresenta erro 404 na página de acesso ao Banco de Talentos. O que pode ser?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - A partir da versão 12.1.28 ou superior  
  
**Solução**  
Para solucionar essa questão, realize os seguintes passos:

1- Acesse o diretório C:\totvs\CorporeRM\Corpore.Net e procure pelo arquivo web.config e edite o mesmo.

-Procure pela tags:

<add key="FrameHtmlUrl" value="**http://dominio\_do\_site\_ou\_ip/FrameHTML/RM**" />

Verifique se está apontando para o servidor e porta corretos.

![framehtml.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402369880855)

​

2- Acesse o diretório C:\totvs\CorporeRM\FrameHTML procure pelo arquivo web.config e edite o mesmo.   
<add key="JOBSERVER3CAMADAS" value="True" />

<add key="Port" value="1200" />

Elas devem ser alteradas para:

<add key="JOBSERVER3CAMADAS" value="false" />

**observação importante:** *esta tag só deve ser alterado caso o ambiente do cliente não seja três camadas*

<add key="Port" value="8050" />

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016016352)

**Importante:**

- Após realizar as modificações, reinicie o serviço do IIS e acesse o banco de talentos novamente.  
  
**Saiba mais:**Avalie também as documentações, se necessário:[- RM - Frame - Alteração de porta do Novo Portal FrameHTML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047347733-RM-Frame-Altera%C3%A7%C3%A3o-de-porta-do-Novo-Portal-FrameHTML?source=search)[- Como Fazer - Alterando o portal FrameHTML para utilizar a porta 80](https://tdn.totvs.com/display/public/LRM/Como+Fazer+-+Alterando+o+portal+FrameHTML+para+utilizar+a+porta+80)
