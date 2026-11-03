---
article_id: 360041682674
category: RH – DIRF
content_hash: 5af8679eadfe66ad17f3c91f156a91c758d627869cd125ecb8ca19e9b1211972
fetched_at: '2026-06-28T22:44:07.060777+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Mensagem de atenção na Geração do Arquivo Magnético
  DIRF Grupo GPM590 e GPM590ESPO
type: support-article
updated_at: '2025-08-20T11:03:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041682674-RH-Linha-Protheus-GPE-Mensagem-de-aten%C3%A7%C3%A3o-na-Gera%C3%A7%C3%A3o-do-Arquivo-Magn%C3%A9tico-DIRF-Grupo-GPM590-e-GPM590ESPO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34312486466839)** Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Mensagem ao gerar o arquivo magnético DIRF:

Atenção  
Verifique a pergunta 22 do grupo 'GPM590' e o grupo de perguntas 'GPM590ESPO'. Execute o atualizado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056544633)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Grupo de perguntas da DIRF desatualizado.  
  
**Solução**1. Crie a linha 22 do Grupo de Perguntas GPM590 manualmente no Configurador conforme imagem abaixo, pelo caminho **>Base de Dados >Dicionário >Base de Dado**s, opção **Perguntas**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546613)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546653)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546673)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055682454)

2. Ainda na opção **Perguntas** da **Base de Dados**, crie o Grupo de Perguntas **GPM590ESPO** manualmente conforme imagem abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546773)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546813)![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056546873)

Após ajustes, salve as alterações.  
  
É possível criar as perguntas atualizando o dicionário com a execução do UPDDISTR, com o arquivo de dicionário da expedição contínua:  
[Expedição contínua - RH Gestão de Pessoal Protheus](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Como executar UPDDISTR - Atualização de Dicionário](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)

**Saiba Mais:**

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
