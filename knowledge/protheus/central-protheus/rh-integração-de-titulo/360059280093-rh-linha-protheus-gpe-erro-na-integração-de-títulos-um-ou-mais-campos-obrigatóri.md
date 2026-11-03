---
article_id: 360059280093
category: RH - Integração de Titulo
content_hash: 7c37ced6789ae615ad8380f979be08e70ef0a2d0eca950b7a6017b1308816803
fetched_at: '2026-06-28T22:43:37.192960+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos: Um ou mais campos
  obrigatórios não foram preenchidos Filial Orig'
type: support-article
updated_at: '2025-08-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059280093-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Filial-Orig
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118821658391) Tempo aproximado para leitura: **00:02:00 min****

**Ocorrência**Na integração de títulos: Um ou mais campos obrigatórios não foram preenchidos Filial Orig.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Filial Orig**. (E2\_FILORIG), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Filial_orig.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097353794)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_FILORIG** no Módulo financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_FILORIG / Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118837482647)

2. No grupo de perguntas da rotina**Integração Financeiro - GPEM670**, existe o parâmetro **Filial Centralizadora**, ao informar o código de uma filial para este item, essa informação é gravada no campo **Filial Orig**. da rotina **Contas a Pagar - FINA050**.  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
