---
article_id: 360053753553
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: aeb1eaeb4d4323a8fb5ab5031f82bf3d28fc425d81a3a7ae37c177855a9c90ce
fetched_at: '2026-06-28T22:40:47.730319+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - ERRO: O valor
  ''xxxxxxx'' informado na coluna 2 para o campo Código da Conta Analítica (CHB_CODCTA)
  não existe na base de dados'
type: support-article
updated_at: '2025-06-13T17:32:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053753553-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-ERRO-O-valor-xxxxxxx-informado-na-coluna-2-para-o-campo-C%C3%B3digo-da-Conta-Anal%C3%ADtica-CHB-CODCTA-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

Ao importar o Lalur para o TAF o sistema apresenta o erro :

Erro 1- Linha 2 - O valor '52111003' informado na coluna 2 para o campo Código da Conta Analítica (CHB\_CODCTA) não existe na base de dados

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088594553)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**Situação é apresentada pois a conta contabil não foi encontrada no TAF CHB\_CODCTA

* Ao visualizar pela configurador veja que a tabela CHB é utilizada na rotina TAFA331

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088594713)

* Vejamos os dois campos CHB\_CODCTA e CHB\_CTACTB

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088594793)

* Campo CHB\_CODCTA  Código da Conta Analítica

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458414)

* Veja que ele é obrigatório porem não está configurado para apresentar no Browse

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088597113)

* Campo CHB\_CTACTB

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458514)

* Esta configurado para aparecer no Browse

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458534)

* Veja que o campo valida a existência da conta na tabela C1O

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458614)

* Ao acessar a [rotina TAFA331](https://tdn.totvs.com/pages/viewpage.action?pageId=269067209) o sistema só apresenta o Campo CHB\_CTACTB e nele o sistema busca se a conta existe na C1O

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087458714)

* Com isso caso a conta não exista na C1O o sistema irá apresentar o erro

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088597333)

A [C1O é o Plano de Contas Contábeis](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) que gera o Registro  J050 , ao gerar uma Revisão do  [Lalur](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-) a Tabela C1O  não e alimentada ,quem alimenta a C1O é a revisão de ECF , [ao gerar o J050 e o J051](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420)  
  
Diante disso necessário gerar uma revisão da ECF (gere com base no regime tributário de sua empresa), para gerar os registros  [J050 e o J051](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)

* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)

* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)

* [IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

Posteriormente revise se o sistema gerou corretamente as contas na [tabela C1O](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

Saiba mais

Para maiores informações, acessar o link: <http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>

Veja também : [MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)
