---
article_id: 360057631414
category: RH - Integração de Titulo
content_hash: d69f1c50f38debbf3a6a5d001c22d05943b074f184cf936551f39f4504a4c624
fetched_at: '2026-06-28T22:43:36.121711+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE  - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos Cl.Vlr. Deb'
type: support-article
updated_at: '2025-07-15T20:37:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057631414-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Cl-Vlr-Deb
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33486833313047)**Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Cl.Vlr. Deb.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Cl.Vlr. Deb.**(E2\_CLVLDB), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![clvlrdeb.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097775454)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_CLVLDB** da SE2 no Módulo Financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_CLVLDB / Aba Uso e desmarcar o campo Obrigatório:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17161511376023)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
3. Verificar se existe alguma validação se usuário que impede que o campo seja vazio ou possua alguma validação específica: ![](https://centraldeatendimento.totvs.com/hc/article_attachments/17161481619863)

Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos.   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
