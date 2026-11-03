---
content_hash: aed5b99955840a19ec3da216ea287af9063c8acc5adb0f02c65ed0147dfda7aa
fetched_at: '2026-06-29T00:10:11.168844+00:00'
page_id: '452719962'
product: rm
source: tdn-rm
title: Buscar resultados da roteirização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719962
version: 2
---

**Buscar resultados da roteirização**

O processo verifica no servidor se as rotas solicitadas foram roteirizadas e atualiza a informação no sistema.

Para o retorno positivo das rotas solicitadas, o campo "Motivos" da Aba "Rota" do Anexo "Informações de Rotas e Transporte", deverá ser automaticamente preenchido com "Concluído" e o campo status deverá ser gravado como "Roteirizado".

Se ocorrer alguma falha no retorno do webservice (Exemplo: "Departamento Técnico") ou quaisquer outros motivos ocasionem no cadastro parcial da rota em questão, o sistema deverá permitir gravar a mensagem de retorno, com o motivo da falha da roteirização para estes casos como "Não Roteirizado".

Alguns exemplos de Status das solicitações são:

* Pendente: Foi solicitado o cálculo, mas não foi executado o processo para buscar o resultado.
* Roteirizado: Cálculo e busca no servidor realizados.
* Não Roteirizado: Ocorreu algum erro que impediu o cálculo da rota corretamente.
