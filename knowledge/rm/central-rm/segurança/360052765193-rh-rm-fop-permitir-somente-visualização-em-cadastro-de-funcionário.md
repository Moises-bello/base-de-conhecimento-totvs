---
article_id: 360052765193
category: Segurança
content_hash: c838edb2a0f829c28eedddae6be450bb67997e3dfc9a4a863108d2b3c807841c
fetched_at: '2026-06-28T22:46:46.794225+00:00'
product: rm
section_id: 1500000834641
source: central-rm
title: RH - RM - FOP - Permitir somente visualização em cadastro de funcionário
type: support-article
updated_at: '2025-03-11T11:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052765193-RH-RM-FOP-Permitir-somente-visualiza%C3%A7%C3%A3o-em-cadastro-de-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como bloquear as alterações do cadastro de funcionário, permitindo que o usuário apenas visualize?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para desabilitar as permissões de alteração na tela de cadastro de funcionário realize os procedimentos abaixo:  
  
1. Acesse o módulo Serviços Globais  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319219832855/mceclip0.png)  
  
2. Clique em Segurança  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319266342807/mceclip1.png)  
  
3. Clique sobre o campo **Usuário** e verifique qual perfil está associado a ele. Lembrando que é importante certificar-se que o módulo das alterações estão sendo realizadas no **Folha de Pagamento**, conforme imagem abaixo: **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319263613335/mceclip2.png)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319317630231/mceclip3.png)**4. Em seguida, ainda em Serviços Globais, acesse o Perfil, dê duplo clique sobre o perfil que verificou anteriormente, vá na aba**Acesso a campos**, selecione a Tabela **PFUNC**:   
  
É importante que sempre verifique que o módulo utilizado, neste caso é importante que esteja no módulo **Folha de Pagamento**:  
 **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319362431767/mceclip4.png)  
  
5.** Desmarque a opção **Pode Alterar  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9319425967127/mceclip5.png)**Após todos esses processos realizados, os campos da tabela **PFUNC** serão apresentados para esse usuário na cor cinza, indicando que ele estará desabilitado para alteração, permitindo assim só a visualização do campos. É importante ressaltar que desabilitar o flag "Pode Alterar" conforme o exemplo acima, todos os campos da tabela ficarão desabilitados. Caso queira filtrar campos específicos, é necessário expandir a visualização para desabilitar o flag apenas dos campos desejados.
