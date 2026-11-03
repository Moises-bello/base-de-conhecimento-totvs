---
article_id: 9071036090007
category: RH - Tipos de Ausências
content_hash: 371bf0d05e2526b96a4adfd80b632414bb528838dade9f7346956e9156ba5e21
fetched_at: '2026-06-28T22:43:21.039717+00:00'
product: protheus
section_id: 360011967353
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o lançamento
  de ausências
type: support-article
updated_at: '2025-08-08T18:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9071036090007-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-lan%C3%A7amento-de-aus%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16007022027031) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os parâmetros utilizados para o lançamento de ausências?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Os parâmetros que envolvem o lançamento de ausências são:  
  
**MV\_AFASEAI** - Duração mínima do afastamento para envio por EAI.  
  
**MV\_CATNPGT** - Identifica as categorias que não deverão validar o numero de pagamento informado.  
  
**MV\_DIASPER** - Determina a quantidade de Dias do Período para Cálculo. ( **1** = Se o divisor será a quantidade de dias do mês do período; **2** = Se o divisor será sempre 30).  
  
**MV\_DTCGINI** - Parâmetro eSocial que determina a data que a carga inicial foi enviada para o governo e concluída.  
  
**MV\_DTFIMA** - Gerar evento S-2230 com Data Fim : **.F.** - Não gerar e **.T.** para gerar o evento S-2230 já com a data fim do afastamento  
  
**MV\_EFDAVIS** - Na ocorrência de inconsistência na eSocial **0** - Emite aviso; **1** - Avisa e impede processo; **2** - Não emite aviso.  
  
**MV\_FASESOC** - Responsável por gerenciar o faseamento do eSocial. **(Vazio)** - 1a Fase / **1** - 1a Fase + 2a Fase / **2** - 1a Fase + 2a Fase + 3a Fase  
  
**MV\_IORGGPE** - Define se haverá substituição de postos no módulo Gestão Pessoal - SIGAGPE ( **0** - sem substituição de posto; **1** - com substituição de posto)  
  
**MV\_MDTGPE** - integração do SIGAMDT com o SIGAGPE. Informar **S** = Sim ou **N** = Não  
  
**MV\_MDTPS** - Indica se o cliente é um prestador de serviço de medicina. Informar **S** = Sim ou **N** = Não  
  
**MV\_ORGCFG** - Configura o modo de uso do módulo Arquitetura Organizacional. **0** = Não utiliza; **1** = Utiliza com controle de postos; **2** = Utiliza sem controle de Postos.  
  
**MV\_RHTAF** - Habilita a integração de dados do eSocial com TAF. Se **.T.**, passa a integrar dados de eventos não periódicos do SIGAGPE com o SIGATAF.  
  
**MV\_TECXRH** - Define se o gestão de serviço esta integrado com Rh do Microsiga Protheus. Conteúdo padrão: **.F.**  
**MV\_TSREP** - Define se haverá integração entre o módulo Sigapon e o aplicativo TSA (Totvs Controle de Acesso). Conteúdo: **.T.** = Sim; **.F.** = Não.  
  
**MV\_VLDRG3** - Valida se está vigente o período de bloqueio da folha antes de incluir o afastamento.  
  
**MV\_VLESOC** - Versão do leiaute do e-Social. Preencher de acordo com o leiaute que está utilizando, conforme exemplo: 02\_05\_00 ou S\_01\_00\_00.

**Saiba Mais**[RH - Linha Protheus - GPE - Como Lançar Ausências para um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011457651-RH-Linha-Protheus-GPE-Como-Lan%C3%A7ar-Aus%C3%AAncias-para-um-Funcion%C3%A1rio?source=search)[RH - Linha Protheus - GPE - Como efetuar manutenção da Ausência após o fechamento do período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060779613)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEA240-Lançamentos de Ausências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5421742901399--RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEA240-Lan%C3%A7amentos-de-Aus%C3%AAncias?source=search)
