---
article_id: 24271682179351
category: GPE - eSocial - Processo Trabalhista
content_hash: 68055f0d3d5652307849eef463c23f5689999fd5c421151cbeb1e96514e6bcc6
fetched_at: '2026-06-28T22:45:00.509096+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2500 - Codigo da ocorrência: 186 -
  Tipo do contrato deve ser igual a 8 quando o grupo "Identificacao do contribuinte,
  caso tenha havido imposicao de responsabilidade indireta" for preenchido.'
type: support-article
updated_at: '2024-06-19T14:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24271682179351-RH-Linha-Protheus-GPE-eSocial-S-2500-Codigo-da-ocorr%C3%AAncia-186-Tipo-do-contrato-deve-ser-igual-a-8-quando-o-grupo-Identificacao-do-contribuinte-caso-tenha-havido-imposicao-de-responsabilidade-indireta-for-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24271682168215) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Sequência: 000003 - Tipo: Erro - Codigo da ocorrência: 186  
Localização: /eSocial/evtProcTrab/ideTrab/infoContr/tpContr  
Descrição: Tipo do contrato invalido.Acao sugerida: Tipo do contrato deve ser igual a 8 quando o grupo "**Identificacao do contribuinte, caso tenha havido imposicao de responsabilidade indireta**" for preenchido.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o leiaute S-1.2 disponibilizado pelo eSocial, o campo **Tipo de contrato** do grupo  informações do contrato de trabalho, deverá ser preenchido obrigatoriamente com o **tipo 8 - Responsabilidade indireta**, quando forem preenchidos os **campos de identificação do responsável direto.**  
Acesse a rotina **Dados eSocial**, aba **Contrato de Trabalho**, campo **Tipo** e selecione **Responsabilidade Indireta:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24284053930007)  
  
Não sendo este o cenário, bastará manter os campos **Tipo inscrição e Número inscrição**, referentes a **responsabilidade direta, em branco.**Essa informação está localizada na rotina APTA100, em Atualizações - Processo Trabalhista - Processos - Processos:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24284068695447)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas?source=search)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
