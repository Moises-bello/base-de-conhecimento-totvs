---
content_hash: 2e1fcc53e63eae890b58655f0c0d8a5b5c24caee382b5e20e81b988117e69275
fetched_at: '2026-06-29T00:10:00.918778+00:00'
page_id: '452718629'
product: rm
source: tdn-rm
title: Inserir no Fluxo
type: documentation
url: https://tdn.totvs.com/display/LRM/Inserir+no+Fluxo
version: 3
---

**Inserir no Fluxo**

O processo "Inserir no fluxo" poderá ser executado quando o sistema estiver ou não integrado com o Totvs Gestão do Relacionamento com o Cliente.

Somente requisições com status "Pendente", e sem parecer incluído, poderão utilizar este processo que tem como objetivo a inclusão da requisição no fluxo de aprovações segundo o mapeamento de etapas configuradas para cada tipo de requisição.

Após a inclusão, a requisição adquirirá o status "Em andamento" sendo encaminhada para a primeira pessoa definida pelo fluxo de aprovações. Para prosseguir com o repasse da requisição entre os participantes do fluxo o processo deverá ser feito, obrigatoriamente, no Totvs RM Portal através da opção "Avançar Etapa".

Não é obrigatória a utilização do fluxo de aprovações, com isso, o usuário terá a flexibilidade para controlar manualmente as requisições que desejar. Para isto, basta incluir os pareceres e definir os status que a requisição adquirirá, podendo ser "Em andamento", "Aprovado", "Reprovado".

Deve-se tomar o cuidado com o processo manual, pois uma vez que a requisição "Pendente" tenha algum parecer vinculado, esta não poderá ser incluída no fluxo de aprovações; vale ressaltar também que os pareceres incluídos não podem ser excluídos.

**Observação**

O controle manual das requisições só será permitido no Totvs Gestão de Pessoas, desta forma as requisições abertas pelo Totvs RM Portal serão administradas pelo Totvs RM Portal.

Caso o Sistema esteja parametrizado para utilizar Gestão de Hierarquia por "Posição" a requisição será encaminhada para o próximo aprovador de acordo com a Gestão por Posição.
