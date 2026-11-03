---
article_id: 29247585410839
category: SIGAEST - PROCESSAMENTOS
content_hash: 8a3a2598a637364314c52c8c2908f32f56c7b599648d3bb2067b4ac7a2f268d4
fetched_at: '2026-06-28T22:39:04.999011+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - type mismatch on compare
  on ESTMETRICS(ESTXFUN.PRW)
type: support-article
updated_at: '2025-08-12T13:00:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29247585410839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-type-mismatch-on-compare-on-ESTMETRICS-ESTXFUN-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29247616843031) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Durante o processamento, ou uso de alguma rotina, ocorre o seguinte erro ao chamar a função EstMetriCs: **type mismatch on compare on ESTMETRICS(ESTXFUN.PRW) 27/05/2024 13:58:10 line : 135**, o porque o erro é ocasionado e como corrigir esse erro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O erro "**type mismatch on compare**" ocorre porque o sistema está comparando uma variável do tipo **lógico (L)** com valores do tipo **caractere (C),** ou vice versa com outros tipos que não são representados um para outro.

Do exemplo acima do erro apresentado, podemos informar que na linha **135** do fonte **ESTXFUN** na data informada, A variável **cCusFil** é atribuída como resultado da função **SuperGetMV**, que retorna valores dependentes do parâmetro **MV\_CUSFIL**.

**Trecho como exemplo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29247616847383)

Porém se for consultado no arquivo error.log a variavel cCusFil, consta que o tipo dela é **L (Lógico)** e o retorno esperava **C (caracter).** Essa variavel representa o parametro **MV\_CUSFIL**, que no padrão seu conteudo é caracter e não lógico.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29247585394583)

Veja aqui como o parametro é cadastrado no padrão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34121327283095)

**Mais detalhes sobre o parametro:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do parâmetro MV\_CUSFIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL)

**O meu parametro esta como tipo logico, como eu faço para ajustar?**

Esse procedimento, deve ser realizado por uma pessoa com conhecimento de dados e acesso ao configurador, normalmente o administrador do sistema de sua empresa.

**PASSO 1 - Acesse o modulo SIGACFG(Configurador), abrindo seu executavel Smartclient ou via Web, de acordo suas configurações de ambiente, aqui segue um exemplo via webbrowser:**

**![entrandonosigacfg.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29248224264343)**

**PASSO 2 - Acesse: Ambiente > Cadastros > Parâmetros, expanda sessão da empresa, clique em Parâmetros, depois clique na primeira Lupa no menu acima, depois clique no campo abaixo da informação: Procurar por:, e digite o nome do parâmetro MV\_CUSFIL em seguida clique abaixo em buscar.**

![filtrandoparametro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29248898115735)

**PASSO 3 - Selecione o parametro na primeira linha da busca efetuada, depois clique no menu no bloco de notas que possui um lapis, o parametro vai ser aberto para edição, veja que o tipo esta como Lógico(exemplo com erro), voce deve mudar para Caracter(Que é o correto), aproveite e valide se o conteudo é conforme seu escopo de negocio, conforme boletim do parametro [MV\_CUSFIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL) , feito isso, clique na opção de saida.**

![alterandopadrametro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29248898124183)

Caso você faça uso das procedures de estoque, sendo essas da procedure de numero **14 a 22**, é sugestivel que seja feita a reinstalação das procedures, para nova leitura do parametro que foi alterado.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Isso serve para qualquer tipo de erro relacionado a chamada de "type mismatch on compare"?**

Na maioria dos casos sim, na duvida quando não houver uma verificação pontual de qual a validação esta sendo realizada, basta enviar ao suporte o error.log gerado em nosso portal de atendimento via ticket, informando qual o processo sendo realizado que ocorre o erro, de forma que possamos avaliar e retornar com o parecer sobre.

**Saiba mais:**  
*[Clique aqui e veja mais artigos sobre Estoque Custos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - type mismatch on compare on MA330FOK(MATA330.PRX)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427879770391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-type-mismatch-on-compare-on-MA330FOK-MATA330-PRX)*
