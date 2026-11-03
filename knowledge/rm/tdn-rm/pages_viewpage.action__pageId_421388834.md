---
content_hash: 3adcce984a1c12f907a8291b766abb997adcc7c92ac31dd38b4c186586713324
fetched_at: '2026-06-29T00:09:19.225437+00:00'
page_id: '421388834'
product: rm
source: tdn-rm
title: Contabilização com valor zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388834
version: 9
---

Disponibilizado o atributo "Não validar valor contabilizado zero" no cadastro de [Evento Contábil](http://tdn.totvs.com/x/hcpEGQ)[,](http://tdn.totvs.com/x/hcpEGQ) de modo a permitir a visualização de partidas contábeis de valor zero durante o processo de contabilização de lançamentos financeiros e baixas de lançamentos financeiros. O atributo somente estará disponível para uso de eventos contábeis associados aos processos: Lançamento e Baixa.

**Assistente de Baixa de Lançamentos Financeiros**

Ao informar um evento contábil para o campo "Evento contábil default para todos os itens de baixa" e clicar no botão "Aplicar Evento", se o evento em questão estiver com o atributo "Não validar valor contabilizado zero" marcado, eventuais partidas com valor zero serão descartadas no processamento da baixa.

Ao informar um evento contábil para o campo "Evento contábil default para todos os itens de baixa", e clicar no botão "Carregar Contabilização", se o evento em questão estiver com o atributo "Não validar valor contabilizado zero" marcado, se houverem eventuais partidas com valor zero, será apresentado um alerta com o termo "A contabilização gerada pelo evento contábil possui partidas com valor igual a zero, e partidas com valor diferente de zero. Ao realizar a baixa serão salvo apenas as partidas com valor maior que zero".

Ao editar a contabilização do lançamento financeiro (tela compartilhada), e informar um evento contábil que tenha o atributo "Não validar valor contabilizado zero", se houverem partidas com valor zero, estas serão apresentadas. Se após a edição da contabilização, esta for confirmada com partidas com valor zero, será apresentado um alerta com o termo "Existe(m) partida(s) com valor zero". Ao avançar o processamento da baixa, eventuais partidas com valor zero serão descartadas.

**Cadastro de Itens de Baixa**

O status contábil do item de baixa poderá ter um dos valores: "Contábil" ou "Baixa Contábil", desde que tenha sido gerada contabilização durante o processamento.  
 Ao informar um evento contábil durante o processamento da baixa de lançamento financeiro, se este tenha o atributo "Não validar valor contabilizado zero", e nenhuma das partidas retorne um valor maior que zero, nenhuma contabilidade será gerada, e o item de baixa gerado terá status "Não Contábil".

**Serviço de Contabilização da Baixa**

Não serão salvos os registros no banco de dados quando o valor contábil dos Itens de Baixa estiverem vinculados ao Evento Contábil que retorne partidas com valor zero, somente irá ocorrer quando a contabilidade for gerada via Evento e o mesmo possuir o atributo "Não validar valor contabilizado zero". Ao contrário irá ocorrer exceção visto que não é possível salvar lançamentos com valor zero. Caso seja realizado qualquer alteração na contabilização através da edição do Item de Baixa não serão salvas.

**Inclusão de Lançamentos**

Ao incluir um novo lançamento pelo Educacional com bolsa 100%, se informado um evento contábil com o atributo "Não validar valor contabilizado zero", a contabilização de inclusão apenas apresentará as partidas geradas pelo evento contábil com valor 0 (zero), sem nenhum efeito na contabilidade.

**Tabelas utilizadas:**

FLANBAIXA - Itens de Baixa do Lançamento Financeiro  
 TEVENTOSCONT - Eventos Contábeis.   
    
   Informações Complementares

* [BT - Contabilização com valor zero](http://tdn.totvs.com.br/display/LRM/RMFIN00002_FIN_BT_Contabilizacao+Evento+Valor+Zerado_FIN000040?preview=/150635810/151192144/FIN_BT_Contabilizacao%20Evento%20Valor%20Zerado_FIN000040.pdf)
