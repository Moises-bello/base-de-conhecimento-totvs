---
article_id: 360057272234
category: RH - Integração de Titulo
content_hash: f72b8196da4368f6dfb7525011bc49a849dbfd13bb55a2b533874261fbe0f00d
fetched_at: '2026-06-28T22:43:36.459103+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Validação de títulos gerados com o cálculo da Férias
type: support-article
updated_at: '2025-08-13T17:58:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057272234-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-de-t%C3%ADtulos-gerados-com-o-c%C3%A1lculo-da-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34147865590039) Tempo aproximado para leitura: **00:02:00 min******Dúvida**Validação de títulos gerados com o cálculo de férias  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Realizada a implementação de tratamento para validação antes da exclusão de férias que já tenham títulos gerados/integrados com o **Financeiro - SIGAFIN**.  
O sistema precisa emitir uma mensagem informando que já existem títulos gerados/integrados destes cálculos, alertando o usuário da necessidade de efetuar a manutenção desses títulos antes de realizar nova integração.

Efetuada a criação da Tabela **RJ1 - Detalhes de Títulos** para que nela sejam gravadas os históricos de títulos referente aos roteiros ADI, FER, FOL e RES. Criado mecanismo para verificar durante a exclusão ou recálculo das férias se existe algum registro deste na tabela RJ1. Caso exista, será exibido o alerta abaixo, dando ao usuário possibilidade de prosseguir ou não com a operação: 

![Mensagem_F_rias.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097131994)

Obs.: Existe também a possibilidade de bloqueio, neste caso antes de executar o recálculo o usuário deve excluir o título gerado através da rotina **Manutenção de Títulos - GPEM650**, essa informação é valida através do parâmetro **MV\_BTITFER**.

Parâmetro responsável por controlar a ação de **Exclusão** dos dados de cálculo gerados:

![MV_BTITFER.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097176574)

MV\_BTITFER: Configura Integração Título para Férias.

0=Não Trata

1=Tratamento com Mensagem

2=Tratamento Com Bloqueio

Detalhes da tabela RJ1 (releases anteriores ao 12.1.25 necessária a criação via Configurador - lembrando que campos criados dessa maneira ficam marcados como campos de usuário e suas respectivas manutenções via **UPDDISTR**, caso necessárias, serão limitadas): 

Novos Campos da RJ1

![Novos_campo_da_RJ1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099442293)

IMPORTANTE: O tamanho do campo **RJ1\_NUMTIT** deve ser igual ao do campo **RC1\_NUMTIT** para que a implementação funcione corretamente.

Campos novos incluídos na Chave Única:

![Chave_unica_RJ1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099486693)

**Saiba Mais:**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)

[Títulos Financeiros por Roteiros](https://tdn.totvs.com/pages/viewpage.action?pageId=556890394)
