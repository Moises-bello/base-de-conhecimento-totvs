---
article_id: 40336032390167
category: Folha Mensal
content_hash: edf91eb35c23e47f1b6ca0df1f9ab8a8b1352ebf62a257e700e46d6a730840ce
fetched_at: '2026-06-28T22:46:57.914625+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Arredonda INSS teto quando funcionário possui
  outro vínculo de terceiros'
type: support-article
updated_at: '2026-05-08T18:52:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40336032390167-RH-RM-FOP-Folha-Mensal-Arredonda-INSS-teto-quando-funcion%C3%A1rio-possui-outro-v%C3%ADnculo-de-terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40336032359703) Tempo aproximado para leitura: **00:01:22 min**  
  
**Dúvida**  
Ao calcular folha da competência 03/2025 para um funcionário que tenha outro vínculo externo e a soma das bases dos dois vínculos é atingido o teto do limite de contribuição de INSS, o RM está arredondando a 4 faixa do cálculo do INSS, causando diferença de valores com o governo, visto que o eSocial trunca todas as faixas de cálculo. Como resolver?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2506.285
* 12.1.2510.206
* 12.1.2602.126
* 12.1.2606 e superiores

**Solução**  
Foi realizada a alteração conforme orientação da conclusão da Consultoria, dessa forma, o cálculo será feito sobre cada faixa e o truncamento ocorrerá após a segunda casa decimal.  
Verifique as informações no link: [Orientação Consultoria de Segmentos - 7495069- Novo Cálculo de INSS com a Reforma da Previdência](https://tdn.totvs.com/pages/releaseview.action?pageId=525805955)

Também foi realizada a criação do parâmetro "**Arredonda INSS teto quando funcionário possui outro vínculo de terceiros**" localizado em **Configurações | Parametrizador | Folha Normal | Encargos Sociais** para o caso de entendimento que o arredondamento deve continuar sendo realizado.

**Saiba Mais:**

[Encargos Sociais](https://tdn.totvs.com.br/display/public/LRM/Encargos+Sociais)

#
