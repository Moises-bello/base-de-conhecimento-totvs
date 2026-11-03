---
article_id: 360009087511
category: Pessoas
content_hash: 445d797400fe75bbdc600932f55cf7391c3e158f3633f282915d7adc7b83afd3
fetched_at: '2026-06-28T22:47:24.023144+00:00'
product: rm
section_id: 1500000834861
source: central-rm
title: RH - RM - RHU - Situações para execução do processo de Unificar Pessoas
type: support-article
updated_at: '2025-05-06T21:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009087511-RH-RM-RHU-Situa%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-processo-de-Unificar-Pessoas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15869424981911) Tempo aproximado para leitura: 00:01:30 min****Dúvida**Quando pode ser executado o processo de unificar pessoas?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **Todas as versões**  
  
**Solução**A unificação de pessoas será aplicada somente para registro simples, cadastros que foram efetuados recentemente sem vínculos, uma vez que um dos registros possuem maiores vínculos, a unificação não será efetuada.  
  
**1 –** A Unificação funciona para registros simples, ou seja, registros que não tenham ramificações.

Exemplo:

* Aluno cadastrado em duplicidade (porém há somente o cadastro de aluno).
* Pessoa cadastrada no banco de talentos em duplicidade.

**2 –** A Unificação de registros com ramificações não pode ser realizada!

Exemplo:

* Aluno cadastrado com duplicidade, porém o aluno tem lançamentos de notas, vínculo com turmas, lançamentos financeiros, etc.
* Candidatos que tem cadastro em duplicidade, porém ambos os registros estão associados em processos seletivos diferentes ou participam de turmas de treinamentos, etc.
* Funcionários com lançamentos de movimentações de folha, etc...

Nestes casos não podemos, nem devemos interferir em registros filhos, principalmente de outros produtos, pois estaremos interferindo em regra de negócios que não são de nossa autoria.

**Importante**As tabelas que se relacionam com a tabela PPESSOA terão os registros agregados, desde que estes não violem as regras de integridade do banco de dados (Chave Primária e Estrangeira).

**Saiba mais**  
Para maiores informações, acesse:

- [RH - RM - RHU - Unificar pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014630691)
