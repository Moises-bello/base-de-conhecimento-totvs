---
article_id: 32780539754391
category: eConsignado (Crédito do Trabalhador)
content_hash: 6f5a0c6a5b88e49537a7778e35280a7bcba35aefb0b15790c03598e7241fa6c8
fetched_at: '2026-06-28T22:43:07.176213+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Ao importar o arquivo Crédito do Trabalhador gera
  mensagem  " O funcionário não foi encontrado nas filiais informadas"
type: support-article
updated_at: '2025-10-08T18:48:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32780539754391-RH-Linha-Protheus-GPE-Ao-importar-o-arquivo-Cr%C3%A9dito-do-Trabalhador-gera-mensagem-O-funcion%C3%A1rio-n%C3%A3o-foi-encontrado-nas-filiais-informadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32780555842967) Tempo aproximado para leitura:  **00:02:00 min**

**Ocorrência**

Ao importar o arquivo Crédito do Trabalhador gera mensagem "O funcionário não foi encontrado nas filiais informadas"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32780555843223)  
  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**

Esse incidente pode acontecer por alguns motivos.

1. O **índice na tabela SRA** está incorreto, pois o Sistema valida a ordem **24 ( RA\_CODUNIC + RA\_FILIAL )** no índice na tabela SRA.
2. O **grupo de perguntas** da rotina de Importação está incorreto.
3. O **CPF ou Matrícula do eSocial** estão incorretos no arquivo de Importação gerado pelo Portal Emprega Brasil.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se o índice **RA\_CODUNIC + RA\_FILIAL** da tabela SRA está na **ordem 24**.  
 - No padrão a ordem é conforme print abaixo, **validando a posição 24**, e não a letra **Q** (Caso exista customização no índice, ela deve ficar no **final** da ordem padrão).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153217185303)

2. Verifique se o **grupo de perguntas GPM944A** está **igual** ao exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33153206775191)

3. Compare o **cadastro do funcionário** quanto ao numero de **CPF e Matrícula do eSocial** se está **igual** ao do **arquivo**. Caso o arquivo esteja errado, gere novamente o arquivo no Portal Emprega Brasil para importá-lo.

**Saiba mais:**

[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
