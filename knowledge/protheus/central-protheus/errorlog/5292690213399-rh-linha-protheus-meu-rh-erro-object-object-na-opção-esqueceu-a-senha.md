---
article_id: 5292690213399
category: ERRORLOG
content_hash: 8b9e6338004242c430c60cad4c11a6900182df469f65fbd8853e831a739f2589
fetched_at: '2026-06-28T22:44:39.475689+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Erro Object Object na opção esqueceu a senha
type: support-article
updated_at: '2026-06-18T18:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5292690213399-RH-Linha-Protheus-MEU-RH-Erro-Object-Object-na-op%C3%A7%C3%A3o-esqueceu-a-senha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24768613156503) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao utilizar a opção "Esqueceu a senha" no MEU RH, é apresenta o erro: *Object Object*  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Essa mensagem ocorre por conta de problemas na configuração do appserver.ini do Meu RH, especificamente na *tag* *Public* **(*Endpoints* Públicos)** da seção **(URI)** do *REST*.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5292445487767)  
  
**Solução**  
1. Para solução, acesse o Appserver.ini onde esta configurado o ***REST***, após localize a ***URI*** do ***REST*** que é utilizado para o **MEU RH** e altere a *tag* *Public* para:  
  
Public=fwjwt/refresh\_token,auth,setting/companySettings  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27567632194199)  
  
Para saber mais sobre os ***Endpoints* Públicos** referente a *tag* *Public* acesse:   
[Configurando REST](https://tdn.totvs.com/display/NPR/Passo+3%3A+Configurando+REST)  
  
**Saiba Mais  
[Instalação MEU RH:](https://tdn.totvs.com/pages/viewpage.action?pageId=532651492)** [Linha Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=532651492)**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
