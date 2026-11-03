---
article_id: 4410114167703
category: Materiais - Compras (SIGACOM)
content_hash: 2da5fddd42dd361ee8deac88d796389b149bff7baa7810c4c8f5e2591c17f0bb
fetched_at: '2026-06-28T22:41:16.043297+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como restringir um
  usuário de incluir uma solicitação de compras?
type: support-article
updated_at: '2022-10-26T13:57:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410114167703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-restringir-um-usu%C3%A1rio-de-incluir-uma-solicita%C3%A7%C3%A3o-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como restringir um usuario de incluir uma solicitação de compras?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as versões  
  
**Solução**Atualmente, o cadastro de solicitantes (MATA084) é responsável por restringir usuários de ALTERAR/EXCLUIR uma solicitação de compras já existente. Essa regra não se aplica para Inclusões.

Para restringir a inclusão de uma solicitação de compras de um determinado usuário, pode-se utilizar o cadastro de privilégios disponivel no configurador:

**Exemplo:**

Acesse o módulo **Configurador** (SIGACFG) > Vá em **Usuário** > **Senhas** > **Privilégios**  
  
![](https://totvssuporte.zendesk.com/attachments/token/m4bLI9eCx3ZIFUM5aPz2eGQu1/?name=inline1858276110.png)​  
  
Crie uma regra para determinada rotina (Exemplo MATA110):  
  
![](https://totvssuporte.zendesk.com/attachments/token/mHqcioG5eSHlMRbFE9i6PcJ1o/?name=inline334745257.png)  
  
Amarre a regra no usuário:  
  
![](https://totvssuporte.zendesk.com/attachments/token/cQ1THRYgwU1KCpzUudMCgrA3D/?name=inline-484752272.png)​  
Desta forma, o usuário não conseguirá ter acesso ao botão restrito:  
  
![](https://totvssuporte.zendesk.com/attachments/token/Qmu3tEbFavWpVU6dd6QEvjVCg/?name=inline-1533041223.png)

**Importante**: O exemplo acima é pontual para o botão "Aprovação" da Solicitação de compras, para restringir a inclusão, deve criar regra no botão "**Incluir**"

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
