---
article_id: 13111238946327
category: eSocial - Parametrizador
content_hash: 48d0d5a7c67b2973c6e06a4770e973fdbc7cf185d4b6970dd3184e06b0459f89
fetched_at: '2026-06-28T22:47:06.293764+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O evento ''XXXX'' está lançado
  na folha de pagamento para o funcionário de identificador ''xxxx'', porém ele está
  relacionado nos parâmetros do eSocial'
type: support-article
updated_at: '2024-06-13T16:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13111238946327-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-evento-XXXX-est%C3%A1-lan%C3%A7ado-na-folha-de-pagamento-para-o-funcion%C3%A1rio-de-identificador-xxxx-por%C3%A9m-ele-est%C3%A1-relacionado-nos-par%C3%A2metros-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML dos eventos **S-1200, S-2399** e/ou **S-2299** apresenta a mensagem **Erro na validação do campo 'codRubr': O evento 'xxxx' está lançado na folha de pagamento para o funcionário de identificador 'xxxx', porém ele está relacionado nos parâmetros do eSocial (Eventos a desconsiderar e/ou Registros Inativos a Desconsiderar).**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro ocorre quando rubricas (eventos) que poderão ser desconsideradas na carga inicial do evento nos parâmetros do eSocial (Eventos a desconsiderar e/ou Registros Inativos a Desconsiderar).

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse, **Configurações | Parametrizador | eSocial | Eventos a Desconsiderar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13178487395735)

2. Ao acessar o parametrizador anterior mencionado, veja se consta algum evento e **avalie a necessidade da permanência** dele na aba e se enquadra nas **regras**.

3. Após a exclusão do evento no parâmetro, se o erro persistir, acesse **Administração de Pessoal | Eventos;**

4**.** Selecione o evento e clique em **Editar;**

5. Acesse a aba **Identificação**, e desmarque a flag de **Inativo.** Abaixo um exemplo da parametrização:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13178911459735)**

6. Após seguir as orientações acima, gere o XML e envie ao eSocial.  
  
**Saiba mais**  
Para mais informações sobre as regras acesse:

* [Eventos a Desconsiderar](https://tdn.totvs.com/display/public/LRM/Eventos+a+Desconsiderar)
