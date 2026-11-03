---
article_id: 360052073914
category: Encargos
content_hash: 8442db8cec0d0e83d32f3a4482969fef381993d91267a32d4bb66162053e2454
fetched_at: '2026-06-28T22:46:53.255506+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RM - FOP - SEFIP - Menu Editar e Distruibuir SEFIP não aparecem
type: support-article
updated_at: '2023-06-28T18:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052073914-RM-FOP-SEFIP-Menu-Editar-e-Distruibuir-SEFIP-n%C3%A3o-aparecem
---

**Dúvida**

Como habilitar os menus, editar e distribuir SEFIP?

**Ambiente**

RM - Folha de Pagamento - 12.1  
   
**Solução**

1 - Verifique se os parâmetros estão corretamente informados em **Configurações | Parametrizador |  Folha normal |  Tomador de serviço**, pois a flag "Utiliza tomador de serviços" deve estar habilitada para que a opção seja exibida, conforme imagem abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/9gNP0VU7hx0SxOKM8BWRR4dW0/?name=inline134933782.png)​  
  
2 - Verifique se o perfil vinculado ao usuário que está acessando o sistema tem as permissões concedidas conforme imagem abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/qQjohMz7KsRdOMPwcFoGwjXen/?name=inline1102464867.png)  
  
Obs: É necessário verificar o acesso no perfil vinculado ao usuário no módulo específico (Folha de Pagamento), conforme destacado acima.   
  
Passo a passo para conferencia de acesso:   
  
Módulo **Serviços Globais |  Segurança |  Usuários** Acima do botão de Editar/Incluir, altere o campo 'Sistema' para 'RH | Folha de Pagamento', localize o usuário desejado e edite o cadastro. Siga para a aba **Segurança**, e verifique em qual perfil está vinculado.  
  
Depois acesse:  
  
**Serviços Globais |  Segurança |  Perfis**, acima do botão de Editar/Incluir, altere o campo 'Sistema' para 'RH -Folha de Pagamento', Localize o perfil desejado e edite o cadastro >> Acesso a campos'.  
Libere a permissão nos itens:  
  
07.02.03.01 - Distribuir Sefip  
07.02.03.02 - Editar distribuição Sefip
