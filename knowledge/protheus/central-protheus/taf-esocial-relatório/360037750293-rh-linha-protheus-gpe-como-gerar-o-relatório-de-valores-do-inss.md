---
article_id: 360037750293
category: TAF - eSocial - Relatório
content_hash: bb493cfb5898b55a95c4424732000416ee347a0be9395e8a11e1f0a63e82899c
fetched_at: '2026-06-28T22:45:20.054436+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o relatório de valores do INSS
type: support-article
updated_at: '2026-06-26T12:10:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037750293-RH-Linha-Protheus-GPE-Como-gerar-o-relat%C3%B3rio-de-valores-do-INSS
---

**Dúvida**

Como gerar relatório de conferência dos valores do INSS (S-5001)?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17

**Solução**

1 - Acesse o Módulo SIGATAF;

2 - Clique em: **Relatórios -> Conferência -> INSS - Base de Cálculo e Valor Segurado;**

3 - Na tela abaixo, você deve preencher todos os parâmetros que gostaria de gerar ao relatório de conferências:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049676753/mceclip0.png)

**Atenção:**

* **Período?** Mês/ano desejado para impressão das informações do relatório - Competência da Folha de Pagamento que foi integrada com o TAF.
* **Validação**: Permite informar um período igual ou superior à 05/2018, início dos eventos periódicos do eSocial.
* **Lista apenas divergências**: Parâmetro que permite listar somente os casos que apresentaram alguma divergência de valores entre as colunas Folha x TAF x Governo, ou listar todos os colaboradores, independente de divergência ou não.
* **Opções**:

+ **Sim** = lista somente colaboradores com divergência de valores nas colunas de valor.
+ **Não** = lista informações de todos os colaboradores

- **Observação**: Considera apenas as colunas Valor INSS, Valor INSS 13º Salário, Valor Salário-Família, Valor Salário-Maternidade e Valor Salário-Maternidade 13º Salário na comparação de divergência de valores.

* **Lista Trabal. Sem Valor?** Indica se o relatório deverá listar inclusive os trabalhadores que não possuem valores de INSS no período selecionado.
* **CPF Trabalhador?** Caso este parâmetro esteja vazio, o sistema listará todos os trabalhadores disponíveis de acordo com os parâmetros informados. Caso o mesmo esteja preenchido, o sistema listará apenas o trabalhador relacionado ao CPF informado.

4 - Selecione o diretório onde o relatório será salvo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048775634/mceclip1.png)

5 - Em seguida, selecione a(s) filial(is) desejada(s) para impressão:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049676873/mceclip2.png)

6 - O relatório é gerado no formato planilha em arquivo Excel, apresentando na primeira aba o totalizador de valor INSS dos grupos : Folha - TAF - Governo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048775814/mceclip3.png)

**Obs.:** A coluna TAF Estab. será apresentada de forma dinâmica, conforme os estabelecimentos existentes no relatório!
