---
article_id: 360057347754
category: RH - Integração de Titulo
content_hash: 3c80db07ef14f94c62826f9ca22f68b53dccec31527bb80edfad85054a2d0615
fetched_at: '2026-06-28T22:43:37.207472+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos: Um ou mais campos
  obrigatórios não foram preenchidos Form Pagto'
type: support-article
updated_at: '2025-08-12T12:41:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057347754-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Form-Pagto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34106598040855) Tempo aproximado para leitura: **00:02:00 min****

**Ocorrência**Na integração de títulos: Um ou mais campos obrigatórios não foram preenchidos Form Pagto  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Form Pagto** (E2\_PGTO), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Falha_na_gravacao_Form_Pagto.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099541773)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_PGTO** no Módulo financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_PGTO / Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34106585134743)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos.   
 **Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
