---
article_id: 8989164236311
category: Meu RH - Login
content_hash: 5ed9cef66039fee5121f7d86eca8ec6a269aa39c5fb141ebc936c72196170282
fetched_at: '2026-06-28T22:47:27.258234+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH -  Como habilitar ou desabilitar Alterar senha no proximo
  login de forma global
type: support-article
updated_at: '2026-01-16T15:18:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8989164236311-RH-RM-Meu-RH-Como-habilitar-ou-desabilitar-Alterar-senha-no-proximo-login-de-forma-global
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22320773226775) Tempo aproximado para leitura: **00:02:50 min**  
  
**Dúvida**  
Como habilitar ou desabilitar "Alterar senha no próximo login" de forma global?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
Para realizar essa parametrização de forma global *(para todos os usuários),* realize os seguintes passos:

1. Acesse a tela de Usuários no seguinte caminho: Serviços Globais > Segurança > Usuários

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8988336160151)  
  
2. Após isso, selecione quais usuários você deseja realizar a atleração e vá em **Processos e posteriormente** em **Alteração de Múltiplos Registros de Usuário:**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8988534209175)  
  
3. Na nova janela que será apresentada, selecione o campo Alterar senha no Próximo Login, e no campo valor de acordo com sua necessidade, de acordo com o seguinte template:

* Valor: "F", corresponde à false, onde o campo ficará desmarcado/desabilitado;
* Valor: "T", corresponde à true, onde o campo ficará marcado/habilitado;  
    
  ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8988700554007)

4. Após definir o campo e o valor que este irá receber, clique em Executar; e lhe será apresentado a janela de confirmação e conclusão do processo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8988879424535)  
  
**Importante**

Por se tratar de um campo lógico, este só permite dois valores, sendo os mencionado no tópico anterior (as letras "T" ou "F"). Caso você insira qualquer valor diferente desses valores mencionados, será apresentado uma mensagem de erro como a exemplo abaixo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8988935992087)

**Saiba Mais**

[**Cadastro de Usuários na MDI**](https://tdn.totvs.com/pages/viewpage.action?pageId=244425754)
