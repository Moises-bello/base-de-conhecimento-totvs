---
article_id: 360052238433
category: RH - FGTS / SEFIP
content_hash: d5145d18b67c1186e9b9a85a9d640a2fd9c6334f51de8fbf1092680b2775f501
fetched_at: '2026-06-28T22:43:41.399880+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao validar sefip: 990672 - Tipo de Registro
  Invalido'
type: support-article
updated_at: '2021-07-17T03:17:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052238433-RH-Linha-Protheus-GPE-Erro-ao-validar-sefip-990672-Tipo-de-Registro-Invalido
---

**Ocorrência**O sistema esta apresentando a mensagem: Tipo de registro invalido, ao validar o arquivo da **SEFIP** no programa da caixa.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**Esse erro pode ocorrer pois os cadastros na Tabela **S037** não estão corretos.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1**.Entre na Tabela S037 pelo caminho >Atualizações >Definições de Calculo >Manutenção de Tabelas >Tabela S037 - Encargos da Empresa;  
**2**. Deve existir os dois tipos de contrato cadastrados Determinado e Indeterminado:

![image2016-5-2 10:24:29.png](https://tdn.totvs.com/download/attachments/235598829/image2016-5-2%2010%3A24%3A29.png?version=1&modificationDate=1462192082000&api=v2)

**3**.Após o cadastramento correto é só gerar o arquivo da SEFIP novamente.

**OBS:** CADASTROS DEMONSTRADOS ACIMA SÃO APENAS EXEMPLOS, OU SEJA CADA EMPRESA DEVE PREENCHER DE ACORDO COM A SUA NECESSIDADE.

**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FGTS>
