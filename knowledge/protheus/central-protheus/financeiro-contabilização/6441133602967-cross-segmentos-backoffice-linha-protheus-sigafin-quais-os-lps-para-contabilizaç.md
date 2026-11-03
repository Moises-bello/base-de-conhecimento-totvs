---
article_id: 6441133602967
category: Financeiro - Contabilização
content_hash: 5bc93293640007ed20cf19940aafd8417ef3ce618498ac2eb13db222d065ea6d
fetched_at: '2026-06-28T22:38:05.535780+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Quais os LPs para contabilização
  por rotina no Financeiro
type: support-article
updated_at: '2026-05-22T14:33:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6441133602967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-LPs-para-contabiliza%C3%A7%C3%A3o-por-rotina-no-Financeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37067305636375)** Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Quais são os LPs de contabilização do módulo financeiro online e off-line ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - todas as versões  
  
**Solução**

Esse cadastro é o **ponto central de integração** entre o **Financeiro** e a **Contabilidade Gerencial**, pois toda a integração contábil ocorre com base nas regras e dados dos lançamentos definidos.

As **regras de lançamento padrões** determinam como cada processo gerador (dados de origem) de lançamentos será integrado ao destino (contabilidade). Após configurados, os lançamentos passam a ser realizados **automaticamente**, sem necessidade de intervenção do usuário.

A contabilização pode ocorrer de duas formas:

* **Online**: os lançamentos são gerados automaticamente durante a execução dos processos.
* **Offline**: os lançamentos são gerados quando o usuário solicita, por meio da opção *Contabilização Off-Line* (menu Miscelânea).

É fundamental observar o modelo de integração aceito pelo LP acionado. Abaixo, segue o detalhamento completo.

Lista de rotinas disponíveis e os métodos de contabilização 

-- Selecione Uma Rotina --
FINA040 ou FINA740 - Manutenção do Contas a Receber
FINA050 ou FINA750 - Manutenção do Contas a Pagar
FINA060 - Transferências no Contas a Receber
FINA070 - Baixa de Titulos no Contas a Receber
FINA080 - Baixa de Títulos no Contas a Pagar
FINA087A - Recibos Diversos
FINA088 - Cancelamento de Recibos Diversos
FINA090 - Baixa Automática Títulos no Contas a Pagar
FINA100 - Manutenção do Cad.de Movimentos Bancários
FINA110 - Baixa automática Titulos no Contas a Receber
FINA171 e FINA716 - Manutenção de Aplicações/Empréstimos
FINA181 e FINA716 - Resgate de Aplicações/Empréstimos
FINA182 e FINA716 - Resgate de Aplicações/Empréstimos
FINA183 - Retenção de IR último dia do mês
FINA190 - Emissão de Cheques
FINA191 - Cheques Recebidos 
FINA200 - Retorno de Comunicação Bancária 
FINA280 - Faturas a Receber 
FINA281 - Faturas a Receber - TMS 
FINA290 - Faturas a Pagar 
FINA300 - Comunicação Bancaria - SISPAG 
FINA330 - Compensação de Adiantamento a Receber 
FINA340 - Compensação de Adiantamento a Pagar 
FINA350 - Variação Monetária 
FINA375 - Apuração de IR 
FINA376 - Aglutinação de Impostos
FINA377 - Apuração de INSS 
FINA390 - Cheques sobre Titulos 
FINA430 - Retorno de Comunicação Bancária a Pagar 
FINA450 - Compensação entre Carteiras 
FINA460 - Liquidação de Títulos a Receber 
FINA550 - Movimentos do Caixinha 
FINA565 - Liquidação de Títulos a Pagar 
FINA590 - Manutenção de Borderô 
FINA677 - Prestação de contas 
CTBAFIN - Contabilização Off Line 
Verifique todos os Lps Disponiveis 
  
  

| Funcionalidade (USO) | Manutenção do Contas a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos no Contas a Receber | 500 | X | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 | X | X |
| No cancelamento de títulos tipo RA no Contas a Receber | 502 | X |  |
| Na substituição de títulos provisórios no Contas a Receber | 503 | X |  |
| Na inclusão de títulos gerados através do desdobramento no Contas a Receber | 504 | X | X |
| No exclusão de títulos do Contas a Receber | 505 | X |  |
| No inclusão de títulos com rateio CC e multiplas naturezas no Contas a Receber | 506 | X | X |
| No cancelamento de títulos com rateio CC e múltiplas naturezas no Contas a Receber | 507 | X |  |
| Na cancelamento de títulos gerados através do desdobramento no Contas a Receber | 529 | X |  |
| Na exclusão de títulos do contas a receber com variação monetária gerada pela rotina FINA350 | 59A | X |  |

