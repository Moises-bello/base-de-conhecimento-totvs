---
article_id: 20052910463767
category: SIGAEST - PROCESSAMENTOS
content_hash: 310e8fb58818c5a6ed374dbce820491bace0defe10cdd080d7886515bd9f196e
fetched_at: '2026-06-28T22:39:04.896607+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de Processamento.
  Saída no final: Favor atualizar a stored procedure e/ou rotina em questão.'
type: support-article
updated_at: '2026-02-26T20:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20052910463767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-de-Processamento-Sa%C3%ADda-no-final-Favor-atualizar-a-stored-procedure-e-ou-rotina-em-quest%C3%A3o
---

O erro "Erro de Processamento. Saída no final: Favor atualizar a stored procedure e/ou rotina em questão" no TOTVS Protheus ocorre devido a procedures desatualizadas. A solução é atualizar os acumulados, reinstalar as procedures indicadas e refazer o processo do início, conforme os links e orientações fornecidos no artigo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20052910459159) Tempo aproximado para leitura: **00:01:40 min**  
  
**Dúvida**  
O que fazer quando apresentar o erro: Erro de Processamento. Saída no final: Favor atualizar a stored procedure e/ou rotina em questão?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Esse problema pode ser apresentado em qualquer rotina de processamento, que faça utilização das procedures. Saiba mais aqui: [Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

**Exemplo do erro na rotina Acompanha Custos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20052910459415)

**Como corrigir esse erro:**

Em base teste efetue a atualização abaixo, caso esteja desatualizado:  
- [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)

- [Central de Atualizações Protheus](https://suporte.totvs.com/portal/p/10098/download?e=946864)

Após as atualizações, reinstale as procedures de 14 a 22 com o novo gestor conforme o boletim abaixo  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada e Incompatível, quais as diferenças? É possível utilizar as rotinas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas-?source=search)

Após Refaça um novo processo de fechamento do "ZERO".

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
