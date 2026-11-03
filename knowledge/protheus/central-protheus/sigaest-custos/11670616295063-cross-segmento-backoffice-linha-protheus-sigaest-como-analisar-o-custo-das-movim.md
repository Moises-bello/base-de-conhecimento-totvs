---
article_id: 11670616295063
category: SIGAEST - CUSTOS
content_hash: b121f4767a88725c4014422389ad13774752c169f3a7adf37ac8dac142aff2a3
fetched_at: '2026-06-28T22:39:00.628775+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como analisar o custo
  das movimentações no estoque?
type: support-article
updated_at: '2025-07-31T20:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11670616295063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-analisar-o-custo-das-movimenta%C3%A7%C3%B5es-no-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33859969598871) Tempo aproximado para leitura: **6min 12s****Dúvida**Como se analisa o custo das movimentações no Estoque?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

É importante atualizar seu produto constantemente, mantendo-o sempre na última versão disponível no Portal de Clientes ([Central de Download](https://suporte.totvs.com/portal/p/10098/download#000006/all/)), a fim de contemplar todas as melhorias e correções disponibilizadas. E antes de tudo, ter processado o custo médio, para apuração das movimentações para a analise de custos.  
  
Efetuar o Backup antes da atualização.  
Todos os procedimentos devem ser realizados primeiro em ambiente TESTE atualizado.

Antes de partimos para a pratica de analise, devemos primeiro entender, o que é custo? e como funciona o custo, calculado pelas movimentações no estoque hoje?

**Seu custo pode ser: Mensal, Diário ou Sequencial**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Quais são os Métodos de Apropriação para execução do Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-?source=search)  
  
**Seu custo pode ser aglutinado por: Armazém, Empresa ou Filial**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do parâmetro MV\_CUSFIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL?source=search)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Armazém?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944424817047/)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio Offline por Filial?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11944742266647)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como funciona o Custo Médio por Empresa?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11945935810839)  
  
Sabendo disso, pode-se analisar o custo e movimentações de um produto, após **processamento do custo médio**, através do relatório **Kardex por periodo MATR900**.  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-?source=search)  
  
Para melhor entendimento, sobre os perguntes utilizados no custo médio, siga as instruções sobre cada parâmetro:  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio?source=search)

**Como são ordenadas as movimentações após o processamento de custo médio?­**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como é feita a ordenação dos movimentos no Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio)

A fim de entendermos o conceito da rotina de custo médio, pode-se definir que ela ira atualizar todas as suas movimentações dentro do período aberto, até a data limite final selecionada para execução, visando reordenar as suas movimentações de acordo seu [método de apropriação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-?source=search), bem como custeio de seus movimentos sob o [método aglutinado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL?source=search) configurado.

**(isso é definido no  momento da implantação).**  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Recálculo do Custo Médio (MATA330) - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013945671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-MATA330-Conceito-e-Informa%C3%A7%C3%B5es?source=search)  
  
Sobre como entender a memoria de calculo de suas movimentações, pode-se validar como é formado o custo, **de acordo o seu TES aplicado**, que vai incidir nos impostos configurados, a serem levados ou não ao custo.

O custo médio é calculado a partir de suas notas de entrada, também pode acabar sendo alterado ao decorrer do período, por conta de movimentos internos que adentram no seu estoque.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os significados dos códigos dos tipos de Movimentos Internos RE/DE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE-)

De forma genérica, abaixo segue como é calculado o custo total sob os **documentos de entrada, pedidos de venda e movimentos internos.**  
  
[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202-MP-SIGAEST-Como-%C3%A9-calculado-o-campo-D1-CUSTO-ao-efetuar-um-Documento-de-Entrada-?source=search)  
[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422-MP-SIGAEST-Como-%C3%A9-calculado-o-campo-D2-CUSTO1-ao-efetuar-Pedido-de-Venda-?source=search)  
[MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161-MP-SIGAEST-Como-%C3%A9-calculado-o-campo-D3-CUSTO1-ao-efetuar-Movimentos-Internos-?source=search)

**Entendi todo o conceito de custos, agora como é que eu analiso o custo das movimentações?**

1-Passo: Saber qual é o seu [método de apropriação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033673914-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Quais-s%C3%A3o-os-M%C3%A9todos-de-Apropria%C3%A7%C3%A3o-para-execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-?source=search).

2-Passo: Saber qual é o tipo de [custo aglutinado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011068802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CUSFIL?source=search) para seu estoque.

3-Passo: Já foi executado o recalculo de [custo médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio?source=search), para o período que deve ser avaliado? (caso não, é recomendável que execute).

4-Passo: Após validar a execução do custo médio, extraia o relatório [MATR900](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-?source=search) como pede o boletim para analise de custos e movimentações.

5-Passo: Efetue a geração do relatório MATR900, e configurado corretamente de acordo as configurações passadas, verifique se em sua opinião o custo está incorreto em alguma movimentação, ou ordenação, com todos os conceitos anteriores informados. Caso sua avaliação seja que o mesmo esteja incorreto, abra uma solicitação junto ao Suporte Técnico do Estoque/Custos, encaminhando o relatório MATR900 além dos [Perguntes do custo médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio?source=search), destacando onde está o erro e o porquê em sua avaliação para o suporte avaliar sua questão.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
