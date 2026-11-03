---
article_id: 20156679527575
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 680f3a4146ab187c386eae0382608788b77bc5e2a28eae44648e74bbaed7b48b
fetched_at: '2026-06-28T22:38:55.660961+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - Botão Retorno
  Beneficiamento não é exibido
type: support-article
updated_at: '2025-03-12T12:22:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20156679527575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-Bot%C3%A3o-Retorno-Beneficiamento-n%C3%A3o-%C3%A9-exibido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20156675416215) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**

Após [configurar o ambiente para retorno de Beneficiamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050279993-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Retorno-de-beneficiamento-com-v%C3%ADnculo-e-baixa-autom%C3%A1tica-da-OP-no-documento-de-entrada), na rotina Documento de Entrada **não apresenta** o Botão **"Retorno Ben."**, o que devemos analisar para exibição do Botão?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20156907201047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20156907209751)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para esse cenário primeiramente avaliar se o **parâmetro MV\_PRNFBEN** esta habilitado igual a T e compartilhado para todas as Filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20157272865047)

Avaliar se o **parâmetro MV\_TMPAD** esta configurado com o **Tipo de Movimentação** cadastrada na rotina MATA230 na Filial que esta tentando efetuar o Retorno de Beneficiamento, Caso o mesmo não esteja cadastrado na Filial o Botão não é apresentado. É necessário que tenha o registro em cada filial cadastrada. Veja um exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20157272876823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20157241642775)

No exemplo acima, observe que o parâmetro não contempla as TMS cadastradas para produção, dessa forma ou deve-se criar a TM ou ajustar para uma TM existente.

Após esses ajustes funcionará como esperado.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
