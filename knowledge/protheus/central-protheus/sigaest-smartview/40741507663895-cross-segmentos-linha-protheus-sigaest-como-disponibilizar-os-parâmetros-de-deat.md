---
article_id: 40741507663895
category: SIGAEST - SMARTVIEW
content_hash: 5d15070eadbc17aa57ff306c9daf1914ec62a47ec1a5f1e9b5fdc699c0f8cea1
fetched_at: '2026-06-28T22:38:47.115697+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmentos (Linha Protheus) - SIGAEST - Como disponibilizar os parâmetros
  de De/Até Armazém no relatório Posição de Estoque ESTSV020
type: support-article
updated_at: '2026-05-26T14:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40741507663895-Cross-Segmentos-Linha-Protheus-SIGAEST-Como-disponibilizar-os-par%C3%A2metros-de-De-At%C3%A9-Armaz%C3%A9m-no-relat%C3%B3rio-Posi%C3%A7%C3%A3o-de-Estoque-ESTSV020
---

A ausência dos parâmetros "De Armazém" e "Até Armazém" no relatório ESTSV020 via Smart View ocorre por falta da atualização do dicionário de dados. Para disponibilizá-los, é necessário baixar e aplicar o pacote acumulado mais recente do Backoffice, executar o compatibilizador UPPDISTR e validar os parâmetros no Smart View.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40741471728919) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
Como disponibilizar os parâmetros de intervalo de Armazém (De Armazém / Até Armazém) no relatório Posição de Estoque (ESTSV020) via Smart View?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A ausência dos parâmetros "De Armazém" e "Até Armazém" na tela inicial do relatório ESTSV020 ocorre quando o ambiente não possui a aplicação das atualizações do dicionário de dados contidas no pacote acumulado do módulo.

Para que os parâmetros sejam incorporados ao comportamento padrão do objeto de negócio do relatório (eliminando a necessidade de utilização de filtros manuais ou customizações), é necessário atualizar o ambiente com o pacote de expedidos mais recente.

**Passo:**

* Realize o download do pacote de acumulados mais recente do Backoffice no [Portal de Downloads da TOTVS.](https://tdn.totvs.com/pages/releaseview.action?pageId=522000602)
* Aplique o pacote de atualização em seu ambiente de homologação.
* Execute o compatibilizador **UPPDISTR** para que as alterações de dicionário e parâmetros sejam processadas no banco de dados.
* Após a conclusão do processo, acesse novamente o Smart View e valide a exibição dos parâmetros "De Armazém" e "Até Armazém" na rotina ESTSV020.

![Captura de tela 2026-05-26 105808.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40741471731479)

**Saiba mais:**

[**Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SmartView ESTSV020 - Como criar um filtro de Armazém no relatório Posição de Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40509981455767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SmartView-ESTSV020-Como-criar-um-filtro-de-Armaz%C3%A9m-no-relat%C3%B3rio-Posi%C3%A7%C3%A3o-de-Estoque)

[**Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos**](https://tdn.totvs.com/x/pwKQLg)
