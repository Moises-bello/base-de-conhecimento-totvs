---
article_id: 37453982729751
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 8cd42c0f3ac27a593ab3bf10d94d08687bf6b09fe1c0d379ccad568e09854870
fetched_at: '2026-06-28T22:39:09.633488+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Nao respeita
  o tamanho do armazem via grupo de campo
type: support-article
updated_at: '2026-01-05T19:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37453982729751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Nao-respeita-o-tamanho-do-armazem-via-grupo-de-campo
---

O campo "armazem" na rotina MATA340 do TOTVS Protheus deve ser alterado exclusivamente via Grupo de Campos 024, respeitando tamanho mínimo e máximo de 2 a 6 caracteres. Alterações diretas no campo são bloqueadas, e recomenda-se reinstalar as procedures após a modificação. Caso o problema persista, limpar o profiler do usuário pode ajudar.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37453982705303) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O pergunte "Do Armazem","Ate o armazem", no local de estoque na rotina MATA340 não respeita o tamanho inserido no dicionario via grupo de campos 024. Como resolver?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
O campo em questão se trata do armazem, esse campo pode ser alterado **apenas "VIA GRUPO DE CAMPOS"**, dessa forma, basta configurar no "**Grupo de campos 024"**, que a rotina e todas as demais tabelas vinculadas ao tamanho do armazem, vão ter o tamanho do armazem da forma que voce deseja respeitando o limite minimo e maximo de 2 a 6.

![grup.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37454309640855)

Essa alteração é exclusivamente via grupo de campos, pois dentro do do configurador a alteração apenas para o "campo em si" não é permitida ela é bloqueada, por isso não recomendo que façam via SX1 visto que existe o grupo de campo para o "Código do armazem".

Sugerimos a alteração de forma "Exclusiva".

Após a alteração é recomendado a reinstalação das procedures.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

## **Questões identificadas:**

* Se a alteração foi realizada com sucesso, mas a rotina ainda persiste em apresentar um tamanho diferente do configurado, é sugerido testar com outros usuarios, e caso seja especifico do usuario, a limpeza do profiler é recomendada [Framework - Linha Protheus - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)
