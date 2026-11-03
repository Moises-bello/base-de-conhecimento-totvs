---
article_id: 4414531587479
category: Faturamento - Cadastros
content_hash: 07cbd155837f4e47d3cebefd2792509c35927a15e99b4c3d3092f5d478e67361
fetched_at: '2026-06-28T22:38:35.440556+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Configuração de Produto Inteligente.
type: support-article
updated_at: '2025-04-17T19:42:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414531587479-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-de-Produto-Inteligente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31493867396759) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como configurar e utilizar o Produto Inteligente no Pedido de Vendas (MATA410)?  
  
**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

1. Acesse o Módulo Estoque/Custos (04 - SIGAEST);
2. Acesse a rotina Configurador de produtos (MATA093), e inclua uma família de produtos;
3. Inclua as características da Família de produtos (MATA098);
4. Defina a fórmula com os fatores de multiplicação para cada característica (MATA098)

       Outras Ações > Formulas;
5. Inclua dois produtos do tipo MP (MATA010);
6. Retorne ao MATA093, e defina os dados padrões;

      Outras Ações > Dados Padrões;
7. Altere a disponibilidade para uso;
8. Gere os produtos, Outras Ações > "Gerar Autom";
9. Visualiza as estruturas criadas (MATA200). Verifique que o produto ABF1 respeitou o fator de multiplicação definido na característica;
10. Para utilizar o produto inteligente na rotina de Pedido de Vendas (MATA410), o campo Produto deve ser preenchido com o código definido na rotina Configurador (MATA093).

**Observação 1:** Ao utilizar o código inteligente nas rotinas, devemos digitar o código "Configurador"  
Caso ainda haja dúvida no processo de configuração ou erro na rotina, contate a equipe de Atendimento Estoque/Custos

**Observação 2:** Não é utilizado nas rotinas de Call Center

**Saiba mais:** [Configuração de Produto Inteligente](https://tdn.totvs.com/x/NhD7I)
