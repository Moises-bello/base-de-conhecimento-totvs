---
content_hash: a9640eee5ae424454d8739a37e6c5d3aeff67ca2ef68685e6a2b1767f1cad322
fetched_at: '2026-06-29T00:09:26.659745+00:00'
page_id: '423938352'
product: rm
source: tdn-rm
title: Processos em que o relacionamento do participante é válido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938352
version: 2
---

É possível definir que no momento em que a contabilização é gerada pelo serviço de origem o Participante do SPED Contábil seja preenchido automaticamente na Partida.  
   
Para que esta funcionalidade seja realizada é necessário marcar em quais os Processos o Relacionamento do Participante será válido.  
   
Quando o Processo marcado for executado e a "data de contabilização" estiver dentro do período de Relacionamento, ao gerar a contabilização para a Contabilidade o campo "Participante (SPED Contábil) da Partida já será preenchido com o Participante.  
   
**Exemplo**  
   
-Foi criado o seguinte Participante:  
   
Tipo do Participante = Cliente/Fornecedor  
Cliente/Fornecedor = C00002 – Empresa de Software  
Tipo de Relacionamento = Matriz no Exterior  
Data início do relacionamento = 01/05/2010  
Data término do relacionamento = 31/05/2010  
Processos em que o relacionamento do participante é válido = Movimento  
   
-Ao gerar a contabilização realizada no dia 17/05/2010 de um *Movimento* para a Contabilidade o Participante criado será preenchido automaticamente na Partida.  
   
-Ao gerar a contabilização realizada no dia 26/04/2010 de um Movimento para a Contabilidade o Participante criado "não" será preenchido na Partida.  
   
-Ao gerar a contabilização realizada no dia 17/05/2010 de um *Lançamento Financeiro* para a Contabilidade o Participante criado "não" será preenchido na Partida.
