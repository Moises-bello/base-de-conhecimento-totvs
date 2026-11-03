---
article_id: 360020932031
category: ADVPL - Classe e Função
content_hash: bead28a075276596de357c7eff82ac26759c28950b38eab5e8564288215b0132
fetched_at: '2026-06-28T22:40:15.718867+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criação utilização
  de variável de memoria no padrão MVC
type: support-article
updated_at: '2022-01-03T20:28:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020932031-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-utiliza%C3%A7%C3%A3o-de-vari%C3%A1vel-de-memoria-no-padr%C3%A3o-MVC
---

**Dúvida**

Qual a forma correta de enviar uma informação para o campo B1\_COD (na tela de inclusão) do MATA010 (Produto)?   
Temos uma rotina de código mnemônico que utiliza a instrução M->B1\_COD := <conteúdo> para enviar o código calculado para o campo no MATA010.

Esta rotina parou de funcionar a algumas versões e precisaremos reativar.   
Obrigado!  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Solução**

Com o novo conceito de desenvolvimento mudou para o padrão MVC, algumas coisas mudaram e uma delas é pegar o conteúdo de uma variável de memória de um campo no cabeçalho e utilizá-lo numa célula de um grid, como modelos 2 e 3 por exemplo.

Exemplificando:

Estou na tabela de preço (OMSA010), rotina que foi convertida para MVC, e quero alimentar um campo no grid com o conteúdo do campo do cabeçalho.

Irei utilizar como exemplo o campo DA0\_DATDE (Data Inicial) para alimentar o campo DA1\_DATVIG (Vigencia).

Posso trabalhar de duas formas

Utilizando uma função padrão Tovts – **FWFldGet** <http://tdn.totvs.com/display/framework/FWFldGet>  
Criando minha própria função ou usando função padrão

1º Passo:

Abra o seu configurador ou apsdu e vá no SX3 do campo DA1\_DATVIG

2º Passo:

Edite o campo DA1\_DATVIG e no configurador vá em “inicializador padrão” ao invés de utilizar

M->DA0\_DATDE escreva agora FWFldGet(“DA0\_DATDE”), ou seja, quando você inicializar uma nova linha o protheus irá pegar o valor digitado no campo da Data inicial e irá replicar no campo Vigência da linha do item

Onde:

cMaster é nome do objeto

cCampo é o nome do campo que deseja capturar

2º Passo:

Edite o campo DA1\_DATVIG e no configurador vá em inicializador padrão e escreva U\_SUAFUNCAO(‘DA0MASTER’, ‘DA0\_DATDE’) , ou seja, quando você inicializar uma nova linha o Protheus irá pegar o valor digitado no campo da Data inicial e irá replicar no campo Vigência da linha do item.

Usando uma função criada, você pode fazer outras validações que não cabem na linha do inicializador padrão.
