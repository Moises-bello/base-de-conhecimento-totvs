---
article_id: 13254432727063
category: eSocial - Parametrizador
content_hash: d112cabeeeaf0c942debefd9d45fd98870a1b4598e53e6991f2f308563d0000a
fetched_at: '2026-06-28T22:47:06.285227+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O evento ''xxxx'' está configurado
  para o tomador de CPF ''xxxxxxxxxxx'', porém ele está relacionado nos parâmetros
  do eSocial'
type: support-article
updated_at: '2024-12-27T12:22:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13254432727063-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-evento-xxxx-est%C3%A1-configurado-para-o-tomador-de-CPF-xxxxxxxxxxx-por%C3%A9m-ele-est%C3%A1-relacionado-nos-par%C3%A2metros-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML dos eventos S-1200, S-2399 e/ou S-2299 apresenta a mensagem **Erro na validação do campo 'codRubr': O evento 'xxxx' está configurado para o tomador de CPF 'xxxxxxxxxxx', porém ele está relacionado nos parâmetros do eSocial (Eventos a desconsiderar e/ou Registros Inativos a Desconsiderar). Avalie a necessidade da utilização deste evento e ajuste a parametrização.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro ocorre quando a rubrica ou tomador de serviços está vinculado nos parâmetros **Eventos a desconsiderar e/ou Registros Inativos a Desconsiderar,** mas está sendo considerado no XML para envio ao eSocial.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse, **Configurações | Parametrizador | eSocial | Eventos a Desconsiderar;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13311623043479)

2. Após, avalie a necessidade de retirá-las para a correta geração do XML. Abaixo algumas validações que devem se atentar para que a verba não possa estar nos parâmetros:

* As rubricas do tipo **Provento** e/ou **Desconto** **são obrigatórias** para o eSocial. Caso sejam parametrizadas nesta etapa(Eventos a Desconsiderar), os xmls referentes a desligamento e/ou periódico (S-2299, S-2399 e S-1200) que possuírem essa rubrica serão gerados com erro.
* Não podem ser informados no campo **Eventos a Desconsiderar,** as rubricas do tipo **Base de cálculo** que possui código de cálculo ou alguma incidência.

3. Após seguir as orientações acima, gere o XML e envie ao eSocial.

**Saiba mais**  
Para mais informações sobre as regras acesse:

* [Eventos a Desconsiderar](https://tdn.totvs.com/display/public/LRM/Eventos+a+Desconsiderar)
