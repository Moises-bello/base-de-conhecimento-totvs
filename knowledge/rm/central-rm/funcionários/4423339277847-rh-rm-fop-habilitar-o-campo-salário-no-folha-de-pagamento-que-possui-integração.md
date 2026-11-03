---
article_id: 4423339277847
category: Funcionários
content_hash: abb73b2c2ef84f449b692e05aefc859532de8ca76ed22abf7801848771a2bdfe
fetched_at: '2026-06-28T22:47:03.352794+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Habilitar o campo Salário no Folha de Pagamento que possui
  integração com o módulo Gestão de Pessoas
type: support-article
updated_at: '2025-03-11T11:01:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4423339277847-RH-RM-FOP-Habilitar-o-campo-Sal%C3%A1rio-no-Folha-de-Pagamento-que-possui-integra%C3%A7%C3%A3o-com-o-m%C3%B3dulo-Gest%C3%A3o-de-Pessoas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00min****Dúvida**Como habilitar o campo Salário no **Cadastro do Funcionário | Salário / Jornada | Mensal** no módulo Folha de Pagamento que possui integração com o módulo Gestão de Pessoas?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9801685989271)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Primeiramente, verifique se utiliza a integração com o módulo Gestão de Pessoas. Sendo o caso, valide algumas situações:

1. Deve liberar as permissões através do módulo: **Serviços Globais | Segurança | Perfis | Sistema: Folha de Pagamento - aba Acesso a Campos.** Localize a tabela **PFUNC** e libere as permissões no campo **SALARIO**:  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9801832675607)**Atente-se ao perfil associado ao usuário. Caso não saiba qual perfil está associado ao usuário em questão, verifique em: **Serviços Globais | Segurança | Usuários | Segurança**e selecione o perfil desejado. O processo deve ser realizado para todos os perfis vinculados ao usuário.

2. Acesse o módulo: **Gestão de Pessoas | Configurações | Parametrizador |  Requisições - 1** e **desmarque** os parâmetros **Requisição obrigatória para alterar cargo e/ou salário** e **Requisição obrigatória para transferir e alterar dados funcionais**, conforme abaixo:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9801930937239)  
  
**Saiba mais**[RH - RM - FOP - Liberação e restrição de permissões de acesso a campos e menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414666224023-RH-RM-FOP-Libera%C3%A7%C3%A3o-e-restri%C3%A7%C3%A3o-de-permiss%C3%B5es-de-acesso-a-campos-e-menus?source=search)
