---
article_id: 10325977087255
category: GPE - eSocial - Não Periódicos
content_hash: 296d41028df7a5d088378acc375c18d9c84b5db4c213d9d7259f75c47df3c402
fetched_at: '2026-06-28T22:45:06.069597+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Rescisão contrato de trabalho
  intermitente a pedido
type: support-article
updated_at: '2023-08-30T17:33:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10325977087255-RH-Linha-Protheus-GPE-eSocial-S-2299-Rescis%C3%A3o-contrato-de-trabalho-intermitente-a-pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17153279610519) Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**

Realizado cálculo de rescisão para funcionário com contrato intermitente, onde o funcionário não teve convocações para o mês e pediu demissão. Realizado o calculo de Rescisão e ao transmitir para o RET (Governo) é apresentado erro **Sequência: 000001-Tipo: Erro - Codigo da ocorrência: 8 Localização: /eSocial/evtDeslig/info Deslig/verbasResc/dmDev Descrição: Grupo 'Verbas rescisorias relativas ao periodo de apuracao deve ser preenchido. Verifique as condicoes de preenchimento no leiaute  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal - Todas as versões  
  
**Causa**

No leiaute S-1.1 do eSocial, informa que no evento S-2299 a tag **verbasResc** é obrigatória

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17153216803863)  
Fonte: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#r_2299_infoDeslig_verbasResc>   
  
**Solução**

Rescisão para trabalhador com contrato intermitente só deve existir se houverem convocações no período. Trabalhadores sem convocações no período, não haverá calculo de folha de pagamento e sem convocações, o trabalhador ficará inativo.  
No **eSocial não existe tratativa para o cenário de rescisão de trabalhador com contrato intermitente e sem convocações**.  
Em caso de dúvidas relacionadas a este retorno no evento S-2299 referente ao cenário aqui exposto, sugerimos que entre em contato diretamente com o RET (Governo). O questionamento pode ser realizado através dos canais de comunicação disponíveis no Portal do eSocial abaixo.  
  
[Fale Conosco](http://portal.esocial.gov.br/servicos/contato-1)  
Central de Atendimento: 0800 730 0888  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - Como calcular Rescisão Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022766711-RH-Linha-Protheus-GPE-Como-calcular-Rescis%C3%A3o-Contrato-Intermitente?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
