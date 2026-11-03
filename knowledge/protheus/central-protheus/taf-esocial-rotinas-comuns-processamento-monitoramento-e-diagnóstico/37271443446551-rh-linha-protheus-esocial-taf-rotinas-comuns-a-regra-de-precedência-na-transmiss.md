---
article_id: 37271443446551
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: a495bf80a70ef80c89c05e2afc42a36c264f668c89218ee86eed37d8b10dcb0f
fetched_at: '2026-06-28T22:45:20.871293+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - eSocial - TAF - Rotinas Comuns - A regra de precedência
  na transmissão de eventos não foi seguida. Eventos desse tipo não devem ser enviados
  para processamento em paralelo.
type: support-article
updated_at: '2026-06-22T21:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37271443446551-RH-Linha-Protheus-eSocial-TAF-Rotinas-Comuns-A-regra-de-preced%C3%AAncia-na-transmiss%C3%A3o-de-eventos-n%C3%A3o-foi-seguida-Eventos-desse-tipo-n%C3%A3o-devem-ser-enviados-para-processamento-em-paralelo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37271413114775) Tempo aproximado para leitura: 00**:01:28 min**  
  
**Ocorrência**  
Ao enviar várias mensagens de forma simultânea para o**eSocia**l, é retornada a seguinte mensagem: **A regra de precedência na transmissão de eventos não foi seguida. Eventos desse tipo não devem ser enviados para processamento em paralelo**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37271443433623)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Causa**  
A mensagem ocorre devido ao grande fluxo de envios de informações para o servidor do **eSocial,**ou o envio dos **leiautes** ocorreram de forma simultânea sem a ordem cronológica.   
  
**Solução**  
O **eSocial** controla a precedência no recebimento dos eventos por empregador e por empregado, conforme as regras definidas no **leiaute**, com o objetivo de garantir a integridade dos dados da empresa e dos trabalhadores.  
O primeiro evento a ser transmitido deve ser sempre o **S-1000 (Informações do Empregador/Contribuinte/Órgão Público)**. Após isso, devem ser enviados os eventos de tabelas.  
  
Esses eventos possuem uma particularidade, quando houver necessidade de envio de mais de um lote. O usuário deve aguardar a confirmação de sucesso do processamento de um lote antes de enviar o próximo, respeitando essa sequência.  
  
Além disso, para todos os tipos de eventos, é fundamental seguir a ordem lógica de envio, conforme as regras definidas no leiaute. No caso específico dos eventos de tabelas, a transmissão deve ocorrer lote a lote, de forma sequencial e por empregador.

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)  
selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
