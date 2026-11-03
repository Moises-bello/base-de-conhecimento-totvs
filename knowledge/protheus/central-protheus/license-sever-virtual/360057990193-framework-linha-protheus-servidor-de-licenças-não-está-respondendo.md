---
article_id: 360057990193
category: License Sever Virtual
content_hash: 87bd2874420c5d00fc75aedb6efee5d2095a2f9e949bc5c22f6c1e1d84e96e74
fetched_at: '2026-06-28T22:42:20.078180+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Servidor de Licenças não está respondendo
type: support-article
updated_at: '2024-05-09T11:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057990193-Framework-Linha-Protheus-Servidor-de-Licen%C3%A7as-n%C3%A3o-est%C3%A1-respondendo
---

**Dúvida**  
Como proceder caso o Servidor de Licenças pare de responder?  
  
**Ambiente**Protheus  - License Server Virtual - Todas as versões  
  
**Solução**Problema ocorre pois o Servidor de Licenças **perdeu a comunicação** com o Protheus ou as configurações de apontamento **não estão corretas**.  
  
Favor realizar os seguintes procedimentos:  
- Acessar o appserver.ini do Protheus e verificar as configurações abaixo;  
  
[LICENSECLIENT]  
server= <---IP ou nome da máquina (serviço de licença)  
port= <---Porta (serviço de licença)  
  
<https://tdn.totvs.com/display/framework/Configurando+o+Microsiga+Protheus>
