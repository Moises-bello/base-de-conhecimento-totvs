---
content_hash: ec6666cdd97f6ad8de6cf75fb622a89725f5b01ceee39a2bb3ac74f94799729c
fetched_at: '2026-06-29T00:10:47.510090+00:00'
page_id: '558241024'
product: rm
source: tdn-rm
title: Configuração para Formato da Moeda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=558241024
version: 10
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de Utilização**

**01. VISÃO GERAL**

  Nesse documento será apresentada a configuração necessária para utilizar a moeda no formato americano dentro do sistema RM.

       Existe hoje no sistema a tag "**LocalizationLanguage**" que trata outras funcionalidades do sistema, como tradução dos itens da Devex (Filtro de uma coluna,  agrupamento de colunas, etc), por isso foi criada uma nova tag "**LocalizationFormats**" para tratar apenas formatação de números, para que assim, como no padrão do Windows, seja possível setar uma cultura para localização de linguagem e outra cultura para localização de Formatação. 

Lembrando que alguns parâmetros podem não obedecer à cultura por questões de regra de negócio e informações do próprio servidor.​

Como exemplo temos o "cifrão", que não será alterado de real para dólar, para que tal configuração seja realizado será necessário a alteração do "Simbolo da Moeda", parâmetro disponível na tela de "Parâmetros Globais, aba "Gerais".

**02. **EXEMPLO DE UTILIZAÇÃO****

 Como exemplo vamos utilizar o código da cultura, definido pelo windows (<https://docs.microsoft.com/pt-br/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c>), que tem como exemplo o "English-Canada". A tag deve ser adicionada no arquivo de configuração "**RM.exe.config**", como mostrar imagem abaixo:

       Em seguida, após realizar login no sistema, acesse um campo do tipo moeda e verifique se a configuração foi aplicada. Para o exemplo foi acessada a tela de "Funcionários", aba "Salário/Jornada", campo "Mensal". Verifique que os valores estão sendo apresentados da forma correta de acordo com o configuração aplicada "English Canadá" (en-CA) "," (virgula) e "." (Ponto).
