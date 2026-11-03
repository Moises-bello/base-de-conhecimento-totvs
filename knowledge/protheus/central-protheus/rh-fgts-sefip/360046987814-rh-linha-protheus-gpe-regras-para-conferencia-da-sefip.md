---
article_id: 360046987814
category: RH - FGTS / SEFIP
content_hash: 94d1e7aee227f93041d803652377d6965bcbd7ab8b7216b0ce85efd72cf9bd88
fetched_at: '2026-06-28T22:43:41.483628+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Regras para conferencia da SEFIP
type: support-article
updated_at: '2021-08-09T10:42:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046987814-RH-Linha-Protheus-GPE-Regras-para-conferencia-da-SEFIP
---

**Dúvida**Como conferir a geração da SEFIP ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – à partir da versão 12.1.17  
  
**Solução**

Após executar a rotina SEFIP será apresentado um LOG com as informações detalhadas utilizadas na geração do arquivo SEFIP.re.

**LOG DE OCORRÊNCIAS - SEFIP**

1. Grupo de perguntas da geração.
2. Parametrizações das tabelas S037 e S38 - Encargos Empresa.
3. Parâmetros MV\_SOMAVIS
4. Id de calculo da verba de Base INSS ou FGTS, que o arquivo busca dentro do calculo do funcionário.
5. Código e data de movimentações, Afastamento, Transferências e etc.

![](https://tdn.totvs.com/download/attachments/273315331/image2017-4-24%2010%3A26%3A56.png?version=1&modificationDate=1493041492000&api=v2)

![](https://tdn.totvs.com/download/attachments/273315331/image2017-4-24%2010%3A29%3A5.png?version=1&modificationDate=1493041492000&api=v2)

Após fechar essa janela, será apresentada a opção de gerar um comparativo SEFIP.re X Cálculo da folha.

O nome do arquivo seguirá esse exemplo:  sefipxfolha\_012017

![](https://tdn.totvs.com/download/attachments/273315331/image2017-4-24%2010%3A29%3A57.png?version=1&modificationDate=1493041492000&api=v2)

Obs: Caso não haja divergências, não será apresentado dados no relatório:

![](https://tdn.totvs.com/download/attachments/273315331/image2017-4-24%2010%3A37%3A52.png?version=1&modificationDate=1493041492000&api=v2)
