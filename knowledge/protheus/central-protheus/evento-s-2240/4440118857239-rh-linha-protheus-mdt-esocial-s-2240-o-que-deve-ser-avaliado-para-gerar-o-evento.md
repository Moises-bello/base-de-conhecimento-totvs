---
article_id: 4440118857239
category: Evento S-2240
content_hash: b324f6174c42faabf85003fa3ecefe01c85c641ac92cf5b9e2ffc6a102781e7b
fetched_at: '2026-06-28T22:45:23.757981+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 -​ O que deve ser avaliado para
  gerar o evento S-2240 em uma admissão
type: support-article
updated_at: '2024-11-29T13:39:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4440118857239-RH-Linha-Protheus-MDT-eSocial-S-2240-O-que-deve-ser-avaliado-para-gerar-o-evento-S-2240-em-uma-admiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28149910621335) Tempo aproximado para leitura: **00:05:01 min** **Dúvida**O que deve ser avaliado para gerar o evento S-2240 em uma admissão?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O parâmetro de integração entre o Módulo MDT e GPE deve estar Ativo **MV\_MDTGPE = S**.  
  
Os parâmetro de configurações dos eventos de SST deve ser revisados havendo dúvidas consulte a documentação de apoio:  
[RH - Linha Protheus - MDT - eSocial - Quais são os parâmetros utilizados nos eventos SST (Medicina) do eSocial no modulo SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027665951-RH-Linha-Protheus-MDT-eSocial-Quais-s%C3%A3o-os-par%C3%A2metros-utilizados-nos-eventos-SST-Medicina-do-eSocial-no-modulo-SIGAMDT)  
  
Saneamento da base deve ser realizado em caso de dúvidas consulte documentação de apoio:  
[RH - Linha Protheus - MDT - eSocial - Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631-RH-Linha-Protheus-MDT-eSocial-Existe-v%C3%ADdeos-com-o-passo-a-passo-de-gera%C3%A7%C3%A3o-dos-eventos-SST-Medicina-e-Seguran%C3%A7a-do-Trabalho-no-eSocial)  
  
**Importante!**  
Na admissão se estiver conforme exigido pelo eSocial será enviado o evento S-2240.  
Se o funcionário estiver exposto a algum Risco, sistema envia o código do eSocial Cadastrado no agente do risco, ou seja, o 01.01.001, 02.01.001, etc. E caso o funcionário não esteja exposto a nenhum risco envia o código da ausência, que é o 09.01.001.  
Se não estiver tudo dentro do esperado será gerado um log de inconsistência e deverá ser ajustado para posterior envio do evento, todos os erros mapeados no log de inconsistências juntamente com a solução estão mapeados em nossa página Centralizadora na opção de Relatório de Inconsistência Consulte:  
<https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-2240#Deck_tecnica-relatorio_inconsistencias>

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
