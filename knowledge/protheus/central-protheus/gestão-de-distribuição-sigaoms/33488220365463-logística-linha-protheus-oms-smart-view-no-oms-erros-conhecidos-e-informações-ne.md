---
article_id: 33488220365463
category: Gestão de Distribuição (SIGAOMS)
content_hash: 601968079126e489025e947131fba03e3c54814c1738b351bc8b56b1ee1b7995
fetched_at: '2026-06-28T22:45:51.041240+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Smart View no OMS, erros conhecidos e informações
  necessárias para análise do suporte
type: support-article
updated_at: '2025-07-24T22:02:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33488220365463-Log%C3%ADstica-Linha-Protheus-OMS-Smart-View-no-OMS-erros-conhecidos-e-informa%C3%A7%C3%B5es-necess%C3%A1rias-para-an%C3%A1lise-do-suporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33488245944599) Tempo aproximado para leitura: **00:02:06 min**  
  
**Dúvida**  
**Smart View** no **OMS**, quais erros conhecidos e informações necessárias para análise do suporte?  
  
**Ambiente**  
TOTVS Logistica - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.1.2310  
  
**Solução**  
No link abaixo, você encontrará respostas para as dúvidas mais comuns e orientações sobre erros na integração do **Protheus** com o **Smart View**.  
  
Essa seção foi desenvolvida para facilitar o acesso a informações importantes e auxiliar na resolução rápida de possíveis problemas:

* [FAQ - Protheus/Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=881560666)

Para a abertura de tickets para análise de erros, siga as instruções abaixo para coletar as informações do seu ambiente:  
  
Acesse a URL de diagnóstico (por padrão: <http://localhost:7019/diagnostic>).

* Localize a tag “**Caminho de log**”.
* Acesse o diretório indicado nesse caminho.
* Pare o serviço do **Smart View**.
* No diretório do *log*, renomeie os arquivos *.txt* e *.log* do dia atual.
* Em seguida, acesse o diretório principal do **Smart View** e entre na **pasta** ***logs***.
* Renomeie o arquivo *.txt* do dia atual nessa pasta.
* Inicie novamente o serviço do **Smart View**.Reproduza o cenário do problema.

Após isso, envie:

* Os arquivos ***.txt***e ***.log*** **do dia atual**, localizados no diretório indicado no **Caminho de log**;
* O arquivo ***.txt*** **do dia atual**, localizado na **pasta logs do diretório principal do Smart View**;
* O **inspetor de objetos** completo;
* Envie **evidências** ou **prints** de tela que mostrem claramente o erro ocorrido em seu ambiente.

**Importante**  
As atualizações dos relatórios são incluídas periodicamente no pacote acumulado do módulo **OMS**.  
Para acessá-lo, utilize o link: [Logística - Linha Protheus - OMS - Pacote Acumulado do TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008813881-Log%C3%ADstica-Linha-Protheus-OMS-Pacote-Acumulado-do-TOTVS-OMS)  
  
  
**Saiba mais**  
Para acompanhar as atualizações e novas liberações de relatórios no **OMS**, acesse o link abaixo:  
[Smart View - SIGAOMS](https://tdn.totvs.com/pages/releaseview.action?pageId=933155698)  
[Logística - Linha Protheus - OMS - Utilizando Relatórios Smart View no SIGAOMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32754099854487-Log%C3%ADstica-Linha-Protheus-OMS-Utilizando-Relat%C3%B3rios-Smart-View-no-SIGAOMS)  
[Logística - Linha Protheus - OMS - Relatórios Descontinuados – Migração para Smart View](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33479851538455-Log%C3%ADstica-Linha-Protheus-OMS-Relat%C3%B3rios-Descontinuados-Migra%C3%A7%C3%A3o-para-Smart-View)
