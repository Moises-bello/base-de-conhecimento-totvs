---
article_id: 38643317434135
category: Financeiro - Configurador de Tributos
content_hash: 9dbbef48fc4c286d1ecb6c90c58d27d3d509723fb384e5745d4ced520748a75c
fetched_at: '2026-06-28T22:37:46.250635+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Lei 15.270/2025 - FISA170
  -  Reforma do Imposto de Renda 2026 no configurador de tributos
type: support-article
updated_at: '2026-02-25T21:11:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38643317434135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Lei-15-270-2025-FISA170-Reforma-do-Imposto-de-Renda-2026-no-configurador-de-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332740119) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar o IRPF conforme a Lei 15.270/2025 para títulos avulsos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

A **Lei 15.270/2025**promove uma ampla **reestruturação**no**Imposto de Renda da Pessoa Física (IRPF)**. A partir de **1º** **de janeiro de 2026** passam a vigorar as novas regras, que estabelecem:

* **Isenção** do imposto para quem recebe até **R$ 5.000,00 mensais**;
* **Redução**do imposto para quem recebe entre **R$ 5.000,01 e R$ 7.350,00**. O valor a deduzir sobre o imposto já apurado conforme a tabela vigente do IRRF deverá ser calculado pela seguinte fórmula:
* R$ 978,62 – (0,133145 × rendimentos tributáveis sujeitos à incidência mensal);

* Tributação de 10% sobre a distribuição de **lucros e dividendos**, para valores que excederem R$ 50 mil por beneficiário/fornecedor;

Para atender essas necessidades na operação de inclusão de títulos a pagar (FINA050), foram disponibilizados novos recursos nas Regras Financeiras da rotina **Configurador de Tributos (FISA170)**.

Para utilizar os novos recursos, é necessário:

1. Atualizar o dicionário de dados (UPDDISTR) com o [pacote acumulado do Backoffice de fevereiro/2026](https://tdn.totvs.com/pages/viewpage.action?pageId=587835160). Será criado o campo **FKS\_DEDSIM****(Dedução Simplificada)** e as **tabelas****F7S (faixa especial/redutor)** e **F7R (deduções por valor fixo)**;
2. Atualizar os programas com a patch da issue DSERFIS4-3208 ou aplicar o pacote acumulado do Backoffice de março/2026;

* 12.1.2310:<https://r.totvs.io/p/1239180> ;
* 12.1.2410:<https://r.totvs.io/p/1239181> ;
* 12.1.2510:<https://r.totvs.io/p/1239182> ;

Importante: Processo via Documento de Entrada.

Está FAQ contempla o processo de cálculo do IRPF de títulos a pagar avulsos, ou seja, que não possuem vinculo com um Documento de Entrada (MATA103).

Caso a origem do título seja através do Documento de Entrada (MATA103), será necessário parametrizar as Regras Fiscais (FISA170). Para mais informações: [CFGTRIB - Cálculo de IRPF utilizando a tabela progressiva, com desconto simplificado ou desconto normal](https://tdn.totvs.com/pages/viewpage.action?pageId=1028926771)

Cadastro de Regra de título:

Esse cadastro permitirá definir as características do título de retenção do IRPF a ser gerado no contas a pagar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332743447)

* Na inclusão da regra de título, atente-se para os campos abaixo:
  + O campo "Tp Movto." deve ser preenchido com a opção "2-Impostos" para que seja gerado um título de retenção no contas a pagar;
  + O campo "Participante" deve ser preenchido com a opção "1-Fornecedor", e com isso também deve ser definido qual o fornecedor que será atrelado ao título do IRPF (Ex: União);
  + Deve ser definida a carteira que o título será gerado. Portanto, preencha no campo "Carteira" a opção "1-Pagar";
  + O campo "Natureza" deve ser preenchido a critério de cada empresa. Ele não impactará o calculo e será apenas para fins classificatórios;
  + O campo "Tipo do Título" definirá qual o tipo do título a pagar do IRPF;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332744471)

Configurando a isenção/dedução de IR no cadastro da tabela progressiva:

