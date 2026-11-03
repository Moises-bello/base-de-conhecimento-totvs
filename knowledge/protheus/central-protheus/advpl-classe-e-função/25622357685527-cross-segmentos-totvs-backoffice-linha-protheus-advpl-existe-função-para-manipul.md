---
article_id: 25622357685527
category: ADVPL - Classe e Função
content_hash: 9bb8901e61c41f69859ff9f8128dc98732c9b9a2f31f8cb3b8bf283ee9145ba5
fetched_at: '2026-06-28T22:40:21.613756+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Existe função para
  manipular o profile do usuário?
type: support-article
updated_at: '2024-08-20T10:40:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25622357685527-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Existe-fun%C3%A7%C3%A3o-para-manipular-o-profile-do-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25622357658519) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Existe função para manipular o profile do usuário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para realizar a manipulação do profile do usuário existe a função FwProfile, essa função fornece um objeto que permite o controle do profile do usuário.

**Exemplo**

```
#INCLUDE 'Protheus.ch'  
  
User function FwProftst()  
  
Local oProf := FwProfile():New()  
Local aProf := {}  
Local aProf2 := {}  
Local cProf := ""  
  
oProf:SetUser("000000")  
oProf:SetProgram("FATA010   ")  
oProf:SetTask("PROTHEUS  ")  
oProf:SetType("BRWFWLKAC5")  
oProf:Activate()  
  
aProf:= oProf:Load(.F.)  
aProf2:= oProf:GetProfile()  
cProf:= oProf:LoadStrProfile(.F.)  
  
oProf:SetStringProfile("TESTE")  
oProf:Save()  
  
Return
```

**Saiba mais:**

[FwProfile](https://tdn.totvs.com/display/public/framework/FWProfile)

[Framework - Linha Protheus - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)
