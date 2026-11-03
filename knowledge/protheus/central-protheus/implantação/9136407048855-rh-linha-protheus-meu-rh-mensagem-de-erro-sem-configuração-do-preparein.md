---
article_id: 9136407048855
category: IMPLANTAÇÃO
content_hash: c66494f3cdbdc65fbd7f0b0d0abf02ad3dae11a40008164c29bcbd4a10bb68af
fetched_at: '2026-06-28T22:44:33.374782+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - mensagem de erro "sem configuração do PrepareIn"
type: support-article
updated_at: '2026-06-23T21:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9136407048855-RH-Linha-Protheus-MEU-RH-mensagem-de-erro-sem-configura%C3%A7%C3%A3o-do-PrepareIn
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27598971520023)Tempo aproximado para leitura: 00:02:00 min****Dúvida**Quando a chave **[HTTPENV]** dentro do appserver.ini, na *tag* **PREPAREIN** estiver escrito de maneira incorreta, como por exemplo **PREPARELN,** ao acessar o MEU RH o sistema gera o erro abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9136308143895)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Para solução do erro é necessário corrigir a *tag* PREPAREIN dentro do appserver.ini, segue abaixo demonstração do erro e em seguida a correção:  
  
**1º A *tag* PrepareIn foi escrita de forma incorreta onde foi apresentado erro ao acessar o MEU RH:**  
  
![PrepareIn_errado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9136463669015)  
  
**2º Corrigido a *tag* PrepareIn no appserver.ini e o acesso ao MEU RH funcionou corretamente :**  
![PrepareIn_correto.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/9136781883159)  
  
Importante frisar que, para o Meu RH, é necessário sempre que o conteúdo da *tag* PrepareIn seja igual ao **código do Grupo de Empresa, cadastrado no SIGAMAT.**  
  
**O App Meu RH não funcionará com PrepareIn=ALL.**  
 **Saiba Mais  
[RH - Linha Protheus - MEU RH - Erro ao realizar o logout no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8837812804119)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
