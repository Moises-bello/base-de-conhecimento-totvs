---
article_id: 1500010519121
category: SIGAEST - PODER DE TERCEIROS
content_hash: 47884337210e595eba22ebf22f422df81767492761abd9e7514bfdfbdc57118b
fetched_at: '2026-06-28T22:39:03.163584+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como eliminar saldo
  em Poder de terceiro (retorno simbólico)
type: support-article
updated_at: '2026-06-03T16:41:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010519121-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-eliminar-saldo-em-Poder-de-terceiro-retorno-simb%C3%B3lico
---

A baixa de saldo em Poder de Terceiro no Protheus é feita exclusivamente via Notas Fiscais de Entrada ou Saída, não havendo movimentações internas para isso. Para corrigir saldos, pode-se estornar e reemitir documentos com TES correto ou emitir Nota de Retorno Simbólico, que ajusta o saldo sem atualizar o estoque. A validação fiscal e contábil é recomendada antes da emissão.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910032536087) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**

Tenho um saldo de produto em Poder de Terceiro (SB6) e preciso dar baixa. Como realizar esse procedimento? Como eliminar saldo em Poder de terceiro?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
A movimentação de Poder DE/EM Terceiros no Protheus é realizada, **exclusivamente, através de Notas Fiscais (Documento de Entrada / Documento de Saída).** Saiba mais em: [**Como efetuar o Controle de Poder De/Em Terceiros?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros)

Não há rotinas ou movimentações internas no Protheus padrão que permitam a manipulação de saldos em Poder de Terceiro, pois isso poderia comprometer a integridade de um saldo que pertence à Terceiros.

Assim, duas ações são possíveis para correção do Saldo em Poder de Terceiros:

* **Estorno e Reemissão dos documentos**

Se identificar que foram emitidas notas com TES incorreto, não realizando a movimentação devida de Saldo - F4\_ESTOQUE - ou a movimentação devida em Poder de Terceiros - F4\_PODER3 - ([detalhes aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros)), o procedimento ideal é excluir o Documento de Entrada / Saída, e emitir novamente utilizando o TES correto. Consulte sua área Fiscal e Contábil para avaliar a viabilidade de exclusão das Notas.

* **Emissão de Nota de Retorno Simbólico**

Para situações pontuais onde o saldo precisa ser eliminado, uma alternativa é realizar o Documento de Entrada / Documento de Saída que caracterize um **Retorno Simbólico**, com o TES devidamente configurado para promover a baixa de Poder de Terceiros, para fins de ajuste nos saldos do ERP, mantendo o registro da Nota como referência da movimentação.

***Obs**: Questões sobre a necessidade ou não da transmissão desse Documento, bem como características fiscais devem ser validadas com o contábil e fiscal de sua Organização. A ação aqui recomendada se resume a movimentação sistêmica.*

**Exemplo de como realizar o Retorno Simbólico:**

**Produto:** MP2

**Saldo Físico em poder de terceiro:** 50

**Nota Fiscal da remessa ao terceiro:** 000055

**Fornecedor:** 01

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020021001)

Para fazermos uma baixa simbólica, basta que façamos um Documento de Entrada (MATA103), selecionando o produto MP2, fornecedor 01 e a Nota Fiscal 000055 para referenciar a devolução.

**Observação**: como este é um saldo **nosso** **que está em poder de terceiros**, o retorno é via Documento de Entrada. Se fosse um material **de terceiros em nosso poder**, o retorno seria pela rotina Pedido de Vendas (MATA410) e o TES seria exatamente igual ao abaixo, porém, com tipo de Saída.

**O TES a ser utilizado** deve estar parametrizado da seguinte forma:

**Atualiza Estoque (F4\_ESTOQUE)**: Não

**Tipo do TES (F4\_TIPO)**: Entrada

**Poder de Terceiros (F4\_PODER3)**: Devolução

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500016894982)

**Observações:**

* O TES está configurado para não atualizar o estoque, pois normalmente nestes casos este estoque nem existe mais, então não atualizando, este saldo não somará ao saldo físico existente no momento;
* O código do TES é meramente ilustrativo, a codificação fica à critério do usuário.

Efetuando a baixa simbólica do poder de terceiros na prática:![Baixa_simbolica_poder3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019751742)

**Observação importante**: A série da NF fica à critério da empresa validar com a sua contabilidade para finalização do Documento. Além disso, questões sobre a necessidade ou não da transmissão desse Documento, bem como características fiscais devem ser checados com o contábil e fiscal de sua Organização. A ação aqui recomendada se resume a movimentação sistêmica.

Com isso, vamos emitir novamente o relatório MATR480 - Relação de Materiais "de" e "em" terceiros:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020021321)

Vamos nos ater apenas às 2 primeiras linhas, que dizem respeito a remessa e devolução referente ao documento **000055**. Perceba que na coluna "Saldo" zerou, pois os 50 itens a partir de agora foram devidamente devolvidos (mesmo que simbolicamente - sem atualizar estoque).

**Saiba mais:**

[SIGAEST - Poder de/em terceiros: Como a tabela SB6 efetua o controle dos saldos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700511412375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Poder-de-em-terceiros-Como-a-tabela-SB6-efetua-o-controle-dos-saldos)

[SIGAEST - Como efetuar o Controle de Poder De/Em Terceiros?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005090232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-o-Controle-de-Poder-De-Em-Terceiros)

[*Mais artigos sobre Poder de Terceiros no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)
