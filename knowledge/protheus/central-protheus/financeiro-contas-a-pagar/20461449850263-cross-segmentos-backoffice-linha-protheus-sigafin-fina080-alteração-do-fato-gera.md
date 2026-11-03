---
article_id: 20461449850263
category: Financeiro - Contas a Pagar
content_hash: 5348e01650f4925128817b24f1aa90e7f725b1ec60f73cdd232a30858ae42b37
fetched_at: '2026-06-28T22:38:09.567018+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Alteração
  do fato gerador dos impostos IRRF/PCC
type: support-article
updated_at: '2024-01-10T12:19:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20461449850263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Altera%C3%A7%C3%A3o-do-fato-gerador-dos-impostos-IRRF-PCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20461449833111) Tempo aproximado para leitura: **00****:02:00 min** **Dúvida**Qual o impacto da alteração do fato gerador dos impostos depois de gerado o título?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Quanto a alteração do fato gerador de **IRRF/PCC**, orientamos a troca somente com o acompanhamento de um analista in loco.

Se essa troca foi realizada com este acompanhamento, o processo após o **Titulo/NF** já ter sido gerado, seria o seguinte para manter a integridade da base:

1 - Com o **cadastro do fornecedor** configurado para **retenção do IRRF** **na baixa**, cancelar a baixa do título no financeiro.

2 - Altere o **cadastro do fornecedor** para **retenção do IRRF** **na emissão**, campo **Calc IRRF** conteúdo 1 = Normal, do mesmo jeito que estava na entrada da NF.

3 - Faça o cancelamento da nota

4 - Altere o **cadastro do fornecedor** para **retenção do IRRF na baixa**, ou seja, configurar o campo **Calc** **IRRF** com conteúdo 2 = IRRF Baixa

5 - Faça a entrada da nota

**Obs: Se não houve baixa do título no financeiro, desconsiderar o passo 1.**

Caso não seja possível o estorno da **NF/Titulo,** indicamos avaliar junto do analista in loco pontualmente o cenário.

**Importante:**

Não orientamos a troca do fato gerador com o sistema em andamento, pois pode ocorrer duplicidades.
