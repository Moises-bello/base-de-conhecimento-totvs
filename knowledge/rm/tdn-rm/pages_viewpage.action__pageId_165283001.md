---
content_hash: 47b4d36d475c9f13403cc97c293cbd34759d43f6653957cb11b2d945fb178da4
fetched_at: '2026-06-29T00:05:57.182130+00:00'
page_id: '165283001'
product: rm
source: tdn-rm
title: RMFIS00006_EFD Contribuições - Geração - Parâmetros da Geração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165283001
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal           **Versão:** 11.82.3x |
| **Processo** | **:** | EFD Contribuições - Tela de Geração |
| **Subprocesso** | **:** | Parametrização |
| **Data da publicação** | **:** | 02/10/2014 |

O objetivo deste artigo é orientar sobre o preenchimento dos campos para a geração da rotina, na tela de parametrização. Acompanhe o *passo a passo*.

Primeiramente, acesse o Menu de geração, para selecionar o layout EFD Contribuições importado: **Rotinas Legais | Rotinas Federais -> EFD PIS/COFINS.**

O sistema reporta como *default* ‐ ***C:\TOTVS\CorporeRM\RMLiber\Saidas***, o local onde será salvo o arquivo texto da rotina. Entretanto, este caminho pode ser alterado.

-1
incomplete


69
complete
**Data do Layout Gerador de Saídas**

 Neste campo é consistido a data do Layout EFD Contribuições. Atenção, para sempre manter o ambiente atualizado.

-1
incomplete


70
complete
**Coligada**

71
complete
**Filial**

 Informe a Coligada e Filial que deseja realizar a escrituração.

-1
incomplete


72
complete
**Considerar Operações das Filiais SCP**

               Caso este parâmetro esteja marcado são selecionados os dados de todas as filiais que sejam **SCPs**, independente de seu CNPJ, e que o **Sócio Ostensivo** seja a Filial parametrizada na geração. As informações das filiais **SCPs** antes eram geradas no arquivo como se fossem do Sócio Ostensivo, de acordo com as alterações introduzidas no Layout 1.14, à partir de Janeiro de 2014 a **EFD Contribuições** deverá ser transmitida separadamente, para cada **SCP**s, além da transmissão da EFD Contribuições, da própria sócia ostensiva. Além disso, será necessária também a geração de um novo registro, de código 0035, para identificar as **SCPs**.

-1
incomplete


73
complete
**Considerar Data Leitura para Seleção de Lançamentos de Energia Elétrica**

     Considera os documentos de Energia Elétrica de acordo com a Data de Leitura definida.

-1
incomplete


74
complete
**Versão do Layout**

              Este campo é atualizado de acordo com o layout EFD Contribuições.

-1
incomplete


75
complete
**Indicador de Situação Especial**

               Se o arquivo a ser gerado tem alguma situação especial. Indicador de situação especial:

0 ‐ Abertura

1 ‐ Cisão

2 ‐ Fusão

3 ‐ Incorporação

4 – Encerramento

-1
incomplete


76
complete
**Número do Recibo declaração anterior (somente para retificadora)**

Somente será informado se o arquivo a ser gerado é Retificador.

-1
incomplete


77
complete
**Data Inicial/Final**

Informar a data inicial e final da geração da rotina, esta data é mensal.

,

-1
incomplete


78
complete
**Gerar Bloco D**

Algumas empresas não tem a obrigação de informar o Bloco D, se informar “**NÃO**” será gerado somente os registro de Abertura e Encerramento deste Bloco(D001 e D990).

-1
incomplete


79
complete
**Gerar Registro M350**

PIS/PASEP - Folha de Salários. Eventos à serem excluídos da base de PIS.

-1
incomplete


80
complete
**Indicador de Atividade Preponderante**

Informar o indicador da atividade preponderante exercida pela pessoa jurídica no período da escrituração, conforme um dos tipos abaixo:

0 – Industrial ou equiparado a industrial;

1 – Prestador de serviços;

2 ‐ Atividade de comércio;

