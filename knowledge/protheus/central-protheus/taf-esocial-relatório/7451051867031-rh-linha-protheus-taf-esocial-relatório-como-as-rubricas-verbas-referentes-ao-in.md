---
article_id: 7451051867031
category: TAF - eSocial - Relatório
content_hash: c0973172fabe7888bf95768e71bbaab1b040fd5f8991938a7cc23fffea33a7a4
fetched_at: '2026-06-28T22:45:19.969076+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Relatório - Como as rubricas (verbas)
  referentes ao INSS, devem estar configuradas, para que sejam consideradas no Relatório
  de Conferência de INSS ?
type: support-article
updated_at: '2024-05-29T14:42:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7451051867031-RH-Linha-Protheus-TAF-eSocial-Relat%C3%B3rio-Como-as-rubricas-verbas-referentes-ao-INSS-devem-estar-configuradas-para-que-sejam-consideradas-no-Relat%C3%B3rio-de-Confer%C3%AAncia-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22381525720087) Tempo aproximado para leitura: **00:05:00min****Ocorrência**Como as rubricas (verbas) referentes ao INSS, devem estar configuradas, para que sejam consideradas no Relatório de Conferência de INSS ?  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS - (TAFA552A)- Todas as versões  
  
**Solução**

Referente á duvida de configuração de rubricas de INSS.

É Importante reforçar, que as rubricas somente serão consideradas no relatório de INSS, **quando possuir uma configuração pré-determinada.**

Caso as rubricas cadastradas no TAF, estejam com a configuração errada, mesmo que sejam integradas para o TAF, e transmitidas ao governo, o **valor não será apresentado no Relatório de Conferencia INSS.**

Valide se as rubricas de INSS para Valor, e Base, no TAF, estão com as configurações corretas x Colunas do Relatório:

**Relatório com as informações sintéticas:**

Na apresentação das informações de INSS, pelo eSocial do Futuro, podemos visualizar se os valores das colunas estão iguais, como no exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7473197356823)

ou divergentes:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7473275714583)

Vamos entender qual a configuração que a rubrica (verba) precisa ter, para que seja sumarizada na coluna **"Valor INSS - Vigente na base do TAF",** esta coluna mostra o  Valor de INSS vigente na base do TAF e transmitido ao eSocial:

1. Identifique quais são os códigos de rubricas, utilizados pela folha, para INSS.

   \*dica: pelo extrato de pagamento, gerado pelo ERP, é possível identificar os códigos.

2. Abra a tabela de rubricas, C8R do TAF, correspondente ao evento S-1010 do eSocial, ou realize a conferencia pela rotina TAFA232 ( menu: Atualizações>Eventos Esocial>Tabelas> Rubricas)  no TAF.

[Automação Fiscal - TAF - Funcionalidades - Como acessar a APSDU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109773)

3. Com a tabela aberta, é possível realizar filtros, contendo os números das rubricas, e/ou as configurações que serão apresentadas.

4. Valide se as rubricas atendem as configurações pré-determinadas:

*\*\* Natureza da rubrica = **9201***

*\*\* Incidência tributária da rubrica para a Previdência Social = **31***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7489873127703)

Exemplo de Filtro dentro da tabela C8R:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7489958010391)

Apresentação após o filtro:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7490231862679)

*Observação:*

Se a divergência de valor, estive no valor retornado pelo governo, na coluna ***"Valor INSS - Calculado pelo eSocial (Valor da DCTFWEB)"***, verificar a documentação no link abaixo:

[Automação Fiscal - Relatório - O valor calculado pelo eSocial (DCTFWEB), no relatório de INSS, está errado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7345360456343)

**Relatório com as informações analíticas:**

Na apresentação das informações analíticas de INSS, gerada por CPF, podemos visualizar, além do valor do INSS, exemplificado no item anterior, o valor de Base considerada no TAF.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7493502481047)

Vamos entender qual a configuração que a rubrica (verba) precisa ter, para que seja sumarizada na coluna **"TAF",** linha **"BASE INSS";** Esta linha demonstra o  valor de Base INSS disponíveis nas tabelas do TAF.

1. Identifique quais são os códigos de rubricas, utilizados pela folha, para INSS.

   \*dica: pelo extrato de pagamento, gerado pelo ERP, é possível identificar os códigos.

2. Abra a tabela de rubricas, C8R do TAF, correspondente ao evento S-1010 do eSocial, ou realize a conferencia pela rotina TAFA232 ( menu: Atualizações>Eventos Esocial>Tabelas> Rubricas)  no TAF.

[Automação Fiscal - TAF - Funcionalidades - Como acessar a APSDU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109773)

3. Com a tabela aberta, é possível realizar filtros, contendo os números das rubricas, e/ou as configurações que serão apresentadas.

4. Valide se as rubricas atendem as configurações pré-determinadas:

*\*\* Natureza da rubrica = **9901***

*\*\* Indicativo do tipo de rubrica = **3 (Informativa)***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7513902523031)***

Exemplo de Filtro dentro da tabela C8R:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7513957338903)

Apresentação após o filtro:

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7513954968215)***

**Resultado das análises:**

1. Identificado que o código de rubrica no TAF, referente á INSS, está errada, não possui a configuração correta para ser considerada no relatório de conferência de INSS.

Será necessário corrigi-la no TAF.

Valide se a mesma rubrica está correta no seu ERP e no governo (eSocial).

2. Não foi identificado na tabela do TAF, ou dentro da rotina, um código de rubrica com as configurações pré-determinadas.

Valide se existe no seu ERP um código de rubrica com as configurações corretas. Pode ocorrer dessa rubrica, ainda não estar integrada no TAF.

Se necessário, crie uma código de rubrica, que contemple as configurações.

3. Identificado que existe código de rubrica, com as configurações pré-estabelecidas, porém, no relatório  de conferencia de INSS, os valores de INSS e/ou de base, **na coluna TAF**, não estão corretos.

*Abra um ticket para o suporte padrão TAF, com as seguintes informações:*

a) Informe em qual dos relatórios foi detectada a divergência, sintético ou analítico;

b) Informe o nome da coluna, que o valor está errado,

c) Informe o valor esperado (correto);

d) Informe qual o código de rubrica não está sendo considerado, ou está sendo considerado de forma errada.

e) Relate se existe alguma particularidade nos registros retornados errados;

f) Encaminhe as informações de um colaborador que identificou erro:

XML do evento S-5001; ([Automação - Configuração - Gerar XML de retorno dos eventos no TAF)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046869313)

XML do evento que o originou (S-1200, S-2299 ou S-2399);

g) Encaminhe uma cópia da tabela V3N, filtrada pelo período de apuração em questão.

h) Encaminhe uma cópia da tabela C8R.

**Documentações relacionadas ao assunto:**

Painel de Conferência de INSS (documentação que explica como gerar o relatório, e as informações contidas nele).

<https://tdn.totvs.com/pages/releaseview.action?pageId=528452133>

Documentação que exemplifica como corrigir as rubricas.

[RH - Linha Protheus - GPE - eSocial - S-5001 - Como conferir as divergências encontradas entre o INSS apurado pelo governo e o relatório do TAF (TAFR120)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024628231)
