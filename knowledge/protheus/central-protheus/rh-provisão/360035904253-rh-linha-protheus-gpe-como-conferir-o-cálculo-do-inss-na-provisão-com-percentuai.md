---
article_id: 360035904253
category: RH - Provisão
content_hash: cf5c540e3d213a7ac8712254b358d7a36a64f17c4e309309d9e2d816737099c1
fetched_at: '2026-06-28T22:43:55.753184+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir o cálculo do INSS na Provisão, com
  Percentuais de INCRA, SESI, SENAI, SENAC, SEBRAE, SENAR, SECONC, SEST, SENAT ou
  SESCOOP
type: support-article
updated_at: '2025-06-13T21:16:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035904253-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-do-INSS-na-Provis%C3%A3o-com-Percentuais-de-INCRA-SESI-SENAI-SENAC-SEBRAE-SENAR-SECONC-SEST-SENAT-ou-SESCOOP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32806233071895) Tempo aproximado para leitura: **00:01:00 min****

**Dúvida**Como conferir o cálculo de Provisão, com Percentuais de INCRA, SESI, SENAI, SENAC, SEBRAE, SENAR, SECONC, SEST, SENAT ou SESCOOP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para compor a Alíquota de INSS do Cálculo da provisão, o sistema utilizará os mesmos percentuais que foram calculados na Folha de pagamento.  
Quando os campos de % INCRA, SESI, SENAI, SENAC, SEBRAE, SENAR, SECONC, SEST, SENAT, SESCOOP ou Adicional SENAI, estão preenchidos, os mesmos também serão considerados no cálculo das provisões, além dos Percentuais de Empresa e Acidente de Trabalho.

Para compor o percentual de INSS da provisão, realize os seguintes passos:  
  
1. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas / Visualize as S037 e S038 e verifique os campos preenchidos referentes aos percentuais de empresa, Acidente de Trabalho e Terceiros. No exemplo abaixo, preenchemos os campos %SENAI, %SESI e %Adic.SENAI, além do %Empresa, %Terceiros e %Acid.Trab:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046968213)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046108414)

2. Some todos os percentuais destacados acima.   
  
Empresa **20,00** + Acidente de Trabalho **2,92** + Terceiros **5,80** (os percentuais de SENAI E SESI estão compreendidos neste percentual, portanto os mesmos não deverão ser somados separadamente) + Resultado do cálculo do Adicional Senai **0,20 = 28,92%.**  
3. Acesse: Consultas / Cálculos / Por Funcionário e confirme que estes valores foram calculados corretamente na Folha de Pagamento.  
  
4. Acesse: Miscelânea / Provisões / Provisões de Férias/13º Salário, e emita o relatório de Provisões. Confirme que o cálculo do INSS das provisões está correto. Veja no exemplo abaixo, que o percentual utilizado foi 28,92%:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046969073)

**Saiba Mais**

Para mais informações sobre o Cálculo de Adicional SENAI acesse: <https://tdn.totvs.com/pages/releaseview.action?pageId=322143033>
