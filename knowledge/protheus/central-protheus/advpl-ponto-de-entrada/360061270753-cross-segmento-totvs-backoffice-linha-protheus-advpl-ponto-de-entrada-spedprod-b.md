---
article_id: 360061270753
category: ADVPL - Ponto de Entrada
content_hash: 4f1fc80d30c45938cd31e68e2c451c90b4fc050c85eb26b4f85037a02e5227cd
fetched_at: '2026-06-28T22:40:11.593548+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL  - Ponto de Entrada
  SPEDPROD : Bloco C197'
type: support-article
updated_at: '2021-06-30T00:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061270753-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-SPEDPROD-Bloco-C197
---

**Dúvida**O Ponto de Entrada SPEDPROD permite alterar a alíquota do Bloco C197?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12

**Solução**O ponto de entrada não atende o requisito de alteração de alíquota para o bloco C197.

**Conceito do Ponto de Entrada SPEDPROD**Informo que este ponto de entrada foi criado para que o registro 0200 - Tabela de Identificação do Item (**Produtos e Serviços**). Este registro tem um campo de **alíquota de ICMS** (campo 12) e o ponto de entrada altera apenas o valor deste campo e deste registo.  
O ponto de entrada se baseia nos registros de movimentações para gerar as informações do registro de identificação do item e permite mudar a alíquota porque deve apresentar a **alíquota de ICMS** aplicável ao item nas operações internas.

**Recomendação Desenvolvimento**Os registros de movimento seguem as regras de tributação especifica da operação as informações de alíquota de tributos não pode ser alteradas em tempo de processamento na geração do arquivo. Nem mesmo para um registro de informações complementares.  
Assim este PE não atende a esta necessidade e não temos e nem podemos desenvolver um PE com estas características.  
  
**Saiba Mais:**  
[SPEDPROD - Retorna Array de Informações](https://tdn.totvs.com/pages/releaseview.action?pageId=6077114)
