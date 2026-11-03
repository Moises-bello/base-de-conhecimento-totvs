---
article_id: 360045473993
category: GPE - eSocial - Periódicos
content_hash: 2e404c65c1a9d3af26b0cf82b5b6eb6a3839a9adb4ef1b112326f0901848c909
fetched_at: '2026-06-28T22:45:08.662456+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 317
  - O trabalhador do CPF #39xxxxxxx#39; matricula #39xxxxxxx#39; devera encontrar-se
  ativo no periodo #39xxxx-xx#39'
type: support-article
updated_at: '2025-07-21T16:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045473993-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-317-O-trabalhador-do-CPF-39xxxxxxx-39-matricula-39xxxxxxx-39-devera-encontrar-se-ativo-no-periodo-39xxxx-xx-39
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27088637394967)** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**  
Descrição: O trabalhador do CPF #39xxxxxxx#39; matricula #39xxxxxxx#39; devera encontrar-se ativo no período #39xxxx-xx#39; Ação Sugerida: Verificar se o trabalhador encontra-se ativo no período ou se possui vinculação com outros eventos enviados posteriormente  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse erro de retorno do governo ocorre quando é enviado o evento S-1200 para o eSocial para um funcionário demitido ou inativo para o período informado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27088637413271)  
  
**Solução**1. Verificar se o funcionário esta ativo no eSocial;  
2. Caso esteja ativo, verificar qual a data de inicio do funcionário, verificar se o período que foi enviado o evento de admissão para o eSocial esta dentro do período do evento S-1200, período informado na mensagem de retorno;  
3. Caso o funcionário esteja demitido (S-2299) no site do eSocial, será necessário verificar a necessidade de envio do evento S-1200 para o eSocial, pois no evento S-2299 são enviados todos os pagamentos do período para o funcionário, após envio do desligamento, só é aceito o evento S-1200 em caso de rescisão complementar fora do mês da rescisão original.  
4. Caso o sistema esteja enviando o evento S-1200 incorretamente, será necessário verificar se o ambiente possui todas as atualizações referente ao eSocial no *link* [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
