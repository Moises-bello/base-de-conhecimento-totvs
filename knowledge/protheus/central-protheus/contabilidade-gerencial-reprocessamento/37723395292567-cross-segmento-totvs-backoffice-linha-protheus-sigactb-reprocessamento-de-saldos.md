---
article_id: 37723395292567
category: Contabilidade Gerencial - Reprocessamento
content_hash: 51c9852c702f5e344a08d9f08631b24fa8d9cab301f2c2333d385c41f8f4e3bc
fetched_at: '2026-06-28T22:40:42.026518+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Reprocessamento
  de saldos diferentes do Saldo 1 (Real) no Fechamento Contábil (CTBA960)
type: support-article
updated_at: '2026-03-20T14:44:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37723395292567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Reprocessamento-de-saldos-diferentes-do-Saldo-1-Real-no-Fechamento-Cont%C3%A1bil-CTBA960
---

**Dúvida**  
Como realizar o Reprocessamento de Saldos para tipos de saldo diferentes do "1 - Real" (como Orçado ou Gerencial) através da opção de ajuste de saldos na rotina de Fechamento Contábil (CTBA960)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - A partir da Versão 12.1.2410

**Solução**  
Para realizar o reprocessamento de saldos em um tipo diferente do "1 - Real" (padrão) na rotina CTBA960, é necessário definir o escopo de atuação logo no início do assistente (wizard) de fechamento.

Realize os seguintes passos:

1. Acesse a rotina **Fechamento Contábil (CTBA960)**;
2. Na etapa **1 - Parâmetros de fechamento**, localize o campo **Tipo Saldo**;
3. Altere a seleção para o tipo de saldo que deseja ajustar (Exemplo: "2 - Orçado", conforme demonstrado na imagem abaixo);
4. Clique no botão **Avançar**;
5. Siga o fluxo até a etapa 4 **-** Ajuste de Saldos;
6. Na aba ou seção de ajuste, clique em **Refaz Saldos** para processar a correção no tipo de saldo selecionado anteriormente.

**Importante** O sistema reprocessará apenas os movimentos e saldos correspondentes ao "Tipo de Saldo" selecionado nos parâmetros iniciais desta rotina. Para reprocessar o saldo Real novamente, será necessário reiniciar o processo selecionando a opção "1 - Real".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37733691080855)![]()![]()

**Saiba mais:**  
[CTBA960 - Fechamento Contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34334419010839-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Fechamento-Cont%C3%A1bil)  
[CTBA960 - Processo de atualização de saldos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36347421005975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA960-Processo-de-atualiza%C3%A7%C3%A3o-de-saldos)  
[Fechamento Contábil (SIGACTB)](https://tdn.totvs.com/pages/releaseview.action?pageId=722662924)  
[Correção automática de Saldos (CTBA980)](https://tdn.totvs.com/pages/releaseview.action?pageId=851295422&searchId=L9A7D3ETG)
