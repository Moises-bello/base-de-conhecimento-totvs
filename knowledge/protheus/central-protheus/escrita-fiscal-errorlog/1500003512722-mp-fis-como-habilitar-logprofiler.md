---
article_id: 1500003512722
category: Escrita Fiscal - Error.log
content_hash: 98d1bdb3e98dd25157e502f5ffdbf80090bd0602884ebbb58fc60d498e950e1f
fetched_at: '2026-06-28T22:39:32.892517+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: MP - FIS - Como Habilitar LogProfiler
type: support-article
updated_at: '2021-04-28T13:51:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003512722-MP-FIS-Como-Habilitar-LogProfiler
---

**Dúvida**  
Procedimentos de Como habilitar LogProfiler  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O log LogProfiler é o monitoramento de rotinas ADVPL, utilizado principalmente para detectar problemas de lentidão.   
  
Segue abaixo o procedimento para geração do log:

1. Primeiramente, pare o serviço do **Appserver**;  
2. Abra o arquivo appserver.ini deste Server e inclua, na seção do ambiente, o comando **LogProfiler=1.**

Exemplo:

|  |
| --- |
| [Environment]  ...  LogProfiler=1 |

3. Certifique-se que existe, no arquivo appserver.ini, na seção [General], a linha Consolelog=1.  
Se não tiver, insira esta linha;  
4. Na pasta Appserver, renomeie o arquivo console.log para console.bak;  
5. Reinicie o serviço do Appserver;  
6. Acesse apenas a rotina em que está ocorrendo a lentidão;  
7. Feche o Smartclient;  
8. Pare o serviço do Appserver;  
9. Renomeie o novo arquivo console.log gerado para console\_lentidao.log;  
10. Reinicie o serviço do Appserver;  
11. Envie os arquivos console\_lentidao.log e console.bak para o suporte avaliar.

**OBS**: Após habilitar o log, o ambiente deverá está exclusivo para geração do Log.
