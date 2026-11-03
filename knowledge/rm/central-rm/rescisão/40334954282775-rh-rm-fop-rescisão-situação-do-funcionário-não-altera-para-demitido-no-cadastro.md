---
article_id: 40334954282775
category: Rescisão
content_hash: 5cc1b68fccfed7717640355cc4f94ad6395b4b96f9fbbd65785ffe786f09d5df
fetched_at: '2026-06-28T22:46:54.107027+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Situação do funcionário não altera para demitido
  no cadastro da rescisão'
type: support-article
updated_at: '2026-05-08T19:27:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40334954282775-RH-RM-FOP-Rescis%C3%A3o-Situa%C3%A7%C3%A3o-do-funcion%C3%A1rio-n%C3%A3o-altera-para-demitido-no-cadastro-da-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40334914509847) Tempo aproximado para leitura: **00:01:32min**  
  
**Dúvida**  
Ao realizar o cadastro de uma rescisão para um funcionário, a situação não é alterada de Ativo para Demitido, permanecendo incorreta no cadastro de funcionários.  
  
**Ambiente**  
TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Este comportamento ocorre quando a data de demissão do funcionário pertence a um mês diferente da competência atual configurada no sistema.

A alteração automática da situação para Demitido no cadastro do funcionário só é efetivada quando a rescisão é calculada dentro do mês de competência vigente.

Caso a rescisão seja programada para uma competência futura, a situação permanecerá como Ativo até que a liberação de competência seja realizada para o respectivo período.

1. Verifique a competência atual do sistema;
2. Valide a data de desligamento informada na rescisão do funcionário;
3. Se a data de desligamento for posterior à competência atual, o cadastro da rescisão deverá ser feita somente após a virada de mês (Liberação de Competência), ou deverá realizar o processo de Rescisão Próximo Mês: [RH - RM - FOP - Rescisão próximo mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6496448675607-RH-RM-FOP-TRCT-Rescis%C3%A3o-pr%C3%B3ximo-m%C3%AAs)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337593756823)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40337593759895)

**Saiba Mais:**

[RH - RM - FOP - Liberação de competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060636393-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-compet%C3%AAncia)
