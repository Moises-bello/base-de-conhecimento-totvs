---
article_id: 34523342968855
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 1027ffc4c90513577b19cebdcdde26d95917a57e032f2d5e7a72260f44c61c33
fetched_at: '2026-06-28T22:37:56.537837+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Pagar
  - FINA420 - Não gera linha final do arquivo de remessa
type: support-article
updated_at: '2025-08-29T11:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34523342968855-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Pagar-FINA420-N%C3%A3o-gera-linha-final-do-arquivo-de-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34523340136215) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao gerar o arquivo TXT, a rotina não está fazendo a quebra de linha na última linha do trailler do arquivo, causando incosistencia no validador do banco que não consegui identificar o final do arquivo.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o campo EE\_FIMLIN não está ativado para uso dentro da rotina FINA130 - Parametros de Bancos  
  
**Solução**  
**Acesse o SIGACFG** e siga o caminho:  
**Base de Dados >> Dicionário de Dados >> Tabela SEE**.

Em seguida:

* Localize o campo **EE\_FIMLIN**;
* Habilite a opção **"Usado"**;
* Salve o dicionário;
* Defina o campo com o valor **1 - Sim**.

Após essa configuração, será gerada a linha final de arquivo.  
  
O objetivo desta rotina é atender tanto à necessidade que alguns bancos têm de que sejam incluídos os caracteres finalizadores de linha na gravação do registro Trailer no CNAB modelo 1/2 como para aqueles bancos que não exigem esses caracteres.  
Para atender às exigências de todos os bancos, deve-se habilitar ou criar o campo "Final linha" (EE\_FIMLIN) na tabela SEE (Comunicação remota), conforme descrição a seguir.

|  |  |
| --- | --- |
| **Tabela** | SEE |
| **Campo** | EE\_FIMLIN |
| **Título** | Final de linha |
| **Validação** | Pertence ( **12** ) |
| **Opções** | 1 = Sim (padrão do sistema)  Indica se devem-se incluir os caracteres de final de linha (Chr(13)+(Chr(10)) ao gravar o registro Trailler no Cnab modelo 1/2, visto que alguns bancos invalidam o tamanho do registro quando ele não contém os finalizadores de linha.  2 = Não |

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações e dúvidas para uso do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-e-d%C3%BAvidas-para-uso-do-CNAB)
