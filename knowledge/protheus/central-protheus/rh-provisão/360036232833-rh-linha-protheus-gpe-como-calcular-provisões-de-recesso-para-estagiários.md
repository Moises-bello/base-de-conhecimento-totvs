---
article_id: 360036232833
category: RH - Provisão
content_hash: 271c5b46d7fb44deb7b33cbf23f9697f7e323a0e776f93ad7c265f733c6767b5
fetched_at: '2026-06-28T22:43:55.728534+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Provisões de Recesso para Estagiários
type: support-article
updated_at: '2025-06-17T20:26:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036232833-RH-Linha-Protheus-GPE-Como-calcular-Provis%C3%B5es-de-Recesso-para-Estagi%C3%A1rios
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17821445165591)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como calcular Provisões de Recesso para Estagiários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Foi disponibilizado o cálculo de provisão para Estagiários, agora é possível provisionar os valores referentes ao Recesso do Estágio.

Para que o cálculo seja realizado foram criados 5 identificadores de cálculo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047530633)

Para cadastrar as verbas de Provisão de Recesso, realize os seguintes passos:  
  
**1**. Acesse Atualizações / Definições de Cálculo / Verbas (GPEA040);  
  
**2**. Cadastre as novas verbas de Provisão de Recesso com os Identificadores acima.  
Observação: Todas as verbas devem ser cadastradas como Base **Provento** no campo "**Tipo do Cod.**" (RV\_TIPOCOD), e não há obrigatoriedade de preenchimento da Aba "Incidências", tendo em vista que estas verbas não são verbas de Cálculos;  
  
**3**. Acesse: Atualizações / Funcionários / Controle Dias de Direito (GPEA050), Selecione o Estagiário e clique em Visualizar.  
Verifique se o Período de Recesso do Estgiário está cadastrado com a verba de Identificador de Cálculo 0891:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17821161853719)  
  
**4**. Acesse Miscelânea / Provisões / Provisão de Férias /13º Salário (GPEA070) / Outras Ações / Cálculo e preencha os parâmetros para processamento da provisão;  
É importante validar se as categorias de Estagiário estão selecionadas na pergunta "Categorias a Calc.?"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16663742607383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16663780626327)

**5**. Após o processamento das Provisões, clique na opção Visualizar ou emita o relatório de Provisão de Férias, e confirme que o cálculo da Provisão de Recesso foi realizada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17821270011159)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17821278822167)

Observação: Não será processado o cálculo de Provisão de 13º Salário.

**Saiba mais**[RH - Linha Protheus - GPE - Como realizar cadastro de Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgoxKjSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBhWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNjU2MTE5Mi1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1yZWFsaXphci1jYWRhc3Ryby1kZS1Fc3RhZ2klQzMlQTFyaW8GOwhUOg5zZWFyY2hfaWRJIik5YTA5ZWYyYy1kZjkwLTRmZTUtYmMxOC1mZGMxZDYzMDMzM2QGOwhGOglyYW5raQ86C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdyZWNlc3NvIGVzdGFnaWFyaW8GOwhUOhJyZXN1bHRzX2NvdW50aQHD--5f53637d38d38bb123f81b098394301c135042f0)
