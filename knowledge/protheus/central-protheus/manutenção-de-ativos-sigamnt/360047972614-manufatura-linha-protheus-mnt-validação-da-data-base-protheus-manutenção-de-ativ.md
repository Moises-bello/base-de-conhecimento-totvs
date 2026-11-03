---
article_id: 360047972614
category: Manutenção de Ativos (SIGAMNT)
content_hash: 12e6cf94fbcb6a12f5bbdf03a25011130e29f613cbeb0707651e7f66e031d463
fetched_at: '2026-06-28T22:42:34.522469+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Validação da Data Base Protheus Manutenção
  de Ativos
type: support-article
updated_at: '2021-09-24T12:16:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047972614-Manufatura-Linha-Protheus-MNT-Valida%C3%A7%C3%A3o-da-Data-Base-Protheus-Manuten%C3%A7%C3%A3o-de-Ativos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como é realizada a validação da **Data Base** no módulo de **Manutenção de Ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A validação de campos de data sempre são realizadas em comparativo a **Data base** do **Protheus**. Como o produto não tem um campo **hora**, fica exclusiva a utilização da **Data Base** e **Hora da Máquina** para validações com controle de hora.   
  
Por esse motivo, as rotinas podem apresentar mensagens referente ao horário informado superior ao atual quando é retroagido a data do Sistema. Lembrando que o **Protheus** entende a **Data base** como data atual.  
  
**Exemplo**  
Se for alterada a data do **Protheus** para ontem e for digitada uma hora maior que a hora do computador, é apresentada a mensagem que não é possível realizar uma operação com data superior a do Sistema, em casos onde exista essa regra.   
  
Em situações como previsão de insumos, planejamento de **OS** **- Ordem de serviço** não vai existir essa situação pois trata-se de uma projeção.  
  
**Importante**  
A validação citada acima cabe em toda a extensão do produto, isto é, todos os módulos utilizam deste formato.
