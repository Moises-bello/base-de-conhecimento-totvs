---
article_id: 38125821037335
category: Materiais - Compras (SIGACOM)
content_hash: f3222c95a82e319d0924c0971d7285a87f8dc29f326e3254e35bbdc06bc50ec8
fetched_at: '2026-06-28T22:41:21.827587+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - InterFunctionCall:
  cannot find function PGCA020 in AppMap on __EXECUTE(APLIB090.PRW)'
type: support-article
updated_at: '2026-02-03T12:41:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38125821037335-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-InterFunctionCall-cannot-find-function-PGCA020-in-AppMap-on-EXECUTE-APLIB090-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38125804686359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao tentar abrir a rotina do Novo Fluxo de Compras, é gerado o erro ***InterFunctionCall: cannot find function PGCA020 in AppMap on \_\_EXECUTE(APLIB090.PRW) 14/11/2025 17:24:58 line : 735*** ou o **help NOFUNCW**  
**Problema: Opção não disponível no Protheus**  
**Função: PGCA020Called By \_\_EXECUTE**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38125821032727)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2310  
  
**Causa**  
O erro em questão ocorre pois foi configurada a função PGCA020 no menu do Compras para a rotina do Novo Fluxo de Compras. A função que deve ser utilizada é a PGCA010.  
  
**Solução**  
Acesse o cadastro de menu do compras e verifique como está cadastrada a rotina do novo fluxo de compras. A rotina correta é **PGCA010**e não PGCA020.  
   
Necessário adicionar ao menu do Compras a rotina **PGCA010**para acesso ao NFC via menu do Protheus. A partir do release **12.1.2410** a rotina estará no menu por padrão.  
   
**Exemplo**:  
![](https://tdn.totvs.com.br/download/attachments/680260500/image-2023-12-12_9-37-52.png?version=1&modificationDate=1702384673137&api=v2)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
