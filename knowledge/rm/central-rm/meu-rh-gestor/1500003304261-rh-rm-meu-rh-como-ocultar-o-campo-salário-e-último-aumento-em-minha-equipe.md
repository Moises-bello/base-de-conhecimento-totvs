---
article_id: 1500003304261
category: Meu RH - Gestor
content_hash: 5d29dbea1ba588e2b6bb817057b97fc5d9e077a40708181ecc84272fc9472fbf
fetched_at: '2026-06-28T22:47:32.435686+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Como ocultar o campo salário e último aumento em Minha equipe
type: support-article
updated_at: '2024-10-15T18:14:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003304261-RH-RM-Meu-RH-Como-ocultar-o-campo-sal%C3%A1rio-e-%C3%BAltimo-aumento-em-Minha-equipe
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22218761552535)**Tempo aproximado para leitura**: 00:02:00 min**

**Dúvida**Como ocultar o campo salario e o último aumento do funcionário na Gestão do time?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Versão 12.1.32 ou superiores  
  
**Solução**  
Para solucionar essa dúvida, **existem duas opções**, realize os seguintes passos:  
  
**1° Opção:**  
1.  Acessar Serviços Globais > Segurança > Perfis > selecionar o Sistema : Folha de pagamento   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22219135288471)  
  
2.  Editar o Perfil vinculado ao usuário do Gestor que está acessando o Meu RH  > Acesso a Campos > Localize  a Tabela PFUNC  > Campo Salário :  
  
Retire as Permissões : Pode Consultar / Pode Alterar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22219080718871)  
  
**Importante:** Caso o usuário do gestor possua mais de um perfil , deve realizar a parametrização nos demais perfis**.**3.  Acessar o Meu RH o campo Salário não é exibido na Minha equipe

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22219135325591)  
  
**2° Opção:**Dentro do Perfil vinculado ao Gestor, ao invés de acessar a aba Acesso a Campos, acessar a aba Acesso a Menus e bloquear o menu **[19.02.01.12] Salário e Último Aumento** conforme print abaixo, obtendo o mesmo resultado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22219135355543)
