---
article_id: 360028185051
category: Comércio Exterior - Easy - Financing
content_hash: 19c0e9c2b3f3eb42ab9e3e1bd9efd150d91fe4a44bce2867c36d71a3446ef1e3
fetched_at: '2026-06-28T22:39:53.001060+00:00'
product: protheus
section_id: 1500001538101
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEFF - Eventos do Easy
  Financing para contratos de Exportação
type: support-article
updated_at: '2022-04-25T20:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028185051-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEFF-Eventos-do-Easy-Financing-para-contratos-de-Exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Quando são gerados os eventos do contrato ACC e ACE?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Financing Control – A partir da versão 11.80  
  
**Solução**A tabela abaixo indica quais eventos são utilizados pelos contratos de exportação no Easy Financing.

Os eventos estão separados em grupos:

**Principal** - Eventos relacionados aos valores de principal do contrato, incluindo a captação do contrato, amortização, variações cambiais, etc.

**Juros** - Eventos relacionados ao juros. Como podem ser cadastrados diferentes tipos de juros para os contratos, os eventos estão relacionados ao um tipo especifico de juros, definindo um intervalo de eventos que possuem o mesmo significado e comportamento no sistema.

**Encargos/ Despesas** - Códigos reservados para uso de encargos/despesas.

**Estorno** - Evento de estorno de outros eventos já contabilizados.

Nas colunas temos a descrição do evento para cada tipo de financiamento da versão padrão do sistema.

Os contratos possuem um comportamento diferenciado conforme a definição de contrato parcelado. Quando o contrato não é parcelado, o comportamento do sistema é sempre equivalente ao tipos de financiamento ACC (FIEX01) e ACE (FIEX02). Quando o contrato é parcelado, o comportamento para criação dos eventos é semelhante ao Pré-pagamento (FIEX03) e Securitização (FIEX04).

Outros tipos de contratos que possam ser cadastrados no sistema através do Cadastro de tipos de financiamento, devem ter os eventos incluídos no Cadastro de Eventos do módulo Easy Financing.

No cadastro de eventos do módulo Easy Financing, os eventos que correspondem ao financiamento de exportação são indicados pelo campo módulo com as iniciais "FIEX" seguida do código do tipo de financiamento.

As descrições consideradas nas telas do sistema para cada evento seguem o que estiver definido no cadastro de eventos e podem divergir da descrição abaixo apresentada.

 

