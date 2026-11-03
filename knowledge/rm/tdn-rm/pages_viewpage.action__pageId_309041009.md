---
content_hash: 46bc562337ef0bedb1892204eca432dddf1610e26eca96590e221841469ed1fb
fetched_at: '2026-06-29T00:08:44.560403+00:00'
page_id: '309041009'
product: rm
source: tdn-rm
title: Art. 394-A. - paragrafo 2 Adicional de insalubridade à gestante ou à lactante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309041009
version: 5
---

**Assunto**

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** |  |
| **Ocorrência:** | Art. 394-A.  ~~§ 2º Cabe à empresa pagar o adicional de insalubridade à gestante ou à lactante, efetivando-se a compensação, observado o disposto no art. 248 da Constituição Federal, por ocasião do recolhimento das contribuições incidentes sobre a folha de salários e demais rendimentos pagos ou creditados, a qualquer título, à pessoa física que lhe preste serviço.~~    Texto MP 808:  Art. 394-A. A empregada gestante será afastada, enquanto durar a gestação, de quaisquer atividades, operações ou locais insalubres e exercerá suas atividades em local salubre, excluído, nesse caso, o pagamento de adicional de insalubridade. ...........................................................................................  § 2º O exercício de atividades e operações insalubres em grau médio ou mínimo, pela gestante, somente será permitido quando ela, voluntariamente, apresentar atestado de saúde, emitido por médico de sua confiança, do sistema privado ou público de saúde, que autorize a sua permanência no exercício de suas atividades.  § 3º A empregada lactante será afastada de atividades e operações consideradas insalubres em qualquer grau quando apresentar atestado de saúde emitido por médico de sua confiança, do sistema privado ou público de saúde, que recomende o afastamento durante a lactação." (NR) |
| **Ambiente:** | Adicional de Insalubridade Gestante |
| **Passo a passo:** | **Este passo a passo  está obsoleto pelo texto da MP 808.**    **Para** **Art. 394-A § 2°**  Siga os passos abaixo:  1º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Eventos  > Novo  Criar eventos para os novos códigos de cálculo:  359 - ADICIONAL DE INSALUBRIDADE PARA GESTANTE  360 - DIFERENÇA DO ADIC.INSALUBRIDADE PARA GESTANTE  .      2º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Cálculos > Valores Fixos  Para o cálculo interno do módulo TOTVS Folha de Pagamento deve ter o valor do salário mínimo cadastrado.      3º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope  Lançamento do evento de Insalubridade para gestantes com cálculo interno do módulo TOTVS Folha de Pagamento que deve ter o valor do salário mínimo cadastrado  Lançar no envelope de pagamento que poderá ser via lançamento de grupo de eventos com Eventos do Grupo ou com Códigos Fixos ou por inclusão diretamente no envelope.          4º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Fórmula  Para o lançamento do evento de Insalubridade para gestantes com cálculo através de fórmula deve cadastrar a fórmula e associar ao evento cadastrado anteriormente.      5º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope  **Atenção:** Lançar no envelope de pagamento que poderá ser via lançamento de grupo de eventos com Eventos do Grupo ou com Códigos Fixos ou por inclusão diretamente no envelope.        6º ) MDI  > RH > Folha de pagamento > Folha Mensal > Lançamentos > Diferença salarial  Para cálculo da diferença de insalubridade o evento de Código de Cálculo 360 deve estar criado conforme item 1. No módulo de lançamento de diferença salarial será calculado e lançado conforme parametrização.      Para um cálculo de abril a agosto com diferença de R$10,00 \* 5 meses = R$50,00.    7º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope  Será lançado o evento com o valor da diferença |
| **Observações:** |  |
