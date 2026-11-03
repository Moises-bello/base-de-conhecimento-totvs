---
article_id: 360028485372
category: LOGIN
content_hash: c9e4754aa1f427dcc2311b669d1a50750b228f5f5d84326c03a348d4953dcdd5
fetched_at: '2026-06-28T22:44:40.709338+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: 'RH - Linha Protheus - MEU RH - Ao acessar o Aplicativo MEU RH ocorre a mensagem:
  Usuário sem acesso a empresa'
type: support-article
updated_at: '2026-06-18T19:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028485372-RH-Linha-Protheus-MEU-RH-Ao-acessar-o-Aplicativo-MEU-RH-ocorre-a-mensagem-Usu%C3%A1rio-sem-acesso-a-empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**MEU RH - O que fazer quando é apresentado o erro no console.log  **Usuário sem acesso a empresa** ao realizar o login no MEU RH?  
  
Mensagem gerada no console.log:  
  
[INFO ][SERVER] [Thread 16484] JOB Thread finished  
[ThreadID 32940] IPCGo Finish Retries 5000 bCalled[1].. 24/05/2019 14:24:33.936  
Descrição de erro: [Saída no final: Usuário sem acesso a empresa  
}Pilha de Erro: [THREAD ERROR ([32348], HTTP\_WT\_P1217ESOCIAL\_HTTPREST\_HTTPENV@T2þLýMGý01, THIS)   24/05/2019 14:24:33 **Saída no final: Usuário sem acesso a empresa**  
on FINAL(MSFINAL.PRW) 09/05/2019 19:09:10 line : 243  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Acesse o Configurador (SIGACFG) no caminho:  **Usuário > Senha > Usuário**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063270294/mceclip0.png)  
  
Localize o cadastro do usuário criado para acesso ao Meu RH,  avalie se  ele não pertence a nenhum grupo de administradores:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6331599366423/mceclip0.png)  
  
Verifique se possui acesso a todas as **Empresas / Filiais.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6331640838423/mceclip1.png)  
  
Por fim se este usuário possui acesso à todos os **módulos:**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6331715591703/mceclip2.png)  
  
Após estes ajustes o login ocorrerá sem erros.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6331699930775/mceclip3.png)  
  
Importante ressaltar que este único usuário criado poderá ser relacionado a todos os participantes que irão acessar o Aplicativo Meu RH.  
**[RH - Linha Protheus - MEU RH - Como relacionar os Participantes?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013)**  
  
**Saiba Mais:  
[RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453)**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
