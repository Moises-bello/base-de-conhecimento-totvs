---
content_hash: 0a24f6e064626699382e7230398a150cd3d075d4e640fc7463bb1169104ccb4b
fetched_at: '2026-06-29T00:09:27.495067+00:00'
page_id: '423938525'
product: rm
source: tdn-rm
title: Recálculo de Diferença entre Débitos e Créditos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938525
version: 2
---

*Atenção!*

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

As diferenças de valores entre débitos e créditos são consistidas por lançamento, usuário e filial, respeitando sempre a opção definida nos parâmetros do sistema. Se  a opção nos parâmetros "Permite diferenças entre filiais" estiver *desmarcada* o controle de diferenças entre débitos e créditos será feito por filial dentro do lançamento. Caso contrário, se a opção nos parâmetros estiver *marcada*, o sistema verificará apenas a diferença entre os valores de débitos e créditos por lançamento, independente das filiais utilizadas. Se o parâmetro "Permite mais de uma diferença" estiver *desmarcado* será permitido somente uma diferença por usuário.

Este processo tem o objetivo de realizar a recálculo na base de dados a fim de identificar as possíveis diferenças entre os valores de débitos e créditos em lançamentos contábeis.

**Configurações e Filtros**

Nesta tela serão definidos todos os filtros a serem considerados pelo sistema:

* Devem-se selecionar quais lotes serão verificados. Deixando em branco, todos os lotes existentes (zero e N) serão analisados.
* O intervalo de datas (inicial e final) que corresponde ao período contábil no qual estão compreendidos os lançamentos desejados para análise.
* A coligada e a filial. Deixando em branco todas as coligadas/filiais serão verificadas.

**Observação**  
Se o parâmetro do sistema "Permite diferença entre filais" estiver *marcado*, a opção de filtro por coligada/filial não ficará disponível na tela do processo e o sistema realizará a verificação das diferenças por filial.

**Atenção**  
Durante a execução do processo o(s) lançamento(s) referente(s) ao(s) lote(s) definido(s) nos filtros será(ão) bloqueado(s) de forma a garantir que nenhuma alteração seja realizada durante a conferência dos valores.

*Log*  
Ao final da execução do processo será exibido um Log com todas as diferenças encontradas.

Para visualizar os lançamentos com diferença deve-se clicar no botão "Abrir Visão das Diferenças".   
A partir desta tela pode-se editar o(s) lançamento(s) e alterar os mesmos a fim de acertar a diferença.

**Observação**  
Para realizar a alteração nestes lançamentos deve-se conferir se o usuário possui permissão para tal ação.
