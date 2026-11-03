---
article_id: 30192023184279
category: Gestão organizacional
content_hash: 847b84924d090595b72a21bd3ef4c1d6ebf8e5cdd61072254eda598d548c97d6
fetched_at: '2026-06-28T22:47:22.241132+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - eSocial: S-2501 - Dúvidas quanto ao preenchimento do campo
  ''Sequencial'''
type: support-article
updated_at: '2026-06-01T12:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30192023184279-RH-RM-RHU-eSocial-S-2501-D%C3%BAvidas-quanto-ao-preenchimento-do-campo-Sequencial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30192029662231) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Quando deverá ser utilizado o campo 'Sequencial' presente no cadastro dos Tributos dos Processos Trabalhistas (S-2501)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2402.245**, **12.1.2406.185**, **12.1.2410.121** e **superiores**.  
  
**Solução**  
O campo, denominado **ideSeqProc** (**Sequencial**), é utilizado para dar um controle de sequência dos registros de eventos S-2501, caso um mesmo processo trabalhista precise ser enviado várias vezes (em diferentes eventos S-2501). Isso pode ocorrer, por exemplo, quando as informações são extensas e precisam ser divididas em partes. Cada uma dessas partes é chamada de "sequencial".

O valor deste campo deve ser único dentre os eventos S-2501 que possuem o mesmo **nrProcTrab** (**Número do Processo Trabalhista**) e o mesmo **perApurPgto** (**Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença**). Ou seja, para o mesmo processo e período de apuração, cada evento S-2501 deve ter um número sequencial diferente neste campo. Isso evita a duplicação e garante que cada conjunto de dados de tributos seja único e identificado corretamente.

Além disso, cada CPF deve estar em um **Sequencial**. Isso significa que não poderá dividir as informações de um mesmo trabalhador em diferentes sequenciais e que cada sequencial do evento S-2501 deve conter as informações completas de diversos trabalhadores (CPF).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31401708318743)

Se o campo **ideSeqProc** não for preenchido, significa que todos os registros daquele número de processo, para um determinado período de apuração contemplará todos os CPFs existentes no S-2500.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31401708324503)  
  
  
**Importante**  
- O campo não deverá ultrapassar três dígitos numéricos.

- A definição de existir ou não um sequencial fica a cargo do cliente dada a volumetria de informações que necessitem ser enviadas ao governo.

**Saiba Mais**  
Para maiores informações, acesse:

- [Entenda o evento S-2501](https://tdn.totvs.com/pages/releaseview.action?pageId=929926219)

- [RH - RM - RHU - eSocial: S-2501 - Dúvidas quanto ao preenchimento do campo 'Sequencial'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30192023184279)

- [RH - RM - RHU - Processos Trabalhistas: Preenchimento indevido do campo 'Sequencial'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30198505796887)  
- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
