---
article_id: 360057622574
category: RH - Integração de Titulo
content_hash: 11713c8e85b05fe1f3d4dcc70842e67cd2f15284b768f9d01e42457eb731737d
fetched_at: '2026-06-28T22:43:36.127475+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE  - Na integração de títulos é apresentada a mensagem:
  Um ou mais campos obrigatórios não foram preenchidos Conta Deb'
type: support-article
updated_at: '2025-07-15T20:38:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057622574-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Conta-Deb
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33486883101975)**Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Conta Deb.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo **Financeiro - SIGAFIN**, o campo **Conta Deb.** (E2\_DEBITO), está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![conta_deb.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097757354)  
Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **E2\_DEBITO**  da SE2 no Módulo Financeiro, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_DEBITO / Aba Uso e desmarcar o campo Obrigatório:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17162109345559)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.

3. Verificar se existe alguma validação se usuário que impede que o campo seja vazio ou possua alguma validação específica:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17162123062679)

Para atender a necessidade exposta, foi verificado que existe o ponto de entrada **GP670ARR** que permite a gravação de outros campos.   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
