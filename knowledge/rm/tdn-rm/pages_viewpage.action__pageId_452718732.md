---
content_hash: 6a03fc782ac20d6ac40ed7a1e3d5f74cf7fa4154ae5c41dbc2e7c28dfe4b1985
fetched_at: '2026-06-29T00:10:01.435517+00:00'
page_id: '452718732'
product: rm
source: tdn-rm
title: Orçamento - Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718732
version: 21
---

# **Parâmetros Gerais de Orçamento**

Esta tela está localizada no parametrizador da folha de pagamento, podendo ser acessado pelo seguinte caminho 'Folha de pagamento | Configurações | Parâmetros | Parametrizador | Orçamento '.

Esta tela possui 8 parâmetros, descritos a seguir:

**- Bloquear edição de revisões quando uma nova revisão for criada**

Quando este parâmetro estiver habilitado ao tentar criar uma nova revisão de orçamento todas as revisões anteriores serão bloqueadas para edição. Exemplo:  A revisão de orçamento atual é a revisão 5, nesse caso as revisões de 1 a 4 podem estar ou não bloqueadas para edição, caso uma nova revisão for criada, as revisões de 1 a 5 serão bloqueadas para edição.

**- Bloquear cálculo de revisões quando uma nova revisão for criada**

Quando este parâmetro estiver habilitado ao tentar criar uma nova revisão de orçamento todas as revisões anteriores serão bloqueadas para cálculo. Exemplo:  A revisão de orçamento atual é a revisão 5, nesse caso as revisões de 1 a 4 podem estar ou não bloqueadas para cálculo, caso uma nova revisão for criada, as revisões de 1 a 5 serão bloqueadas para cálculo.

**- Exibir revisões com bloqueio de cálculo ou edição na tela de orçamento.**

Quando este parâmetro está habilitado, na tela de orçamentos, é possível visualizar os orçamentos  que estejam bloqueadas por cálculo ou edição. Se este parâmetro não estiver marcadas as revisões que estejam bloqueadas por edição ou cálculo não são exibidas,

**- Habilitar controle de filtro Seção x Função**

Quando este parâmetro estiver habilitado, os *lookups* de funções presentes no orçamento, só vão retornar as funções vinculadas as seções em que o usuário logado é chefe. Exemplo: Se o usuário logado é chefe da seção 01.01, os *lookups* só vão exibir as funções vinculadas a esta seção.

**- Não gera previsto x realizado (HEADCOUNT)**

Quando este parâmetro está habilitado, durante a execução do orçamento a função previso x realizado não sera gerada, usando a tabela de HEADCOUNT, ao habilitar essa parâmetro o cálculo de orçamento tem o seu desempenho melhorado.

**- Atualizar Limite de Funcionários no Quadro de Lotação**

Quando este parâmetro estiver marcado, ao criar/editar os STEPS de um orçamento, o campo “Limite de funcionário” no quadro de lotação é atualizado, este processo também atualiza o histórico de limites de funcionário. Os STEPS do orçamento que contemplam essa atualização são, "Admissão", "Demissão", Promoção, "Alteração de Seção" e "Transferência".  

**- Alteração do Quadro de Lotação**

Neste parâmetro deverão ser cadastrados os steps para atualização do Quadro de Lotação ("Admissão", "Demissão", "Promoção", "Alteração de Seção" ou "Transferência"). Deverá ser informado o **COD. STEP** e **COD. MOTIVO,**o motivo informado deverá ser o mesmo informado no orçamento, para que seja atualizado no quadro lotação Gestão de Pessoas.

Para maiores detalhes, [clique](https://tdn.totvs.com/pages/viewpage.action?pageId=550114425).
