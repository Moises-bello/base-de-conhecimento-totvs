---
article_id: 360058814633
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3335a34575cd0762c24d728054e7fff0840cd2789ea0bfc5e5af157a8b38f67e
fetched_at: '2026-06-28T22:42:40.889556+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - B1_BASE2 - FWNOWIDTH - Valor atribuído
  difere do tamanho do campo Subfamília
type: support-article
updated_at: '2021-06-23T11:49:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058814633-Manufatura-Linha-Protheus-SIGAPCP-B1-BASE2-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Subfam%C3%ADlia
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Ao incluir um produto utilizando o **Configurador de produtos**, o usuário recebe a mensagem **B1\_BASE2 - FWNOWIDTH - Valor atribuído difere do tamanho do campo Subfamilia**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**No campo **B1\_BASE2 - SubSubFamilia** o Sistema grava numa cadeia de caracteres das opções selecionadas, e se a característica em questão fizer parte de um conjunto, também o seu conjunto. Portanto é necessário que o campo **B1\_BASE2** seja ajustado para o maior valor que pode ser eventualmente gravado considerando todas as famílias de produtos cadastradas no **MATA093 - Configuração**.  
  
**Solução**1. Acesse a rotina **MATA093** e some o tamanho de todas as características de cada família. Essa informação está preenchida no campo **BQ\_TAMANHO - Tamanho**;  
2. Acesse a rotina **MATA098 - Codificação** veja quais características são selecionadas a partir de um conjunto, some ao tamanho da família correspondente o tamanho do código do conjunto indicado. Essa informação está preenchida no campo **BQ\_CONJUNT - Conjunto**;  
3. Altere através do **SIGACFG - Configurador**, ajuste o tamanho do campo **B1\_BASE2** para o maior valor encontrado.
