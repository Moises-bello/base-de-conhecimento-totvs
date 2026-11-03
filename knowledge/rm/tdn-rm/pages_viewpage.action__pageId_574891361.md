---
content_hash: 5db93cfae92f6475792600b4a3ab0bac539ac7ba5a6e6461a890af8e199f4d68
fetched_at: '2026-06-29T00:10:53.081377+00:00'
page_id: '574891361'
product: rm
source: tdn-rm
title: Nota Técnica nº 20/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574891361
version: 13
---

false

**A partir das Versões:**

* 12.1.27.311
* 12.1.28.219
* 12.1.29.148
* ou Superiores
Atenção

**A atualização para os patchs citados acima é apenas para contemplar o item 4 abaixo.****Sendo assim, para os clientes que utilizam TAF Full não é****necessário aplicação do patch somente as configurações nos eventos.**

# Objetivo:

---

Em 01/12/20 foi disponibilizado pelo eSocial a Nota Técnica 20/2020, apontando ajustes no Layout do S-5001 referente ao cálculo de salário maternidade devido à decisão do Supremo Tribunal Federal (STF) sobre o assunto. A decisão indica que é inconstitucional a incidência de contribuição previdenciária a cargo do empregador sobre o salário-maternidade. Mostraremos abaixo os impactos em nosso sistema.

---

Seguem orientações referente ao produto TOTVS Folha de Pagamento, para atender essa alteração:

1) Os eventos com códigos de cálculos de salário maternidade (CC017, CC178, CC371, CC372, CC373 e CC374) deverão ter o parâmetro "**Incidência Exclusiva do Segurado**" marcado, conforme prints abaixo:

 

2) Após a alteração realizada no item 1 serão gerados gatilhos do evento S-1010. Não é obrigatório o envio desses eventos ao governo, pois terão os mesmos codIncCP 21 (Mensal) ou 22 (13º). Assim, caso o usuário não queira enviá-los, poderá excluí-los da fila de eventos.

3) As rotinas de Guia de INSS (GPS), Folha Analítica, Encargos Contábeis e Sefip já consideram o parâmetro "**Incidência Exclusiva do Segurado"**, aplicando no item 1.

Mais informações em:

[Guia de INSS (GPS) e Folha Analítica](https://tdn.totvs.com/pages/viewpage.action?pageId=520101874)

[Guia de INSS (GPS) e Folha Analítica 13o. Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=520671442)

[Encargos Contábeis](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=532664472)

[Sefip](https://tdn.totvs.com/pages/viewpage.action?pageId=590040491)

4) Para o **Relatório Comparativo de INSS (Middleware****)** a coluna "**Base governo**" foi alterada para considerar o Tipo Valor **"19 - Base de cálculo da Contribuição Previdenciária exclusiva do empregado".**
