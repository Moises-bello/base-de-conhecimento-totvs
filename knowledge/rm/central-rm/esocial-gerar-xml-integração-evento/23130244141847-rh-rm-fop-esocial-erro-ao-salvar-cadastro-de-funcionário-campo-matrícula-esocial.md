---
article_id: 23130244141847
category: eSocial - Gerar XML/ Integração Evento
content_hash: d5d9c156000ffddcc0c24db18c954145d0851cac8a8a6eba0903b265066242ca
fetched_at: '2026-06-28T22:47:12.245338+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao salvar cadastro de funcionário: Campo ''Matrícula
  eSocial'' obrigatório'
type: support-article
updated_at: '2026-05-27T21:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23130244141847-RH-RM-FOP-eSocial-Erro-ao-salvar-cadastro-de-funcion%C3%A1rio-Campo-Matr%C3%ADcula-eSocial-obrigat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23130282261271) Tempo aproximado para leitura: **00:01:40 min**  
  
**Ocorrência**  
Ao salvar o cadastro do funcionário é retornado o erro abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23130244119191)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Este erro ocorre quando a flag Gerar matricula automaticamente na admissão de funcionário está marcada. Esta flag esta localizada em: RH/ Folha de Pagamento / Configurações / eSocial / Configurações Gerais 2/7

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23130244123671)

Além do parâmetro acima estar marcado, no cadastro do funcionário esta habilitado para que o campo matricula no cadastro de funcionário seja obrigatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23130402534935)

**Solução**  
Acesse: **RH | Folha de Pagamento | Funcionários ,** selecione uma chapa de um funcionário existente no produto. Após vá na aba **identificação** e clique com o botão direito e desmarque a flag **Preenchimento Obrigatório** no campo Matrícula eSocial, conforme o exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23130407569943)

Feito isso o erro será sanado e será possível cadastrar o funcionário para geração do evento S-2200.
