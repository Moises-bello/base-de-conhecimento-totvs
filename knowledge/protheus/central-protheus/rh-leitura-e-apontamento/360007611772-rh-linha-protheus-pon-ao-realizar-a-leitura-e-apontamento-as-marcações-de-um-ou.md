---
article_id: 360007611772
category: RH - Leitura e Apontamento
content_hash: b52ce672df63700707d83f3485ed22180b31cf0233884dc86393820954664eb0
fetched_at: '2026-06-28T22:44:45.889417+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Ao realizar a leitura e apontamento, as marcações
  de um ou mais funcionários aparecem em duplicidade
type: support-article
updated_at: '2025-11-05T14:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007611772-RH-Linha-Protheus-PON-Ao-realizar-a-leitura-e-apontamento-as-marca%C3%A7%C3%B5es-de-um-ou-mais-funcion%C3%A1rios-aparecem-em-duplicidade
---

**Dúvida:**Como evitar que, ao realizar a leitura e apontamento, as marcações de um ou mais funcionários apareçam em duplicidade?  
  
**Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução:** Para que este problema seja solucionado, realize os seguintes passos:  
  
**1.** **Parâmetro MV\_MCIGUAL,** se configurado com o conteúdo **N** e o funcionário bater o ponto duas vezes por engano ou por um erro de REP que gerou duplicidade, o sistema impedirá que essas marcações subam na tabela  SP8 duas ou mais vezes.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36122018465047)  
  
**2.** **Parâmetro MV\_DESPMIN,** este parâmetro controla o intervalo de tempo mínimo entre duas ou mais marcações. Caso exista mais de uma marcação com intervalo igual ou menor ao informado no parâmetro, ela será desconsiderada.  
Exemplo: O funcionário registrou a marcação às 08:00 e às 08:03, se este parâmetro estiver preenchido com 05, a marcação das 08:03 será ignorada, exemplo de preenchimento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36121998552727)  
**\*\*Se o parâmetro estiver com conteúdo 00 ou em branco, todas as marcações, inclusive as duplicadas vão subir para a SP8, com isso é necessário que seu conteúdo possua informações maior ou igual à 01**  
  
**3.** **Parâmetro** **MV\_MCIMPAR** se configurado o conteudo **S,** o sistema despreza marcação que menos coincida com a tabela de horário padrão, quando houver imparidade.  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36122018467735)  
\*\*Valida este parâmetro com base de que se a batida for a mesma do mesmo REP, NSR e PIS ou CPF se estiver duplicada no arquivo, o sistema fará a leitura e gravará somente uma das batidas.**  
  
**Saiba mais:**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=274333684)[Documentação sobre o parâmetro MV\_DESPMIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403030035223)  
[Pacote de Expedição Contínua RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
