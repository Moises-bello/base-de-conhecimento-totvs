---
article_id: 19562562030743
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: e311a5285746368a8d654ff153b4bf1fd84d5748e76bff9775d505f0fbc18227
fetched_at: '2026-06-28T22:39:08.095274+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como aumentar o tamanho
  do campo do Armazém (NNR_CODIGO)?
type: support-article
updated_at: '2025-03-12T12:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19562562030743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-aumentar-o-tamanho-do-campo-do-Armaz%C3%A9m-NNR-CODIGO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19562546282135) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como aumentar o tamanho do campo do armazem? É possivel aumentar o tamanho do campo **Armazem (NNR\_LOCPAD)**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Devido à restrição de modificações no campo em questão, foi estabelecido um conjunto de opções para o tamanho do campo. Contudo, é importante observar que o limite máximo permitido é 6 (seis), conforme ilustrado na imagem adiante, exemplificando o padrão estabelecido.

Ressalta-se que, para esta situação específica, é imperativo adotar o tamanho limite determinado, em virtude de algumas fontes que fazem referências aos campos em questão.

**IMPORTANTE**: É crucial salientar que, antes de efetuar qualquer alteração, é recomendável validar se há alguma rotina ou relatório que possa ser impactado por este ajuste no tamanho do campo. Cabe ressaltar que o **tamanho padrão é nativamente definido como 2**, sendo a decisão de ampliar o grupo de campos uma prerrogativa que deve ser submetida à análise de caso e à responsabilidade da parte encarregada do processo.

Após efetuados os ajustes como indicado abaixo, é necessário que ***efetue a reinstalação de todas as STORED PROCEDURES do ambiente***. Efetue o processo como indicado nessa **FAQ (*[link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-e-Incompat%C3%ADvel-quais-as-diferen%C3%A7as-%C3%89-poss%C3%ADvel-utilizar-as-rotinas)*)**.

Ressalta-se, ainda, que não há um mapeamento ou documento técnico abrangente que detalhe todos os possíveis impactos decorrentes da alteração do tamanho dos campos no Protheus quando já em utilização, por isso, deve-se efetuar uma avaliação minuciosa interna, visando não ocorrer impactos indesejados.

**Pode ser feito via modulo SIGACFG:**

Configurador > Base de dados > Dicionario de dados > Grupo de camps > Codigo de Armazem > Editar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19562540521111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19562555478679)

Após, salve as alterações, reinicie o sistema e avalie o campo de armazém agora com o tamanho desejado.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