| Funcionalidade (USO) | Manutenção do Contas a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos com rateio CC e múltiplas naturezas no Contas a Pagar | 508 | X | X |
| No cancelamento de títulos com rateio CC e múltiplas naturezas no Contas a Pagar | 509 | X |  |
| Na inclusão de títulos no Contas a Pagar | 510 | X | X |
| Na inclusão de títulos com rateio CC no Contas a Pagar | 511 | X | X |
| Na cancelamento de títulos com rateio CC no Contas a Pagar | 512 | X |  |
| Na inclusão de títulos tipo PA no Contas a Pagar | 513 | X | X |
| No cancelamento de títulos tipo PA no Contas a Pagar | 514 | X |  |
| No cancelamento de títulos no Contas a Pagar | 515 | X |  |
| Na substituição de títulos provisórios no Contas a Pagar | 533 | X | X |
| Na inclusão de títulos gerados por desdobramento no Contas a Pagar | 577 | X | X |
| No cancelamento de títulos gerados por desdobramento no Contas a Pagar | 578 | X |  |

| Funcionalidade (USO) | Transferências no Contas a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na transferência para Carteira de Cobrança no Contas a Receber (0/F/G) | 540 | X | X |
| Na transferência para Carteira de Cobrança Simples/Cartório no Contas a Receber (1/H) | 541 | X | X |
| Na transferência para Carteira de Cobrança Descontada no Contas a Receber (2) | 542 | X | X |
| Na transferência para Carteira de Cobrança Caucionada no Contas a Receber (3) | 543 | X | X |
| Na transferência para Carteira de Cobrança Vinculada no Contas a Receber (4) | 544 | X | X |
| Na transferência para Carteira de Cobrança Advogado no Contas a Receber (5) | 545 | X | X |
| Na transferência para Carteira de Cobrança Judicial no Contas a Receber (6) | 546 | X | X |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 | X | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 | X | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 | X | X |
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 | X | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 | X | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 | X | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 | X | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 | X | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 | X | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 | X | X |

| Funcionalidade (USO) | Baixa de Titulos no Contas a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |

| Funcionalidade (USO) | Baixa de Títulos no Contas a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos por vendedor no Contas a Pagar | 518 | X |  |
| No cancelamento da baixa de títulos por vendor no Contas a Pagar | 519 | X |  |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X | X |

| Funcionalidade (USO) | Recebimento Diversos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de recibos do valor total recebido | 575 | X | X |
| Na inclusão de NCC / RA - Saldo remanescente | 575 | X | X |
| Na baixa do valor total/parcial do titulo baixado | 575 | X | X |

| Funcionalidade (USO) | Recebimento Diversos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline | No estorno/cancelamento de um recibo | 576 |  | X |

| Funcionalidade (USO) | Baixa Automática Títulos no Contas a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 | X | X |

| Funcionalidade (USO) | Manutenção do Cad.de Movimentos Bancários | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de movimentos a pagar com rateio nos Movimentos Bancários | 516 | X | X |
| Na inclusão de movimentos a receber com rateio nos Movimentos Bancários | 517 | X | X |
| No cancelamento de movimentos a receber com rateio CC nos Movimentos Bancários | 557 | X | X |
| No cancelamento de movimentos a receber com rateio CC nos Movimentos Bancários | 558 | X | X |
| Na inclusão de movimento de saída banco origem transferência nos Movimentos Bancários | 560 | X | X |
| Na inclusão de movimento de entrada banco destino transferência nos Movimentos Bancários | 561 | X | X |
| Na inclusão de movimentos a pagar nos Movimentos Bancários | 562 | X | X |
| Na inclusão de movimentos a receber nos Movimentos Bancários | 563 | X | X |
| No cancelamento de movimentos a pagar nos Movimentos Bancários | 564 | X | X |
| No cancelamento de movimentos a receber nos Movimentos Bancários | 565 | X | X |

