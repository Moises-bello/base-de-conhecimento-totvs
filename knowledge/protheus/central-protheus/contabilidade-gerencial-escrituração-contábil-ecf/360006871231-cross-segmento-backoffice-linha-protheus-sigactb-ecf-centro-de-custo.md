---
article_id: 360006871231
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 97793c5f9988e7a662478037636035e6d9fdbb1866fe624976687a03b70889f5
fetched_at: '2026-06-28T22:40:47.330209+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Centro de Custo
type: support-article
updated_at: '2024-11-04T18:02:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871231-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Centro-de-Custo
---

**Dúvida**Para gerar a ECF com Centro de Custo, se faz necessário amarrar o Centro de Custo ao plano referencial e a Conta Contábil?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

**Importante (Impacta na ECF) :  [ECD LEIAUTE 9 Modificação da chave do registro I051 X Centro de custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003493582-MP-SIGACTB-ECD-LEIAUTE-9-Modifica%C3%A7%C3%A3o-da-chave-do-registro-I051-X-Centro-de-custo-)**

**[Bloco M - Geração Centro de Custo M300/M310](https://tdn.totvs.com/pages/releaseview.action?pageId=822682054)**

**1-** Para gerar o ECF com Centro de Custo é necessário primeiramente, que o Centro de Custo esteja apurado.

Veja como realizar a  [APURAÇÃO DO CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

Após realizar apuração de resultado emita relatórios de centro de custo para verificar se o centro de custo apurados foram realmente zerados e o se o saldo gerado no centro de custo de apuração está correto.  
Link com a lista de relatórios por centro de custo no sistema: [Relatórios com Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018817912-MP-SIGACTB-Relat%C3%B3rios-com-Centro-de-Custo)

* caso exista diferença de saldo dos relatórios de centro de custo será necessário revisar os movimentos existente para os centros de custo
* Caso o centro de custo possua saldo anterior , será gerado no arquivo
* Caso exista saldo anterior , movimento no período e ou saldo final com centro de custo em contas de ativo e passivo, será gerado no arquivo
* Sugerimos conferencia das tabelas abaixo e verifique o [COMPARTILHAMENTO DAS TABELAS(CQA, CQ0, CQ1,....CQ9 ,CTC,CTF)](http://tdn.totvs.com/display/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)
* As tabelas CTT ,CT1, CVD e CVN são tabelas do grupo de cadastro [(](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)[Caso ocorra o compartilhamento das tabelas que estejam divergente entre as demais tabelas do seu grupo, o sistema poderá eventualmente trazer informações incorretas ou até gerar erro. Não é recomendado esta prática.)](https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB)

**2-** Deverá amarrar o Centro de Custo com a Conta Referencial através da rotina CTBA020, conforme imagem abaixo:

![CCPlanRef.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007140651)

<https://tdn.totvs.com/pages/releaseview.action?pageId=284465420>

 A Conta referencial foi informada mais de uma vez pois possui centro de custo diferentes ,somente nesta situação pode ser informada mais de uma vez a conta  referencial

Exemplo:

   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 002

   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 003

   CVD\_CTAREF 11.10.1001  CVD\_CUSTO 004

**3-** Ao fazer a importação dos arquivos para o TAF, deve-se selecionar a pergunta "Processa C. Custo" como Sim na rotina de Central de Escrituração(CTBS001), conforme imagem abaixo:

![CCCentralEsc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007140611)

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)

**4**- Acesse a Rotina - TAFA061 (Cadastro de Centro de Custo) e veja que o centro de custo foi gerado , para mais detalhe **[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035548174-MP-SIGACTB-ECF-J100-COMO-GERAR-?source=search)**

Os passos anteriores referem-se a geração centro de custo para ECF**, para gerar o centro de custo** **ECF + Lalur****seguir os passos a seguir : [LALUR - Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046640714-MP-SIGACTB-LALUR-Centro-de-Custo?source=search)**

**Saiba mais:**

* Não gera Registro L210: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006856251-MP-SIGACTB-ECF-N%C3%A3o-gera-registro-L210)
* Tabelas ECF: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
* Parâmetro de Integração CTB/TAF: [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)
