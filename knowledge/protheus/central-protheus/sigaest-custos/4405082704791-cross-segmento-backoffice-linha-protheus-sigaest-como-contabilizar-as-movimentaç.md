---
article_id: 4405082704791
category: SIGAEST - CUSTOS
content_hash: e85dfd1295058343b8be71c43e9884f12e44b0f207e244cc2e1643aba1aca1d3
fetched_at: '2026-06-28T22:39:00.687911+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar
  as Movimentações no Estoque Custos?
type: support-article
updated_at: '2026-06-17T20:06:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos
---

O artigo explica como configurar o ambiente do TOTVS BackOffice (Protheus) para contabilizar movimentações de estoque e custos, detalhando os métodos ONLINE e OFFLINE definidos pelo parâmetro MV\_CUSMED, as rotinas necessárias (MATA330/MATA331), a importância dos lançamentos padronizados (LPs) e cuidados com datas e regras específicas para contabilização.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25679741315607) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como configurar o ambiente para contabilizar as movimentações do estoque custos?

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Primeiro passo, é entender que **existem 2 tipos de contabilização: ONLINE e OFFLINE**, e esse metodo é definido pela regra de negocios de cada empresa, ou seja, apenas 1 dos metodos podem ser utilizados por regra.

Esse metodo, é definido através do parametro **MV\_CUSMED**, para mais detalhes sobre o conceito do metodo desejado, valide o seguinte boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual é o conceito de contabilização ONLINE e OFFLINE através do parametro MV\_CUSMED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007482371-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-%C3%A9-o-conceito-de-contabiliza%C3%A7%C3%A3o-ONLINE-e-OFFLINE-atrav%C3%A9s-do-parametro-MV-CUSMED)

**Se o parametro MV\_CUSMED estiver como M (mensal), precisará executar as rotinas Recálculo do Custo Médio (MATA330) e depois á Contabilização Off-line (MATA331) ou ja contabilizar no na MATA330 com o pergunte "Gera lanc contabil = sim"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25679741324439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25679741330583)

**Na rotina Acompanha Custos, é a mesma coisa:**

Dentro de "Configurar parametros":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41304314058135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41304357623575)

**Nota**: É de suma importância e obrigatório realizar o cálculo médio(MATA330) para que o sistema preencha os campos **D1\_SEQCALC, D2\_SEQCALC e D3\_SEQCALC**.

Caso esses campos não estejam preenchidos e avance para a etapa de contabilização(MATA331), o sistema não realizará a contabilização!

**Se o parâmetro MV\_CUSMED estiver com conteúdo "O", irá contabilizar automaticamente assim que feito a movimentação sem a necessidade de executar as rotinas MATA330/MATA331:**

Ao acessar por exemplo a rotina de "**movimentação do internas (MATA241)**", consegue validar e mostrar em tela a contabilização que está sendo feita, basta clicar no botão **F12** dentro da rotina, que irá aparecer as seguintes opções:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25679741335319)

Toda contabilização, precisa de um LP (Lançamento padrão), com a definição da sua regra interna particular, para determinar que aquele movimento sera contabilizado somente se as condições da sua regra forem atendidas, abaixo segue uma listagem dos LP's utilizados no Estoque Custos:

[Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-MP-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)

No Suporte Padrão sempre iremos orientar que coloque a **regra padrão para testes**, com um sintaxe simples, essa sintaxe é feita no LP na carga inicial dos Lps por padrão, exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25679709401879)

**Nota:** A data de contabilização dos movimentos internos, também recebe o campo **D3\_DTLANC** com a data do processamento "Data limite final" do recalculo.

**Mas qual é a data que grava no para contabilização?**

A **Data de lançamento** é a data colocada no recalculo em **Data limite final** (Primeiro parametro do recalculo). Após ajuste todas tabelas terão a **data de lançamento da data limite final.**

**Portanto é IMPORTANTE** certificar, de preencher a **DATA LIMITE FINAL** correta para o periodo de contabilização!

**Sobre a aglutinação dos lançamentos contabeis no historico**

Para a contabilização com histórico aglutinado do cálculo do custo médio, em relação a gravação e historico, é necessário que o sistema esteja configurado da seguinte forma:  
**\*** ***Cadastro do Lançamento Padronizado***  
Obrigatório o preenchimento do campo *Hist Aglut (CT5\_HAGLUT)*  
**\*** ***Parâmetros (SX6)***  
MV\_AGLHIST <https://tdn.totvs.com/x/cScEN> = T  
MV\_AGLPROC <https://tdn.totvs.com/x/aikEN> = MATA330

**Observação:**

Os movimentos internos contabilizados por **consumo** são todos aqueles que todo material que é solicitado a título de consumo, por exemplo papel A4 para impressão, caneta, papel higiênico, óleo de lubrificação de maquinas e etc.

Sendo os movimentos RE0 onde NÃO tem movimento com OP associado, além dos movimentos RE6/DE6.

Os movimentos internos contabilizados por **produção** são todos aqueles que **possuem** os campos D1\_OP, D2\_OP e D3\_OP preenchidos, além dos movimentos de Transferência entre Armazéns e filiais,

Os movimentos de transferencia entre armazéns e filiais será **contabilizados na etapa de produção** da LP 670 e 672 pois não se enquadram como **movimentos de consumo,** pois não estão saindo do estoque para serem consumidos, as transferências requisitam o produto de um local e movimentam para outro local, ou ainda pode ser transferido de um produto para outro produto, e sua contabilização ocorre na etapa de produção.

**Para mais informações acesse:**

[MATA330/MATA331 - Contabilização dos Lançamentos por Consumo](https://tdn.totvs.com/pages/releaseview.action?pageId=708091293)

**Importante**

O Suporte Técnico não valida/configura **lançamentos padrões**, por envolver informações sobre o negócio/processos que deseja contabilizar. Informamos que as configurações de **LPs** são de responsabilidade do **cliente/analistas de implantação**, já que o mesmo é liberado para **configurações e customizações específicas**. Caso não tenha conhecimento na utilização do **cadastro de LP**, solicite ao seu executivo de soluções de negocio (ESN) a visita de um analista in loco para avaliar seu ambiente.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de aplicação na thread de Contabilização*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001884321-MP-SIGAEST-MATA330-Erro-de-aplica%C3%A7%C3%A3o-na-thread-de-Contabiliza%C3%A7%C3%A3o)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