| Funcionalidade (USO) | Baixa automática Titulos no Contas a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |

| Funcionalidade (USO) | Manutenção de Aplicações/Empréstimos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de movimentos de Aplicações Financeiras/Empréstimos | 580 | X | X |
| No cancelamento de movimentos de Aplicações Financeiras/Empréstimos | 581 | X |  |

**Importante ⚠️**   
O Lançamento Padrão 581 (Exclusão de contrato) funciona apenas na forma
de
**Contabilização OnLine (independentemente do parâmetro definido na rotina de Aplicações e Empréstimo)**,
pois o contrato é removido, o que inviabiliza a contabilização posterior
na forma OffLine (via CTBAFIN). Para que a exclusão do contrato seja
contabilizada, é necessário que a contabilização da inclusão (seja OnLine
ou OffLine) já tenha sido realizada.

| Funcionalidade (USO) | Resgate de Aplicações/Empréstimos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de movimentos de resgate de Aplicações Financeiras/Empréstimos | 585 | X | X |
| No estorno de movimentos de resgate de Aplicações Financeiras/Empréstimos | 586 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X | X |

| Funcionalidade (USO) | Resgate de Aplicações/Empréstimos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No estorno de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 584 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X |  |

| Funcionalidade (USO) | Resgate de Aplicações/Empréstimos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No estorno de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 584 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X |  |

| Funcionalidade (USO) | Emissão de Cheques | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão/liberação de Cheques sobre Títulos do Contas a Pagar | 566 | X | X |
| Na geração de Cheques | 590 | X | X |
| No cancelamento de Cheques | 591 | X |  |

| Funcionalidade (USO) | Cheques Recebidos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Compensação de Cheques Emitidos | 559 | X | X |
| Estorno da Compensação de Cheques Emitidos | 583 | X |  |

| Funcionalidade (USO) | Retorno de Comunicação Bancária | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |

| Funcionalidade (USO) | Faturas a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na geração de Fatura a Receber | 595 | X |  |
| No cancelamento de Fatura a Receber | 592 | X |  |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X |  |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 | X |  |

| Funcionalidade (USO) | Faturas a Receber - TMS | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No cancelamento de Fatura a Receber | 592 | X |  |

| Funcionalidade (USO) | Faturas a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X |  |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X |  |
| Na geração de Faturas a Pagar | 587 | X |  |
| No cancelamento de Faturas a Pagar | 593 | X |  |

| Funcionalidade (USO) | Comunicação Bancaria - SISPAG | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 | X | X |

| Funcionalidade (USO) | Compensação de Adiantamento a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No cancelamento de Compensações de Adiantamentos de títulos a Receber | 588 | X |  |
| Na realização da Compensação de Adiantamentos de títulos a receber | 596 | X | X |

| Funcionalidade (USO) | Compensação de Adiantamento a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No cancelamento de Compensações de Adiantamentos de títulos a Pagar | 589 | X |  |
| Na realização de Compensação de Adiantamentos de títulos a Pagar | 597 | X | X |

| Funcionalidade (USO) | Variação Monetária | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na Variação Monetária - Contas a Receber | 589 |  | X |
| Na Variação Monetária - Contas a Pagar | 599 |  | X |

| Funcionalidade (USO) | Apuração de IR | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos gerados para o pagamento de IRRF no Contas a Pagar | 510 | X | X |

| Funcionalidade (USO) | Aglutinação de Impostos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos gerados p/pagamento de Impostos Aglutinados no Contas a Pagar | 510 | X | X |
| Na baixa de títulos de pagamento de impostos aglutinados no Contas a Pagar | 530 | X | X |

| Funcionalidade (USO) | Apuração de INSS | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos gerados para o pagamento de INSS no Contas a Pagar | 510 | X | X |

| Funcionalidade (USO) | Cheques sobre Titulos | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão/liberação de Cheques sobre Títulos a Pagar | 566 | X | X |
| Na inclusão de Cheques Avulsos | 567 | X | X |
| No cancelamento de Cheques Avulsos | 568 | X |  |
| No Redepósito de Cheques sobre Títulos a Pagar | 569 | X |  |
| No cancelamento de Cheques sobre Títulos a Pagar | 571 | X |  |

