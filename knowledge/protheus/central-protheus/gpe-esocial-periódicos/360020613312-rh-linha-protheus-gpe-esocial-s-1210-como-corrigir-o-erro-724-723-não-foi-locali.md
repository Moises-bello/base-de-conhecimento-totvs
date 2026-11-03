---
article_id: 360020613312
category: GPE - eSocial - Periódicos
content_hash: 378138530bfcf67458e265e4c86726c06be191e09bd221fdc3191599ed1c327b
fetched_at: '2026-06-28T22:45:08.903546+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como corrigir o erro 724 / 723
  (não foi localizada remuneração) em meses onde houve calculo de 13º salario e rescisão
type: support-article
updated_at: '2025-07-21T14:46:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020613312-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-corrigir-o-erro-724-723-n%C3%A3o-foi-localizada-remunera%C3%A7%C3%A3o-em-meses-onde-houve-calculo-de-13%C2%BA-salario-e-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26833860544535) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**

Como corrigir o erro **724 / 723** (não foi localizada remuneração) em meses onde houve calculo de 13º salario e rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**O erro pode ocorrer por causa dos seguintes motivos:

1. Não existir recibo chave de identificação do 13º salário no evento S-2299.

2. Não existir recibo chave de identificação do 13º salário no evento S-1210.  
  
**Solução**Aplicar pacotes disponíveis na página entregas legais [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  
1. Se no mesmo mês que foi gerado o S-2299 houve o calculo do 13º salário deve existir a chave de identificação do 13º no evento S-2299, caso não exista será necessário retificar o S-2299 conforme artigo: [Como retificar um evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020865371)

Exemplo de um S-2299 que tem a chave de identificação do 13º salario.   
Caminho do TAF: *Atualizações > Eventos eSocial > Não-periódicos > Desligamento:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26833836067735)  
  
2. Se no mesmo mês que foi gerado o S-2299 houve o calculo do 13º salario deve existir a chave de identificação do no S-1210, caso não exista será necessário excluir o evento S-1210 e gerar o evento novamente.

Exemplo de um S-1210 que tem a chave de identificação do 13º salario.  
Caminho do TAF: *Atualizações > Eventos eSocial > Periódicos > Pagto Rend Trab:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26833836069783)  
  
Consulte também o artigo: [Quais os prazos para envio de S-1200, S-1210 e S-1299 referentes à folha anual e Como informar período de apuração anual no evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020493932)  
  
**Saiba Mais**  
[S-1210 - Inconsistência do RET - 723, 724, 726 no retorno do evento transmitido ao governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
