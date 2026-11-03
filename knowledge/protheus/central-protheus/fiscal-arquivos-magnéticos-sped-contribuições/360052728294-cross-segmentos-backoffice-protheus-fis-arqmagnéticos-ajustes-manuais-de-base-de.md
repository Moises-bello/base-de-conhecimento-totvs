---
article_id: 360052728294
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 0edf06795d1e6025542ef57977460b9e4b49dc6116518b1abdeb2afaa812b5db
fetched_at: '2026-06-28T22:42:04.893894+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Ajustes Manuais
  de Base de Cálculo de PIS e COFINS
type: support-article
updated_at: '2022-08-31T12:52:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052728294-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Ajustes-Manuais-de-Base-de-C%C3%A1lculo-de-PIS-e-COFINS
---

**Dúvida**  
Ajustes Manuais de Base de Cálculo de PIS e COFINS  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Cadastro de Ajustes Manuais de Base de Cálculo de PIS e COFINS

Está disponível na apuração da EFD Contribuições, o cadastro de Ajustes Manuais de Base de Cálculo de PIS e COFINS, para geração dos registros M215 e M615 a partir de janeiro de 2019.

Sempre que houver necessidade de realizar ajuste manual de base de cálculo, basta acessar no menu da Apuração de PIS e COFINS a opção Ajuste Base de Cálculo de PIS e COFINS.

**Procedimento de Utilização:**

Nesta rotina conseguiremos incluir ajustes manuais de base de cálculo, por meio dos seguintes campos:

Tributo: Informar qual o tributo deve ser ajustado, 1=PIS ou 2=COFINS;

Ind. Ajuste: Informe o indicador de ajuste, 0=Ajuste de Redução ou 1=Ajuste de Acréscimo;

Val. Ajuste: Informe neste campo o valor do ajuste de base de cálculo a ser realizado;

Cód. Ajuste: Indique o código de ajuste conforme tabela 4.3.18 da Receita Federal;

Cod. Contrib: Informe qual o código da contribuição conforme tabela 4.3.5 da Receita Federal que deverá ser ajustado;

Num. Doc/Proc: Informe neste campo o Número do processo, documento ou ato concessório ao qual o ajuste está vinculado, se houver.

Descrição: Informe a descrição deste ajuste, campo de preenchimento livre;

Data Refer: Data de referência, esta data indica em que período da apuração o ajuste deverá ser realizado.

Cta Contábil: Informe o código da conta analítica contábil;

CNPJ: Informe aqui o CNPJ a que se refere o ajuste manual;

Inf. Compl.: Campo de preenchimento livre, para complementar a descrição do ajuste manual.

Ind. Ajuste: Informe o indicador de ajuste, 0=Ajuste de Redução ou 1=Ajuste de Acréscimo;

Uma vez cadastrados estes ajustes serão utilizados na apuração da EFD Contribuições, para reduzir ou acrescentar a base de cálculo. Na tela de apuração será possível verificar os ajustes de base de cálculo, através de duplo clique nas linhas totalizadoras de ajustes de base de cálculo.

Importante lembrar que esta rotina somente deverá ser acessada na hipótese de ajuste de base de cálculo manual, e para período a partir de janeiro de 2019.

Caso o contribuinte tenha decisão judicial autorizando exclusão do ICMS a Recolher da base de cálculo, não há necessidade de acessar esta rotina, pois os ajustes nos registros M215 e M615 serão gerados automaticamente pela apuração da EFD Contribuições.
