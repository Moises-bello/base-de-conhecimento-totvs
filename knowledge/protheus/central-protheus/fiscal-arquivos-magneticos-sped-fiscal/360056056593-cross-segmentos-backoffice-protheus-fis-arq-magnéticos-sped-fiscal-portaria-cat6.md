---
article_id: 360056056593
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: fedff5ac99bb8d6d5ce90b4bdca27d3db10780ba490b26c41e3a30d18dcedbd3
fetched_at: '2026-06-28T22:42:01.022131+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  -  Portaria CAT66/2018 - Registros C197 e D197 - códigos de ajustes SP90090104  e
  SP90090278
type: support-article
updated_at: '2023-01-30T13:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056056593-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Portaria-CAT66-2018-Registros-C197-e-D197-c%C3%B3digos-de-ajustes-SP90090104-e-SP90090278
---

**Dúvida**Como configurar códigos de ajustes SP90090104 e SP90090278 registros C197 e D197?

**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.8  
  
**Solução**Portaria CAT66/2018 SP - Permitir a informação, através dos registros C197 e D197, dos valores das colunas de Outras e Isentas/Não Tributadas, além do ICMS-ST na condição de substituído;

**Projeto Eliminação da GIA:**  
A Secretaria da Fazenda e Planejamento do Estado de São Paulo inicia a Fase de Transição do projeto de **Eliminação da GIA**, mais uma medida concreta de simplificação de obrigações acessórias alinhada ao Programa de Conformidade Tributária, o "**Nos Conformes**". O projeto visa eliminar a necessidade da entrega mensal de duas declarações similares: a **GIA** e a **EFD ICMS/IPI**. Ao final, somente a **EFD** permanecerá obrigatória no Estado de São Paulo;

A **Eliminação da GIA** refere-se, portanto, à dispensa da obrigação, pelo contribuinte paulista, de entregar mensalmente a GIA, tendo em vista que a SEFAZ-SP gerará automaticamente uma **GIA virtual** a partir da **EFD ICMS/IPI;**

Para isso, foi necessário abrir a possibilidade para que sejam declarados, na **EFD**, os valores das colunas:

* Outras;
* Isentas/Não Tributadas;
* ICMS-ST na condição de substituído;

Tais valores serão informados através dos registros **C197**e**D197**, utilizando-se dos códigos de ajuste:

* **SP90090104** - Valor correspondente à coluna Isentas/Não Tributadas e Outras (artigos 214 e 215 do RICMS/2000);
* **SP90090278** - Valor correspondente ao ICMS ST na condição de substituído (artigo 278, § 1º, do RICMS/2000);

Quanto à escrituração dos valores:

* A escrituração dos valores da coluna **Isentas/Não Tributadas** deverá ser efetuada através do campo **VL\_ICMS**, para cada **CFOP** que conste dos registros **C190/D190** do documento fiscal, de forma sumarizada para todos os códigos CST e alíquotas informadas;
* A escrituração dos valores da coluna **Outras** deverá ser efetuada através do campo **VL\_OUTROS**, para cada **CFOP** que conste dos registros **C190/D190** do documento fiscal, de forma sumarizada para todos os códigos CST e alíquotas informadas;
* A escrituração dos valores de ICMS ST deverá ser efetuados pelos valores calculados ou declarados na inclusão do documento de entrada;

As disposições sobre a utilização dos códigos acima são dadas pela [Portaria CAT 66/2018](https://legislacao.fazenda.sp.gov.br/Paginas/pcat662018.aspx), e demais instruções disponibilizadas no [Manual de informação dos códigos SP90090104 e SP90090278](https://portal.fazenda.sp.gov.br/servicos/sped/Downloads/ManualPcat662018.pdf).

<https://portal.fazenda.sp.gov.br/servicos/sped/Downloads/ManualPcat662018.pdf>

**Dica:**

Quando os registros **C197** e **D197** não forem informados para os novos códigos, os valores das colunas **Outras** e **Isentas/Não Tributadas**, serão calculados tendo como base o registro **C190**, com fórmulas dispostas na **Portaria CAT 66/2018**.  A informação da coluna Isentas/Não Tributadas pelo código de informação **SP90090104** é situação extraordinária sempre que tais fórmulas não se aplicarem;

## Procedimentos para Configuração:

Como os valores serão informados através dos registros **C197**e**D197**, o **TES** deve ser ajustado com os novos códigos, para gravação da **tabela CDA** com os respectivos valores;

1. Cadastro de TES (MATA080):

* Configuração do TES para que o valor de **Isento** seja impresso na coluna de **VL\_ICMS** - Valor da coluna Isentas/Não Tributadas (RICMS, artigo 214, § 3º, 7, "a" e artigo 215, § 3º, 5, "a");

Exemplo:

Informar o campo **L.Fisc. ICMS** igual a **Isento** no cadastro do TES e definir um código de reflexo configurado com o campo **Valor** igual a **O-Isentas/Não Trib.** e o campo **Vl.Reg.197** igual a **Valor ICMS;**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093843093/mceclip0.png)

