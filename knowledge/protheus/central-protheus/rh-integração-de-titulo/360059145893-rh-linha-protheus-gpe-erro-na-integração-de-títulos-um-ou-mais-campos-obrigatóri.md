---
article_id: 360059145893
category: RH - Integração de Titulo
content_hash: 980e155c76cb04b4e16ff8d69874aa2d4d836b40a2becac2f4133db556e6740b
fetched_at: '2026-06-28T22:43:36.472091+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE- Erro na integração de títulos: Um ou mais campos
  obrigatórios não foram preenchidos Conta Orçamentária'
type: support-article
updated_at: '2025-07-15T20:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059145893-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Um-ou-mais-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos-Conta-Or%C3%A7ament%C3%A1ria
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33486990450583)**Tempo aproximado para leitura: 00:02:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Um ou mais campos obrigatórios não foram preenchidos. Conta Orçamentária  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois no Módulo Financeiro ou Planejamento e Controle Orçamentário, o campo Conta Orçamentária, está configurado como obrigatório.   
  
**Solução**Erro apresentado: ![Falha_na_gravacao_Conta_Or_amentaria.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097134914)

Para solucionar essa ocorrência, temos duas opções:   
  
1- Desabilitar o campo **Conta Orçamentária** no Módulo Financeiro ou Planejamento e Controle Orçamentário, através do Configurador.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

**Acessar:** Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SE2 ->Campo E2\_xxxx / Aba Uso e desmarcar o campo Obrigatório:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17011785760407)

2. Customizar um **ponto de entrada na rotina GPEM670**, de modo que o campo seja preenchido automaticamente durante o processo de integração de títulos.   
  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada GP670ARR que permite a gravação de outros campos.   
  
  
3. Verificar se existe alguma validação se usuário que impede que o campo seja vazio ou possua alguma validação específica:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17011755684119)  
   
  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[MP - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-MP-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670?source=search)