3 – Atividade financeira;

4 – Atividade imobiliária;

9 – Outros.

-1
incomplete


81
complete
**Contribuição Previdenciária Indicador da Incidência**

Apuração da Contribuição Previdenciária, necessária para geração do Bloco P.

-1
incomplete


82
complete
**Lucro Presumido**

Seleção do tipo de Regime Lucro Presumido: Regime de Caixa - Escrituração Consolidada e Regime de Competência - Escrituração Detalhada.

-1
incomplete


85
complete
**Lucro Presumido com base nas informações do Lançamento Fiscal ou Movimento**

              Geração do arquivo texto será realizada apenas com base nos lançamentos fiscais no TOTVS Gestão Fiscal.

-1
incomplete


86
complete
**Lucro Presumido - Considerar Base de Cálculo como valor da Receita**

Ao gerar o registro F500, o valor da base de cálculo será o mesmo valor da Receita.

-1
incomplete


87
complete
**Tipo de movimento(Pedido/Medição) a ser considerado no registro 1900**

Gera o Registro 1900, com este campo habilitado será considerado os Movimentos 2.1 (Previsão da Medição), que possuam os tributos PIS ou COFINS emitidos no período de geração da Rotina.  Os Movimentos Faturados e Escriturados a partir do Movimento 2.1(Pedido\Medição) que são gerados no Movimento 2.2, deve ser identificados para que não sejam considerados novamente. Caso o Campo “ Gerar Registro 1900 Considerando Movimento 2.1(Pedido\Medição)” esteja desabilitado o sistema considera os valores conforme consistência já existente atualmente.

-1
incomplete


88
complete
**Tipo de Movimento(Venda) a ser considerado no registro F500**

 Geração do registro F500 com base nos valores do tributo INSS nos lançamentos fiscais.

-1
incomplete


89
complete
**Cenário Patrimônio**

Segunda moeda a ser utilizada na geração dos registros F120 e F130.

-1
incomplete


90
complete
**Tipo de Escrituração**

Informe o tipo de escrituração – Original ou Retificadora.

-1
incomplete


91
complete
**Indicador da Natureza da Pessoa Jurídica**

Informe o Indicador de acordo com tipo da natureza da Pessoa Jurídica. Informação pertinente a geração das Filiais SCP.

-1
incomplete


92
complete
**Rotina**

Selecione a rotina legal pertinente. Acesse:Cadastros | Tabelas Auxiliares -> Configuração de Campos -> Rotina Fiscal.

-1
incomplete


93
complete
**Classificação de Municípios**

Selecione a tabela de Municípios. Exemplo: IBGE, SISCOMEX e RFB).

-1
incomplete


94
complete
**Classificação de Países**

 Selecione a tabela de Países. Exemplo: SISCOMEX e BACEN

-1
incomplete


95
complete
**Classificação de Países(Comércio Exterior)**

Selecione a tabela SISCOMEX

-1
incomplete


96
complete
**Código Indicador da Incidência Tributária no Período**

Indique o código correspondente ao(s) regime(s) de apuração das contribuições sociais a que se submete a pessoa jurídica no período da escrituração:

‐ No caso da pessoa sujeitar‐se apenas à incidência não cumulativa, deve informar o indicador “1”;

‐ No caso da pessoa sujeitar‐se apenas à incidência cumulativa, deve informar o indicador “2”;

‐ No caso da pessoa sujeitar‐se aos dois regimes (não cumulativo e cumulativo), deve informar o indicador “3”.

-1
incomplete


97
complete
**Código Indicador de Método de apropriação de Créditos**

Este campo deve ser informado no caso da pessoa jurídica apurar créditos referentes a operações (de aquisições de bens e serviços, custos, despesas, etc) vinculados a mais de um tipo de receita (não‐cumulativa e cumulativa):

‐ Operações tributadas no Mercado Interno;

‐ Operações não‐tributadas no Mercado Interno (Alíquota zero, suspensão, isenção e não‐incidência);

