---
article_id: 360036174793
category: Inspeção de Entradas (SIGAQIE)
content_hash: ada186b3fba9b9596da7ac27d1d5427f1e35452be787a06a80011a10d8a3d4c0
fetched_at: '2026-06-28T22:42:27.153481+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - QIEA230 - Não há dados para a geração
  Ind. Qual. neste mês/ano
type: support-article
updated_at: '2021-08-09T12:53:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036174793-Manufatura-Linha-Protheus-SIGAQIE-QIEA230-N%C3%A3o-h%C3%A1-dados-para-a-gera%C3%A7%C3%A3o-Ind-Qual-neste-m%C3%AAs-ano
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:15****min**  
**Ocorrência**Na rotina **QIEA230 - Índice de Qualidade** exibe a mensagem **Não há dados para a geração Ind. Qual. neste mês/ano**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**A mensagem é exibida na geração dos índices da qualidade pela rotina **QIEA230** porque para gerar o índice de qualidade nesta rotina é necessário que os índices que compõe este cálculo já estejam cadastrados no Sistema.  
  
**Solução**A maioria dos índices podem serem calculados automaticamente pelo Sistema por meio da fórmula padrão. No entanto, o **ICT - Índice de Capacitação Tecnológica** e o **IPR - Índice de Variação de Preços** são calculados apenas a partir da utilização do *Rdmake* **QIEA231**.  
Na rotina **QIEA240 - Índice de IQF** são definidos se os índices que compõem o **IQF - Índice de Qualidade do Fornecedor** são do tipo **Informado**ou **Calculado**.  Se for do tipo **Informado**, os valores mensais para cada Produto/Fornecedor deverão ser cadastrados na rotina **QIEA280 - Índices Mensais** antes de gerar o **IQF** mensal.  
Se for do tipo **Calculado**, a sua fórmula deverá ser redefinida através da customização do *RdMake* **QIEA231**. É neste fonte que as fórmulas deverão ser revisadas.
