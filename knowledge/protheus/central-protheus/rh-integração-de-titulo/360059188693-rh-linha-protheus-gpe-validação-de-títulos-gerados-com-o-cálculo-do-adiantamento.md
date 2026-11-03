---
article_id: 360059188693
category: RH - Integração de Titulo
content_hash: 9ca80cb1fc1386c8225577607b3f8a164c92eb21e2d519d996471136dfa1dd71
fetched_at: '2026-06-28T22:43:36.467006+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Validação de títulos gerados com o cálculo do Adiantamento
type: support-article
updated_at: '2025-08-13T17:57:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188693-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-de-t%C3%ADtulos-gerados-com-o-c%C3%A1lculo-do-Adiantamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34147804421399) Tempo aproximado para leitura: **00:02:00 min**  
Dúvida**Validação de títulos gerados com o cálculo do adiantamento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Realizada a implementação de tratamento para validação antes da exclusão do cálculo de adiantamento que já tenham títulos gerados/integrados com o **Financeiro - SIGAFIN**.  
O sistema precisa emitir uma mensagem informando que já existem títulos gerados/integrados para o cálculo em questão, alertando o usuário para necessidade de efetuar a manutenção desses títulos antes de realizar nova integração.

Efetuada a criação da Tabela **RJ1 - Detalhes de Títulos** para que nela sejam gravadas os históricos de títulos referente aos roteiros ADI, FER, FOL e RES. Criado mecanismo para verificar durante a exclusão ou recálculo do adiantamento se existe algum registro na tabela RJ1. Caso exista, será exibido o alerta abaixo, dando ao usuário possibilidade de prosseguir ou não com a operação: 

![help_titulo_calculo.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099507333)

Obs.: Existe também a possibilidade de bloqueio, neste caso antes de executar o recálculo o usuário deve excluir o título gerado através da rotina **Manutenção de Títulos - GPEM650**, essa informação é valida através do parâmetro **MV\_BTITADT**.

Parâmetro responsável por controlar a ação de **Exclusão** dos dados de cálculo gerados:

![MV_BTITADT.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097201154)

MV\_BTITADT: Configura Integ. Título para Adiantamento.

0=Não Trata

1=Tratamento com Mensagem

2=Tratamento Com Bloqueio

Detalhes da tabela RJ1 (releases anteriores ao 12.1.25 necessária a criação via **Configurador - SIGACFG** lembrando que campos criados dessa maneira ficam marcados como campos de usuário e suas respectivas manutenções via **UPDDISTR**, caso necessárias, serão limitadas):   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052402893/mceclip0.png)

![Novos_campo_da_RJ1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099473773/Novos_campo_da_RJ1.JPG)

IMPORTANTE: O tamanho do campo **RJ1\_NUMTIT** deve ser igual ao do campo **RC1\_NUMTIT** para que a implementação funcione corretamente.

Campos novos incluídos na Chave Única:

![Chave_unica_RJ1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097164174/Chave_unica_RJ1.JPG)

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
