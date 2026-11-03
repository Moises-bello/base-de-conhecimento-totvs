---
article_id: 360060289014
category: LEGAIS - BLOCO H/MATR460
content_hash: 37910543829df1d5f445e65bfc1d650224bdf6fbf08cf0765adfb847d16d32ce
fetched_at: '2026-06-28T22:42:14.953078+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Validação
  do parâmetro MV_SDTESN3
type: support-article
updated_at: '2026-02-12T14:07:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-SDTESN3
---

O parâmetro MV\_SDTESN3 no relatório MATR460 do Protheus define como o saldo em poder de terceiros, referente a TES que não atualiza estoque, será considerado na impressão do relatório, influenciando diretamente a composição do saldo exibido, especialmente em operações como Devoluções Simbólicas.

**Dúvida**

Qual o objetivo da utilização do parâmetro MV\_SDTESN3 e o que ele influencia na impressão do relatório MATR460 (P7)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

**Possuímos um vídeo, demonstrando os diferentes resultados explicados nesta documentação:**

O parâmetro **MV\_SDTESN3** no relatório de **Registro de Inventário Modelo 7 (MATR460)** considera, em sua impressão, o saldo de poder de terceiros no Tipo de Entrada/Saída (TES) que **não** atualiza estoque. Desta forma, ele é utilizado quando a pergunta do relatório **Saldo em poder de 3º?** estiver configurada com a opção **SIM** e pode assumir os seguintes critérios:

* 0 (zero): desconsidera saldo com registro da tabela **SB6 (Saldo em/de poder de terceiros)** que contém TES que não atualiza estoque (comportamento padrão).
* 1 (um): considera saldo com TES que não atualiza estoque e, inclusive, subtrai da composição do saldo em estoque os itens que estão em poder de terceiros.
* 2 (dois): considera saldo com TES que não atualiza estoque, porém, não realiza a subtração do saldo em poder de terceiros para composição do saldo em estoque.

**Exemplos em que se aplica**

Normalmente este parâmetro é ativado quando se utiliza Devoluções Simbólicas, porque elas normalmente não movimentam estoque, mas, se o parâmetro estiver desabilitado, o relatório MATR460 continuará imprimindo o saldo como se estivesse pendente de devolução.

Quando se utiliza com frequência TES que não atualiza estoque em movimentos de poder de terceiros ele se torna muito importante para satisfazer o saldo que será impresso no relatório MATR460, muito por conta de ele ser um espelho do Bloco H do Sped Fiscal.

**Saiba mais:**

[*MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901)

[*MP - SIGAEST - Validação do Parâmetro MV\_R460TPC*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161)

[*Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
