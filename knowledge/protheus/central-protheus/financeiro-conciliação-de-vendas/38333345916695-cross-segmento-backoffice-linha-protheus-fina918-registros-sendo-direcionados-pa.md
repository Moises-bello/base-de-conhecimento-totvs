---
article_id: 38333345916695
category: Financeiro - Conciliação de Vendas
content_hash: f640330ca72d7f8a89db6363c9f8008403e69333254123e50928204cbbb1aa0d
fetched_at: '2026-06-28T22:37:26.246893+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmento Backoffice Linha Protheus - FINA918 - Registros sendo direcionados
  para a aba não conciliados, o que validar
type: support-article
updated_at: '2026-02-11T19:25:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38333345916695-Cross-Segmento-Backoffice-Linha-Protheus-FINA918-Registros-sendo-direcionados-para-a-aba-n%C3%A3o-conciliados-o-que-validar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38333329217687) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
No conciliador SITEF, alguns títulos estão sendo direcionados para a aba “Não conciliados” após a importação do arquivo.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta.  
  
**Solução**  
Para solucionar a ocorrência, é necessário validar os pontos abaixo:  
  
**Relacionamento de campos SE1 x FIF x MEP para conciliação de pagamentos Software Express, Rede, Amex e Cielo.**  
Para os registros aparecerem na aba **Conciliados**ou **Conciliados Parcialmente,**os seguintes campos das tabelas **SE1**, **FIF**e **MEP**precisam ter o mesmo conteúdo.

|  |  |  |  |
| --- | --- | --- | --- |
| E1\_FILORIG | = | FIF\_CODFIL |  |
| E1\_DOCTEF | = | FIF\_NUCOMP | Se o MV\_BLADOC = .T. |
| E1\_NSUTEF | = | FIF\_NSUTEF | Se o MV\_BLADOC = .F. |
| E1\_PARCELA | = | MEP\_PARCEL | Se o MV\_USAMEP = .T. |
| MEP\_PARTEF | = | FIF\_PARCEL | Se o MV\_1DUP = A e MV\_USAMEP = .T. |
| E1\_PARCELA | = | FIF\_PARALF | Se o MV\_1DUP = A e MV\_USAMEP = .F. |
| E1\_PARCELA | = | FIF\_PARCEL | Se o MV\_1DUP = 1 e MV\_USAMEP = .F. |
| E1\_EMISSAO | = | FIF\_DTTEF |  |
| FIF\_CODAUT  FIF\_CODAUT  E1\_CARTAUT | =  =  = | E1\_CARTAUT  Em Branco  Em Branco | Verifica em ordem se alguma das condições atende para que o registro seja apresentado na aba conciliados. |

**Relacionamento de campos SE1 x FIF para conciliação de pagamentos PIX e Carteiras Digitais.**  
Para os registros aparecerem na aba **Conciliados** ou **Conciliados Parcialmente,**os seguintes campos das tabelas **SE1**e **FIF**precisam ter o mesmo conteúdo.

|  |  |  |
| --- | --- | --- |
| E1\_FILORIG | = | FIF\_CODFIL |
| E1\_DOCTEF | = | FIF\_NUCOMP |

**Relacionamento de campos FJU x FIF para conciliação de pagamentos PIX e Carteiras Digitais.**  
Para os registros aparecerem na aba **Estornados,**os seguintes campos das tabelas **FJU**e **FIF**precisam ter o mesmo conteúdo".

|  |  |  |
| --- | --- | --- |
| FJU\_EMIS | = | FIF\_DTTEF |
| FJU\_DOCTEF | = | FIF\_NUCOMP |

**Saiba mais**

[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877#Abas-5)
