---
article_id: 6366955589015
category: SIGAEST - CUSTOS
content_hash: cadec76b6d936407544727012aa40241c3fb43d40113e25123dda3f8ac94d1ef
fetched_at: '2026-06-28T22:39:02.091755+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Alterando
  ordenação de movimentos internos - PE MA330TRB - Modelo
type: support-article
updated_at: '2025-03-12T12:23:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6366955589015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Alterando-ordena%C3%A7%C3%A3o-de-movimentos-internos-PE-MA330TRB-Modelo
---

**Dúvida**É possível alterar a ordenação dos movimentos internos ao efetuar o recalculo do custo médio?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Sim, isso é possível ser efetuado, através do PE MA330TRB.

**Sobre a sequência da Ordenação 300:**

- O Recalculo do Custo Médio (MATA330), quando processado por apropriação Mensal ou Diária, utiliza uma chave:

**(TRB\_DTBASE+TRB\_SEQPRO+TRB\_ORDEM+TRB\_NIVEL+TRB\_NIVSD3+TRB\_CHAVE+TRB\_SEQ)** para ordenação dos movimentos no arquivo de trabalho (TRB). Esta chave utilizada para ordenação atende o processo produtivo da grande maioria das empresas, **porém** em alguns processos, devido a sequência em que os movimentos são gerados, as Transferências (RE4 / DE4) e Desmontagens (DE7 / RE7) **por exemplo**, podem não ser ordenados conforme o esperado.

Para estas situações existe o parâmetro **[MV\_SEQ300](https://tdn.totvs.com/pages/releaseview.action?pageId=6087434)**, que tem como objetivo ordenar os movimentos de **Ordem 300** (Movimentos Internos) por sequência de inclusão (**D3\_NUMSEQ**) ignorando a chave padrão. Com a ativação do parâmetro a grande maioria das exceções são tratadas e solucionadas.No entanto existem processos muito específicos que mesmo a ativação do parâmetro não realiza a ordenação esperada dos movimentos.

Para estes casos será necessário utilizar o ponto de entrada **MA330TRB** para manipular o arquivo de trabalho (TRB) e definir uma regra especifica de ordenação com base nos movimentos do cliente. Quando há a necessidade de utilização do ponto de entrada, o processo do cliente deve ser estudado para identificar um padrão para as movimentações e consequentemente uma regra para ordenação delas.

**Exemplo com mais detalhes, disponibilizado pelo time de Produto(Desenvolvimento)**

[EXEMPLO DE USO DO PE MA330TRB](https://tdn.totvs.com/x/2uNc)

**É importante informar, que esse é apenas um exemplo**, **você pode se adequar melhor ainda junto ao seu desenvolvedor**, configurando o melhor cenário possível para seu tipo de negocio.

O desenvolvimento do P.E é responsabilidade do cliente.

Caso não possua de um desenvolvedor, hoje a TOTVS disponibiliza do time **HUB PLATAFORMAS.**

Para assuntos sobre customizações TOTVS, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de pontos de entrada e rotinas automáticas documentadas  no portal TDN para uso no produto padrão.

Estas documentações possuem exemplos de utilização previamente testados, caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas (hub.plataformas@totvs.com.br).

Esta equipe oferece os serviços de criação e manutenção de fontes customizados, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

Após informar sua necessidade ao time em questão, estes irão verificar tal viabilidade e propor um orçamento para que seja aplicado.

**Saiba Mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como é feita a ordenação dos movimentos no Recálculo do Custo Médio?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005800542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-no-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-?source=search)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
