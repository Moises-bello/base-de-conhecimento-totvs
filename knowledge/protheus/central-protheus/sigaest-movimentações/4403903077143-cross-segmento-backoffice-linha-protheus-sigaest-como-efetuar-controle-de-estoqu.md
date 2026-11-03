---
article_id: 4403903077143
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4d3b8939d053413da9f84bc3bf86e0990b7b94a083bc9a325b396354949be97c
fetched_at: '2026-06-28T22:38:54.395246+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar controle
  de Estoque?
type: support-article
updated_at: '2025-03-12T11:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403903077143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-controle-de-Estoque
---

**Dúvida**Como efetuar controle de Estoque no Protheus?

**Ambiente**:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O controle de Estoque em si é algo que não há uma regra geral, onde cada empresa controla de acordo com sua regra de negócio, porém o Protheus dispõe de rotinas que são utilizadas constantemente por muitas empresas para controle de estoque. Vamos listar as principais rotinas (de muitas) que o Estoque possui, com as observações prévias:

- Durante a explicação de cada rotina, algumas palavras-chaves terão hiperlinks para acesso ao detalhamento do tema;

- Estas são apenas algumas das rotinas de controle de estoque, portanto, caso seja um usuário novo, é recomendável que solicite junto ao seu Executivo de Soluções de Negócio TOTVS um treinamento do módulo para maior detalhamento das rotinas.

1° Cadastro de Produtos (Módulo 04 - Estoque/Custos -> Atualizações -> Cadastros -> Produtos): Essa rotina permite cadastrar novos produtos, delegando o código do produto, descrição, armazém (local de estoque) padrão que o produto normalmente ficará, dentre outros campos de controles do produto (**[endereçamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014866531-MP-SIGAEST-Controle-de-Endere%C3%A7amento-Rotina-MATA265-Import%C3%A2ncia-do-par%C3%A2metro-MV-LOCALIZ)**, **[lotes](https://tdn.totvs.com/pages/releaseview.action?pageId=367232994)**, **[centro de qualidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011947711-MP-SIGAEST-Controle-de-Qualidade-Materiais-Baixas-do-CQ-MATA175)**, etc)

2° - Movimentações Internas (Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> **[Movimentação Interna Simples](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026780773)**/**[Movimentação Interna Múltipla](https://mail.google.com/mail/u/0/#inbox/FMfcgzGkZGjsHWJrdTXGsBsWGcSLWGSK)**): Por meio desta rotina é possível efetuar requisições do estoque (retiradas do estoque) e devoluções ao estoque (retornar saldo ao armazém de estoque), sempre que necessário e para qualquer finalidade que a empresa julgar necessário.

3° - **[Processo de Inventário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque?source=search)** (Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Inventário | Miscelânea -> Processamentos -> Inventário): Por meio da rotina de Inventário é possível a empresa efetuar contagens dos produtos em seus armazéns de Estoque para manter o controle rigoroso dos saldos físico e financeiro dos produtos que contém no estoque. Normalmente o usuário faz uma contagem física e depois digita no sistema. Então por meio do inventário é possível comparar diferenças entre o que contou e o que o sistema apontou de saldos, podendo acertar o saldo da diferença para o Estoque do Sistema ficar homogêneo com o Estoque Físico real.

4° - **[Transferência de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011935502)** (Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Transferência Simples/Transferência Múltipla): Essa rotina tem por finalidade poder transferir saldo de produtos, seja entre armazéns diferentes, ou até mesmo passar o saldo de um produto para outro. Por exemplo: uma empresa que trabalha com recipientes de um líquido pode ter um cadastro da litragem e do recipiente, então transfere o saldo da litragem para o recipiente caso cada um tenha seu código de produto diferente.

5° - **[Solicitações ao Armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511)** (Módulo 04 - Estoque/Custos -> Atualizações -> Movimentações -> Internas -> Armazém -> Solicitar/Gerar Pré Requisição/ Baixar Pré-Requisição): Essa rotina é muito parecida com a de Movimentos Internos, pois tem como finalidade requisitar um saldo do estoque para utilização ou qualquer outra finalidade. A diferença nele é que algumas empresas tem um controle mais rigoroso para remoção de produtos do estoque, portanto solicitam por meio da rotina de Solicitação ao Armazém, e normalmente o time responsável pelo Estoque trata de liberar ou não o saldo do produto que o usuário requisitou. **[Esta rotina pode gerar Solicitação de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004328202)** quando não há saldo para atender a solicitação e mesmo assim o time de Estoque irá liberar o saldo.

6° - **[Refaz Custo de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)** (Módulo 04 - Estoque/Custos -> Miscelânea -> Processamentos -> Refaz Custo de Entrada): Esta rotina tem por única finalidade revisitar todos os **[Documentos de Entradas](https://tdn.totvs.com/display/public/PROT/DOCUMENTO+DE+ENTRADA+GERAL)**e checar se as configurações de Custos em cima do valor da nota + impostos estão condizentes com o configurado no **[Tipo de Entrada e Saída (TES)](https://www.youtube.com/watch?v=jQfWP5WqvaE)**e em caso de, o TES configurado ter passado por alguma alteração de impostos por exemplo, essa rotina remonta o Custo da Nota de Entrada conforme essas mudanças (desde que o Documento de Entrada tenha sido feito em um **período de estoque em aberto**)

7° - **[Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671)** (Módulo 04 - Estoque/Custos -> Miscelânea -> Cálculos -> Custo Médio): Essa rotina é uma das mais importantes do módulo de Estoque, pois ela tem por finalidade analisar todos os movimentos de Compras/Entradas Fiscais, Movimentos Internos Gerais e Vendas/Saídas Fiscais), **[reordenando os movimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005800542)** conforme  a legislação consolidada no RIR/1999, art. 295. No Custo Médio **[existe toda uma parametrização prévia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291)** antes da execução para que os Custos finais dos produtos naquele período de estoque fique da maneira mais interessante para a empresa. Após a execução, existe o relatório **[Kardex por Período para análise dos custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)** do produto após o recálculo.

8° - **[Virada de Saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-MP-SIGAEST-Roteiro-para-fechamento-dos-estoques?source=search)** (Módulo 04 - Estoque/Custos -> Miscelânea -> Fechar Períodos -> Virada de Saldos): Esta rotina permite a empresa virar os saldos de estoque de um período para outro. Muitas empresas costumam fazer virada de saldos no último dia do mês corrente, para, os saldos finais do mês anterior, tornarem os saldos iniciais do próximo mês, desta forma a empresa "passa a régua" no controle de estoque daquele período e ele fica gravado para histórico e também para garantir performance do sistema (já que outros processamentos não fazem checagem em movimentos de período fechado).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre **Movimentações no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[Clique aqui e veja mais artigos sobre **Custos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Clique aqui e veja mais artigos sobre **Cadastros e Configurações Gerais no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[Clique aqui e veja mais artigos sobre **Processamentos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*

*[Clique aqui e veja mais artigos sobre **Relatórios no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*

*[Clique aqui e veja mais artigos sobre **Saldos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*

*[Clique aqui e veja mais artigos sobre **Virada de Saldos no Estoque**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538921-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)*
