---
article_id: 360006983291
category: Contabilidade Gerencial - Relatórios Razões
content_hash: 1b17051a287c326dffc3ad616efc605cf6b37242928163ccaa63a01aba2eb926
fetched_at: '2026-06-28T22:40:41.089026+00:00'
product: protheus
section_id: 1500001548782
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR400: Lentidão na
  impressão'
type: support-article
updated_at: '2025-12-16T19:33:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006983291-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR400-Lentid%C3%A3o-na-impress%C3%A3o
---

**Ocorrência:**  
No módulo Contabilidade Gerencial - SIGACTB, durante a impressão do relatório Razão Contábil, é apresentada uma grande lentidão.  
  
**Ambiente:**  
Microsiga Protheus - Versão 12  
  
**Solução:**  
A correção desta inconsistência deve ser realizada seguindo as orientações abaixo:  
  
1- Efetue download do pacote disponível no <https://tdn.totvs.com/pages/releaseview.action?pageId=334342777>  
2- Após a aplicação do pacote, é necessário verificar o parâmetro MV\_CTBRAZB, configurando-o com ".T.", conforme instruções contidas em [documento.](http://tdn.totvs.com/pages/releaseview.action?pageId=372552940)

 3- Caso a estrutura do plano de contas estiver incorreta também pode ocasionar lentidão, com isso se faz necessário realizar a rotina CTBA170 conforme indicado na documentação :[MP - SIGACTB - CTBR040 - Criando Arquivo Temporário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440451-MP-SIGACTB-CTBR040-Criando-Arquivo-Tempor%C3%A1rio)

* [MP - SIGACTB - CTBA102 Lentidão envolvendo processos de contabilização ou atualização de saldos contábeis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006878452-MP-SIGACTB-CTBA102-Lentid%C3%A3o-envolvendo-processos-de-contabiliza%C3%A7%C3%A3o-ou-atualiza%C3%A7%C3%A3o-de-saldos-cont%C3%A1beis?source=search)
* [MP - SIGACTB - CTBR040 - Criando Arquivo Temporário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440451-MP-SIGACTB-CTBR040-Criando-Arquivo-Tempor%C3%A1rio?source=search)
* [MP - SIGACTB - Erro no arquivo temporário ao gerar relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016501852-MP-SIGACTB-Erro-no-arquivo-tempor%C3%A1rio-ao-gerar-relat%C3%B3rios-?source=search)
