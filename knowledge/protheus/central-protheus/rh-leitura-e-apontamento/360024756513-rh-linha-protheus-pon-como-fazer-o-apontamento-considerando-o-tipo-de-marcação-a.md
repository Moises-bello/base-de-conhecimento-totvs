---
article_id: 360024756513
category: RH - Leitura e Apontamento
content_hash: e9c877996d4afefa51048e4aad784317bb843c2105d6916ea85d55a5eb3eb98f
fetched_at: '2026-06-28T22:44:45.913109+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Como fazer o apontamento considerando o Tipo de
  marcação - Apontamento por marcação
type: support-article
updated_at: '2025-10-07T20:38:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024756513-RH-Linha-Protheus-PON-Como-fazer-o-apontamento-considerando-o-Tipo-de-marca%C3%A7%C3%A3o-Apontamento-por-marca%C3%A7%C3%A3o
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31782648989463) Tempo aproximado para leitura: 00:01:30 min******Dúvida**Como fazer o apontamento considerando o Tipo de marcação - Período antes e após retorno do intervalo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para que o apontamento considere as marcações, é necessário alterar o cadastro do turno de trabalho vinculado ao funcionário. Para isso, siga as etapas abaixo:

- Primeiramente, verifique qual turno está vinculado ao funcionário para o período de apontamento aberto. Essa informação pode ser visualizada por meio da troca de turno. Veja mais detalhes na documentação sobre a troca de turno: [RH - Linha Protheus - PON - Como funciona a Troca de Turno dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios)

- Após visualizar o turno vinculado ao funcionário, acesse em **Atualizações > Cadastros Gerais > Turnos de Trabalho**, aba **Informações Ponto**, e altere o campo **Apon. Tip Mar** para **Sim**, e **salve**:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607354696343)**

Após salvar, ao acessar as rotinas de manutenções serão apontados os eventos com base nos tipos de marcações. Veja um exemplo de apontamento com uma escala 08:00-12:00-13:00-17:00:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29607330230679)

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho)
