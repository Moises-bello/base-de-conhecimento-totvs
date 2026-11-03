---
article_id: 19452617838103
category: GPE - eSocial - Periódicos
content_hash: 653471ecda6f23495dac186ee5c1a9e4087ee90b7da31ed6e157bf026420f4a0
fetched_at: '2026-06-28T22:45:08.888473+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Código da Ocorrência: 861 -
  A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato
  de trabalho'
type: support-article
updated_at: '2023-11-30T16:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19452617838103-RH-Linha-Protheus-GPE-eSocial-S-1210-C%C3%B3digo-da-Ocorr%C3%AAncia-861-A-data-de-pagamento-deve-ser-maior-ou-igual-ao-m%C3%AAs-anterior-de-rescis%C3%A3o-do-contrato-de-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19452632266903) Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Na transmissão do evento S-1210 para o RET (Governo) é retornado a inconsistência: **Código da Ocorrência: 861** - A data de pagamento deve ser maior ou igual ao mês anterior de rescisão do contrato de trabalho.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Conforme mensagem apresentada, a inconsistência geralmente é retornada quando não foi identificado o evento**S-2299** (Desligamento) ou o evento **S-1200** (Remuneração do Trabalhador) anterior ao envio do evento **S-1210** (Pagamento de Rendimentos do Trabalho).  
  
**Solução**O evento S-1210 só será aceito após transmissão do evento de Remuneração (S-1200/S-2299).Verifique se o evento **S-2299** foi transmitido e se consta as verbas rescisórias. Caso seja um funcionário ativo, verifique se o evento **S-1200** foi transmitido.  
  
**Observação**  
Se for um funcionário desligado e com calculo de rescisão complementar em meses posteriores ao Desligamento, os valores da rescisão complementar devem ser integrados no evento S-1200. Saiba mais acessando o artigo abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Como registrar uma rescisão complementar no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005103432-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Como-registrar-uma-rescis%C3%A3o-complementar-no-eSocial?source=search)  
  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-informa%C3%A7%C3%B5es-de-dissidio-e-rescis%C3%A3o-complementar-por-dissidio-no-esocial?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
**Próximos Treinamentos**[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
