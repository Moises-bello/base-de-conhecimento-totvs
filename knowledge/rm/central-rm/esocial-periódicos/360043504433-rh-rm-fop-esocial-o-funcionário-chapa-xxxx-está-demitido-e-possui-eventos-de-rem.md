---
article_id: 360043504433
category: esocial - Periódicos
content_hash: 4230450663cfd33fc417d5437af60321e69cf764a3ef3772a337061c8f93beb4
fetched_at: '2026-06-28T22:47:09.440301+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - O funcionário chapa 'xxxx' está demitido e possui
  eventos de remuneração que não se referem a pagamentos de dissídio ou convenção
  coletiva
type: support-article
updated_at: '2024-06-18T11:57:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043504433-RH-RM-FOP-eSocial-O-funcion%C3%A1rio-chapa-xxxx-est%C3%A1-demitido-e-possui-eventos-de-remunera%C3%A7%C3%A3o-que-n%C3%A3o-se-referem-a-pagamentos-de-diss%C3%ADdio-ou-conven%C3%A7%C3%A3o-coletiva
---

**Ocorrência**Ao gerar o evento S-1200 de rescisão complementar para funcionário demitido ocorre o erro: O funcionário chapa 'xxxx' está demitido e possui eventos de remuneração que não se referem a pagamentos de "Dissídio/Acordo Coletivo/ Convenção Coletiva ou Tipo F - Outras verbas de Natureza salarial ou não salarial devidas após o desligamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das versões 12.1.24.270 - 12.1.25.213 - 12.1.26.158 - 12.1.27.101  
  
**Causa**Este incidente ocorre pois a data de demissão é menor que o primeiro dia do período de apuração que está sendo processado, ou seja, o funcionário está demitido e possui verbas no envelope de pagamento na competência atual que não são referentes à acordo coletivo ou convenção coletiva. Funcionários demitidos só podem ter verbas no XML S-1200 na competência da rescisão original ou em competência anteriores a rescisão original. As verbas referente a rescisão complementar não serão as do envelope do funcionário e sim as verbas que estão nas abas 'Verbas geradas por diferença' e 'Detalhamento de verbas geradas pela diferença de férias (Envelope).

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Folha de Pagamento | Folha Mensal | Cancelamento**e cancele toda movimentação para o funcionário no mês;  
1.1. Cadastre um acordo coletivo ou utilize um acordo já cadastrado**;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058851633/mceclip0.png)

2. Acesse **Folha de Pagamento | Rescisão | Complementar**;   
2.1. Informe no campo **Dados do dissídio/convenção/acordo coletivo** o acordo cadastrado conforme passo 1.1 e avance o processo;  
3. Uma vez executada a rotina, basta gerar o evento **S-1200**em **eSocial | Gerar XML** (Eventos Periódicos). Dentro do grupo **infoPerAnt**, as informações do acordo e o valor serão gerados no grupo **ideADC** conforme exemplo abaixo.es

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058851993/mceclip1.png)

**Importante**Todas as verbas para funcionários demitidos deverão ser lançadas somente através da rotina de rescisão complementar, desta forma as verbas serão associadas ao acordo coletivo e serão geradas dentro do grupo **infoPerAnt**.  
  
**Saiba mais**Para mais informações sobre diferença salarial e verbas devidas após desligamento acesse:[TDN - Como gerar diferenças de desligamento que não são retificações?](https://tdn.totvs.com/pages/releaseview.action?pageId=419535619)[RM - eSocial - Pagamento de PLR para funcionário demitido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038007153-RM-eSocial-Pagamento-de-PLR-para-funcion%C3%A1rio-demitido)