| Funcionalidade (USO) | Retorno de Comunicação Bancária a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X |  |
| Na baixa de títulos manual ou automática no Contas a Pagar | 532 |  | X |

| Funcionalidade (USO) | Compensação entre Carteiras | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| No cancelamento da Compensação entre Carteiras | 530 | X |  |
| Na Compensações entre as Carteiras a Pagar / a Receber | 532 | X |  |

| Funcionalidade (USO) | Liquidação de Títulos a Receber | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na geração do Títulos a Receber (Liquidação) | 500 | X | X |
| Na exclusão do Título de Liquidação | 505 | X |  |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| No cancelamento da baixa dos Títulos | 527 |  | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| No estorno da variação monetária ao cancelar uma liquidação | 59A | X |  |

| Funcionalidade (USO) | Movimentos do Caixinha | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na efetivação de movimentos do Caixinha | 572 | X | X |
| Na efetivação de movimentos do Banco para o Caixinha - Reposição | 573 | X | X |

| Funcionalidade (USO) | Liquidação de Títulos a Pagar | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na geração do Título a Pagar (Liquidação) | 510 | X | X |
| No cancelamento da Liquidação | 515 | X |  |
| Na baixa p/ Liquidação (baixa dos títulos que irão compor a liquidação) | 530 | X | X |
| No cancelamento da baixa p/ Liquidação | 531 | X |  |

| Funcionalidade (USO) | Manutenção de Borderô | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 | X | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 | X | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 | X | X |
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 | X | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 | X | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 | X | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 | X | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 | X | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 | X | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 | X | X |

| Funcionalidade (USO) | Prestação de contas | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Prestação de Contas | 8B3 |  | X |
| Estorno da Prestação de Contas | 8B4 | X |  |
| Cabeçalho Prestação de Contas | 8B5 |  | X |
| Estorno do Cabeçalho Prestação de Contas | 8B6 | X |  |

**Importante ⚠️**   
O parâmetro MV\_DTCTBPC define se a contabilização da prestação de contas
será feita na data da prestação de contas ou na data da emissão dos títulos
a receber ou a pagar. Esse parâmetro é utilizado somente na contabilização
off-line (CTBAFIN).  
**MV\_DTCTBPC:** Data que será considerada para contabilização da
Prestação de Contas.

- 1= Data Inc. Prest.(FLF\_EMISSA)
- 2 = Data Emissão Titulo (E2\_EMIS1 para a carteira a pagar / E1\_EMISSAO
  para a carteira a receber)
  
**DEMAIS INFORMAÇÕES**  
Na rotina de contabilização off-line, se estiver configurado para contabilizar
pela data de emissão do título:- Não irá contabilizar as prestações de contas que possuam as despesas
  no mesmo valor que o adiantamento, isto é, para as prestações de contas
  sem título a pagar ou a receber. Nesse caso, essas prestações de contas
  devem ser contabilizadas manualmente;
- O filtro para contabilização é a data de emissão do título;
- Sempre irá contabilizar todos os títulos do período solicitado independente
  da configuração da Carteira (Pagar/Receber/Ambos);
- Só é permitido contabilizar a prestação de contas pela data de emissão
  do título (MV\_DTCTBPC=2) através da rotina Contabilização Off-line (CTBAFIN);

