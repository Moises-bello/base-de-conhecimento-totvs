---
article_id: 360059213893
category: RH - Integração de Titulo
content_hash: f3229171f84368a42521301b65865b4bdeeaae69609d370e248ffa28f9f9a917
fetched_at: '2026-06-28T22:43:36.490632+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE  - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos. C.Custo Deb'
type: support-article
updated_at: '2025-08-12T12:28:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059213893-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-C-Custo-Deb
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118864596119) Tempo aproximado para leitura: **00:02:00 min****

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. C.Custo Deb.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **C.Custo Deb.** (E2\_CCD), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Falha_na_gravacao_c_custo_deb.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097234434)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_CCD** da SE2 no Módulo Financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_CCD/ Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118864597655)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos.   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
