---
article_id: 360037531594
category: MDT - eSocial
content_hash: 83057d2c021a88caed5291dd00b43c7c0ec694ab376d24b49afd0181e3038884
fetched_at: '2026-06-28T22:44:29.337287+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Como cadastrar responsáveis Ambientais
  para o período de exposição do funcionário
type: support-article
updated_at: '2025-08-05T16:54:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037531594-RH-Linha-Protheus-MDT-eSocial-Como-cadastrar-respons%C3%A1veis-Ambientais-para-o-per%C3%ADodo-de-exposi%C3%A7%C3%A3o-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372574339095)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Após habilitar parâmetro **MV\_NG2ESOC** e efetuar cadastros no módulo SIGAMDT ou SIGAGPE, o sistema passa a validar as informações para o eSocial, sendo preciso cadastrar o responsável ambiental para que a mensagem não gere novamente.  
 **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões   
  
**Causa**  
Essa mensagem ocorre devido a não existir profissional responsável pelos riscos ambientais, ou por não existir laudo com um responsável vinculado.  
  
**Solução**Para o período de exposição do funcionário, deve ser vinculado pelo menos um responsável ambiental por meio da rotina de Laudos. No Laudo, deve constar um responsável cadastrado como 'Responsável Ambiental = Sim' e que possua o tipo definido no parâmetro **MV\_NG2REST**. Além disso, o Laudo deve ter um período de vigência que englobe o período de exposição do funcionário.

1. Para cadastrar um responsável ambiental:  
  
Acesse no modulo SIGAMDT o caminho: Atualizações - Sesmt - Sesmt/usuar.aten. e cadastre/altere o responsável deixando o campo "**Resp.Amb. = SIM**."  
 **![](https://totvssuporte.zendesk.com/attachments/token/KiMEDxINo36v44f0ytMVXoJMk/?name=inline1112299557.png)​**2. Para vincular o responsável ambiental ao laudo:  
  
Acesse no modulo SIGAMDT o caminho: Atualizações - Laudos - Laudos (MDTA210) e vincule o Responsável no campo **Resp. Elab.**, conforme imagem abaixo.  
**Importante:** o Laudo deve ter um período de vigência (data inicio) contemplado pelo período de exposição do funcionário.  
 **![](https://totvssuporte.zendesk.com/attachments/token/S5I3m0inZOqf1NJWzT242Ypf4/?name=inline-1840936605.png)****Observações**

* Para acessar a documentação dos eventos SST (Medicina e Segurança do Trabalho) acesse o link: **[Eventos Não Periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=390398468)**. Clique no evento desejado e verifique as abas Conceito, Premissas, Como Gerar.
* Para acessar o documento de De/Para de campos dos eventos SST (Medicina e Segurança do Trabalho) acesse o link: **[Correspondência Layouts eSocial x Protheus (SST)](https://tdn.totvs.com/pages/viewpage.action?pageId=344457675)**. Clique no evento desejado e veja os campos do Medicina e TAF utilizados em cada evento.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
