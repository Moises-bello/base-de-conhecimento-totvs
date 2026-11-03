---
article_id: 40308022741399
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 5a34b89040a1f4d124c9e3678c04db743ff55d0f8aecbf6ea3bd7525eb499ed1
fetched_at: '2026-06-28T22:40:32.606830+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBM300 - Cópia
  de saldos não considera todos os lançamentos
type: support-article
updated_at: '2026-05-07T19:05:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40308022741399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBM300-C%C3%B3pia-de-saldos-n%C3%A3o-considera-todos-os-lan%C3%A7amentos
---

A rotina de Cópia de Saldos (CTBM300) no TOTVS Protheus copia lançamentos contábeis conforme o campo CT2\_MLTSLD e o parâmetro "Método de cópia ?". Se configurado como "Cópia Simples", só são copiados registros com CT2\_MLTSLD vazio; se "Múltiplos Slds", apenas os com CT2\_MLTSLD preenchido. O campo é definido pelo Lançamento Padrão, que deve ser revisado para garantir a cópia correta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40308038216343) Tempo aproximado para leitura: **10 min**  
  
**Ocorrência**  
Ao executar a rotina de Cópia de Saldos (CTBM300) para copiar os valores entre os tipos de saldo, nota-se que nem todos os lançamentos contábeis são copiados para o destino.  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - a partir versão 12  
  
  
**Causa**  
O comportamento ocorre devido à regra de preenchimento do campo CT2\_MLTSLD (Múltiplos Saldos) nos lançamentos contábeis. A rotina de Cópia de Saldos (CTBM300) segue regras específicas para descobrir os saldos de destino, baseadas na configuração do parâmetro **"Método de cópia ?":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308022717335)

* Caso a pergunta **"Método de cópia ?"** esteja configurada com a opção **"Cópia Simples"**, somente serão considerados registros da tabela CT2 que estejam com o campo CT2\_MLTSLD vazio.
* Caso a pergunta **"Método de cópia ?"** esteja configurada com a opção **"Múltiplos Slds"**, somente serão considerados registros da tabela CT2 que estejam com o campo CT2\_MLTSLD preenchido.

O campo CT2\_MLTSLD é preenchido conforme a configuração do Lançamento Padrão (LP). No cadastro do LP, se o campo "Outras ações -> Múltiplos saldos" estiver preenchido com o tipo 1, o sistema entende que os registros contabilizados com essa LP serão copiados para o tipo de saldo selecionado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308038218647)

**Solução**

1. Avalie a configuração da pergunta "Método de cópia ?" nos parâmetros da rotina CTBM300. 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308022717335)
2. Verifique os lançamentos na tabela CT2 que não foram copiados e confirme se o campo CT2\_MLTSLD está preenchido ou vazio. 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40308038220439)
3. Caso aplicável ao seu cenário, revise a configuração do seu Lançamento Padrão (LP), verificando o preenchimento do campo "Outras ações -> Múltiplos saldos".

**Saiba mais:**  
[Como usar múltiplos saldos no Lançamento Padrão (CTBA080) e Cópia de Saldos (CTBM300)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019924132-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Como-usar-m%C3%BAltiplos-saldos-no-Lan%C3%A7amento-Padr%C3%A3o-CTBA080-e-C%C3%B3pia-de-Saldos-CTBM300)  
[CTBM300 - Cópia Simples](https://tdn.totvs.com/pages/viewpage.action?pageId=905630354)
