---
article_id: 36628277293591
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: bfa76e07d9594f0f568695425d1b045bf66a1c6fc9d5b404f8d5ddd1b6f6a1d3
fetched_at: '2026-06-28T22:37:24.228248+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos – TOTVS Backoffice Protheus  - SIGAGCT - Ao tentar alterar
  ou incluir rateio numa medição cadastrada ocorre error.log - erro no parâmetroFWFormGridModel:
  Este modelo não permite a alteração...'
type: support-article
updated_at: '2026-01-14T13:30:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36628277293591-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGAGCT-Ao-tentar-alterar-ou-incluir-rateio-numa-medi%C3%A7%C3%A3o-cadastrada-ocorre-error-log-erro-no-par%C3%A2metroFWFormGridModel-Este-modelo-n%C3%A3o-permite-a-altera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36628293361943) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao tentar alterar ou inserir rateio numa medição cadastrada ocorre error.log - erro no parâmetroFWFormGridModel: Este modelo não permite a alteração de uma linha on FWFORMGRIDMODEL:SETVALUE(FWFORMGRIDMODEL.PRX)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos

**Solução**

Para solucionar a dúvida, siga os passos abaixo:

1. Realize a atualização em ambiente de Homologação com os pacotes de correção adequados:
   * [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)
   * [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)

     Obs: Após cada atualização, aplique os arquivos de dicionário e rode o comando `upddistr`.
   * Pacote [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)
2. Execute os testes desativando as customizações do ambiente utilizando os três métodos especificados na documentação.

   [Cross Segmentos - Linha Protheus - Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)
3. Caso nos testes ainda ainda assim apresentem o mesmo comportamento, orienta-se a abertura de ticket no suporte para a analise enviando:
   * Envie um vídeo demonstrando todo o processo, desde o cadastro de um novo contrato, incluindo as condições e particularidades relevantes.
   * Informe o comportamento inconsistente encontrado, demonstrando cadastrais como:
     + Tipos de Contrato (CNTA021)
     + Tipos de Planilha (CNTA230)
     + Tipos de Revisão (CNTA010) caso a inconsistência ocorra no momento da revisão.
   * No vídeo, mostre ao realizar o cadastro do contrato os dados do Cabeçalho do Contrato, Planilhas, Itens das Planilhas, Cronograma financeiro, físico e contábil, se aplicável.
4. Encaminhe um arquivo `.csv` atualizado com as datas das fontes.

***Saiba Mais :***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
