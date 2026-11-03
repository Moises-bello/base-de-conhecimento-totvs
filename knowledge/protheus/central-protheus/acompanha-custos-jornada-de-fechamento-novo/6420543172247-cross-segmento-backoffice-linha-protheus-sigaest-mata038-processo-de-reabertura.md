---
article_id: 6420543172247
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 69d7b41dd58ebe13d173139cb054a739c00f6e5bac34cb5f029727e5bb7a1062
fetched_at: '2026-06-28T22:38:48.230506+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo
  de Reabertura de Estoque
type: support-article
updated_at: '2025-03-12T12:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20620495715223) Tempo aproximado para leitura: **00:03:10 min** **Dúvida**Como funciona o processo de Reabertura de Estoque na Nova Jornada de Fechamento (MATA038)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.33.

**Solução**

A funcionalidade de Reabertura de estoque é acessada pelo histórico de fechamento e apresenta uma listagem com os últimos fechamentos concluídos em cada filial e tem o propósito de conduzir o usuário em um processo de reabertura de período de estoque fechado, permitindo correções de movimentações realizadas com inconsistência, que possa ter gerado informações divergentes de estoque.

|  |
| --- |
| **Caso a empresa esteja com a Release 12.1.27, não é possível concluir a configuração e abrir a nova rotina. Neste caso, recomendamos seguir as orientações da documentação abaixo:**  **[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os possíveis impactos da Reabertura de Estoque?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002994501)** |
| **Informação Adicional**  A **Reabertura de Estoque** **para clientes que utilizam o "Novo WMS"** ativado (MV\_WMSNEW = .T.) passa a estar disponível no fonte "distribution.WMS.FechamentoEst.tlpp" com data de 18/01/2024 ou posterior *(liberação [a partir de Março/24 via Expedição Continua do módulo WMS](https://tdn.totvs.com/x/vVUxIQ))*. Esta é uma [melhoria desenvolvida pelo módulo WMS](https://tdn.totvs.com/x/AhhkLw) a partir de [sugestão inserida na Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/community/posts/13666237414295-TOTVS-Log%C3%ADstica-Linha-Protheus-WMS-Reabertura-de-estoque-quando-utilizado-WMS?page=1#community_comment_14309221695127). |

**Demonstração**

**![](https://tdn.totvs.com/download/attachments/604835358/reabertura.gif?version=1&modificationDate=1645189832873&api=v2)**

**Tipos de Reabertura**

Ao clicar no botão "Reabrir" é aberta a janela para selecionar quais filiais serão reabertas, com isso temos dois tipos de reabertura:

**Reabertura Total**  
Caso sejam selecionadas todas as filiais, a reabertura será total, ocorrendo para todas as filiais que foram compreendidas quando efetuado o fechamento.

**Reabertura Parcial**  
Caso não sejam selecionadas todas as filiais, a reabertura só ocorrerá para a(s) filial(ais) que foram selecionadas, assim será gerado um novo registro na tabela de Fechamento Realizados (D3Y) contendo as filiais reabertas.

**Iniciando o Processo**

Ao clicar no botão Reabrir uma modal para seleção de quais filiais terão seu estoque reaberto será exibida com as filiais que são compreendidas no fechamento em questão.

![](https://tdn.totvs.com/download/attachments/604835358/reabertura_selecao_filiais.gif?version=1&modificationDate=1643286380727&api=v2)

**Reabrir**

O botão "Reabrir" é habilitado nos itens por meio de permissão de acesso. É possível efetuar a reabertura de estoque quando o mesmo esteja concluído, sendo apresentado na listagem e o botão habilitado.

**OBS**:  **Permissão 195 no SIGACFG(Configurador), versões igual ou superior a Release 12.1.33,  versão anterior fica liberado para uso por qualquer usuário.**

![](https://tdn.totvs.com/download/attachments/604835358/reabertura.gif?version=1&modificationDate=1645189832873&api=v2)

**Acompanhar Reabertura**

Após as filiais serem selecionadas e validadas o usuário será direcionado para uma tela onde poderá acompanhar as etapas do fechamento.

![](https://tdn.totvs.com/download/attachments/604835358/reabertura_concluido.gif?version=1&modificationDate=1643286736947&api=v2)

**E se minha filial for nova e o periodo reaberto?**

Caso você tenha uma filial que nunca teve fechamento, e efetuar o fechamento, e logo após a reabertura do periodo, por padrão a filial não tinha fechamentos anteriores, então logo assume-se o parametro MV\_ULMES com data historica sitemica de 19970101, por premissa e sugestão, orientamos que o parametro MV\_ULMES seja usado de forma exclusiva para cada uma de suas filiais.

**A reabertura de estoque, apaga os lançamentos contabeis?**

Não, a rotina de reabertura não tem relação com os lançamentos, somente com saldos (SB9,SBK,SBJ por exemplo, e esses dados são APAGADOS da base, não são setados como D\_E\_L\_E\_T\_ ='\*' a unica validação do processo é nas tabelas de log D3X,D3Y e D3W).

A unica forma de apagar os lançamentos, é durante o processo de contabilização, com o pergunte (Gera lançamentos contabeis = NAO) ou então através da contabilidade.

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)*
