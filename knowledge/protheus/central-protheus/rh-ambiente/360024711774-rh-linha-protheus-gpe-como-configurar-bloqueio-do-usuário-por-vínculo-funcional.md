---
article_id: 360024711774
category: RH - Ambiente
content_hash: db855ff62cccec29820805af383fea1ba9b79adacf6e3c56bc030c849138e076
fetched_at: '2026-06-28T22:43:09.604789+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar Bloqueio do Usuário Por Vínculo
  Funcional
type: support-article
updated_at: '2026-06-24T19:38:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024711774-RH-Linha-Protheus-GPE-Como-configurar-Bloqueio-do-Usu%C3%A1rio-Por-V%C3%ADnculo-Funcional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31662885951767) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como configurar **Bloqueio do Usuário Por Vínculo Funcional** de acordo com a **Situação cadastral** do Funcionário na Folha de Pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O **Vinculo Funcional** tem a finalidade de **bloquear** o **acesso** ao **Protheus** para usuários vinculados a uma matrícula. Os acessos serão de acordo com a sua Situação na Folha.  
  
**Observação:** Essa configuração em caso de demissão efetuará o bloqueio em todos os módulos que o usuário(a) possuía acesso.    
  
**Exemplo:** **Usuária America**, está com o Vínculo Funcional amarrado ao **Funcionária 000010 - América.** Se a América for **demitida**, a América usuária, **automaticamente não terá mais acesso ao sistema.** onde será mostrada a tela abaixo ao tentar fazer login com usuário e senha:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7815568108951)

**Passo a Passo para configurar:**  
1- Acesse o Configurador (SIGACFG)/ Usuários/ Senhas/ Política, e defina em qual situação o Usuário que está amarrado ao Funcionário não poderá acessar o sistema, que fica na aba Outros;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7811771587863)

A lupa contida do lado do campo, mostrará a situação do funcionário que será bloqueada. Neste exemplo, marcamos os funcionários Demitidos.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7811850674583)

**2 -** Acesse o Configurador (SIGACFG)/ Usuários/ Senhas/ Usuários, e amarre o funcionário ao usuário, criando então o vínculo. Os campos para preenchimento ficam na aba **Parametrização;  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7811914615831)**Confirme o ajuste e desta forma, o sistema já está configurado para o vínculo funcional.   
  
**Importante:** O bloqueio para acesso logo após o **login** ocorre quando o sistema é **iniciado em SIGAGPE**. Caso a inicialização seja feita através do **SIGAADV ou SIGAMDI**, o bloqueio é realizado quando o **usuário tenta o acesso das rotinas através dos menus.**

**Saiba Mais:**[RH - Linha Protheus - GPE - Como restringir o acesso do usuário à alteração de campo específico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052716514-RH-Linha-Protheus-GPE-Como-restringir-o-acesso-do-usu%C3%A1rio-%C3%A0-altera%C3%A7%C3%A3o-de-campo-espec%C3%ADfico?source=search)  
[RH - Linha Protheus - GPE - Como permitir que um usuário tenha acesso apenas a Funcionários Demitidos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057151373-RH-Linha-Protheus-GPE-Como-permitir-que-um-usu%C3%A1rio-tenha-acesso-apenas-a-Funcion%C3%A1rios-Demitidos?source=search)
