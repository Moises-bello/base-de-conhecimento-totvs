---
article_id: 29125283921687
category: Rental by ItUp Business
content_hash: 542c384af32f92462e97a355dedd086b4b7c8368005a4a301ccd766249ab08a5
fetched_at: '2026-06-28T22:36:20.687572+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Quando o campo B1_GRUPO está
  preenchido, o sistema não permite a edição do campo FPA_GRUA.
type: support-article
updated_at: '2026-04-09T12:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29125283921687-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Quando-o-campo-B1-GRUPO-est%C3%A1-preenchido-o-sistema-n%C3%A3o-permite-a-edi%C3%A7%C3%A3o-do-campo-FPA-GRUA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29125326405399) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
O Sistema não abre o campo FPA\_GUA (Equipamento), para edição ou preenchimento.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Causa**  
Quando for necessário realizar a locação de itens do estoque (sem o campo "**equipamento**" **FPA\_GRUA** preenchido) deve-se preencher no cadastro do produto o campo **Grupo** (**B1\_GRUPO**) e associar esse grupo ao parâmetro **MV\_LOCX014** desta forma o sistema entenderá que esses equipamentos não necessitam de um código de bem.  
  
**Solução**  
Cria o campo  **BM\_XACESS** na tabela **SBM** (**Grupo de produtos**) com as opções 1= Sim , 2= Não, para esse caso ele ignora o MV e considera o campo como fator de liberação e entendimento de produtos locados por quantidade.  
  
E deixe o campo **BM\_XACESS** com a informação igual a **2 - NÃO**

**![Captura de tela 2025-01-10 140259.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29125283875991)**

**Saiba Mais:** [***Abas - Locação***](https://tdn.totvs.com/pages/releaseview.action?pageId=895592955)