* Configuração do TES para que o valor de **Outros** seja impresso na coluna de **VL\_OUTROS** - Valor da coluna outras (RICMS, artigo 214, § 3º, 7, "b" e artigo 215, § 3º, 5, "b"), de acordo com o CST;

Exemplo:

Informar o campo **L.Fisc. ICMS** igual a **Outros** no cadastro do TES e definir um código de reflexo configurado com o campo **Valor** igual a **Q-Valor da coluna Outras** e o campo **Vl.Reg.197** igual a **Valor Outras;**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093843473/mceclip3.png)

* Configuração do TES para **Redução de base com material de Uso e Consumo**, nesse caso será impresso ambas as colunas **VL\_ICMS** e **VL\_OUTROS;**

Exemplo:

Informar o campo **L.Fisc. ICMS** igual a **Isento**, informar o percentual de redução no campo **%Red.do ICMS,**informar **Sim** no campo **Mat. Consumo** no cadastro de TES e definir dois códigos de reflexos sendo, um com o campo **Valor** igual a **O-Isentas/Não Trib.** e o campo **Vl.Reg.197** igual a **Valor ICMS**e outro com o campo **Valor** igual a **Q-Valor da coluna Outras** e o campo **Vl.Reg.197** igual a **Valor Outras;**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093844073/mceclip4.png)

Gerando um C197 para operações onde é totalmente tributada o ICMS , onde não existe valor de Outras ou Isentas/Não Tributadas. Nesse caso, o contribuinte não precisaria enviar registro C197 com o código SP90090104;

No entanto, o contribuinte não pode tomar crédito de IPI, mas no EFD ICMS IPI o registro C190 o valor do IPI não pode ser destacado no campo próprio;

Caso o contribuinte não envie o registro C197 relativo ao código SP90090104, uma fórmula será aplicada para calcular o valor da coluna Outros ICMS na GIA, baseada no registro C190, e essa fórmula, incorretamente, resultará num valor de para a coluna de Outras;

Para contornar o Manual indica o envio dos registros C197 com valores zerados para que o valor de Outros/Isentas da operação seja zero, porém com alíquota de 0,01;

Para isso precisamos  configurar um Reflexo conforme exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100599853/mceclip0.png)

O Sistema hoje com essa configuração irá gerar um lançamento da tabela CDA e o SPEDFISCAL está preparado para buscar Valor Maior Zero ou Alíquota maior que Zero e Base igual a Zero;

Permitindo gerar um C197 conforme manual.![](https://tdn.totvs.com/download/attachments/421389418/image2020-7-8_20-59-36.png?version=1&modificationDate=1594252776520&api=v2)

Informações:

* Recomendamos o preenchimento dos campos do cadastro de **Reflexo** (FISA072) **Base p/ calc.** e **Alíquota** com o conteúdo igual a **Z-Zero**. Caso seja necessário um preenchimento diferente, deverá ser feito em apenas um dos reflexos;
* Será permitido incluir mais de uma vez o mesmo código de lançamento quando o terceiro caractere do código for igual a "9" (Código informativo) e possuir códigos de reflexo diferentes;
* Foi realizado tratamento específico para que, quando utilizados os códigos **SP90090104** e **SP90090278**, o campo **DESCR\_COMPL\_AJ,**dos registros**C197**e**D197**, seja composto apenas pelo**CFOP**utilizado no registro **C190/D190**que corresponde às colunas **Isentas/Não Trib.** e **Outras**.

Para o código de lançamento **SP90090278**recomendamos a seguinte configuração de reflexo:![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093844633/mceclip5.png)

Importante:

O registro **C195** é o registro pai do registro **C197**. Em situações em que existirem mais de um **CFOP** para o mesmo Código de Lançamento (**SP90090104** / **SP90090278**) deverá ser configurado, no **TES**, campo de **Observação de Lançamento Fiscal** (CC7\_IFCOMP), um código diferente para cada CFOP. Caso isso não ocorra, apenas um registro **C195** será informado, o que causará erro na validação do arquivo.

Mais informações no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=702821923>
