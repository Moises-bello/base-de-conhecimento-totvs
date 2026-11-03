---
article_id: 23606437272343
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 1ddc94d3c74dbfc601eb9ca844a692100732bd19685ce39b27ce03e1f17a8b5e
fetched_at: '2026-06-28T22:42:02.611243+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos -SPED FISCAL-
  Como Gerar o Registro 1601, Relacionado ao Cadastro de Forma de Pagamento.
type: support-article
updated_at: '2024-09-04T18:09:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23606437272343-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-Gerar-o-Registro-1601-Relacionado-ao-Cadastro-de-Forma-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23606437236119) Tempo aproximado para leitura: **00:05:00 min****Dúvida.**

Como gerar o Registro 1601 do Sped Fiscal, relacionado à forma de Pagamento?  
**Ambiente.**

Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.2210

**Solução:**

**Solução:**

A **Rotina FISA312** passou por uma mudança recentemente, devido à uma instrução da Receita.   
O meio de pagamento não é discriminado no layout do **Registro 1601**, porém, influenciará o regime de Apuração a ser considerado, se **Competência** ou **Caixa**.

Cabe a cada **UF** determinar o regime de apuração das **Formas de Pagamento**, conforme consta no material “**[Perguntas Frequentes v7.3](http://sped.rfb.gov.br/arquivo/show/7200)**”:

"Cada meio de **pagamento** pode ter um **Regime de Apuração** diferente e a regra depende de cada **Unidade Federativa (UF)**.   
Por exemplo, uma **UF** pode determinar que para o **Boleto**, o valor deve ser **Apurado** conforme a **Data de Emissão** e a outra **UF** pode determinar que seja **Apurado** pela **Data do Pagamento**.

O **componente** irá considerar o **Regime de Apuração** que estiver parametrizado, sendo determinado pelo **consumidor do componente**.”

O **componente** irá considerar o **Regime de Apuração** que estiver parametrizado, sendo determinado pelo **consumidor do componente**, nessa questão, foi criado a seguinte opção para integração das informações do **Financeiro** para **Rotina FISA312**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23606437238807)

Somente poderá ser informado um tipo de **Regim**e por forma de **Pagamento** por **Filial**.

**Exemplo:** Quando cadastrar uma forma de pagamento **BOL** por **Regime Competência** e no mesmo período de importação dos movimentos do **Financeiro** o **título tiver baixa**, ele será importando por **competência** conforme cadastro, **não sendo possível incluir outro Regime para a forma de Pagamento** **BOL:**

*Print:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23606437243031)

Importante: O **Cadastro de Relacionamento** da forma de **Pagamento**, deverá ser vinculado no **módulo do Financeiro** por meio da **Rotina FINA490** (**Motivo de Baixa**).

*Print* Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23606437245591)

*Print:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23606437247383)

**Atenção:** Não serão considerados **títulos** com **recebimento** ou **pagamento** em espécie (**FKF\_ESPEC = S** ou **F7G\_ESPEC = S**) e os bancos listados nos parâmetros **MV\_CXFIN** e **MV\_CARTEIR**.

**Observação:** A rotina passou a validar o parâmetro **MV\_FINFMPG**, este parâmetro deverá ser utilizado nas forma de **Pagamento** da **Tabela 24** da **SX5** que não movimentam **Instituições Financeiras** para geração **SPED 1601**.

Preenchimento do parâmetro citado, havendo necessidade de utilização:

**MV\_FINFMPG= CI|CO|CQ|FA|FID|R$|RA|VA|VP**

Para o correto funcionamento da rotina FISA312, o ambiente deve estar atualizado com os últimos dicionários referente a expedição continua dos módulos Fiscal e Financeiro:

**Fiscal:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

**Financeiro:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=531017758>  
  
Para que o registro referente o pagamento seja considerado no 1601 do SPED FISCAL é necessário que ele (Banco - SA6) possua um vinculo de cadastro de cliente (Mesmo cadastro do banco na SA1) no campo "Cliente (A6\_CODCLI)".

**Exemplo:**

**Banco Itaú no cadastro de Bancos SA6:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26134189279127)

**Banco Itaú no cadastro de Clientes SA1:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26134151107991)

Caso não exista o vínculo acima, será processado na rotina FISA312 os pagamentos baixados no Financeiro, mas ao gerar o arquivo do Sped Fiscal, não serão gravados registros do 1601 para o participante (Banco) sem o vínculo.

**Documentação complementar:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=754623335#SPDFISCadastrodeopera%C3%A7%C3%B5escominstrumentosdepagamentoseletr%C3%B4nicosparaoregistro1601doSPEDFiscal-04.CADASTRO-FORMADEPAGAMENTOPORREGIME>

<https://tdn.totvs.com/pages/releaseview.action?pageId=781865016>

Abaixo link com informações elaboradas pela nossa consultoria segmentos referente a obrigatoriedade de entrega do registro 1601 de cada unidade federativa:

<https://www.totvs.com/blog/fiscal-clientes/efd-icms-ipi-registro-1601/>

Anexo, segue vídeo contemplando um exemplo da execução da rotina.
