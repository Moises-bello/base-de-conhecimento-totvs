---
article_id: 17318863418135
category: SIGAEST - INVENTÁRIO
content_hash: e836945b73a5e63550ada71c4cb4cf8609b933d0efdc193e42cb31a7e01ec0c9
fetched_at: '2026-06-28T22:38:50.423329+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR285 - Não apresenta
  dados, como conferir?
type: support-article
updated_at: '2023-09-06T16:26:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17318863418135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR285-N%C3%A3o-apresenta-dados-como-conferir
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17318879884183) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Foi digitado o inventário, ao emitir o relatório de ***Conferência (MATR285)*** apresenta a mensagem ***"Não há dados a serem exibidos"***, como avaliar a Conferência? Qual o motivo de não exibir no relatório?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17320208513047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17320055719703)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para esse cenário revise como indicado abaixo:

***- 1º -*** Verifique se a parametrização do relatório esta condizente com a Digitação do Inventário. No exemplo abaixo, ***observe que o intervalo dos Armazéns estão fora da digitação***, recomendável conferir todos os parâmetros se estão indicando o Inventário desejado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17320723228311)

***- 2º -*** Caso mesmo ajustando os parâmetros do relatório e não exibir os dados, verifique **se o parâmetro MV\_CONTINV esta habilitado**, quando esse parâmetro esta habilitado, não deve utilizar o relatório MATR285 para conferências. **Obs.:** [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061630273-MP-SIGAEST-MATA340-MV-CONTINV-m%C3%BAltiplas-contagens-de-invent%C3%A1rio-por-sele%C3%A7%C3%A3o-de-contagem) e veja o conceito do parâmetro MV\_CONTINV.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17321008181783)

***Dica:*** Na rotina **DIGITAÇÃO DO INVENTÁRIO (MATA270)**, caso apresente **Legendas** como no exmplo abaixo, indica que o parâmetro esta habilitado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17321057324823)

***- 3º -*** Desabilitando o parâmetro MV\_CONTINV, revisando os parâmetros do relatório e pronto, o relatório é emitido corretamente para as conferências.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17321778564503)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre INVENTÁRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[SIGAEST - MATR285 - Valor zerado na coluna Diferença Valor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17270096259479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR285-Valor-zerado-na-coluna-Diferen%C3%A7a-Valor)

[SIGAEST - MATR285 e MATR900 - Como conferir após o processamento do inventário os itens que foram ajustados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11302587586711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR285-e-MATR900-Como-conferir-ap%C3%B3s-o-processamento-do-invent%C3%A1rio-os-itens-que-foram-ajustados)
