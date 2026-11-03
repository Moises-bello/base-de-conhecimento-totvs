---
content_hash: 8eeef52d126adfd4a6db8e3ccddcccfeb515d591cb9b6edec1c96ab8e899446b
fetched_at: '2026-06-29T00:10:01.359325+00:00'
page_id: '452718699'
product: rm
source: tdn-rm
title: Benefícios - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718699
version: 4
---

**Benefícios**

Controle de benefício por pontuação

Campo para definição dos parâmetros que darão suporte ao controle de pontuação utilizado para calcular "créditos" disponíveis para aquisição de benefícios.

Marcando este parâmetro, só será possível realizar o lançamento de benefício ara um funcionário no RM Vitae ou realizar a requisição de solicitação de um benefício no Portal, caso este tenha a pontuação necessária disponível para adquirir o mesmo, tornando-se necessário especificar para cada beneficio a sua pontuação para aquisição.

Por Cargo: Esse parâmetro habilita / desabilita o campo Pontos disponíveis através do cargo (Pontos cadastrados na tela de cadastro de cargo).

Por Função: Esse parâmetro habilita / desabilita o campo Pontos disponíveis através da função (Pontos cadastrados na tela de cadastro de função).

Por Seção: Esse parâmetro habilita / desabilita o campo Pontos disponíveis através da seção (Pontos cadastrados na tela de cadastro de seção).

Por Funcionário: Esse parâmetro habilita / desabilita o campo Pontos disponíveis através do funcionário (Pontos cadastrados na tela de cadastro de funcionários).

**Atenção:**

Para controlar benefícios por pontuação por Funcionário é necessário que o sistema esteja configurado para trabalhar integrado ao sistema RM Labore, nas opções de parâmetros da Integração.

Atualizar valor e periodicidade ao calcular benefícios na Folha de Pagamento

Marcando este parâmetro, no Assistente de Lançamento de Benefícios, ao lançar um benefício para um funcionário, os campos "valor" e "periodicidade" estarão bloqueados para alterações, considerando o valor de cadastro.

Marcando este parâmetro, se o valor do benefício for alterado em seu cadastro, ao processar o Cálculo de Benefícios de Funcionários (sistema Folha de Pagamento), o valor do benefício será alterado na Consulta Movimento da Integração (sistema Folha de Pagamento).

Atualizar Benefício Selecionado

Marcando esse parâmetro,  o sistema irá incluir ou substituir  somente o benefício selecionado, sem impactar os que já haviam sido calculados e armazenados na tabela PFMOVTEMP.
