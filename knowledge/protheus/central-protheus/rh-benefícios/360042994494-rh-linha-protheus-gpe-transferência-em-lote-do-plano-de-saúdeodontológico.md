---
article_id: 360042994494
category: RH - Benefícios
content_hash: 678f8ac0ba3d336c157db8fd97aa6d1edad43e2671524a8c34efbbebedd72b52
fetched_at: '2026-06-28T22:44:04.806038+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Transferência em Lote do Plano de Saúde/Odontológico
type: support-article
updated_at: '2025-09-08T19:32:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042994494-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-em-Lote-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32646877340439) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a **Transferência em Lote** do Plano de Saúde ou Plano Odontológico?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Por meio desta opção é possível **transferir de uma só vez** todos os Funcionários de **Plano de Saúde/Odontológico**, sem ter a necessidade de efetuar a alteração manualmente para cada um.  
Quando for efetuada a alteração de Plano de Saúde/Odontológico, será gerado um registro no arquivo de **Histórico de Alterações de Planos (Tabela RHN)**.  
  
Para realizar a **Transferência em Lote**, realize os seguintes passos:

**1.** Realize a inclusão do novo Fornecedor nas tabelas de Fornecedores referente a Assistência Médica (S016) ou Assistência Odontológica (S017), conforme necessidade.  
No exemplo abaixo, foi incluído um novo Fornecedor de Assistência Médica na tabela S016:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646877343639)

**2.** Realize a inclusão do novo plano na tabela referente ao novo Plano de Saúde/Odontológico.   
No exemplo, foi incluído um novo plano na tabela S028 - Assistência Médica por Valor Fixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858404119)

**3.** O Funcionário está cadastrado no **Cód. Fornecedor 02 e Cód. Plano 15:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858405143)**

**4.** Para realizar a transferência, acesse **Atualizações> Benefícios> Plano de Saúde> Plano de Saúde Ativos>** clicar em **Outras Ações/Transferência em Lote:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858410775)

Preencha os parâmetros para a Transferência na opção **Perguntas:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858412695)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646877354775)

Neste exemplo, a alteração de Assistência Médica ficará da seguinte forma:  
- Fornecedor **02** para Fornecedor **01**  
- Plano de Saúde de Valor Fixo código **15** para código **14**  
- Período de Inicio do plano **05/2025**  
  
Execute a transferência na opção **Informações:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858414999)

Consulte o processamento na opção **Log de Processos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646877358103)**

**5.** Na rotina de **Planos Ativos** é possível verificar o novo plano, onde o Fornecedor, Código de Plano e Inicio foram **alterados**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646877361815)

**6.** Acesse **Atualizações> Benefícios> Plano de Saúde> Histórico Alterações de Plano,** para verificar o Histórico do plano anterior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32646858422679)

**OBS:** A rotina de transferência **não altera o tipo de plano**, apenas o código do mesmo tipo de plano, por exemplo, não é possível alterar o plano por Faixa Etária para um plano por Valor Fixo.

**Saiba Mais:**[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11223604924695-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-de-sa%C3%BAde)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11301756760855-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-coparticipa%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Documentações relacionadas a rotina de plano odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11245418684951-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-a-rotina-de-plano-odontol%C3%B3gico)
