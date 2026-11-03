---
article_id: 17707437931031
category: Inspeção de Processos (SIGAQIP)
content_hash: cfdae83447ab97ef92db4e42bc6a3386c590e32ba6f0729f37cca953ae632731
fetched_at: '2026-06-28T22:42:25.845517+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Mensagem integração com Controle de
  Não Conformidade no APP Minha Produção
type: support-article
updated_at: '2025-04-03T17:24:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17707437931031-Manufatura-Linha-Protheus-SIGAQIP-Mensagem-integra%C3%A7%C3%A3o-com-Controle-de-N%C3%A3o-Conformidade-no-APP-Minha-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17707412775959) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Ao utilizar **SIGAQIP - Inspeção de Processos** no **APP Minha Produção** ocorre a mensagem **Integração com Controle de Não Conformidades ativa. Utilize o Protheus para informar as NCs e preencher ou editar o Laudo**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**A mensagem ocorre quando o parâmetro **MV\_QIPQNC - Define se haverá integração entre os ambientes de Controle de Não-conformidade e Inspeção de Processos (1=SIM / 2=NAO)**, está com conteúdo igual a **1 - Sim.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Altere o conteúdo do parâmetro **MV\_QIPQNC para 2 - Não** para **encerrar a ocorrência da mensagem**;  
2. Ou, caso mantenha o conteúdo do parâmetro **MV\_QIPQNC igual a 1 - Sim**, será **obrigatório** o preenchimento, edição e/ou alteração de Laudo **via Protheus.** Assim como o registro de **NC - Não Conformidade**.  
  
**Saiba mais**  
A mensagem ocorre quando o ambiente não está atualizado. Atualmente, conforme documentação [Manufatura - Linha Protheus - SIGAQIP - Funcionalidade e Interface do SIGAQIP no APP Minha Produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16255926887575-Manufatura-Linha-Protheus-SIGAQIP-Funcionalidade-e-Interface-do-SIGAQIP-no-APP-Minha-Produ%C3%A7%C3%A3o) esta funcionalidade faz parte do escopo do **SIGAQIP** no **APP Minha Produção**. O pacote de atualização está disponível em [Manufatura - Linha Protheus - SIGAQIP - Pacote de Atualização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12320591674519-Manufatura-Linha-Protheus-SIGAQIP-Pacote-de-Atualiza%C3%A7%C3%A3o).
