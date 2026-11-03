---
article_id: 33257465987735
category: eConsignado (Crédito do Trabalhador)
content_hash: eef233ce32e8afdd6cef7106e9b83e65cc330c8a648e962154e4c45225672d2e
fetched_at: '2026-06-28T22:43:07.263124+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - eConsignado - Erro de chave duplicada na SRK ao
  importar arquivo eConsignado
type: support-article
updated_at: '2026-05-20T12:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33257465987735-RH-Linha-Protheus-GPE-eConsignado-Erro-de-chave-duplicada-na-SRK-ao-importar-arquivo-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33257480135063) Tempo aproximado para leitura: **00:02:00min**

**Dúvida**  
Porquê o sistema apresenta erro de chave duplicada na SRK ao tentar importar o arquivo eConsignado ?  
**THREAD ERROR ([197476], carlos.nunes, DAM-153) 04/07/2025 11:30:57 SRK020: DB error (Insert): -37 File: SRK020 - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Cannot insert duplicate key row in object 'dbo.SRK020' with unique index 'SRK020\_UNQ'. The duplicate key value is (01, 001052, 527, 209101 , , , 006150, 0).**  
  
**Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Solução**  
Esse erro ocorre devido a utilização do grupo de perguntas errado no momento da importação.   
O sistema passou por adequações para que seja possível realizar a importação de mais de um contrato de eConsignado  
  
Para solucionar essa dúvida, realize os seguintes passos:

Aplique o ultimo pacote disponível do RH expedição continua e execute o UPDDITR.   
Versão **12.1.2310**: <https://suporte.totvs.com/portal/p/10098/download?e=1123885> >> **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**  
Versão **12.1.2410**: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>  
Versão **12.1.2510**: <https://suporte.totvs.com/portal/p/10098/download?e=1221795>

Com isso vai ser criado o novo grupo de Perguntas GPM944A pra rotina de Importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33257465972887)

Caso seja necessário, inclua o grupo de perguntas de forma manual.   
O campo consulta Padrão deve ser pesquisado como XM0

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33257465974039)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Econsignado - Como incluir a rotina de Importação do arquivo Econsignado GPEM944](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32201275142295-RH-Linha-Protheus-GPE-Econsignado-Como-incluir-a-rotina-de-Importa%C3%A7%C3%A3o-do-arquivo-Econsignado-GPEM944)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
