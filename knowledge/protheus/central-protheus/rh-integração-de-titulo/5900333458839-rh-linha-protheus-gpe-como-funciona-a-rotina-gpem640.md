---
article_id: 5900333458839
category: RH - Integração de Titulo
content_hash: 02529ba0c270ad38b4e16dbdedf91fc16907490db87f89d92da688a43edcbe42
fetched_at: '2026-06-28T22:43:36.521327+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como funciona a rotina GPEM640
type: support-article
updated_at: '2025-07-18T13:44:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5900333458839-RH-Linha-Protheus-GPE-Como-funciona-a-rotina-GPEM640
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona a rotina GPEM640?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução****Definição de títulos - GPEM640**Esta rotina define as regras para a geração dos títulos a pagar.

Após definir as regras dos títulos, devem ser efetuadas a Geração, Manutenção (se necessário) e a integração com Financeiro, afim de que os esses títulos sejam efetivamente pagos.  
  
Na definição dos títulos, o sistema considera as datas de vencimentos por funcionário e gera um título para cada tipo de pagamento, a fim de que os pagamentos tenham vencimentos diferentes para um mesmo funcionário.

Por exemplo:

Ao definir títulos de férias com agrupamentos de funcionários, é possível gerar uma data de vencimento diferente para cada título de cada funcionário.  
[RH - Linha Protheus - GPE - Como configurar um título de férias para busca de data de vencimento automaticamente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036119174-RH-Linha-Protheus-GPE-Como-configurar-um-t%C3%ADtulo-de-f%C3%A9rias-para-busca-de-data-de-vencimento-automaticamente)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Importante:**  Para os títulos do tipo ‘Imposto de Renda’, é possível definir qual será o de Código de Retenção utilizado para geração do título:  |  |  | | --- | --- | | **1.** | **Informado** = Código de Retenção informado no momento da definição do título, campo ‘Cod Ret Inf’ ; |  |  |  | | --- | --- | | **2.** | **Funcionário** = Código de Retenção cadastrado para o funcionário no [Cadastro de Funcionários](http://www.fbsolutions.com.br/help-online-protheus/gpea010.htm). Para esse tipo de retenção, o agrupamento deverá ser obrigatoriamente por Filial. | |

**Procedimentos**

Para definir Títulos:

|  |  |
| --- | --- |
| **1.** | Em **Definição**, clique em **Incluir**. |

|  |  |
| --- | --- |
| **2.** | Informe os dados conforme orientação dos helps de campo. |

|  |  |
| --- | --- |
| **3.** | Na área**Vencimento do título**, selecione o tipo de vencimento e observe com especial atenção o preenchimento do campo: |

|  |  |
| --- | --- |
| • | **Vencto dia não útil** |

Indica se o pagamento do título deve ser antecipado, caso a data de pagamento seja um dia não útil, como por exemplo: sábados, domingos ou feriados. Selecione:

**1 -** **Antecipa**- para que o vencimento real do título seja antecipado, nos casos em que esse vencimento for um dia não útil.

**2 -** **Prorroga**- para que o pagamento do título seja postergado.

|  |  |
| --- | --- |
| **4.** | Na área **Títulos disponíveis para seleção**, marque os títulos desejados. |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Importante:**  Todas as verificações das verbas e dos arquivos a serem processadas para sua composição são executadas automaticamente para os tipos de títulos abaixo:  |  |  | | --- | --- | | • | INSS Folha de Pagamento |  |  |  | | --- | --- | | • | INSS 13º. Salário |  |  |  | | --- | --- | | • | Imposto de Renda |  |  |  | | --- | --- | | • | Pensão Alimentícia |  |  |  | | --- | --- | | • | Definido pelo Usuário |  |  |  | | --- | --- | | • | INSS Dissídio |  |  |  | | --- | --- | | • | INSS RRA |  |  |  | | --- | --- | | • | Imposto de Renda RRA |  |  |  | | --- | --- | | • | DARF Desoneração | |

 

|  |  |
| --- | --- |
| **5.** | Ao marcar a opção Definido Pelo Usuário, as regras pertinentes a verbas e arquivos devem ser definidas manualmente e, assim, habilitar a opção Definir Título. |

 

|  |  |
| --- | --- |
| **6.** | Clique em Definir Título. |

 

|  |  |
| --- | --- |
| **7.** | É apresentada a tela Definição das Regras para Composição do Título. |

|  |  |
| --- | --- |
| **8.** | Defina os títulos conforme necessidade. |

|  |  |
| --- | --- |
| **9.** | Confira os dados e confirme. |

**Tabelas utilizadas**

|  |  |
| --- | --- |
| • | RC0 - Definições |

•   SED -  Naturezas

|  |  |
| --- | --- |
| • | RC1 - Movimento de Títulos |

|  |  |
| --- | --- |
| • | SA2 Fornecedores |

|  |  |
| --- | --- |
| • | SRA Funcionários |

|  |  |
| --- | --- |
| • | SRQ Beneficiários |

Documentos para apoio na configuração/definição de títulos:  
[RH - Linha Protheus - GPE - Como criar e configurar um título de folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028042632-RH-Linha-Protheus-GPE-Como-criar-e-configurar-um-t%C3%ADtulo-de-folha-de-pagamento#:~:text=Realize%20a%20configura%C3%A7%C3%A3o%20de%20acordo,realizada%20a%20busca%20da%20verba.)  
[RH - Linha Protheus - GPE - Como gerar um título de Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405047881879-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-Vale-Alimenta%C3%A7%C3%A3o)  
[RH - Linha Protheus - GPE - Como configurar e conferir um título da 1ª Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057657314-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-da-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Como configurar e conferir um título de adiantamento quinzenal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027265791-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-de-adiantamento-quinzenal-)  
[RH - Linha Protheus - GPE - Como configurar e conferir um título de Pensão Alimentícia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403038748439-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-de-Pens%C3%A3o-Aliment%C3%ADcia)  
[RH - Linha Protheus - GPE - Como configurar e conferir um título do Roteiro VEX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058130654-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-do-Roteiro-VEX)  
[RH - Linha Protheus - GPE - Como criar um título rateado por centro de custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028706011-RH-Linha-Protheus-GPE-Como-criar-um-t%C3%ADtulo-rateado-por-centro-de-custos)  
[RH - Linha Protheus - GPE - Como gerar título de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036988633-RH-Linha-Protheus-GPE-Como-gerar-t%C3%ADtulo-de-rescis%C3%A3o)  
[RH - Linha Protheus - GPE - Como gerar um título de FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055528913-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-FGTS)  
  
Saiba Mais:  
[Página Centralizadora rotina Integrações de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
