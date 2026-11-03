---
article_id: 33258031690135
category: RH - Calculo Autonomo/Prolabore
content_hash: 0837a45c0679062aa0adf1f434cbf0922330609fba0cd21e1e916a48965b5015
fetched_at: '2026-06-28T22:43:15.182391+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Error Log ao realizar lançamentos para Autônomo
  ou Pró-Labore - on GPEA090MNT(GPEA090.PRX)
type: support-article
updated_at: '2025-09-15T12:51:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33258031690135-RH-Linha-Protheus-GPE-Error-Log-ao-realizar-lan%C3%A7amentos-para-Aut%C3%B4nomo-ou-Pr%C3%B3-Labore-on-GPEA090MNT-GPEA090-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33258031644951) Tempo aproximado para leitura: **00:02:00min**  
  
**Ocorrência**  
Ao realizar o lançamento de uma verba para Autônomo ou Pró-labore, é apresentado o Error Log  
**THREAD ERROR ([14936], Administrator, SRVAPP)   28/04/2025 09:27:46**  
**type mismatch on $  on GPEA090MNT(GPEA090.PRX) 28/03/2025 13:36:39 line : 704**  
  
**Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Causa**  
O erro ocorre pois no cadastro existem inconsistências no Cadastro.  
  
**Solução**  
Para solucionar essa ocorrência, realize as validações:  
- O Processo - Para Autônomo ou Pró-labore o processo deve ser 00003 ou 00004.  
- Campo SIt Fol - O campo SIT FOL / Cat. Func / Cod Processo e Salario NÃO podem estar oculto.   
- Categoria - As categorias a ser utilizada é A ou P.   
[RH - Linha Protheus - GPE - Como configurar os campos que serão apresentados no cadastro de Autônomos/Contribuinte Individual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009855832-RH-Linha-Protheus-GPE-Como-configurar-os-campos-que-ser%C3%A3o-apresentados-no-cadastro-de-Aut%C3%B4nomos-Contribuinte-Individual)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34944009438359)

**Saber Mais:**

[RH - Linha Protheus - GPE - Como efetuar desligamento de Autônomo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422800931735-RH-Linha-Protheus-GPE-Como-efetuar-desligamento-de-Aut%C3%B4nomo?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar um Autônomo MEI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035241534-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-MEI?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052067393-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-ou-Pr%C3%B3-labore?source=search)  
[RH - Linha Protheus - GPE - Alteração contratual de intermitente para indeterminado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003354442-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-contratual-de-intermitente-para-indeterminado?source=search)  
[RH - Linha Protheus - GPE - Onde alterar os dados cadastrais do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016407931-RH-Linha-Protheus-GPE-Onde-alterar-os-dados-cadastrais-do-funcion%C3%A1rio?source=search)