‐ Operações de Exportação.

No caso da pessoa jurídica adotar o método da Apropriação Direta, para fins de determinação do crédito vinculado a mais de um tipo de receita, informar neste campo o indicador “1”;

No caso da pessoa jurídica adotar o método do Rateio Proporcional com base na Receita Bruta, para fins de determinação do crédito vinculado a mais de um tipo de receita, informar neste campo o indicador “2”. Neste caso, a escrituração do Registro “0111” é obrigatória.

• **Observação**

O sistema trás como *default* o “NÂO SE APLICA”, mas tem que ser informado “1 ou 2”.

-1
incomplete


98
complete
**Código Indicador do Tipo de Contribuição Apurada no Período**

Indique o código correspondente ao tipo de contribuição apurada no período, a saber:

‐ Indicador “1”: No caso de apuração das contribuições exclusivamente às alíquotas básicas de 0,65% ou 1,65% (PIS/Pasep) e de 3% ou 7,6% (Cofins);

‐ Indicador “2”: No caso de apuração das contribuições às alíquotas específicas, decorrentes de operações tributadas no regime monofásico (combustíveis; produtos farmacêuticos, de perfumaria e de toucador; veículos, autopeças e pneus; bebidas frias e embalagens para bebidas; etc) e/ou em regimes especiais (pessoa jurídica industrial estabelecida na Zona Franca de Manaus ou nas Áreas de Livre Comércio, por exemplo).

A pessoa jurídica sujeita à apuração das contribuições sociais a alíquotas específicas deve informar o indicador “2” mesmo que, em relação a outras receitas, se submeta à alíquota básica.

-1
incomplete


99
complete
**Operações Institucionais Realizadas no Período**

N – Não se Aplica

01 – Exclusivamente operações de Instituições Financeiras e Assemelhadas.

02 – Exclusivamente operações de Seguros Privados.

03 – Exclusivamente operações de Previdência Complementar.

04 – Exclusivamente operações de Capitalização.

05 – Exclusivamente operações de Planos de Assistência à Saúde.

       06 – Realizou operações referentes a mais de um dos indicadores acima.

**Observação**: Utilizando a opção **“N - Não se aplica”** não será gerada informações do **Bloco I**.

-1
incomplete


100
complete
**Receita Bruta Não-Cumulativa - Tributada Mercado Interno(R$)**

Informe neste campo o valor total da receita bruta auferida no mercado interno pela pessoa Jurídica, vinculadas as receitas tributadas no regime não cumulativo:

‐ a alíquotas básicas de 1,65% (PIS/Pasep) e de 7,6% (Cofins);

‐ a alíquotas próprias do regime monofásico (diferenciadas e/ou por unidade medida de produto);

‐ a outras alíquotas específicas.

-1
incomplete


101
complete
**Receita Bruta Não-Cumulativa - Não Tributada Mercado Interno (R$)**

Informe neste campo o valor total da receita bruta auferida no mercado interno pela pessoa Jurídica, vinculadas as vendas efetuadas com suspensão, isenção, alíquota zero ou não‐incidência das contribuições sociais.

-1
incomplete


102
complete
**Receita Bruta Não-Cumulativa - Exportações (R$)**

Informe neste campo o valor total da receita bruta auferida relativa a operações de:

‐ exportação de mercadorias para o exterior;

‐ prestação de serviços para pessoa física ou jurídica residente ou domiciliada no exterior, cujo pagamento Represente ingresso de divisas;

‐ vendas a empresa comercial exportadora com o fim específico de exportação.

-1
incomplete


103
complete
**Receita Base Cumulativa (R$)**

Informar neste campo o valor total da receita bruta auferida pela pessoa jurídica, vinculada a receitas tributadas no regime cumulativo a alíquotas de 0,65% (PIS/Pasep) e de 3% (Cofins).

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx)

**COMUNIDADE **[R@Fiscal](http://fluig.totvs.com/portal/p/10097/subject/rfiscal)****

**Canais de Atendimento:**

**Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
