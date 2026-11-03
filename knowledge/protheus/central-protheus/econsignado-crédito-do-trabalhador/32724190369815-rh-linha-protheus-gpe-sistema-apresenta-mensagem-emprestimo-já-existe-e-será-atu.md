---
article_id: 32724190369815
category: eConsignado (Crédito do Trabalhador)
content_hash: 03fd2d1792c9aab18e944a800692aa424403062891f62bf98d1ca3ec66193d65
fetched_at: '2026-06-28T22:43:07.136578+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Sistema apresenta mensagem "Emprestimo já existe
  e será atualizado"  - Econsignado MP(1.292/2025)
type: support-article
updated_at: '2025-06-11T15:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32724190369815-RH-Linha-Protheus-GPE-Sistema-apresenta-mensagem-Emprestimo-j%C3%A1-existe-e-ser%C3%A1-atualizado-Econsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32724184695447) Tempo aproximado para leitura: **02:00:00min** **Dúvida**Sistema apresenta mensagem "Empréstimo já existe e será atualizado"

**Ambiente**TOTVS RH - TOTVS RH (Linha Portheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Isso ocorre pois já foi realizada uma importação para aquele colaborador no qual as informações já foram gravadas na SRK, com isso o sistema sinaliza que com a nova importação o empréstimo vai ser atualizado.   
  
**1.** O colaborador de exemplo já possui na rotina de Histórico de Importação o registro do empréstimo referente a competência de Maio.   
Então na importação de Junho o sistema vai atualizar a SRK

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32725229162775)

**2**. Na rotina GPEM944 após a importação do arquivo, o sistema no campo observação apresenta a mensagem "Empréstimo já existe e será atualizado"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32725175364887)

**3**. Após GRAVAR o sistema atualiza a rotina de lançamentos futuros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32725229174295)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32725229175703)

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)  
[RH - Linha Protheus - GPE - Econsignado - Como incluir a rotina de Importação do arquivo Econsignado GPEM944](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32201275142295-RH-Linha-Protheus-GPE-Econsignado-Como-incluir-a-rotina-de-Importa%C3%A7%C3%A3o-do-arquivo-Econsignado-GPEM944)  
[RH - Linha Protheus - GPE - Provisionamento nas Férias referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32480529848087-RH-Linha-Protheus-GPE-Provisionamento-nas-F%C3%A9rias-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[RH - Linha Protheus - GPE - Importação do arquivo Crédito trabalhador mês atual - Econsignado MP(1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32576676990487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-do-arquivo-Cr%C3%A9dito-trabalhador-m%C3%AAs-atual-Econsignado-MP-1-292-2025)  
[RH - Linha Protheus - GPE - Provisionamento no Adiantamento referente ao Econsignado (Programa Crédito do Trabalhador MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32581967990935-RH-Linha-Protheus-GPE-Provisionamento-no-Adiantamento-referente-ao-Econsignado-Programa-Cr%C3%A9dito-do-Trabalhador-MP1-292-2025)  
[RH - Linha Protheus - GPE - Como consultar o Historico de Importação RUO Econsignado (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32579319541271-RH-Linha-Protheus-GPE-Como-consultar-o-Historico-de-Importa%C3%A7%C3%A3o-RUO-Econsignado-MP1-292-2025)
