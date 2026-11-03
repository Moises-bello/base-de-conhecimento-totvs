---
article_id: 360058188054
category: Meu RH - Férias
content_hash: 034624f6c518f8430bfdd34af5cf004949ca06b37f5e1756b4db26cb8eb0b66e
fetched_at: '2026-06-28T22:47:31.724522+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Como desabilitar a Sugestão de Férias do Meu RH
type: support-article
updated_at: '2024-10-29T19:32:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058188054-RH-RM-Meu-RH-Como-desabilitar-a-Sugest%C3%A3o-de-F%C3%A9rias-do-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22161665050903) Tempo aproximado para leitura: 00:03:07 min**

**Dúvida**Como desabilitar a Sugestão de Férias pelo funcionário, porém, mantendo a visualização das férias ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.31  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**1º-** Acessar Serviços Globais:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27418826270359)  
  
**2º -** Acesse **Segurança | Perfis,** selecione o sistema Folha de Pagamento e edite o perfil vinculado ao usuário desejado. Clique na aba **Acesso a Menus** e **bloqueie** os seguintes acessos: 

* [19.01.06.09.01] Incluir Sugestão
* [19.01.06.09.02] Excluir Sugestão
* [19.01.06.09.03] Editar Sugestão

OBS: Para que o funcionário possa visualizar suas férias é necessário que a primeira etapa esteja habilitada 19.01.06.09 Caso contrario o menu de férias não será apresentado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27418826273303)  
  
  
**4º -** Após realizar este  bloqueio o usuário associado ao perfil modificado não conseguirá mais solicitar, editar ou excluir as sugestões férias, somente poderá consultar as que seu gestor marcar para ele. 

**Antes do bloqueio**

O subordinado consegue solicitar suas próprias férias e após a solicitação excluir, ajustar e consultar (ver detalhes.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416580460183)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416571250455)

**Depois do bloqueio**

O subordinado não consegue solicitar suas próprias férias e só consegue consultar (ver detalhes), das sugestões realizadas pelo seu gestor.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416566263063)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416580610839)

**Importante**

Caso queira permitir que o subordinado realize suas próprias sugestões de férias, basta permitir os acessos mencionados na etapa 02 desta documentação.

**Saiba mais**

[Solicitação de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=444616153)

[Recibo de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=528914699)

[Solicitar antecipação de férias](https://tdn.totvs.com/pages/viewpage.action?pageId=592547694)
