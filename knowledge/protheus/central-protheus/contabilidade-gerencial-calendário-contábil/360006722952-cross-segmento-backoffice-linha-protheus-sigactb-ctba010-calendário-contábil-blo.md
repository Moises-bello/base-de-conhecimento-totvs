---
article_id: 360006722952
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 1abe0509af6a2b7b8a0e70618452d16fe3d3af338d1accc92ccb885966116f9a
fetched_at: '2026-06-28T22:41:03.433443+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA010 - Calendário
  contábil bloqueado ou fechado.
type: support-article
updated_at: '2023-06-15T12:11:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Calend%C3%A1rio-cont%C3%A1bil-bloqueado-ou-fechado
---

**Dúvida**Como abrir período contábil bloqueado/fechado para movimentação?  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contábil – A partir da versão 11.80 **Solução**

Acessar a rotina Cadastro de calendário contábil (CTBA010) posicionar no período do calendário que esta bloqueado ou fechado, alterar e mudar o status para 1- Aberto.

* Bloqueio /Desbloqueio por processo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009782692)

|  |  |
| --- | --- |
| **Passo a passo:** | **Conceito status para o cadastro do calendário:**   * **1 -** Aberto: Indica que o período pode receber lançamentos normalmente; * **2 -** Fechado: Indica que o período já foi encerrado e **nenhum** lançamento pode ser efetuado. A extração de informações (relatórios e consultas) está disponível. Esse status é gerado automaticamente pela rotina Encerramento do Exercício; * **3 -** Transportado: Indica que o período já foi encerrado e transportado para uma base backup. **Nenhum** lançamento pode ser efetuado e a extração de informações (relatórios e consultas) não está mais disponível; * **4 -** Bloqueado: Indica que este período está temporariamente bloqueado para lançamentos contábeis. A extração de informações (relatórios e consultas) está disponível, bem como a geração de rotinas internas do módulo contábil;   **Conceito status para o bloqueio por processo:**   * **1 -**Aberto: Indica que o período pode receber lançamentos normalmente; * **2 -**Fechando: Indica que o período já foi encerrado e **nenhum** lançamento pode ser efetuado. Esse status é gerado automaticamente pela rotina Encerramento do Exercício; * **3 -**Transportado: Indica que o período já foi encerrado e transportado para uma base backup. **Nenhum** lançamento pode ser efetuado. * **4 -** Bloqueado: Indica que este período está temporariamente bloqueado para lançamentos contábeis. * **5 -** Período: Indica que o período já foi encerrado e **nenhum** lançamento pode ser efetuado. |
| **Observações:** | As rotinas internas do módulo de contabilidade (Ex. Apuração de Resultado) é executada normalmente quando o calendário esta com status bloqueado, ficando restrita para os status Fechado no calendário e Bloqueado/Período/Fechado para processo |

* Alterar o Status do calendário para aberto

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067654873)

Necessário para o correto funcionamento se faz necessário que as tabelas abaixo estejam com o mesmo compartilhamento

CTE - Moeda X Calendário  
CTG - Calendário Contábil  
CQD - Bloqueio do calendário Contábil   
CTO - Moeda cadastrada  
CTP - Cambio

Para mais detalhes verifique : <https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>

[MP - SIGACTB: Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)

Veja também :

[Tabelas utilizadas](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba010_tabelas.htm)

[MV\_CTBCTG - Bloqueio de Movimentação por Amarração Calendário X Moeda X Tipo de Saldo](http://tdn.totvs.com/pages/releaseview.action?pageId=49283869)

[Calendário contábil P12](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba010.htm)

[Moed. x Cal x Tip. Saldo](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba011.htm)

[Moeda x Calendário](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba200.htm)

[Bloqueio Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=253988018)

[CTBA102 - Permitindo inclusão de lançamentos mesmo com calendário bloqueado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14766971052951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-mesmo-com-calend%C3%A1rio-bloqueado-?source=search)
