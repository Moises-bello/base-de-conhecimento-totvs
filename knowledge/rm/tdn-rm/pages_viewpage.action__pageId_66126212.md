---
content_hash: cb117b5981ce6b56dcf0bec8b55e205a23489d7c3a969efd2a18ca20de7b518c
fetched_at: '2026-06-29T00:11:13.437222+00:00'
page_id: '66126212'
product: rm
source: tdn-rm
title: NF-e - Parametrizar o sistema para emissão de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66126212
version: 11
---

1538655999529\_-1360407308

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | Paramtrizar o sistema para emissão de NF-e |
| **Subprocesso** | **:** | Paramtrizar o sistema para emissão de NF-e |
| **Data da publicação** | **:** | 09/07/2013 |

**Introdução:**

Este documento tem o objetivo de direcionar a implantação da NF-e, porem é muito importante que este processo seja acompanhado por um **consultor Totvs** e um responsável de **TI** da empresa para evitar alguns problemas.

**Importante: se algum dos passos não for executado com sucesso os passos seguintes apresentarão problemas até que a pendência seja resolvida.**

**Passo 1: Instalar e configurar TopConnect**

Siga os passos do link abaixo para a correta instalação e configuração do TopConnect:

**Passo 2: Instalar e configurar o TSS**

Siga os passos do link abaixo para a correta instalação e configuração do TSS:

**Passo 3: Preparar o certificado**

Siga os passos do link abaixo para a correta preparação do certificado digital:

Certificado Digital - Preparar Certificado Digital para Emissão de NF-E

**Passo 4: Configurar os parâmetros da NF-e para a Filial**

Siga os passos do link abaixo para a correta configuração:

**Passo 5: Revisar cadastros**

Siga os passos do link abaixo para conferir os cadastros necessários para a emissão de NF-e:

**Passo 6: Parametrizar o movimento Saída**

Siga os passos do link abaixo para a correta parametrização dos movimentos de Saída para emissão de NF-e:

**Passo 7: Parametrizar o movimento Entrada**

Siga os passos do link abaixo para a correta parametrização dos movimentos de Entrada para emissão de NF-e:

**Passo 8: Enviar a NF-e**

Acesse o seguinte menu: Utilitários SPED NF-e (Estadual) Processos Enviar NF-e.  
Será apresentada uma tela para informar quais movimentos serão enviados, preencha conforme os dados parametrizados e clique em “Executar”.

Após executar o envio a nota ficará com o status pendente, conforme figura abaixo.

Basta aguardar alguns minutos e executar o processo “Consultar Autorização/Cancelamento” e NF-e mudará de pendente para autorizada conforme figura abaixo:

Nesta visão ficaram todas as NF-e que passaram pelo processo descrito acima “Enviar NF-e” podem assumir um dos seguintes STATUS:

Pendente (P)

Inconsistente (I)

Rejeitada (R)

Autorizada (A)

Cancelada (C)

Em Contingência (T)

Cancelamento Pendente (K)

Denegada (W)

Onde:

**Pendente**Sempre que ocorrer o processo “Enviar NF-e” for executado com sucesso a NF-e ficará aguardando validação da SEFAZ ou seja Pendente.

**Inconsistente**Sempre que ocorrer um erro no processo “Enviar NF-e” a NF-e assumirá este status e isto significa que nota(neste caso o movimento) precisa de algum “ajuste” para ser enviada com sucesso.

**Rejeitada**Ao executar o Processo “Consultar Autorização/Cancelamento” se a SEFAZ não autorizar uma NF-e ela assumirá este STATUS, deverá ser verificado a orientação da mensagem de erro para saber o que fazer.

**Autorizada**Sempre que a SEFAZ autorizar uma NF-e, ao executar o Processo “Consultar Autorização/Cancelamento” ela assumirá este STATUS e significa que a NF-e já esta autorizada no site da SEFAZ.

**Cancelada**Sempre que a SEFAZ autorizar o cancelamento de uma NF-e, ao executar o Processo “Consultar Autorização/Cancelamento” ela assumirá este STATUS e significa que a nota já esta cancelada no site da SEFAZ.

**Em Contingência**Ela assumirá este STATUS sempre que for utilizada a modalidade de emissão contingência off-line, e significa que está autorizada a emissão do DANFE em papel especial, mas a NF-e ainda não foi enviada para validação da SEFAZ. Normalmente esta modalidade é utilizada quando existe algum problema envolvendo a SEFAZ ou o cliente que impede a transmissão da NF-e.

**Cancelamento Pendente**Sempre que for solicitado o cancelamento de uma NF-e ela assumirá este status enquanto aguarda a resposta da SEFAZ.

**Denegada**Ao executar o Processo “Consultar Autorização/Cancelamento” se a SEFAZ não autorizar uma NF-e informando que o cliente desta nota está com irregularidades fiscais ela assumirá este STATUS sendo este Status final da nota.

**Passo 9: Emitir o Relatório DANFE**

Após a autorização da NF-e deverá ser impresso o relatório DANFE (Documento de Auxiliar da Nota Fiscal Eletrônica) que está previsto na legislação e deve obrigatoriamente acompanhar o transporte da mercadoria.

O DANFE só poderá ser impresso para NF-e autorizadas e não deve ser confundido com a NF-e, pois este é apenas um documento auxiliar que contém informações resumidas da NF-e que é o XML.

Para imprimir o relatório DANFE acesse o menu: Utilitários SPED NF-e (Estadual) Marque a NF-e que será impressa Processos Imprimir DANFE ou imprimir DANFE.NET (RM Reports) Selecione o relatório DANFE disponibilizado pelo suporte e realize a impressão normalmente.

**Passo 10: Enviar XML por email**

Siga os passos do link abaixo para enviar o XML por email para o cliente da NF-e:

**Informações adicionais**

**NF-e de Ajuste - Cancelamento indevido:**

**NF-e de Ajuste - Estorno:**

**Emissão de NF-e em DPEC:**

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)**

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
