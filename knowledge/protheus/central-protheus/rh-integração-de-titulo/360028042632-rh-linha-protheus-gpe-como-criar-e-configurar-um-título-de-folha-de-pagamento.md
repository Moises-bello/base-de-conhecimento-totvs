---
article_id: 360028042632
category: RH - Integração de Titulo
content_hash: a9dc7cdb09799ed742646066b4874c7181f34194bba8baf9a3abd829dd5fcece
fetched_at: '2026-06-28T22:43:36.213156+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar e configurar um título de folha de pagamento
type: support-article
updated_at: '2025-07-29T18:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028042632-RH-Linha-Protheus-GPE-Como-criar-e-configurar-um-t%C3%ADtulo-de-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33797533358231) Tempo aproximado para leitura: **00:01:30 min****

**Dúvida**Como criar e configurar um título de folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da Versão 12.  
  
**Solução**  
Para criar um título de folha de pagamento, realize os seguintes passos:  
  
1) Faremos como exemplo a geração do título de FGTS da folha de pagamento:

**ATENÇÃO:** As configurações demonstradas nos *prints* abaixo servem apenas para ilustrar o processo. Realize a configuração de acordo com a regra de negócio da sua empresa.

**-> Acesse Miscelânea / Títulos / Definição:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028337351)**

2) Clique no botão Definir título, será apresentada uma janela para configuração da verba e da tabela em que será realizada a busca da verba.  
Veja que a verba utilizada neste caso é a verba de depósito de FGTS mensal (ID 0018) e a tabela para busca é a tabela SRC, onde se encontram os valores de movimento do período em aberto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028340032)

**Atenção:** A legenda da  verba selecionada para geração deverá ser verde para que seja considerada na geração. Legendas vermelhas são consideradas como dedução do valor.

**Obs:** Importante atentar-se no momento da geração do título, na configuração da verba nesta definição. Se o movimento de folha esta aberto, a busca de verbas de folha deverá ocorrer na tabela **SRC (Movimento do período)** e caso o movimento de folha esteja fechado a busca será na tabela **SRD (Histórico de movimento)**.

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
