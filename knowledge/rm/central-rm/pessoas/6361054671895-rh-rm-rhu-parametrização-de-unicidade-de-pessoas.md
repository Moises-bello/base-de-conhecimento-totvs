---
article_id: 6361054671895
category: Pessoas
content_hash: d28e0c31cba116502cd66ae72d1fa7e503de9e7c29543e681dcfeee284786bdf
fetched_at: '2026-06-28T22:47:24.004559+00:00'
product: rm
section_id: 1500000834861
source: central-rm
title: RH - RM - RHU - Parametrização de Unicidade de Pessoas
type: support-article
updated_at: '2025-10-30T18:13:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6361054671895-RH-RM-RHU-Parametriza%C3%A7%C3%A3o-de-Unicidade-de-Pessoas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15869382445847) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Quais os tipos de parametrização para validar a unidade no cadastro de pessoas ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Todas as versões   
  
**Solução**

A unicidade de pessoas pode ser validada por:

**- Nome, Dt. Nascimento, CPF, Estado Natal e Cidade Natal:** Marcando este parâmetro, a validação da unicidade de Pessoas no sistema compara os campos Nome, Dt. Nascimento, CPF, Estado Natal e Cidade Natal com as pessoas já cadastradas no sistema. 

**- CPF:** Marcando este parâmetro, a validação da unicidade de Pessoas no sistema compara somente o campo CPF. Quando este campo for marcado o sistema solicita confirmação do usuário, informando a mensagem que o parâmetro 'CPF Não obrigatório' será desmarcado para todas as coligadas. E se o usuário confirmar a alteração, serão desabilitados os parâmetros 'CPF Não obrigatório' e 'Permitir CPFs duplicados'.

**Importante**

- Quando este parâmetro estiver marcado o campo Dt. Nascimento no cadastro de Pessoas não é obrigatório.  
- As próximas opções 'CPF obrigatório' e 'Permitir CPFs duplicados' ficam desabilitadas para alteração com a validação de unicidade por CPF.  
- CPF obrigatório: Marcando este parâmetro, no cadastro de Pessoas o sistema obriga o preenchimento do campo CPF.

Obs: Se a pessoa cadastrada for estrangeira (nacionalidade diferente de Brasileira), o sistema permite o cadastro sem informar o CPF

- Marcando o parâmetro 'Permitir CPFs duplicados', o sistema permite o cadastro de Pessoas diferentes com CPF's iguais.  
  
Para ter acesso a parametrização, acesse o menu **Configurações** | **Parametrizador** | **Selecione a etapa 07.00.00.01 - Validações** e valide.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26808034562199)

Saiba Mais

Para maiores informações, acesse:

- [RH - RM - RHU - Unificar pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014630691)

- [RH - RM - RHU - Situações para execução do processo de Unificar Pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009087511)
