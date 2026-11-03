---
article_id: 7499195957655
category: MDT - PCMSO
content_hash: 731bdde64721d09135231473b5331dd9abf97caa31028a368745e32dc4953a07
fetched_at: '2026-06-28T22:44:28.513634+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Quais os parâmetros que auxiliam na Geração de
  Exames
type: support-article
updated_at: '2025-09-03T13:59:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7499195957655-RH-Linha-Protheus-MDT-Quais-os-par%C3%A2metros-que-auxiliam-na-Gera%C3%A7%C3%A3o-de-Exames
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25674326160791)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais os parâmetros que auxiliam na na Geração de Exames?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cada empresa pode ter um cenário específico portanto é importante avaliar os parâmetros abaixo:  
  
**\* MV\_MDTFERI =** Considerar programação de férias na geração de programação de exames? S=Sim ou N=Não.

**\* MV\_MDTPS =** Indica se o cliente e um prestador de serviço S=Sim ou N=Não.

**\* MV\_NG2CATF =** Indica as categorias funcionais de funcionários que não terão exames gerados na programação. Exemplo: A/M/T.

**\* MV\_NG2D190 =** Indica a quantidade de dias que o funcionário não terá exame agendado na reprogramação por data informada, baseado na data do ultimo exame agendado.

**\* MV\_NG2PCOB =** Indica se o PCMSO devera ser gerado individualmente por centro de custo. S=Sim, N=Não.

**\* MV\_NG2PDAD =** Indica se na programação de exames será permitido gerar exames na data de admissão do funcionário. Informar 1=Sim ou 2=Não.

**\* MV\_NG2PMUD =** Indica se irá gerar Pós-Admissional em Mudança de Função\Setor para Exames por Risco\Função. 1=Sim;2 =Não.

**\* MV\_NG2PRCL =** Indica se a programação de exames será feita com filtragem dos funcionários de acordo com o código do cliente informado na sua Ficha Medica. (S / N). 

**\* MV\_NGMDTPS =** Indica se o cliente e um prestador de serviço de medicina (S / N). 

**\* MV\_NGMDTVA =** Indica se irá considerar afastados na programação de exames. 1=Sim;2=Não selecionados. 1 = Todos; 2 = Selecionados.   
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
