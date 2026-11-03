---
article_id: 1500000887242
category: RH - Integração de Titulo
content_hash: 692c056cfd8c959869c3f8cc2d83238a3198cc96892d95dcdcc458d8d5ba7904
fetched_at: '2026-06-28T22:43:37.228315+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos: DV Agência'
type: support-article
updated_at: '2025-08-12T12:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000887242-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-DV-Ag%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34105997112599) Tempo aproximado para leitura: **00:02:00 min****

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos: DV Agência.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**Esse incidente ocorre pois no Módulo **Financeiro - SIGAFIN**, o campo **DV Agência**(E2\_FAGEDV), está configurado como obrigatório ou possui customização para validar o preenchimento.   
  
**Solução**Erro Apresentado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102127913)

Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilite o campo **E2\_FAGEDV**  da SE2 no Módulo Financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acesse:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_FAGEDV / Aba Uso e desmarcar o campo Obrigatório:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102130453)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099946274)

2. Customize um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos.   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
