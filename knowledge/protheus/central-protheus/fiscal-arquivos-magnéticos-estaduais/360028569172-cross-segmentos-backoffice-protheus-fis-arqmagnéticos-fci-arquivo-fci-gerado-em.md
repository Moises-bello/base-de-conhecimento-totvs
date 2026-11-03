---
article_id: 360028569172
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 6e82305dc5a405af4ff879e0f8b650ddeb037b66bfce8c8139459028b46b8dd2
fetched_at: '2026-06-28T22:42:08.870014+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FCI - Arquivo
  FCI gerado em branco'
type: support-article
updated_at: '2022-08-17T20:26:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028569172--Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FCI-Arquivo-FCI-gerado-em-branco
---

**Ocorrência**O arquivo do FCI está sendo gerado em branco.  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**O arquivo do FCI está sendo gerado em branco.  
   
 **Solução**Analisar as seguintes informações da tabela CFD:

- **CFD\_FCICOD** = Vazio: produtos que já foram apurados e já possuem códigos de períodos anteriores não devem ser levados para o arquivo a menos que a origem da mercadoria seja alterada.

- **CFD\_ORIGEM** diferente de 0: Origem 0 se trata de produto com origem nacional e portanto não deve ser levado para o arquivo. Só serão levados para o arquivo, produtos com origens 3, 5 ou 8.

- **CFD\_PERVEN** no mesmo mês de geração do arquivo .txt: Somente serão levados para o arquivo, os produtos apurados no mesmo mês que a geração do arquivo.

Pontos de atenção:

- Verifique se na tabela, os campos CFD\_VSAIIE ou CFD\_VPARIM estão zerados, pois estes campos são responsáveis por calcular qual o percentual importado do seu produto (CFD\_CONIMP), que por sua vez é o campo que irá definir qual a origem do seu produto (0 - Nacional, 3 - de 41% a 70% importado, 5 - até 40% importado, 8 - superior a 70% importado).

- Verifique os parâmetros envolvidos na rotina:

**MV\_FCICALC** - Método de cálculo do sistema para encontrar os valores da FCI. Não utilize a opção 2, pois está opção foi descontinuada. O conteúdo do parâmetro deve ser 1 ou 3.

**MV\_FCIVE** - Informe os CFOPs interestaduais que foram utilizados nas vendas dos seus produtos que devem possuir o código da FCI

**MV\_FCICL** - Informe as Classificações Fiscais (CST - Campo D2\_CLASFIS do sistema) que foram utilizados nas vendas dos seus produtos que devem possuir código da FCI.

**MV\_FCIALIQ** - Informe as alíquotas de ICMS que foram utilizados nas vendas dos seus produtos que devem possuir código da FCI.

- **(Caso MV\_FCICALC = 3)** Verifique se suas matérias primas importadas estão com as informações corretas na tabela SD1 (Documento de entrada), com o campo D1\_CLASFIS devidamente preenchido, iniciando por 1, 2, 3 ou 8 e se a tabela SA8 foi preenchida com as informações corretas dos seus produtos com o campo A8\_VLRVI preenchido sempre que o produto possuir conteúdo importado.

- **(Caso MV\_FCICALC = 1)** Verifique se o campo D3\_PERIMP está preenchido.

- Verifique se o produto final que foi produzido está com os apontamentos das matérias primas devidamente amarrados na tabela SD3.

- Verifique se as requisições das matérias primas importadas estão com o campo D3\_CF com um conteúdo que esteja também no parâmetro MV\_FCIMI.

**Lembrando que a operação de Revenda não gera arquivo texto, pois o código da FCI já será informado na entrada do documento e o código deverá ser o mesmo para a saída deste produto.**
