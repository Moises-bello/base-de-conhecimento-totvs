---
article_id: 4435459223191
category: TAF - eSocial - Configuração
content_hash: e8c8f0db7cb2a61ec5617370158d7d082b79f5d7f3680a4be91a607f1a70404b
fetched_at: '2026-06-28T22:45:14.271946+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Como criar permissão
  de acesso nas rotinas do TAF
type: support-article
updated_at: '2024-08-27T19:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4435459223191-RH-Linha-Protheus-eSocial-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-criar-permiss%C3%A3o-de-acesso-nas-rotinas-do-TAF
---

**Dúvida**Como criar usuários e permitir ou negar acesso as rotinas cadastradas no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões

**Solução**

1. Acessar o Configurador:

[TAF - CONFIGURADOR - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413-TAF-CONFIGURADOR-Como-acessar-o-configurador-)

2. Vamos criar um grupo de usuários caso não tenha criado, clique em: Usuário > Senhas > Grupos > Incluir:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435201406487)

3. Preencha os campos: Grupo e Descrição que são obrigatórios;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435204422679)

4. Em seguida, vamos criar as regras de privilégios de alguma rotina específica, clique em Usuário > Senha > Privilégios > Incluir:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435256162839)

**Obs.:** Para configurar a rotina Privilégios, existem 2 opções: 

* **Inclusão manual de rotinas:**
  + Defina um nome (campo Regra) e descrição (campo Comentário) para o Privilégio;
  + Clique 2 vezes abaixo da coluna Transação/Rotina, e digite o nome do objeto da rotina que deseja configurar. **Exemplo:** *MATA010*;
  + Para incluir outras rotinas, tecle seta para baixo no teclado:  
    ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4637298793367)

* **Inclusão de todas as rotinas de um menu:**
  + Clique em Outras Ações (Ações Relacionadas) e selecione Menu: **![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435309118871)**
    - **Obs.:** Não digite no campo Regra!

* + Clique em avançar:  
    ![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435309356695)

* + Selecione o menu **SIGATAF** e **Finalizar**:  
    ![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435305009431)

* + Serão listadas as rotinas conforme imagem:  
    ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435343856919)

**Obs.:** Segue documentação da relação das rotinas do TAF para o e-Social:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=382546926>

* + Vamos supor que o usuário não pode ter acesso a rotina Complemento Cadastral (Evento S-1000) o nome da rotina é TAFA050 de acordo com o TDN acima. Vou deixar a opção 3 - Negado, marcado e clicar em Confirmar para salvar:![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435316187671)

**Observação** **Importante:**Para bloquear os evento **S-2200, S-2206, S-2205, S-2300** e **S-2306** é obrigatório inserir as respectivas rotina e também a rotina **TAFA421.**

5. Para criar o usuário clique em: Usuário > Senhas > Usuario > Incluir;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435148368919)

6. Somente preencher: Usuário | Nome Completo | Senha | Confirmar Senha. / PARAMETROS: Forçar troca de senha no próximo Logon;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435199714839)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435200258967)

7. Clicar na aba Grupo e selecionar o grupo de usuários:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435260427671)

### **Associando Privilégios a um usuário ou grupo de usuários:**

Com o privilégio configurado, para que ele entre em vigor, você deve associá-lo a um Usuário ou Grupo de Usuários.

- Acesse Configurador > Usuário > Senhas > Usuários (ou Grupos)  
- Clique no usuário (ou grupo) e clique em **Outras Ações** (Ações Relacionadas)  
- Clique em **Privilégios**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435285219479)

9. Selecione o privilégio criado de acordo com as regras definidas e clique em Confirmar:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435413461911)

10. Após as modificações deverá aparecer a seguinte no SIGATAF:  
![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4435431760663)11. Para que as permissões sejam aderidas pelo sistema, é necessário que a chave **SECURITY** esteja ativada **SECURITY=1** no appserver.ini onde os serviços do TAF do Futuro foram configurados. A chave SECURITY faz parte do grupo **HTTPREST**.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13019979459479)
