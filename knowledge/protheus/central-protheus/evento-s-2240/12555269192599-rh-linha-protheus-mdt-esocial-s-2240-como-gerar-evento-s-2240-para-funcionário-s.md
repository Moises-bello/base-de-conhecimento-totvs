---
article_id: 12555269192599
category: Evento S-2240
content_hash: c02a93f568a4edd7a3d081974023e066f2b86dfa575eda3e1cd75d3437e44533
fetched_at: '2026-06-28T22:45:23.578585+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como gerar evento S-2240 para
  funcionário sem exposição de Risco
type: support-article
updated_at: '2025-03-11T19:09:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12555269192599-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-gerar-evento-S-2240-para-funcion%C3%A1rio-sem-exposi%C3%A7%C3%A3o-de-Risco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24784882491415) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar evento S-2240 para funcionário sem exposição de Risco?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Há três formas de gerar o evento S-2240 para funcionários não exposto ao risco:  
  
**1-** Na admissão do funcionário realizado pelo módulo SIGAGPE (07), no menu *Atualizações - Funcionários - Funcionários* (**GPEA010**), através dos campos Centro Custo, Função e Departamento o sistema efetua validação para identificar se no módulo SIGAMDT contém risco com essas informações, não encontrando o sistema gera o evento S-2240 com código 09.01.01 (ausência de risco) e integra com módulo TAF.   
  
No exemplo abaixo o sistema gera o evento S-2200 ou S-2300 de acordo com a categoria do funcionário, e não identificando inconsistência o evento S-2240 é gerado em seguida:   
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12555451185687)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12554806796951)  
  
**2-** Se o funcionário já possui cadastro no SIGAGPE mas não gerou o evento, é possível alterar qualquer campo no cadastro do funcionário (**GPEA010**), ao salvar será gerado o evento.  
  
**3-** No módulo SIGAMDT (35) através da rotina *Miscelânea - Implantação - Gerar Riscos eSocia*l (**MDTA881**) é possível executar a rotina que o sistema também gera o evento para funcionários não exposto ao risco, porém, essa rotina não possui um filtro então será integrado todos registros que contém no cadastro do funcionário (SRA), mesmo quem já foi integrado e tem o evento S-2240, por isso, é importante efetuar o saneamento da base e executar a rotina uma única vez.   
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12555565401623)  
  
**Importante:** É necessário que valide as informações:  
  
\* O ambiente deve estar atualizado com Acumulado MDT e TAF:  
[Pacote e Dicionário Correções Expedição Continua MDT](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/MDT_EXPEDICAO_CONTINUA.ZIP)   
[Pacote e Dicionário Correções Expedição Continua TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP)  
  
\* Configurar os parâmetros para envio do evento S-2240:  
[Quais os parâmetros que auxiliam na definição do evento S-2240](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410645170711)  
  
\* É possível deixar os parâmetros de geração do S-2240 de forma exclusiva, porém, todos parâmetros devem ser alterados:  
[Como gerar a Carga de Risco de uma filial específica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4479141016983)  
  
\* **Não** pode ter um risco cadastrado com agente (09.01.001), como informado, o sistema gera o evento automaticamente.   
  
**Saiba Mais**

[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Eventos SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
