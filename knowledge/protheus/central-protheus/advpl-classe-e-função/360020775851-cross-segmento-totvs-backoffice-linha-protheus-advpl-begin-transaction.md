---
article_id: 360020775851
category: ADVPL - Classe e Função
content_hash: ee2cddd6cc705dc9d008bd6959d6e1b8c1d77746efc0667d7660d10ec8fca0bb
fetched_at: '2026-06-28T22:40:14.490645+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Begin transaction
type: support-article
updated_at: '2026-02-06T14:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020775851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Begin-transaction
---

O artigo esclarece que, embora tecnicamente possível, não é recomendado utilizar controle de transação (Begin Transaction/End Transaction) em rotinas automáticas no TOTVS Protheus, pois pode causar conflitos, travamentos, deadlocks e comprometer a integridade dos dados, já que o sistema possui seus próprios controles internos. O uso dessas funções é estritamente proibido no Protheus.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21688717041815) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Rotina automática com controle de transação, pode utilizar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80

**Solução**

### **Visão Geral**

Uma dúvida comum em customizações que utilizam **ExecAuto** (Rotinas Automáticas) é a viabilidade de encapsular a chamada em um bloco de controle de transação (`Begin Transaction` / `End Transaction`).

Embora o AdvPL permita essa estrutura, o uso **não é recomendado** na maioria dos cenários de customização, visando preservar a integridade dos dados e a performance do ambiente.

### **Riscos e Impactos do Uso Indevido**

O uso excessivo ou incorreto de transações em customizações pode gerar os seguintes problemas:

* **Locks e Concorrência:** Uma transação aberta por muito tempo (ou que abrange muitos processos) mantém registros travados no banco de dados, causando lentidão para outros usuários e potenciais erros de *Deadlock*.
* **Conflito com o Padrão:** As rotinas automáticas da TOTVS já possuem, internamente, seus próprios controles de gravação. Abrir uma transação externa pode "concorrer" com as tratativas padrão, impedindo que o sistema gerencie corretamente o *Rollback* em caso de falha.

### **Pontos de atenção**

* `BeginTran()` **e** `EndTran()`**:** Estas funções tem uso **estritamente proibido** no Protheus.
* **Finalização de Thread:** No Protheus, uma transação deve ser aberta e fechada dentro do ciclo de vida da mesma *thread*. Finalizar uma *thread* sem encerrar a transação pode corromper dados.
* **Comandos de Gravação Forçada:** Evite o uso de `DBCommit()` ou `FKCommit()` dentro de blocos de transação customizados, pois eles forçam a gravação física no banco, ignorando a lógica de "tudo ou nada" da transação.

Salvo os casos em que houver exemplo de rotina automática com controle de transação mapeado (documentado), pois do contrário, irá concorrer com as tratativas da rotina padrão.

B*egin Transaction* encadeado, sempre vai garantir toda a transação, porém existem particularidades do Oracle, por exemplo, que sempre realiza o C*ommit* dos dados caso um comando de DDL seja executado dentro da transação (por exemplo, a criação e uma tabela temporária). Este é um comportamento do banco de dados, e não existe atuação no sistema.

Uma das rotinas chamadas também pode estar terminando a transação sem devolver o erro para o sistema. No Protheus, a finalização de uma transação deve, ao final, finalizar a *thread*.  
As rotinas também podem executar ações como [FKCommit](https://tdn.totvs.com/display/public/PROT/FkCommit++-+Executa+o+Flush) ou [DBCommit.](https://tdn.totvs.com/x/SIVc)

**Saiba mais**  
[Controle de transações](https://tdn.totvs.com/pages/viewpage.action?pageId=271843449)
