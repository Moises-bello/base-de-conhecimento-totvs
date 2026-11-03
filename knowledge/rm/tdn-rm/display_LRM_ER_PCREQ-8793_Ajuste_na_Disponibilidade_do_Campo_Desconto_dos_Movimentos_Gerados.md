---
content_hash: 9932e191ff088e3ce3396516c77a438576860a90a4ad3bd13f3a27332359e63f
fetched_at: '2026-06-29T00:06:24.674576+00:00'
page_id: '224119632'
product: rm
source: tdn-rm
title: ER_PCREQ-8793_Ajuste_na_Disponibilidade_do_Campo_Desconto_dos_Movimentos_Gerados
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8793_Ajuste_na_Disponibilidade_do_Campo_Desconto_dos_Movimentos_Gerados
version: 199
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP010 | **IRM1** | PCREQ-5371 |
| **Requisito1** | PCREQ-8793 | **Subtarefa1** | PDR\_CP\_TOP010-19 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## 

## Objetivo

Identificar os movimentos gerados de contratos que contenham dedução e discriminação de valor de dedução e retenção do TOP,   
para que não seja permitido modificar o **Desconto** do movimento no Suprimento/Faturamento.

## 

## Definição da Regra de Negócio

 

Quando o movimento é gerado a partir de um contrato com dedução e discriminação de dedução e retenção,  
o somatório das deduções vai para o campo **Desconto** do movimento do Suprimentos/Faturamento.

Hoje, este campo **Desconto** do movimento, é passível de alteração, o que gera inconsistência.   
Sendo assim, quando for gerado movimento e houver dedução no contrato discriminando valor de dedução e retenção,   
o TOP irá criar a possibilidade do Suprimentos/Faturamento identificar estes movimentos,   
e assim bloquear a edição do campo **Desconto** do movimento. 

Importante

Disponível para integração TOP x Suprimento/Faturamento da linha RM

***Parâmetros*** 

*Parâmetros do Projeto (F6) >> Contratos >> Liberação*

* + *Discriminar valores de retenção e dedução*

 

***Tabelas Utilizadas*** 

* *MCNTPDOMOV*
* *MPDODETRET*

## Geração de Movimento a partir de Contrato do TOP

ImportantePara movimentos gerados de contrato do TOP onde houver dedução e discriminação de dedução e retenção,   
não deve ser possível modificar o **Desconto** do movimento no Suprimentos/Faturamento.

* ### Gerar movimento com parâmetro 'Discriminar valores de retenção e dedução' marcado com valor de dedução.

Quando o movimento é gerado neste cenário, o valor de **Dedução** e **Retenção** é enviado da seguinte maneira:  
O somatório das deduções vai para o campo **Desconto** do movimento do Suprimentos/Faturamento.  
O somatório das retenções vai para o campo **Retenção** do Item do Suprimentos/Faturamento.

 

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
