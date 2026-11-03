---
article_id: 360028244892
category: Gestão de Armazenagem (WMS)
content_hash: 3034190c557c7c789cbcc710ccd9e028800638b7ebf997096556874bc1b9fa34
fetched_at: '2026-06-28T22:45:48.099046+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Processo de Distribuição da Separação
type: support-article
updated_at: '2025-10-31T20:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028244892-Log%C3%ADstica-Linha-Protheus-WMS-Processo-de-Distribui%C3%A7%C3%A3o-da-Separa%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447105368599)*Tempo aproximado para leitura: **00:01:35 min****Dúvida**O que é o processo de distribuição da separação?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 12.1.16  
  
**Solução**Como o processo de **separação por onda** acaba juntando os pedidos de venda e disponibilizando-os para **expedição** na doca, se fez necessário um processo para permitir a **distribuição** na doca dessas quantidades aglutinadas, separando-as nas quantidades solicitadas de cada pedido de venda e direcionando para endereços dentro da doca como colmeias, para posterior montagem de volumes e expedição desses pedidos.  
  
Para atender a necessidade foi disponibilizado o processo de **distribuição da separação**, que gerenciará as quantidades de cada pedido e endereço destino que serão acondicionados os produtos.

* No cadastro **Serviços Vs Tarefas – WMSA070** - deve ser indicado se o serviço realiza distribuição de separação;
* O endereço destino da distribuição deve ser o mesmo para todo o pedido;
* O endereço destino informado só pode estar em uso por uma distribuição;
* A **Distribuição da Separação** somente é executada via coletor de dados através do programa WMSV040. A versão *desktop* permite apenas visualizar as distribuições de separação e monitorar o seu andamento.

Ao executar as ordens de serviço serão geradas as informações correspondentes a distribuição da separação, nas tabelas **D0D – Distribuição Separação** e **D0E – Distribuição Separação Item**, com as quantidades das movimentações e ao serem **finalizadas as movimentações**, serão atribuídas as quantidades separadas.  
  
**Importante**Este processo não realiza a alocação física do produto no endereço, ou seja, não gera saldo na tabela **D14 - Saldo por Endereço WMS** e registro de kardex na tabela **D13 - Movto Estoque por Endereço WMS** para o endereço utilizado na distribuição da separação. Por conta disso, neste processo da distribuição da separação **recomendamos** a utilização de endereços com estruturas físicas que não sejam utilizadas nos processos de endereçamento, a fim de evitar alocações indevidas de produtos.  
  
**Saiba mais**  
Assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
