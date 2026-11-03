---
content_hash: a7316f91eb9d7d72ae022fc10b324e9b2b0aafb0c1a38141e3c4c3bf4512f112
fetched_at: '2026-06-29T00:11:26.332814+00:00'
page_id: '716347936'
product: rm
source: tdn-rm
title: RRA - Rendimentos Recebidos Acumuladamente - ESOCIAL
type: documentation
url: https://tdn.totvs.com/display/LRM/RRA+-+Rendimentos+Recebidos+Acumuladamente+-+ESOCIAL
version: 37
---

false

**A partir das Versões:**

* 12.1.34.258
* 12.1.2205.207
* 12.1.2209.152
* e Superiores.

**[Pacotes de Atualização - TAF#17](https://tdn.totvs.com/pages/viewpage.action?pageId=634272553#PacotesdeAtualiza%C3%A7%C3%A3oTAF-17)**

## **Conceito**

Os rendimentos recebidos acumuladamente são aqueles que se referem a anos-calendário anteriores ao do recebimento e, em razão disso, têm tratamento tributário especifico.

IN RFB 1.500 - Artigo 36. Os RRA, a partir de 11 de março de 2015, submetidos à incidência do imposto sobre a renda com base na tabela progressiva, quando correspondentes a anos-calendário anteriores ao do recebimento, serão tributados exclusivamente na fonte, **no mês do recebimento ou crédito**, em separado dos demais rendimentos recebidos no mês.

Para gerar as informações dos RRA dos funcionários que receberam este tipo de verba, deverá parametrizar e calcular conforme descrito na pagina: [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=715818269)

Após a parametrização e cálculo mencionado acima, o sistema irá criar o histórico em: Funcionários | Anexos | Históricos | Histórico de RRA conforme exemplo abaixo:

Será criado também a aba Informações do(s) Advogado(s) em Funcionários | Anexos | Históricos | Histórico de RRA

Ao criar o histórico de RRA, os campos "Tipo de Processo / Descrição RRA" e "Número do Processo" não são preenchidos, sendo necessário executar a rotina abaixo para preenchimento e para a correta geração do XML do evento S-1200.

Acessar Anuais | DIRF | Informe de Rendimentos | Atualizar Dados da DIRF

É necessário preencher o parâmetro "Atualiza dados do histórico de RRA"

    Selecionar a data de pagamento de RRA que deseja atualizar as informações.

    Selecionar os campos que deseja alterar.

**Atenção:** O campo "Nro Processo" deverá ser preenchido somente se o "Tipo de Processo" for judicial.

**Maiores informações**

falseImportante!Os valores de base de FGTS são lançados nos eventos [Código de Cálculo 69 - Base de FGTS de Diferença Salarial](https://tdn.totvs.com/pages/viewpage.action?pageId=452719698) e [Código de Cálculo 410 - Base de FGTS de Diferença Salarial na Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=485444881).

* [XML - Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=716349098)
* [XML - Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=716349110)
* [XML - Decimo Terceiro Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=716349137)
* [XML - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=716349155)
* [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=715818269)
* [Parametrizador – Geral 2/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715817366)
* [Código de cálculo 459 - DIFERENÇA SALARIAL RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818471)
* [Código de cálculo 460 - INSS DE DIFERENÇA SALARIAL RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=715818516)
* [Código de cálculo 461 - DIFERENÇA DE FÉRIAS RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725439)
* [Código de cálculo 462 - INSS DE DIFERENÇA DE FÉRIAS RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=725725460)
* [Código de Cálculo 463 - DIFERENÇA DE 13º SALÁRIO RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007397)
* [Código de Cálculo 464 - INSS DE DIFERENÇA DE 13º SALÁRIO RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=721007638)