A coluna **"Significado"** indica o que o evento representa para o sistema e a coluna**"Geração do evento"**temos os momentos em que cada evento é criado pelo sistema.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo** | **Evento** | **Descrição ACC (FIEX01)** | **Descrição ACE (FIEX02)** | **Descrição Pré-pagamento (FIEX03)** | **Descrição Securitização (FIEX04)** | **Significado** | **Geração do Evento** |
| Principal | 100 | ACC Contrato | ACE Contrato | Pre Pagamento Contra | Securit. Contrato | Representa a captação do contrato, com a cotação da moeda preenchida no campo taxa do contrato e data do evento correspondente a data de crédito do contrato. | Gerado na inclusão do contrato e atualizado com o preenchimento das informações de taxa do contrato ou data de crédito/data de inicio de juros. |
| 180 | Encerr Contrato ACC | Encerr Contrato ACC | N/A | N/A | Representa o valor encerrado do contrato. | Gerado através da liquidação do evento principal (100), utilizando a opção encerramento de contrato. |
| 190 | Transf Cont ACC/PREP | Transf Cont ACE/PREP | N/A | N/A | Representa o valor transferido do contrato. | Gerado através da liquidação do evento principal (100), utilizando a opção transferência de contrato. |
| 500 | V.C. ACC | V.C. ACE | V.C. Principal | V.C. Principal | Variação cambial do principal quando positiva (cotação da moeda teve alta). | Este evento é gerados nas vinculações de invoice de exportação ao contrato, liquidação de invoice vinculada ao contrato e na contabilização do contrato, nos casos em que o calculo da variação cambial é positiva. |
| 501 | V.C. ACC | V.C. ACE | V.C. Principal | V.C. Principal | Variação cambial do principal quando negativa (cotação da moeda teve baixa). | Este evento é gerados nas vinculações de invoice de exportação ao contrato, liquidação de invoice vinculada ao contrato e na contabilização do contrato, nos casos em que o calculo da variação cambial é negativa. |
| 600 | Transf.ACC P/ACE | Invoice Exportacao | Vinculação Invoice | Vinculação Invoice | Representa a invoice exportação vinculada ao contrato | A vinculação é gerada no contrato quando utilizadas a tela de vinculação de invoice no contrato de financiamento, câmbio de exportação ou através da efetivação de uma pré-vinculação. |
| 630 | Liquidacao Principal | Liquidacao Principal | Liquidação Invoice | Liquidação Invoice | Representa a liquidação invoice exportação vinculada ao contrato, amortizando o saldo devedor do financiamento. | Este evento é criado no momento da liquidação do câmbio exportação de um parcela de invoice vinculada a um contrato de financiamento. É possível efetuar essa liquidação utilizando as rotinas de câmbio exportação, FFC ou câmbio tipo 3 e 4. |
| 660 | Liq Principal Forc | Liq Principal Forc | N/A | N/A | Representa pagamento referente a invoice exportação vinculada ao contrato sem a liquidação do câmbio da invoice correspondente, caso em que o cliente não realizou o pagamento da invoice e o tomador do contrato arcou com o pagamento ao banco, amortizando o saldo devedor do financiamento. | Gerado quando utilizada a opção liquidação no evento de vinculação de invoice (600) através do contrato de financiamento. |
| 700 | N/A | N/A | Parcela do Principal | Parcela do Principal | Parcela do principal para contratos parcelados (pré-pagamento, securitização, etc.) | Gerado quando preenchidas as informações referente ao parcelamento do contrato e a data de crédito/data de inicio de juros. A quantidade de parcelas de principal criadas assim como seus valores e vencimentos respeitam as configurações definidos na aba "Parcelas de Pag." do contrato. |
| Juros | 520 á 529 | Prov Juros ACC | Prov Juros ACE | Provisao de Juros | Provisao de Juros | Provisão ou apropriação de juros, utilizado para contabilização dos juros em andamento no contrato. O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, sua provisão de juros será o evento 520. | Gerada quando ocorre uma vinculação de invoice, liquidação de invoice ou contabilização de contratos. |
| 510 á 519 | Est Prov Juros ACC | Est Prov Juros ACE | Est Prov de Juros | Est Prov de Juros | Representa o estorno de valores já provisionados ou apropriados de juros. O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, o estorno de provisão de juros será o evento 510. | Ocorre em casos que já havia sido lançada uma provisão de juros, porém precisa ser estornada, por exemplo, caso a taxa de juros tenha sido alterada ou uma invoice vinculada e contabilizada precise ser excluída do contrato. O evento é lançado apenas com o valor da diferença que precisa ser estornada. |
| Eventos pares de 550 á 568 | V.C. JUROS ACC | V.C. JUROS ACE | V.C. JUROS | V.C. JUROS | Variação cambial dos juros quando positiva (cotação da moeda teve alta). O evento 550 corresponde a variação cambial positiva para o tipo de juros cadastrado com o código 0. O evento 552 corresponde a variação cambial positiva para o tipo de juros código 1. A formula 550+2\*X, onde X é o código do tipo de juros, indica qual o código do evento para a variação cambial positiva de juros código X. | Gerada quando ocorre uma vinculação de invoice, liquidação de invoice ou contabilização de contratos que possuíam provisão de juros. Devido a necessidade de atualizar o valor em reais dessas provisões, o sistema irá criar este evento de variação com a diferença quando positiva. |
| Eventos impares de 551 á 569 | V.C. JUROS ACC | V.C. JUROS ACC | V.C. JUROS | V.C. JUROS | Variação cambial dos juros quando negativa (cotação da moeda teve baixa). O evento 551 corresponde a variação cambial negativa para o tipo de juros cadastrado com o código 0. O evento 553 corresponde a variação cambial negativa para o tipo de juros código 1. A formula 551+2\*X, onde X é o código do tipo de juros, indica qual o código do evento para a variação cambial negativa de juros código X. | Gerada quando ocorre uma vinculação de invoice, liquidação de invoice ou contabilização de contratos que possuíam provisão de juros. Devido a necessidade de atualizar o valor em reais dessas provisões, o sistema irá criar este evento de variação com a diferença quando negativa. |
| 650 á 659 | Transf Juros ACE | Transf Juros | N/A | N/A | Este evento representa a transferência dos juros de ACC para ACE. O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, o transferência de juros será o evento 650. | Ocorre no momento em que uma vinculação de invoice (evento 600) for realizada e houverem provisões de juros no contrato calculadas durante o período ACC, ou seja, os juros calculados enquanto não havia invoice vinculada são transferidos contabilmente para ACE, com a devida proporção do valor da invoice com relação ao valor do contrato. |
| 620 á 629 | Juros antecipado | Juros antecipado | N/A | N/A | Eventos iniciados com "62" representam Juros a pagar de forma antecipada. 620 é o evento para o tipo de juros código 0, 621 para o tipo de juros código 1 até o 629 que representa o tipo de juros 9. | Esse evento é gerado quando utilizada a opção "Juros Antecipado" na tela de períodos do contrato, podendo ser utilizado para pagamento dos juros no financeiro ou apenas para contabilização de forma antecipada de todo juros do período. |
| Eventos pares de 580 á 598 | V.C. JUR ANT | V.C. JUR ANT | N/A | N/A | Variação cambial dos juros antecipados quando positiva (cotação da moeda teve alta). O evento 580 corresponde a variação cambial positiva para o tipo de juros cadastrado com o código 0. O evento 582 corresponde a variação cambial positiva para o tipo de juros código 1. A formula 580+2\*X, onde X é o código do tipo de juros, indica qual o código do evento para a variação cambial positiva de juros antecipados de código X. | Gerado quando ocorre a contabilização de contratos que possuem juros antecipado ou no momento da liquidação dos juros efetivos. Devido a necessidade de atualizar o valor em reais dos juros pagos antecipadamente, o sistema irá criar este evento de variação com a diferença quando positiva. |
| Eventos impares de 581 á 599 | V.C. JUR ANT | V.C. JUR ANT | N/A | N/A | Variação cambial dos juros antecipados quando negativa (cotação da moeda teve baixa). O evento 581 corresponde a variação cambial negativa para o tipo de juros cadastrado com o código 0. O evento 583 corresponde a variação cambial negativa para o tipo de juros código 1. A formula 581+2\*X, onde X é o código do tipo de juros, indica qual o código do evento para a variação cambial negativa de juros antecipados de código X. | Gerado quando ocorre a contabilização de contratos ou no momento da liquidação dos juros efetivos quando há juros antecipados no contrato. Devido a necessidade de atualizar o valor em reais dos juros pagos antecipadamente, o sistema irá criar este evento de variação com a diferença quando negativa. |
| 640 á 649 | Liq. de Juros | Liq. de Juros | N/A | N/A | Representa a liquidação de juros. O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, sua liquidação de juros será o evento 640. | Este evento é criado no momento em que ocorrer a liquidação do principal (evento 630). |
| 670 á 679 | Liq Juros Forc | Liq Juros Forc | N/A | N/A | Representa a liquidação de juros para encerramento ou transferência de contrato. O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, sua liquidação de juros será o evento 670. | Este evento é criado quando ocorre um encerramento de contrato (evento 180) ou transferência de contrato (evento 190). |
| 710 á 719 | N/A | N/A | Parcela Juros | Parcela Juros | Parcela de juros para contratos parcelados (pré-pagamento, securitização, etc.). O ultimo digito do evento representa o tipo de juros cadastrado, por exemplo, para o tipo de juros cadastrado com o código 0, sua liquidação de juros será o evento 710. | Gerado quando preenchidas as informações referente ao parcelamento do contrato e a data de crédito/data de inicio de juros. A quantidade de parcelas de juros criadas assim como seus valores e vencimentos respeitam as configurações definidos na aba "Parcelas de Pag." do contrato. |
| Encargos/Despesas | 300 á 499 | - | - | - | - | Os eventos entre 300 a 499 são reservados para cadastro de encargos. O sistema não possui carga padrão para esses eventos. Cada código pode ser utilizado efetuando o cadastro do evento pela manutenção de eventos contábeis do módulo de financiamento. | Esses eventos podem ser criados manualmente pelo usuário através da opção "Incluir" na manutenção de um contrato de financiamento, ou gerados de forma automática com a configuração da aba "Encargos" do contrato de financiamento. A configuração permite que um encargo seja gerado de forma automática associado a geração de um outro evento padrão do sistema. |
| Estorno | 999 | Estorno | Estorno | Estorno | Estorno | Representa o estorno de um evento já contabilizado no contrato. O evento 999 mantem a relação com o evento original que foi estornado, para que possa ser contabilizado conforme as contas contábeis de estorno do evento original. | Gerado nas operações de estorno como estorno de vinculação, estorna de liquidação, etc quando o evento original não pode ser excluído por estar contabilizado, obrigando a ser realizado um lançamento de estorno na contabilidade. |

**Link do boletim técnico: [Eventos do Easy Financing para contratos de Exportação](http://tdn.totvs.com/pages/releaseview.action?pageId=272407412)**