| Funcionalidade (USO) | Contabilização Off Line | | | |
| --- | --- | --- | --- | --- |
| LP | Online | Offline |
| Na inclusão de títulos no Contas a Receber | 500 |  | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 |  | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 |  | X |
| No inclusão de títulos com rateio CC e multiplas naturezas no Contas a Receber | 506 |  | X |
| Na inclusão de titulos com rateio CC e multiplas naturezas no Contas a Pagar | 508 |  | X |
| Na inclusão de títulos no Contas a Pagar | 510 |  | X |
| Na inclusão de títulos com rateio CC no Contas a Pagar | 511 |  | X |
| Na inclusão de títulos tipo PA no Contas a Pagar | 513 |  | X |
| Na inclusão de movimentos a pagar com rateio CC nos Movimentos Bancários | 516 |  | X |
| Na inclusão de movimentos a receber com rateio CC nos Movimentos Bancários | 517 |  | X |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 |  | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 |  | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 |  | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 |  | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 |  | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 |  | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 |  | X |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 |  | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 |  | X |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 |  | X |
| No cancelamento da baixa de títulos manual ou automática no Contas a Pagar | 531 |  | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 |  | X |
| Na transferência para Carteira de Cobrança no Contas a Receber (0/F/G) | 540 |  | X |
| Na transferência para Carteira de Cobrança Simples/Cartório no Contas a Receber (1/H) | 541 |  | X |
| Na transferência para Carteira de Cobrança Descontada no Contas a Receber (2) | 542 |  | X |
| Na transferência para Carteira de Cobrança Caucionada no Contas a Receber (3) | 543 |  | X |
| Na transferência para Carteira de Cobrança Vinculada no Contas a Receber (4) | 544 |  | X |
| Na transferência para Carteira de Cobrança Advogado no Contas a Receber (5) | 545 |  | X |
| Na transferência para Carteira de Cobrança Judicial no Contas a Receber (6) | 546 |  | X |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 |  | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 |  | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 |  | X |
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 |  | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 |  | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 |  | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 |  | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 |  | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 |  | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 |  | X |
| Na inclusão de movimentos a pagar nos Movimentos Bancários | 562 |  | X |
| Na inclusão de movimentos a receber nos Movimentos Bancários | 563 |  | X |
| No cancelamento de movimentos a pagar nos Movimentos Bancários | 564 |  | X |
| No cancelamento de movimentos a receber nos Movimentos Bancários | 565 |  | X |
| Na realização da Compensação de Adiantamentos de títulos a receber | 596 |  | X |
| Na realização de Compensação de Adiantamentos de títulos a pagar | 597 |  | X |

