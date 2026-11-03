---
article_id: 21731369575319
category: Materiais - Compras (SIGACOM)
content_hash: 89e52d2493f64e6ed482d92cf9ac624fe4ba644595abf502fa0a8b86fa4092d8
fetched_at: '2026-06-28T22:41:24.344539+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quanto tempo demora
  para realizar a integração do Importador XML x TOTVS Transmite?
type: support-article
updated_at: '2024-04-02T18:41:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21731369575319-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quanto-tempo-demora-para-realizar-a-integra%C3%A7%C3%A3o-do-Importador-XML-x-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21731343709847) Tempo aproximado para leitura: **00:00:05min** **Dúvida**Quanto tempo demora para realizar a integração do Importador XML x TOTVS Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

O tempo de execução depende muito de como está parametrizado todos os seus schedules, porém existe uma API no portal que libera as notas e as mesmas são exportadas para o Protheus.  
  
**OBSERVAÇÃO**.: Caso as notas estejam "**Aguardando SEFAZ"** como demonstra na documentação abaixo o Protheus não irá conseguir importar as mesmas.

 

Como verificar o Status de Integração ERP no Portal do Transmite?   
  
**Duvida 4:** A integração não está ocorrendo e permanecendo com o status de integração ERP como "Pendente"  
[Importador XML X TOTVS Transmite - A integração não está ocorrendo, permanecendo com o status de integração ERP como "Pendente"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20341622133527)

**Duvida 5:** Quando os CTE's não estão sendo integrados e permanecendo com o status de integração ERP como "Pendente"  
[Os CTE's não estão sendo integrados, permanecendo com o status de integração ERP como "Pendente"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20342299956247-Cross-Segmentos-Totvs-Backoffice-Protheus-Importador-XML-X-TOTVS-Transmite-Os-CTE-s-n%C3%A3o-est%C3%A3o-sendo-integrados-permanecendo-com-o-status-de-integra%C3%A7%C3%A3o-ERP-como-Pendente)

Para conhecimento temos essa documentação onde demonstra **"ocorrências/Duvidas"** relacionado a integração e ao Importador XML.  
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - "Ocorrências/Duvidas" X "Soluções" do Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20524264821655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncias-Duvidas-X-Solu%C3%A7%C3%B5es-do-Importador-XML-x-TOTVS-Transmite?source=search)

**Exemplo:**

Fluxo para Integração entre Protheus e API para Importação de Recibos XML:

1 - Início do Fluxo:

* + A rotina **SHEDIMPTRA** é acionada no Protheus conforme agendamento ou condição específica.

2 - Verificação de Recibos Pendentes:

* O Protheus executa a rotina **SHEDIMPTRA**.
* Verifica se existem recibos pendentes.
* Se houverem recibos pendentes:
* + - Prossiga para o passo 3.
* Caso contrário:
  + - Prossiga para o passo 5.

3 - Download e Importação de XMLs:

* O Protheus realiza uma requisição à API para baixar os XMLs dos recibos pendentes.
* Os XMLs são baixados e importados para dentro do Protheus.
* Prossiga para o passo 6.

4 - Fila de Processamento para Recibos Pendentes:

* Caso a API não retorne recibos pendentes na primeira execução da rotina **SHEDIMPTRA**:
* O Protheus solicita arquivos à API para entrar em uma fila de processamento.
* O Protheus aguarda a próxima execução da rotina **SHEDIMPTRA** para verificar novamente os recibos pendentes.
* Prossiga para o passo 1.

5 - Final do Fluxo:

* A execução da rotina **SHEDIMPTRA** é concluída sem recibos pendentes.
* O fluxo termina.

6 - Final do Fluxo de Importação:

* Os XMLs dos recibos pendentes foram baixados e importados com sucesso.
* O fluxo termina.

Temos um documento que fala sobre o fluxo por completo: IX10 - Integração Importador XML x TOTVS Transmite - Linha Microsiga Protheus - TDN

**IMPORTANTE:** O tempo para que o Protheus realize a importação dos rquivos varia por conta da configuração do schedule e de como está a fila de processamento na API do portal do transmite.

***Saiba Mais :***

* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
