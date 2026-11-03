---
article_id: 39819561736855
category: CIPA
content_hash: 0fd835e4b38cccebe63f4927873638411170788a782d6d2d6cf27e972a18dadb
fetched_at: '2026-06-28T22:47:37.642304+00:00'
product: rm
section_id: 1500001076482
source: central-rm
title: 'RH - RM - SMT - CIPA: Utilização do parâmetro "Consistir competência da Folha
  de Pagamento para definição de Membro CIPA"'
type: support-article
updated_at: '2026-04-17T12:46:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39819561736855-RH-RM-SMT-CIPA-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-Consistir-compet%C3%AAncia-da-Folha-de-Pagamento-para-defini%C3%A7%C3%A3o-de-Membro-CIPA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39819577357463) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o comportamento do sistema ao marcar o parâmetro **Consistir competência da Folha de Pagamento para definição de Membro CIPA** no parametrizador do módulo de Segurança e Saúde Ocupacional**?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - A partir da versão **12.1.2510**  
  
**Solução**  
No parametrizador do módulo de Segurança e Saúde Ocupacional (guia Opções | menu Parametrizador | Etapa CIPA) há o parâmetro "Consistir competência da Folha de Pagamento para definição de Membro CIPA".

![Parametro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39819670282135)

Ao marcá-lo a flag Membro CIPA no cadastro do Funcionário se comportará da seguinte forma:

* Com o parâmetro ***marcado:***

Selecionando esta opção, ao realizar a Apuração e Finalização da Eleição da CIPA ou a inclusão manual de Representantes, os funcionários eleitos somente receberão a definição de Membro CIPA (cadastro do funcionário) se a data de início de vigência for igual ou menor ao mês/ano de competência da Folha de Pagamento. Quando se tratar de um início em competência futura, ou se a data término de vigência da CIPA for menor que a competência da folha, os funcionários não receberão essa definição.

* Com o parâmetro ***desmarcado*****:**

Caso esta opção não esteja selecionada, ao realizar a Apuração e Finalização da Eleição da CIPA ou a inclusão manual de Representantes, os funcionários receberão a definição de Membro CIPA (cadastro do funcionário) independente da data de início de vigência em relação ao mês/ano de competência.  
  
**Saiba Mais**

Para maiores informações, acesse:

- [Parametrizador Segurança e Saúde Ocupacional](https://tdn.totvs.com/display/SSTPT/Parametrizador+-+SST)  
- [RH - RM - FOP - Ativação da flag Membro CIPA no cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413311208727-RH-RM-FOP-Ativa%C3%A7%C3%A3o-da-flag-Membro-CIPA-no-cadastro-do-funcion%C3%A1rio)  
- [RH - RM - SMT - Dúvidas frequentes: CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27279685429911-RH-RM-SMT-D%C3%BAvidas-frequentes-CIPA)