* Regras financeiras
  + Cadastro das tabelas progressivas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332744983)

No processo de inclusão desse cadastro, pode ser preenchido o campo Ded. Simplif. (FKS\_DEDSIM) para que no cálculo do IRPF, seja realizado o comparativo entre as deduções "legais x simplificada".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317417751)

Na aba "Faixas da Tabela Progressiva", preencha as faixas da tabela progressiva do IRRF com os valores vigentes:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317418263)

Na aba "Faixas Especiais - Redutores", preencha as regras para que seja aplicado os descontos condicionais sobre o valor do IRPF (casos de isenção ou redução proporcional):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332746775)

Cadastro da Regra de Dedução

* Cadastro da regra de dedução

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317419031)

No processo de inclusão desse cadastro, podem ser definidas 2 formas de deduções:

* Por Regra Financeira - Possibilita que o cálculo de um tributo seja abatido da base de cálculo de outro (ex: subtrair o INSS da base do IR);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332747671)

* Por valores fixos - Possibilita definir deduções que os valores são fixos, ou seja, que não irão ter valores variados dependendo do cálculo (ex: deduções de dependentes);
* Importante: Para o tipo de dedução "Dependente", caso o autônomo possua mais de um dependente, deve ser preenchido no cadastro do fornecedor (SA2) o campo *A2\_NUMDEP*com a quantidade correta;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332748439)

Cadastro Regra de Cálculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317421463)

Na inclusão da regra de cálculo, atente-se para os campos abaixo:

* O campo "% alíquota" não precisa ser preenchido, já que a alíquota será obtida da tabela progressiva;
* O campo "Tabela Progressiva" deve ser preenchido com o cadastro contendo as faixas desejadas;
* O campo "Regra de Dedução" só deve ser preenchido para os casos em que o cálculo do IRPF tenha que aplicar as deduções legais (INSS, dependentes, etc.), caso contrário ele deve ser deixado sem preenchimento;

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317422359)

  Cadastro Regra de Retenção:

  Esse cadastro permitirá definir as regras de cumulatividade para o IRPF.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317423511)

  Na inclusão da regra de retenção, atente-se para os campos abaixo:
* O campo "Cumulativid." deve ser preenchido com a opção "2-Acumula valores de base";
* O campo "Period. Cum." deve ser preenchido com a opção "4-Mensal".

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317424023)

  Cadastro Regra Financeira:

  Esse cadastro permitirá o vinculo de todas as definições acima citadas e identificará que o tributo a ser calculado é o IRRF.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317425175)

  Esse cadastro é dividido em algumas partes:

  Aba Dados Gerais:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643317425687)

  Nessa aba, atente-se para os campos abaixo:

  + O campo "Fato Gerador" deve ser definido com o momento que o sistema irá gerar a retenção do IRPF;
    - Na opção "1-Competência", o tributo será gerado no Contas a Pagar assim que o título for incluso no sistema;
    - Na opção "2-Caixa", o tributo será gerado no Contas a Pagar assim que o título for baixado/pago no sistema;
  + O campo "Vlr. Título" deve ser definido como "1-Subtrair" caso seja desejado que o valor de retenção do IRPF seja subtraído do valor do título (quando o fato gerador for "competência") ou do valor da baixa (quando o fato gerador for "caixa");
  + O campo "Antecipações" deve ser preenchido com "1-Retem" caso a retenção de IRPF deva ocorrer na inclusão de pagamentos adiantados (título do tipo PA), caso contrário preencha como "2-Não".

  Aba Regras Gerais:

  Nessa aba deve ser vinculado os cadastros citados anteriormente, onde determinarão uma série de regras (vencimento do tributo, regra de cálculo, etc);

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38643332752919)

  Importante:

  Vincular a regra financeira no cadastro do Fornecedor e Natureza.

  Saiba mais:

  [Como configurar o IRPF conforme a Lei 15.270/2025 para títulos avulsos?](https://tdn.totvs.com/pages/releaseview.action?pageId=1043719216)
