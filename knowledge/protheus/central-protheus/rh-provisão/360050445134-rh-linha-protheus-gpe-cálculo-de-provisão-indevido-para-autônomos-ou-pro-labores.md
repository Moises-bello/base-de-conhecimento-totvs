---
article_id: 360050445134
category: RH - Provisão
content_hash: 0c0371cc744121d997a55c914f7add414603cad8c3b635316d2ef7e51996c920
fetched_at: '2026-06-28T22:43:56.875999+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Provisão Indevido para Autônomos ou
  Pro-Labores
type: support-article
updated_at: '2022-08-05T21:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050445134-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-Indevido-para-Aut%C3%B4nomos-ou-Pro-Labores
---

**Dúvida**O sistema está gerando Cálculo de Provisão Indevido para Autônomos e/ou Pro-Labores, como corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Por padrão, o Protheus processa cálculo de provisão para todos os funcionários, inclusive Autônomos  Pro-Labore, da mesma forma que a Rotina Controle de Dias de Direito realiza a contagem dos Períodos Aquisitivos independente da Categoria do funcionário.  
Isto ocorre porque alguns clientes tem a necessidade de realizar este controle de provisão para Autônomos ou Pró-Labores.  
  
Para que não sejam processados os cálculos de Provisão com as Categorias A (Autônomos) ou P (Pró-Labores), realize os seguintes passos:  
  
1. Exclua o Cálculo das Provisões indevidos para os Autônomos ou Pro-Labores;  
Para saber como excluir o cálculo das provisões, [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036636774-MP-GPE-Como-Excluir-o-C%C3%A1lculo-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio)  
2. Nos Próximos cálculos de Provisão, na pergunta "**Categorias a Calc**?" retire a opção de cálculo para funcionários com a Categoria A ou P, conforme o exemplo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077280274/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077280314/mceclip1.png)

Desta forma, o sistema não processará provisão para funcionários cadastrados com estas categorias
