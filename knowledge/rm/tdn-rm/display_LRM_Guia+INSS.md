---
content_hash: 485425e2d2d6809e000e457d1915e733c518a0ab2264b092b17e9f804f0a191a
fetched_at: '2026-06-29T00:08:45.318088+00:00'
page_id: '311065805'
product: rm
source: tdn-rm
title: Guia INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/Guia+INSS
version: 4
---

falseATENÇÃO:A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.  

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

  

A Guia da Previdência Social (G

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Versões:** |  |
| **Ocorrência:** | Art. 394-A.  § 2º Cabe à empresa pagar o adicional de insalubridade à gestante ou à lactante, efetivando-se a compensação, observado o disposto no art. 248 da Constituição Federal, por ocasião do recolhimento das contribuições incidentes sobre a folha de salários e demais rendimentos pagos ou creditados, a qualquer título, à pessoa física que lhe preste serviço. |
| **Ambiente:** | Guia de INSS |
| **Passo a passo:** | Para habilitar as alterações da reforma trabalhista; Acesse MDI  > RH > Folha de pagamento > Configurações > Parametrizador > Folha Normal > Geral  Marque o parâmetro: Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017      **Para a Geração da Guia de INSS  Art. 394-A § 2°**  Siga os passos abaixo:    1º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope  Verifique que no envelope do funcionario foi lançado dois eventos com os codigos de calculo (359 e 360) referente a insalubridade.  Evento Diferença do adic. insalubridade para gestante : R$ 90,00  Evento Adicional de insalubridade para gestante: R$ 200,00      1º ) Encargos> Guia de INSS > Guia de INSS  Verifique que após a geração da Guia de INSS de folha normal os valores foram deduzidos corretamente.  O valor total de R$290,00.    2º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope  Verifique que no envelope do funcionario foi lançado três eventos com os codigos de calculo (359, 364 e 363) referente a insalubridade.    Evento Adicional de insalubridade para gestante: R$ 200,00  Evento Diferença Media Adic. Insalub.Gestante13º.Rescisão : R$ 600,00  Evento Media Do Adic.Insalub.Gestante 13º.Rescisão: R$ 130,00    2º ) Encargos> Guia de INSS > Guia de INSS  Verifique que após a geração da Guia de INSS de 13º Rescisãol os valores foram deduzidos corretamente.  O valor total de R$930,00.      3º ) MDI  > RH > Folha de pagamento > Administração de Pessoal > Funcionários > Envelope    Verifique que no envelope do funcionario foi lançado dois eventos com os codigos de calculo (361 e 362 ) referente a insalubridade 13º salario.  Evento Media Do Adic.Insalubridade Gestante 13o.Salário : R$ 60,00  Evento Diferença Media Adic.Insalub.Gestante 13o.Salário: R$ 30,00    3º ) Encargos> Guia de INSS > Guia de INSS  Verifique que após a geração da Guia de INSS de 13º salario l os valores foram deduzidos corretamente.  O valor total de R$90,00. |
| **Observações:** |  |
