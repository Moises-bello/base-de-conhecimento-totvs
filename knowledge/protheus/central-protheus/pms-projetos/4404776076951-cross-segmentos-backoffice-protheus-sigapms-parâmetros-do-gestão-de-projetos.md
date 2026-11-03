---
article_id: 4404776076951
category: PMS - Projetos
content_hash: a4afc61d66470ff679170adb5558cbd00e30a296a262802bd0afe349a8058cde
fetched_at: '2026-06-28T22:37:14.946377+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Parâmetros do Gestão de Projetos
type: support-article
updated_at: '2024-02-23T11:53:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404776076951-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Par%C3%A2metros-do-Gest%C3%A3o-de-Projetos
---

**Dúvida**

Quais são os principais parâmetros do Gestão de Projetos?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões

**Solução**

**Os principais parâmetros para Integração do Sigapms são :**

**MV\_INTPMS =S** Disponibiliza o botão na barra de menu das interfaces para que possa associar a um projeto.

**MV\_PMSTCOD:** Define como o código da EDT/Tarefa será informado pelo usuário ou o sistema irá calcular e preencher automaticamente. Conteúdo 1 manual, 2 automático.

**MV\_PMSIPC:** Define se utiliza a associação automática da nota fiscal de entrada quando o projeto tem solicitação de compras. Conteúdo 1 utiliza a associação automática, 2 não utiliza a associação automática (Default).

**MV\_PMSECOD:** Define como o código da EDT/Tarefa será de numeração sequencial único ou sequencia conforme o nível da estrutura que se encontra. Desde que o parâmetro MV\_PMSTCOD seja igual a 2. Conteúdo 1 estruturado e 2 sequencial

**MV\_PMSRBLQ:** Indica se o inicio de uma revisão será obrigatório para efetuar a alteração na estrutura do projeto.

**MV\_MOEDA1...5:** Titulo da moeda 1 a 5.

**MV\_PMSBXEM:** Indica se exibe ou não a tela de baixa de empenhos na amarração da NFE com o projeto. A tela de baixa de empenhos permite ao usuário selecionar o empenho que será baixado na entrada da NF (empenho gerado a partir de uma solicitação de compras amarrada ao projeto ou um planejamento) Este parâmetro é útil para empresas que não utilizam o controle de empenhos, facilitando a digitação da NF.

**Saiba mais em : <https://tdn.totvs.com/x/-bC2Hg>**
