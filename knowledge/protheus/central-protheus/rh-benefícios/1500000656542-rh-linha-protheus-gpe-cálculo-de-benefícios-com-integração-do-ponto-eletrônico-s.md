---
article_id: 1500000656542
category: RH - Benefícios
content_hash: 1e85a81a456df5824e5eae966fc5af55c93b985f4e1227779b5c0d2482d12d8d
fetched_at: '2026-06-28T22:44:03.583429+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de benefícios com integração do ponto eletrônico
  - SIGAPON
type: support-article
updated_at: '2025-10-20T12:43:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000656542-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-benef%C3%ADcios-com-integra%C3%A7%C3%A3o-do-ponto-eletr%C3%B4nico-SIGAPON
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26985073189143) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como realizar o cálculo de benefícios com integração do ponto eletrônico - SIGAPON?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para que o Sistema utilize como referência de cálculo a **Escala do Ponto (SIGAPON)**, é necessário configurar o parâmetro **MV\_USACPER=.F.**.  
  
Para configurar o parâmetro MV\_USACPER acesse o Módulo Configurador (SIGACFG) em **Ambiente> Cadastros> Parâmetros** (CFGX017):

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10272315966487)**

A integração também **possibilita informar vales diferentes para cada dia da semana,** dando um maior dinamismo para o cálculo. **![](https://tdn.totvs.com/download/attachments/536708194/image2020-2-12_21-7-5.png?version=1&modificationDate=1581552426170&api=v2)**

Além da alteração do parâmetro é necessário que o cadastro do funcionário tenha os campos **Turno de Trabalho, Regra de Apontamento e Sequência Inicial do Turno** informados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10273835309847)  
  
 **Importante:** Mesmo que o parâmetro MV\_USACPER esteja com o conteúdo .F. caso o sistema não consiga montar o calendário do ponto, será utilizado os **dias** **do cadastro de período** do **SIGAGPE.**-Se o MV\_USACPER for configurado com .F. será verificado a escala de horário a partir do **primeiro dia do mês** do cálculo até o último dia do mês. Por exemplo, no cálculo de Março 2022, será verificado a escala de horário do Ponto no SIGAPON do dia 01/03/2022 até o dia 31/03/2022. **Não será calculado conforme o período de Ponto.** Caso o funcionário não possua escala de horário, será utilizado o calendário do período do mês de cálculo.**Saiba Mais**[Parâmetro MV\_USACPER](https://tdn.totvs.com/pages/viewpage.action?pageId=839967848)[RH - Linha Protheus - GPE - Como abater as Faltas no cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028521832-RH-Linha-Protheus-GPE-Como-abater-as-Faltas-no-c%C3%A1lculo-de-Benef%C3%ADcios)  
[RH - Linha Protheus - GPE - Abatimento de faltas para os benefícios do roteiro BEN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003212641-RH-Linha-Protheus-GPE-Abatimento-de-faltas-para-os-benef%C3%ADcios-do-roteiro-BEN)
