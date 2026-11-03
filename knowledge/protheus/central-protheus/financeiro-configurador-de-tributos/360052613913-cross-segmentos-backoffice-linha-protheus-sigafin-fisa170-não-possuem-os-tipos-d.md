---
article_id: 360052613913
category: Financeiro - Configurador de Tributos
content_hash: 7cafb4b5888b3880d2f9f40e1c498f25be9e4cd793d838225a7d673522635c15
fetched_at: '2026-06-28T22:37:46.051476+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Não possuem
  os tipos  de impostos ao criar uma regra de título, no campo  FKL_TIPO
type: support-article
updated_at: '2026-02-04T18:41:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052613913-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-N%C3%A3o-possuem-os-tipos-de-impostos-ao-criar-uma-regra-de-t%C3%ADtulo-no-campo-FKL-TIPO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38167995908503)***Tempo aproximado para leitura: **00:03 min.**  
  
**Dúvida**  
Ao criar uma regra no **Configurador** de impostos - **FISA170** - **Regra financeira** - **Regra de título** e ao selecionar/pesquisar os tipos de impostos, exemplos: (**FE- (FETHAB RETIDO), FC- (IAGRO/FACS RETIDO) e CID - (CID)** no campo**FKL\_TIPO** não aparecem**,** porém, eles se encontram **na tabela 05**na**SX5?**  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FISA170 - Todas as versões.  
  
**Solução**  
Acessar o módulo **Configurador** e cadastrar o conteúdo no parâmetro **MV\_TIPIMP para apresentar** os impostos **FE**- e **FC**- no campo **FKL\_TIPO**.  
![](https://totvssuporte.zendesk.com/attachments/token/lU0fNrpBbTGVwBUbvqUuMO2ep/?name=inline1612564377.png)​

Inclusão da **Regra de Título.**  
  
![](https://totvssuporte.zendesk.com/attachments/token/KK11EvXleBhBX6SIGjgcMVTt8/?name=inline-1537252945.png)​

**Importante**

Caso tenha um novo tipo que não exista na **tabela 05** da **SX5**, basta cadastrá-lo na tabela 05 da **SX5** e atualizar o conteúdo do parâmetro **MV\_TIPIMP**.
