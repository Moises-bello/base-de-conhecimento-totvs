---
article_id: 360035129974
category: RH - Banco De Horas
content_hash: 354980157e3ff2403a790d4a504c4779e5ee3976cac3ebfdf2e308d78a8e170a
fetched_at: '2026-06-28T22:44:54.259194+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Fechamento do Banco de Horas não está gerando os
  eventos para os resultados do ponto
type: support-article
updated_at: '2025-11-07T19:26:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035129974-RH-Linha-Protheus-PON-Fechamento-do-Banco-de-Horas-n%C3%A3o-est%C3%A1-gerando-os-eventos-para-os-resultados-do-ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722253679255) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**O que verificar quando o sistema não está processando o fechamento do banco de horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Acessar em **Atualizações > Cadastro de Funcionários > Funcionários** e verifique inicialmente no cadastro do funcionário os campos **B.H. p/Folha** (RA\_BHFOL) e **Acum. BH** (RA\_ACUMBH) na aba **Relógio Registrador**, estes campos precisam estar configurado com **SIM**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32698329921047)  
  
Além disso, verifique se possui os eventos com **Id de Ponto 023A** **e 024A** cadastrados e, com código para folha informado. Para auxilio no cadastro dos ID **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018706631-RH-Linha-Protheus-PON-Cadastro-dos-eventos-de-Fechamento-de-Banco-de-Horas?source=search)**  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[MP - PON - Como fechar o Banco de Horas por horas normais ou valorizadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011971991-MP-PON-Como-fechar-o-Banco-de-Horas-por-horas-normais-ou-valorizadas?source=search)
