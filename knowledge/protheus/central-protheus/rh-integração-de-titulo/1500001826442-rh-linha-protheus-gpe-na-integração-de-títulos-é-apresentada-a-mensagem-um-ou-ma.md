---
article_id: 1500001826442
category: RH - Integração de Titulo
content_hash: d3d9399b5d942f8a494afd731d967501d8f63373ea0fce2e181b8ea3d3494a87
fetched_at: '2026-06-28T22:43:36.398749+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos. Vlr R$'
type: support-article
updated_at: '2025-07-24T14:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001826442-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Vlr-R
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33686211194519)Tempo aproximado para leitura:00:02:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Vlr R$  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Vlr R$**(E2\_VLCRUZ), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Vlr_R_.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001661942)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar a  obrigatoriedade do campo **E2\_VLCRUZ** da SE2 no Módulo Financeiro, através do **Configurador**.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_VLCRUZ / Aba Uso e desmarcar o campo Obrigatório:  
![E2_VLRCRUZ.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001711161)

Em seguida verificar o conteúdo do campo **Val. Sistema** localizado na Aba Validações da mesma rotina no **Configurador**.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo **E2\_VALOR**/ Aba Validações verificar conteúdo do campo Val. Sistema:  
![E2_VALOR.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001710681)  
 **Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo **E2\_VLCRUZ** / Aba Validações verificar conteúdo do campo Val. Sistema:  
![E2_VLRCRUZ.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360100555834)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.  
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos. 

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