| - | | | |
| --- | --- | --- | --- |
| FINA040 / FINA740 - Manutenção do Contas a Receber | LP | Online | Offline |
| Na inclusão de títulos no Contas a Receber | 500 | X | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 | X | X |
| No cancelamento de títulos tipo RA no Contas a Receber | 502 | X |  |
| Na substituição de títulos provisórios no Contas a Receber | 503 | X |  |
| Na inclusão de títulos gerados através do desdobramento no Contas a Receber | 504 | X | X |
| No exclusão de títulos do Contas a Receber | 505 | X |  |
| No inclusão de títulos com rateio CC e multiplas naturezas no Contas a Receber | 506 | X | X |
| No cancelamento de títulos com rateio CC e múltiplas naturezas no Contas a Receber | 507 | X |  |
| Na cancelamento de títulos gerados através do desdobramento no Contas a Receber | 529 | X |  |
| Na exclusão de títulos do contas a receber com variação monetária gerada pela rotina FINA350 | 59A | X |  |
| - | | | |
| FINA050 / FINA750 - Manutenção do Contas a Pagar | LP | Online | Offline |
| Na inclusão de títulos com rateio CC e múltiplas naturezas no Contas a Pagar | 508 | X | X |
| No cancelamento de títulos com rateio CC e múltiplas naturezas no Contas a Pagar | 509 | X |  |
| Na inclusão de títulos no Contas a Pagar | 510 | X | X |
| Na inclusão de títulos com rateio CC no Contas a Pagar | 511 | X | X |
| Na cancelamento de títulos com rateio CC no Contas a Pagar | 512 | X |  |
| Na inclusão de títulos tipo PA no Contas a Pagar | 513 | X | X |
| No cancelamento de títulos tipo PA no Contas a Pagar | 514 | X |  |
| No cancelamento de títulos no Contas a Pagar | 515 | X |  |
| Na substituição de títulos provisórios no Contas a Pagar | 533 | X | X |
| Na inclusão de títulos gerados por desdobramento no Contas a Pagar | 577 | X | X |
| No cancelamento de títulos gerados por desdobramento no Contas a Pagar | 578 | X |  |
| - | | | |
| FINA060 - Transferências no Contas a Receber | LP | Online | Offline |
| Na transferência para Carteira de Cobrança no Contas a Receber (0/F/G) | 540 | X | X |
| Na transferência para Carteira de Cobrança Simples/Cartório no Contas a Receber (1/H) | 541 | X | X |
| Na transferência para Carteira de Cobrança Descontada no Contas a Receber (2) | 542 | X | X |
| Na transferência para Carteira de Cobrança Caucionada no Contas a Receber (3) | 543 | X | X |
| Na transferência para Carteira de Cobrança Vinculada no Contas a Receber (4) | 544 | X | X |
| Na transferência para Carteira de Cobrança Advogado no Contas a Receber (5) | 545 | X | X |
| Na transferência para Carteira de Cobrança Judicial no Contas a Receber (6) | 546 | X | X |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 | X | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 | X | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 | X | X |
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 | X | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 | X | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 | X | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 | X | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 | X | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 | X | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 | X | X |
| - | | | |
| FINA070 - Baixa de Titulos no Contas a Receber | LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| - | | | |
| FINA080 - Baixa de Títulos no Contas a Pagar | LP | Online | Offline |
| Na baixa de títulos por vendedor no Contas a Pagar | 518 | X |  |
| No cancelamento da baixa de títulos por vendor no Contas a Pagar | 519 | X |  |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X | X |
| - | | | |
| FINA090 - Baixa Automática Títulos no Contas a Pagar | LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 | X | X |
| - | | | |
| FINA100 - Manutenção do Cad.de Movimentos Bancários | LP | Online | Offline |
| Na inclusão de movimentos a pagar com rateio nos Movimentos Bancários | 516 | X | X |
| Na inclusão de movimentos a receber com rateio nos Movimentos Bancários | 517 | X | X |
| No cancelamento de movimentos a receber com rateio CC nos Movimentos Bancários | 557 | X | X |
| No cancelamento de movimentos a receber com rateio CC nos Movimentos Bancários | 558 | X | X |
| Na inclusão de movimento de saída banco origem transferência nos Movimentos Bancários | 560 | X | X |
| Na inclusão de movimento de entrada banco destino transferência nos Movimentos Bancários | 561 | X | X |
| Na inclusão de movimentos a pagar nos Movimentos Bancários | 562 | X | X |
| Na inclusão de movimentos a receber nos Movimentos Bancários | 563 | X | X |
| No cancelamento de movimentos a pagar nos Movimentos Bancários | 564 | X | X |
| No cancelamento de movimentos a receber nos Movimentos Bancários | 565 | X | X |
| - | | | |
| FINA110 - Baixa automática Titulos no Contas a Receber | LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| - | | | |
| FINA171 / FINA716 - Manutenção de Aplicações/Empréstimos | LP | Online | Offline |
| Na inclusão de movimentos de Aplicações Financeiras/Empréstimos | 580 | X | X |
| No cancelamento de movimentos de Aplicações Financeiras/Empréstimos | 581 | X |  |
| - | | | |
| FINA181 / FINA716 - Resgate de Aplicações/Empréstimos | LP | Online | Offline |
| Na inclusão de movimentos de resgate de Aplicações Financeiras/Empréstimos | 585 | X | X |
| No estorno de movimentos de resgate de Aplicações Financeiras/Empréstimos | 586 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X | X |
| - | | | |
| FINA182 / FINA716 - Resgate de Aplicações/Empréstimos | LP | Online | Offline |
| No estorno de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 584 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X |  |
| - | | | |
| FINA183 - Resgate de Aplicações/Empréstimos | LP | Online | Offline |
| No estorno de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 584 | X |  |
| Na inclusão de movimentos de apropriações de Aplicações Financeiras/Empréstimos | 582 | X |  |
| - | | | |
| FINA190 - Emissão de Cheques | LP | Online | Offline |
| Na inclusão/liberação de Cheques sobre Títulos do Contas a Pagar | 566 | X | X |
| Na geração de Cheques | 590 | X | X |
| No cancelamento de Cheques | 591 | X |  |
| - | | | |
| FINA191 - Cheques Recebidos | LP | Online | Offline |
| Compensação de Cheques Emitidos | 559 | X | X |
| Estorno da Compensação de Cheques Emitidos | 583 | X |  |
| - | | | |
| FINA200 - Retorno de Comunicação Bancária | LP | Online | Offline |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| - | | | |
| FINA280 - Faturas a Receber | LP | Online | Offline |
| Na geração de Fatura a Receber | 595 | X |  |
| No cancelamento de Fatura a Receber | 592 | X |  |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X |  |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 | X |  |
| - | | | |
| FINA281 - Faturas a Receber - TMS | LP | Online | Offline |
| No cancelamento de Fatura a Receber | 592 | X |  |
| - | | | |
| FINA290 - Faturas a Pagar | LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X |  |
| No cancelamento da baixa de títulos manual e automática no Contas a Pagar | 531 | X |  |
| Na geração de Faturas a Pagar | 587 | X |  |
| No cancelamento de Faturas a Pagar | 593 | X |  |
| - | | | |
| FINA300 - Comunicação Bancaria - SISPAG | LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 | X | X |
| - | | | |
| FINA330 - Compensação de Adiantamento a Receber | LP | Online | Offline |
| No cancelamento de Compensações de Adiantamentos de títulos a Receber | 588 | X |  |
| Na realização da Compensação de Adiantamentos de títulos a receber | 596 | X | X |
| - | | | |
| FINA340 - Compensação de Adiantamento a Pagar | LP | Online | Offline |
| No cancelamento de Compensações de Adiantamentos de títulos a Pagar | 589 | X |  |
| Na realização de Compensação de Adiantamentos de títulos a Pagar | 597 | X | X |
| - | | | |
| FINA350 - Variação Monetária | LP | Online | Offline |
| Na Variação Monetária - Contas a Receber | 589 |  | X |
| Na Variação Monetária - Contas a Pagar | 599 |  | X |
| - | | | |
| FINA375 - Apuração de IR | LP | Online | Offline |
| Na inclusão de títulos gerados para o pagamento de IRRF no Contas a Pagar | 510 | X | X |
| - | | | |
| FINA376 - Aglutinação de Impostos | LP | Online | Offline |
| Na inclusão de títulos gerados p/pagamento de Impostos Aglutinados no Contas a Pagar | 510 | X | X |
| Na baixa de títulos de pagamento de impostos aglutinados no Contas a Pagar | 530 | X | X |
| - | | | |
| FINA377 - Apuração de INSS | LP | Online | Offline |
| Na inclusão de títulos gerados para o pagamento de INSS no Contas a Pagar | 510 | X | X |
| - | | | |
| FINA390 - Cheques sobre Titulos | LP | Online | Offline |
| Na inclusão/liberação de Cheques sobre Títulos a Pagar | 566 | X | X |
| Na inclusão de Cheques Avulsos | 567 | X | X |
| No cancelamento de Cheques Avulsos | 568 | X |  |
| No Redepósito de Cheques sobre Títulos a Pagar | 569 | X |  |
| No cancelamento de Cheques sobre Títulos a Pagar | 571 | X |  |
| - | | | |
| FINA430 - Retorno de Comunicação Bancária a Pagar | LP | Online | Offline |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 | X |  |
| Na baixa de títulos manual ou automática no Contas a Pagar | 532 |  | X |
| - | | | |
| FINA450 - Compensação entre Carteiras | LP | Online | Offline |
| No cancelamento da Compensação entre Carteiras | 530 | X |  |
| Na Compensações entre as Carteiras a Pagar / a Receber | 532 | X |  |
| - | | | |
| FINA460 - Liquidação de Títulos a Receber | LP | Online | Offline |
| Na geração do Títulos a Receber (Liquidação) | 500 | X | X |
| Na exclusão do Título de Liquidação | 505 | X |  |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 | X | X |
|
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 | X | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 | X | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 | X | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 | X | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 | X | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 | X | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| No cancelamento da baixa dos Títulos | 527 |  | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 | X | X |
| No estorno da variação monetária ao cancelar uma liquidação | 59A | X |  |
| - | | | |
| FINA550 - Movimentos do Caixinha | LP | Online | Offline |
| Na efetivação de movimentos do Caixinha | 572 | X | X |
| Na efetivação de movimentos do Banco para o Caixinha - Reposição | 573 | X | X |
| - | | | |
| FINA565 - Liquidação de Títulos a Pagar | LP | Online | Offline |
| Na geração do Título a Pagar (Liquidação) | 510 | X | X |
| No cancelamento da Liquidação | 515 | X |  |
| Na baixa p/ Liquidação (baixa dos títulos que irão compor a liquidação) | 530 | X | X |
| No cancelamento da baixa p/ Liquidação | 531 | X |  |
| - | | | |
| FINA590 - Manutenção de Borderô | LP | Online | Offline |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 | X | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 | X | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 | X | X |
|
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 | X | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 | X | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 | X | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 | X | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 | X | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 | X | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 | X | X |
| - | | | |
| CTBAFIN - Contabilização Off Line | LP | Online | Offline |
| Na inclusão de títulos no Contas a Receber | 500 |  | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 |  | X |
| Na inclusão de títulos tipo RA no Contas a Receber | 501 |  | X |
| No inclusão de títulos com rateio CC e multiplas naturezas no Contas a Receber | 506 |  | X |
| Na inclusão de titulos com rateio CC e multiplas naturezas no Contas a Pagar | 508 |  | X |
| Na inclusão de títulos no Contas a Pagar | 510 |  | X |
| Na inclusão de títulos com rateio CC no Contas a Pagar | 511 |  | X |
| Na inclusão de títulos tipo PA no Contas a Pagar | 513 |  | X |
| Na inclusão de movimentos a pagar com rateio CC nos Movimentos Bancários | 516 |  | X |
| Na inclusão de movimentos a receber com rateio CC nos Movimentos Bancários | 517 |  | X |
| Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G) | 520 |  | X |
| Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H) | 521 |  | X |
| Na baixa de títulos Cobrança Descontada no Contas a Receber (2) | 522 |  | X |
| Na baixa de títulos Cobrança Caucionada no Contas a Receber (3) | 523 |  | X |
| Na baixa de títulos Cobrança Vinculada no Contas a Receber (4) | 524 |  | X |
| Na baixa de títulos Cobrança Advogado no Contas a Receber (5) | 525 |  | X |
| Na baixa de títulos Cobrança Judicial no Contas a Receber (6) | 526 |  | X |
| No cancelamento da baixa de Titulos no Contas a Receber | 527 |  | X |
| Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7) | 528 |  | X |
| Na baixa de títulos manual ou automática no Contas a Pagar | 530 |  | X |
| No cancelamento da baixa de títulos manual ou automática no Contas a Pagar | 531 |  | X |
| Na baixa de títulos automática com borderô no Contas a Pagar | 532 |  | X |
| Na transferência para Carteira de Cobrança no Contas a Receber (0/F/G) | 540 |  | X |
| Na transferência para Carteira de Cobrança Simples/Cartório no Contas a Receber (1/H) | 541 |  | X |
| Na transferência para Carteira de Cobrança Descontada no Contas a Receber (2) | 542 |  | X |
| Na transferência para Carteira de Cobrança Caucionada no Contas a Receber (3) | 543 |  | X |
| Na transferência para Carteira de Cobrança Vinculada no Contas a Receber (4) | 544 |  | X |
| Na transferência para Carteira de Cobrança Advogado no Contas a Receber (5) | 545 |  | X |
| Na transferência para Carteira de Cobrança Judicial no Contas a Receber (6) | 546 |  | X |
| Na geração do Borderô p/Carteira de Cobrança no Contas a Receber (0/F/G) | 547 |  | X |
| Na geração do Borderô para Cobrança Simples/Cartório no Contas a Receber (1/H) | 548 |  | X |
| Na geração de Borderô para Cobrança Descontada no Contas a Receber (2) | 549 |  | X |
| Na geração de Borderô para Cobrança Caucionada no Contas a Receber (3) | 550 |  | X |
| Na geração de Borderô para Cobrança Vinculada no Contas a Receber (4) | 551 |  | X |
| Na geração de Borderô para Cobrança Advogado no Contas a Receber (5) | 552 |  | X |
| Na geração de Borderô para Cobrança Judicial no Contas a Receber (6) | 553 |  | X |
| No cancelamento do Bordero de títulos do Contas a Receber | 554 |  | X |
| Na transferência para Cobrança Caucionada Descontada no Contas a Receber (7) | 555 |  | X |
| Na geração de Borderó p/Cobrança Caucionada Descontada no Contas a Receber (7) | 556 |  | X |
| Na inclusão de movimentos a pagar nos Movimentos Bancários | 562 |  | X |
| Na inclusão de movimentos a receber nos Movimentos Bancários | 563 |  | X |
| No cancelamento de movimentos a pagar nos Movimentos Bancários | 564 |  | X |
| No cancelamento de movimentos a receber nos Movimentos Bancários | 565 |  | X |
| Na realização da Compensação de Adiantamentos de títulos a receber | 596 |  | X |
| Na realização de Compensação de Adiantamentos de títulos a pagar | 597 |  | X |
