---
article_id: 360042137774
category: TAF - eSocial - Atualização
content_hash: 993cc62c22613a639a031beb0741ca23eb7f27f18c329e92b68c3ae502f7683e
fetched_at: '2026-06-28T22:45:13.204281+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Atualização - Session ['TAF']
  not found in appserver.ini ("Sessão ['TAF'] não encontrada no appserver.ini")
type: support-article
updated_at: '2024-08-30T18:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042137774-RH-Linha-Protheus-eSocial-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Session-TAF-not-found-in-appserver-ini-Sess%C3%A3o-TAF-n%C3%A3o-encontrada-no-appserver-ini
---

**Ocorrência**

Ao acessar o TAF após atualizar o TAF e o TSS, é exibido a mensagem abaixo:

***Session ['TAF'] not found in appserver.ini. Verify the "Enviroment in the Server" in file.*** **(Sessão ['TAF'] não encontrada no appserver.ini. Verifique o "Ambiente do Servidor" no arquivo).**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057014793)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Causa**

A mensagem de erro é gerada devido à configuração incorreta dos arquivos de atalho, que contêm caminhos especificados com apóstrofos.

**Exemplo:** C:\totvs\TAF\bin\smartclient\smartclient.exe -m -q -p='SIGATAF' e='TAF'

**Solução**

1. Clique com o botão direito do mouse sobre o aplicativo "smartclient" e selecione "Propriedades".  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056140634)

2. No campo "Destino", remova todos os apóstrofos ou aspas no caminho especificado. Por exemplo, transforme:  
  
**Antes:**  
*C:\totvs\TAF\bin\smartclient\smartclient.exe -m -q -p='SIGATAF' e='TAF'*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056140734)

**Depois:***C:\totvs\TAF\bin\smartclient\smartclient.exe -m -q -p=SIGATAF e=TAF*

*![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056140794)*

3. Após remover os apóstrofos ou aspas, clique em "Aplicar" e depois em "OK".
