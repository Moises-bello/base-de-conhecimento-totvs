---
article_id: 14437829711383
category: Materiais - Compras (SIGACOM)
content_hash: fe07ab92566537a9393f2846a250855bc331ee930089416d7eec955417f145df
fetched_at: '2026-06-28T22:41:24.107746+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Protheus - Pagamentos
  - PIX - Cadastro Fornecedor
type: support-article
updated_at: '2023-05-08T13:22:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14437829711383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Protheus-Pagamentos-PIX-Cadastro-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:SS min** **Dúvida**

Como é realizado o relacionamento de Chaves PIX vinculadas ao cadastro de fornecedores ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12  
  
**Solução**

**Visão Geral :**

Pagamentos instantâneos (PIX) são as transferências monetárias eletrônicas na qual a transmissão da ordem de pagamento e a disponibilidade de fundos para o usuário recebedor ocorre em tempo real e cujo serviço está disponível durante 24 horas por dia, sete dias por semana e em todos os dias no ano.

As transferências ocorrem diretamente da conta do usuário pagador para a conta do usuário recebedor, sem a necessidade de intermediários, o que propicia custos de transação menores.

O PIX poderá ser transacionado de forma on-line e alguns bancos também estão disponibilizando a forma de comunicação do PIX através do modelo CNAB. O processo está preparado para trabalhar com o modelo de QR CODE Dinâmico.

**Fornecedores**

No cadastro de fornecedores, disponibilizamos uma nova tela para relacionamento de Chaves PIX vinculadas ao cadastro de fornecedores.

Em Outras Ações no cadastro de Fornecedores, a nova opção Chaves PIX, permite que se vinculem Chaves PIX ao mesmo, sendo que somente uma pode ser ativa por vez.

As chaves PIX não podem estar em uso em outro fornecedor, já que o DICT do Bacen garante esta integridade no sistema financeiro.

O sistema permitirá as chaves do tipo : e-mail, número de telefone celular, CNPJ/CPF e aleatória.

Esta nova tabela que armazenará as chaves Pix dos fornecedores (tabela F72) deve ter o mesmo compartilhamento da tabela de fornecedores (tabela SA2) do ambiente.

Para transferências PIX (Modelo 45) onde não se informam os dados PIX do fornecedor, são necessários os campos de Banco, Cod. Agência, Cta Corrente e Tp. Cta. For preenchidos, para que a transferência ocorra com sucesso.

Para maiores dúvidas sobre a utilização do processo financeiro, pode-se verificar juntamente ao suporte ao módulo Financeiro para maiores esclarecimento.

**Saiba mais :**

**[Pagamentos Instântaneos - FIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)**
