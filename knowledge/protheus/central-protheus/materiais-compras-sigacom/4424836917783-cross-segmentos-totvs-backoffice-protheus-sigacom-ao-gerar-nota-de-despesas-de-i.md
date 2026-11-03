---
article_id: 4424836917783
category: Materiais - Compras (SIGACOM)
content_hash: bc155f2441bba1b116bc3ffe2f5afc22a4a5a3f110ab32a340c9124842699ff8
fetched_at: '2026-06-28T22:41:12.967850+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Ao Gerar Nota de
  Despesas de importação(MATA119) está trazendo Itens que não constam na Nota de Origem
  selecionada. '
type: support-article
updated_at: '2022-02-14T17:51:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424836917783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-Gerar-Nota-de-Despesas-de-importa%C3%A7%C3%A3o-MATA119-est%C3%A1-trazendo-Itens-que-n%C3%A3o-constam-na-Nota-de-Origem-selecionada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao Gerar Nota de Despesas de importação(MATA119) está trazendo Itens que não constam na Nota de Origem selecionada.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
  
**Causa**Esse incidente ocorre, quando o campo F1\_OK não é apagado ao Salvar a nota de Despesas de importação, assim podendo gerar duplicidade de itens de outras notas ao gerar uma nova nota de Despesa de importação.

No padrão do sistema , o campo F1\_OK é preenchido temporariamente na inclusão da nota de Despesa de importação e depois seu conteúdo é apagado conforme exemplo do gif abaixo:

![FI_OK.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4424834194711/FI_OK.gif)

**Solução**  
Recomendamos realizar os procedimentos abaixo e caso problema persista entrar em contato com equipe de Suporte.

1. Com um Analista que tenha conhecimento Técnico em Base/Apsdu é necessário realizar um backup do sistema e verificar se possui conteúdo no campo F1\_OK é recomendado apagar todo conteúdo do campo no ambiente de teste mediante a backup.

2. Se mesmo assim o problema persistir verifique por gentileza se o ambiente de teste está atualizado com as atualizações abaixo:

Verifique se o ambiente está atualizado com as atualizações abaixo e caso esteja realize um teste com as customizações desabilitadas pelas 2 formas encaminhadas abaixo:

**1. Rotinas e datas dos fontes envolvidos no processo**  
- Por favor, verifique se já foi realizado teste em ambiente de Homologação com os pacotes mais atuais a seguir:  
Acumulado COM - <https://tdn.totvs.com/pages/viewpage.action?pageId=522011099>  
LIB Atual -<https://suporte.totvs.com/portal/p/10098/download?e=989259>

***Importante:***Para esse teste é imprescindível desativar as customizações existentes no ambiente pelas duas formas (não somente pela chave IXBLOG=NORUN): [Desabilitar customizações através do catálogo de personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-MP-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-) *(Quando executar esse processo na tabela XX7 o campo X7\_STATUS deverá constar igual a 2)*  e [desabilitar através da chave IXBLOG = NORUN no Appserver do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292).

**2.Novo teste com as customizações desabilitadas**  
  
Inclua por gentileza uma nova Nota de importação e acompanhe se o campo F1\_OK será apagado ou não por gentileza na gravação da Nota de Importação.

Caso problema persista orientamos que entre em contato com equipe de Suporte, através da abertura de Ticket no Portal do Cliente enviado o passo a passo para a reprodução da questão no teste realizado em sistema padrão atualizado.

***Saiba Mais :***

[MP - SIGACOM - Como Lançar Despesas de Importação no Compras (MATA119) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024679951-MP-SIGACOM-Como-Lan%C3%A7ar-Despesas-de-Importa%C3%A7%C3%A3o-no-Compras-MATA119-?source=search)

[PÁGINA CENTRALIZADORA DO](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)[COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
