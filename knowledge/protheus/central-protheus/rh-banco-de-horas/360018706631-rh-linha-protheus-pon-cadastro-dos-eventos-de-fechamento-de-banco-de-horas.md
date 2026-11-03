---
article_id: 360018706631
category: RH - Banco De Horas
content_hash: 0d0669c95f9a6b5eb9311816adc670a0ade2def402dd77ae76f204b58c444c19
fetched_at: '2026-06-28T22:44:54.195458+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Cadastro dos eventos de Fechamento de Banco de
  Horas
type: support-article
updated_at: '2025-09-16T12:56:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018706631-RH-Linha-Protheus-PON-Cadastro-dos-eventos-de-Fechamento-de-Banco-de-Horas
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34972321790103) Tempo aproximado para leitura: 00:01:00 min**  
Dúvida**Como cadastrar os eventos de Fechamento de Banco de Horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A rotina de **Fechamento de Banco de Horas** - PONM080, executa a baixa de acordo com os parâmetros solicitados.  
  
Todos os eventos que compõem o saldo (normal e/ou valorizado) das movimentações de Banco de Horas que, estão com o cadastro apontados em Banco de Horas, terão o impacto e serão fechados.  
  
Após a execução do processo de fechamento do BH, o Sistema leva para os resultados as verbas atreladas aos eventos de id de ponto **023A** e **024A**. Após subida aos resultados será possível a realização da integração do ponto com a folha.  
  
Veja os eventos responsáveis para o fechamento do banco de horas:  
**023A** - Fechamento de Banco de Horas Provento  
**024A** - Fechamento de Banco de Horas Desconto  
  
Estes dois eventos, **precisam obrigatoriamente ser cadastrados com vinculo de verba de folha,** ou seja, esta é uma exigência para que as movimentações do banco de horas suba aos resultados terá esta obrigatoriedade cadastral.  
  
Para isto, acesse o cadastro de eventos, em **atualizações - cadastro do ponto - eventos**, veja exemplo dos cadastros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649622423831)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649633853591)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649633855639)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31649622427927)  
  
Cabe lembrar que, os eventos são obrigatórios para cadastro e uso do banco de horas, caso não estejam configurados comprometerá o processo de fechamento do Banco de horas e subida dos totais dos saldos positivos e negativos nos resultados.  
  
****Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)**[RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas)  
[RH - Linha Protheus - PON - Como levar apenas o Saldo de Banco de Horas para os Resultados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059545133-RH-Linha-Protheus-PON-Como-levar-apenas-o-Saldo-de-Banco-de-Horas-para-os-Resultados)  
[RH - Linha Protheus - PON - Como configurar o fechamento do banco de horas, para levar apenas as horas excedentes para a folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013448452-RH-Linha-Protheus-PON-Como-configurar-o-fechamento-do-banco-de-horas-para-levar-apenas-as-horas-excedentes-para-a-folha-de-pagamento)  
[RH - Linha Protheus - PON - Configuração para que as horas sejam apuradas no Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013674751-RH-Linha-Protheus-PON-Configura%C3%A7%C3%A3o-para-que-as-horas-sejam-apuradas-no-Banco-de-Horas)  
[RH - Linha Protheus - PON - Como efetuar a reabertura do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19383612807319-RH-Linha-Protheus-PON-Como-efetuar-a-reabertura-do-banco-de-horas)  
[RH - Linha Protheus - PON - Como zerar o Banco de Horas sem realizar o pagamento ou desconto das horas em Folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013456932-RH-Linha-Protheus-PON-Como-zerar-o-Banco-de-Horas-sem-realizar-o-pagamento-ou-desconto-das-horas-em-Folha)
