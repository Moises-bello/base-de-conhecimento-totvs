---
article_id: 13425096149015
category: GPE - eSocial - Não Periódicos
content_hash: c11716674cca47854c2ffe4c88fdd5eca01cf43901f03975f97141cece22a900
fetched_at: '2026-06-28T22:45:05.981329+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - S-2200 - O que verificar quando o evento S-2200
  não é gerado
type: support-article
updated_at: '2026-06-16T11:46:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13425096149015-RH-Linha-Protheus-GPE-S-2200-O-que-verificar-quando-o-evento-S-2200-n%C3%A3o-%C3%A9-gerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24336316955543) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que verificar quando o evento S-2200 não é gerado ao confirmar uma admissão?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para evitar a integração de informações incompletas do GPE com o TAF sugerimos que mantenha o parâmetro [**MV\_EFDAVIS**](https://tdn.totvs.com/pages/releaseview.action?pageId=286499282) com o conteúdo '**1**' para **avisar e impedir o cadastro até que seja tudo corrigido**.  
  
Para verificar o conteúdo do parâmetro MV\_NTSV, vá no Configurador em **SIGACFG > Ambiente > Cadastros > Parâmetros**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24336687475479)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24336687497623)  
  
Quando deixamos o parâmetro [**MV\_EFDAVIS**](https://tdn.totvs.com/pages/releaseview.action?pageId=286499282) com conteúdo '**1'**, o sistema mostrará em tela quais os campos que faltam preenchimento e que são obrigatórios para a geração do evento S-2200. Segue imagem abaixo como exemplo:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24336697734295)**  
  
Verifique as inconsistências mais recorrentes que não geram o evento S-2200:  
[RH - Linha Protheus - GPE - eSocial - S-2200/S-2206 - As seguintes sequencias não possuem intervalo definido. Rever cadastro de tabela de horário padrão.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8344840740887)  
[S-2200 - Não será possível efetuar a integração. O trabalhador possui afastamento sem motivo informado, ou inválido para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018696391)  
[RH - Linha Protheus - GPE - eSocial - S-2200 - Como enviar a admissão completa quando a admissão preliminar foi enviada por outro software](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12757005282071)  
[RH - Linha Protheus - GPE - eSocial - Erro 000001: xmlParseEntityRef ao gerar S-2200/S-2206/S-2300/S-2306](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13296235629591)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
