---
content_hash: 38b74b9146a213f5cc4ac3a1f4e65f19ffd82233187e7174696da80b4498074a
fetched_at: '2026-06-29T00:09:52.385848+00:00'
page_id: '439358010'
product: rm
source: tdn-rm
title: "Filtro por Usuários - Globais\uFEFF"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439358010
version: 14
---

## **CONTEÚDO**

## **01. VISÃO GERAL**

Neste documento será mostrado como utilizar o filtro por usuário.

## **02. EXEMPLO DE UTILIZAÇÃO**

    Nesta pasta serão definidos os filtros dos usuários. Após as definições, quando o usuário acessar uma tabela ela já estará filtrada de acordo com o filtro selecionado nesta opção. Caso esta tabela possua também a opção de Filtros, além do filtro selecionado a tabela estará filtrada também por essa opção.

Isso se aplica a todas as visões do sistema, ou seja, a visão do sistema que corresponder aos registros de uma tabela, e esta for filtrada

**EXEMPLO:**  
        No módulo “Gestão Financeira”, o usuário “Igor” possui um filtro associado para a tabela de Lançamentos (FLAN), onde ele só pode ver os lançamentos com data da baixa maior que 01/012011 (DATABAIXA > '01/01/2011').

        Ao entrar no cadastro de Lançamentos e selecionar um filtro com todos os registros, serão trazidos somente os lançamentos com data da baixa maior que 01/01/2011, ou seja, não serão apresentados os dados de nenhum registro com baixa anterior à 01/01/2011.

false

**Observação:**

Neste recurso de filtro por usuário, as condições dos filtros criados só poderão conter campos da tabela principal envolvida no processo.

Aproveitando a explicação do exemplo citado acima:

Serão mostrados somente campos da tabela Lançamento que é a principal, sendo que os campos das outras tabelas (CLOTE, GCOLIGADA, etc.) que são relacionadas a ela não aparecerão.

Cache de Segurança de Filtro por Usuário e Filtro por Perfil

A partir dos patches **12.1.24.179, 12.1.25.117** e versão **12.1.26**, quando um filtro por perfil ou filtro por usuário for adicionado ou modificado, as alterações serão aplicadas no RM, **após no máximo 2 minutos estando o usuário usando ou não o sistema**, não tendo a necessidade da reinicialização do Host.

Nas versões **anteriores**aos patches **12.1.24.179 e 12.1.25.117** as alterações de restrição serão propagadas após 2 minutos de **inatividade**do usuário em questão, não tendo a necessidade da reinicialização do Host.

## **03. BLOQUEIO DE BETWEEN NO FILTRO**

Veja aqui para mais informações,
