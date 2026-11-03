---
article_id: 21852387379607
category: Financeiro - Contas a Pagar
content_hash: 22ab2fcfc797235e7dee66b204824e56abbe0ca4401f50c2ea2a2c2307de4c6f
fetched_at: '2026-06-28T22:38:07.238783+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA050 - Rateio CTJ
type: support-article
updated_at: '2024-03-11T16:51:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21852387379607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Rateio-CTJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21852387358999) Tempo aproximado para leitura: **02:00 min** **Dúvida**Na inclusão do Contas a Pagar, os rateios devem aparecer na tabela CTJ?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**A tabela **CTJ**, refere-se a tabela de Critérios de Rateio (Rateio Externo) ao qual há a possibilidade de pré cadastrar um rateio para ser utilizado no momento da inclusão de um título de rateio.  
   
Para o **cadastro do Rateio** (**tabela CTJ**),  há duas possibilidades:  
   
1º) Pela rotina **modulo contábil (34) Atualizações**\**Rateios**\Rateios Externo ( CTBA120 ) através do módulo contábil, após esse cadastro poderá utiliza-lo no momento que efetuar um rateio através da opção rateio pré cadastrado.  
   
2º) Direto na **inclusão do contas a pagar**.  
   
A tabela **CTJ** é onde ficam gravados as configurações de rateios pré-configurados.

Para utilizar o rateio do **Contas a Pagar** com o **cadastro Rateio Externo**, os lançamentos padrão **511 e 512** podem ser cadastrados seguindo o modelo descrito na documentação abaixo:  
[Modelo de montagem do LP 511 - Contabilização OffLine (Rotina: CTBAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=397379594)

**Saiba Mais**

**[Rateio Múltiplas Naturezas com Desdobramento P11](https://tdn.totvs.com/pages/viewpage.action?pageId=80970953)  
[MP - SIGAFIN - Como utilizar rateio de múltiplas naturezas por Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022094831-MP-SIGAFIN-Como-utilizar-rateio-de-m%C3%BAltiplas-naturezas-por-Centro-de-Custo?source=search)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=266964562>  
<https://tdn.totvs.com/display/public/PROT/FIN0036_LPAD_Rateio_Externo_Contas_a_Pagar>  
<https://tdn.engpro.totvs.com.br/display/public/PROT/FIN0001_CPAG_Inclusao_contas_a_pagar_com_rateio>**
