---
article_id: 29563567226775
category: SIGAEST - PROCESSAMENTOS
content_hash: df4d8bb65aa667c54801ade56d62cca4bad30717cb7adaa549193989f3e576a6
fetched_at: '2026-06-28T22:39:04.983332+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos
  deletando registro da SBF
type: support-article
updated_at: '2025-11-06T15:26:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29563567226775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-deletando-registro-da-SBF
---

O artigo aborda a questão de produtos zerados ou negativos sendo deletados da SBF ao executar o Refaz Saldos (MATA300) no TOTVS Backoffice (Linha Protheus). Para evitar isso, é necessário configurar os parâmetros MV\_NEGATBF para .T. e MV\_MT300NG para .F., reinstalar o Procedure 18 e processá-lo novamente. Isso permitirá recriar o SBF mesmo para produtos com saldo zerado ou negativo, evitando a exclusão física dos registros. Links adicionais são fornecidos para mais informações sobre procedimentos e movimentações no estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29563567216279) Tempo aproximado para leitura: **00:01:12 min**  
  
**Dúvida**  
Ao executar o Refaz Saldos (MATA300) alguns produtos zerados ou negativos são deletados da SBF. O que fazer para não deletar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No padrão, com o parâmetro **MV\_MT300NG** ativo e **Procedure 18** instalada, sempre que um endereço na hora do movimento ou durante o **Refaz Saldos ficar zerado (0) ou negativo (-1 em diante)**, ele de fato apaga de forma lógica do banco de dados, ele não ira SETAR o campo **D\_E\_L\_E\_T\_** com o conteudo = **\* ,** indicando que esta deletado, IRA simplesmente DELETAR o registro fisico!

### **Para não deletar registros na tabela SBF com saldo zero, basta configurar os seguintes parâmetros com as seguintes opções:**

MV\_NEGATBF = .T.  
MV\_MT300NG = .F.

Após ajuste, **reinstale o Procedure 18** e processe-o novamente para que ele recrie o SBF mesmo de produtos zerados ou negativos.

REINSTALAR não DESINSTALAR, saiba mais sobre o conceito de reinstalar a procedure e desinstalar aqui:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
