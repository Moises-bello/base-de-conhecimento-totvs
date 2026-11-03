---
article_id: 360046818313
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: c5d9a768bc3aac8e1a08f2f12a47a6aea1eda3b9b89caadde0a5f7db619ef964
fetched_at: '2026-06-28T22:40:44.314219+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - I100 - Centro
  de Custo
type: support-article
updated_at: '2022-07-28T19:41:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-I100-Centro-de-Custo
---

**Dúvida**Como gerar o Centro de Custo na ECD?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da release 12.1.17

**Solução**

**Importante :** [ECD LEIAUTE 9 Modificação da chave do registro I051 X Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-MP-SIGACTB-ECD-LEIAUTE-9-Modifica%C3%A7%C3%A3o-da-chave-do-registro-I051-X-Centro-de-custo-)

**1-** Para gerar o ECD com Centro de Custo é necessário primeiramente, que o Centro de Custo esteja apurado.  
Veja como realizar a  [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

**2-**Após realizar apuração de resultado emita relatórios de centro de custo para verificar se o centro de custo apurados foram realmente zerados e o se o saldo gerado no centro de custo de apuração está correto.  
Link com a lista de relatórios por centro de custo no sistema: [Relatórios com Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817912-MP-SIGACTB-Relat%C3%B3rios-com-Centro-de-Custo)

* caso exista diferença de saldo dos relatórios de centro de custo será necessário revisar os movimentos existente para os centros de custo
* Caso o centro de custo possua saldo anterior , será gerado no arquivo
* Caso exista saldo anterior , movimento no período e ou saldo final com centro de custo em contas de ativo e passivo, será gerado no arquivo
* Sugerimos conferencia das tabelas abaixo e verifique o [COMPARTILHAMENTO DAS TABELAS(CQA, CQ0, CQ1,....CQ9 ,CTC,CTF)](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* As tabelas CTT ,CT1, CVD e CVN são tabelas do grupo de cadastro [(](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)[Caso ocorra o compartilhamento das tabelas que estejam divergente entre as demais tabelas do seu grupo, o sistema poderá eventualmente trazer informações incorretas ou até gerar erro. Não é recomendado esta prática.)](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)

CQA Fila de saldos  
CQ0 e CQ1 Saldos Planos de Contas  
CQ2 e CQ3 Saldos Centro de Custo  
CQ8 e CQ9 Saldos Totais por Entidade  
CT2 Lançamento contábeis

**3-**Deverá amarrar o Centro de Custo com a Conta Referencial através da rotina **CTBA020**, conforme imagem abaixo:

![CCPlanRef.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007140651/CCPlanRef.png)

* Verifique se a conta esta amarradas (plano de contas e plano referencia) a mesma “Nat Conta”
* Verifique se foi informado mais de uma vezes a conta referencial
* A Conta referencial foi informada mais de uma vez pois possui centro de custo diferentes ,somente nesta situação pode ser informada mais de uma vez a conta  referencial
* [ECD LEIAUTE 9 Modificação da chave do registro I051 X Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-MP-SIGACTB-ECD-LEIAUTE-9-Modifica%C3%A7%C3%A3o-da-chave-do-registro-I051-X-Centro-de-custo-)

Exemplo:  
   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 002  
   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 003  
   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 004  
  
<https://tdn.totvs.com/display/public/PROT/ECD0011_ECD+com+centro+de+custo>

**4-** Através do cadastro da visão gerencialCTBA161 - Os campos “Tipo de Saldo”  e “Identific” precisam estar preenchidos e informe um centro de custo 

* Verifique existe a mesma conta analítica informada 2 vezes nas visões gerenciais

**5-**Ao gerar a revisão pela **Central de Escrituração(CTBS001)**, deve-se selecionar a pergunta "Processa C. Custo" como Sim e nas perguntas sobre o Plano de Contas Referencial deverá informar o que realizou a amarração, conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065809374/mceclip0.png)

![CCCentralEsc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007140611/CCCentralEsc.png)

Ao gerar a revisão através da rotina CTBS001 >Verifique se as tabelas CSD e CSE geram informações

**Veja mais:**

* Tabelas ECD: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF)
* Pré-Requisitos para gerar o ECD: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-MP-SIGACTB-ECD-PR%C3%89-REQUISITOS-PARA-GERAR-)
