---
content_hash: 2ad1a9c7dbc02cd79e7c6b26c83622560289b05c1971f7d011bc03b9df15dce8
fetched_at: '2026-06-29T00:10:07.701016+00:00'
page_id: '452719417'
product: rm
source: tdn-rm
title: Gerar XML
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+XML
version: 5
---

Neste módulo será gerada a estrutura de XML dos registros da Fila de Eventos para Integrar com TAF (Sistema da TOTVS responsável pela validação e transmissão dos dados para o governo).   
   
Além do que é dito acima, para os eventos que são relacionados aos funcionários, existirá a possibilidade de utilizar seleções de funcionários, onde poderá escolher os funcionários que desejar, ou apenas gerar os XML's já existentes na fila de eventos.  
   
Obs.: Os eventos serão considerados de acordo com a parametrização de execução do processo de Gerar XML.  
   
**Atenção:**  
Para considerar os Autônomos do Fluxus, o usuário deverá parametrizar o sistema conforme passos a seguir:

* Informar os eventos do tipo Provento/Desconto em: "Parametrizador | eSocial | [Autônomos e Externos 1/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719944)" e "Parametrizador | eSocial | [Autônomos e Externos 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=463823367)".
* Quando for gerar o XML confirmar o parâmetro: "Gerar Autônomos Fluxus/Externos".
* Para auxiliar o usuário na geração dos arquivos , poderão ser gravados vários Perfis de Parâmetros.
* Os Perfis gravados poderão ser reutilizadas nas próximas gerações.

   
Considerações importantes na geração dos arquivos:  
   
Eventos Iniciais  
Eventos de Tabelas  
Eventos Não Periódicos
