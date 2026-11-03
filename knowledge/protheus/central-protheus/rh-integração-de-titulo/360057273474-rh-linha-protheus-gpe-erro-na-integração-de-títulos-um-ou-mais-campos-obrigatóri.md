---
article_id: 360057273474
category: RH - Integração de Titulo
content_hash: 778a35555930b8a4cc72d1958f3a9dcedad36b0516f0b67510f9fe56fdf0a4ce
fetched_at: '2026-06-28T22:43:36.328451+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos: Um ou mais campos
  obrigatórios não foram preenchidos Histórico'
type: support-article
updated_at: '2025-07-14T21:06:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057273474-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Hist%C3%B3rico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33463084392471)**Tempo aproximado para leitura: 00:01:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Histórico  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo financeiro, o campo de Histórico (E2\_HIST), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Falha_na_gravacao_historico.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097133254)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_HIST** no Módulo financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_HIST / Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17960187159575)

2. Verificar via CONFIGURADOR se o campo E2\_HIST possui alguma validação de usuário que impede o campo ser gravado vazio ou validação específica:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33463084398871)  
  
3. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada GP670ARR que permite a gravação de outros campos.   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
