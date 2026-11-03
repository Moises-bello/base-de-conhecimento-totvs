---
article_id: 360050837874
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 56becd939a2f2a6c801391aecb4e0f1a891371574e4d489ea726b0d71e6301a4
fetched_at: '2026-06-28T22:42:06.652613+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Registro 1011 do arquivo magnético.
type: support-article
updated_at: '2023-01-25T20:43:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050837874-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registro-1011-do-arquivo-magn%C3%A9tico
---

**Dúvida**Como gerar o registro **1011** do **EFD contribuições**?  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 12.  
  
**Solução**

Este registro tem objetivo de detalhar os valores da **Contribuição com Exigibilidade Suspensa**, porém com processos sem **trânsito em julgado**. Registro válido a partir de janeiro de 2020.

As informações deste registro têm origem da tabela **CIE - Exigibilidade Susp EFD Con;**

Para configurar como as informações devem ser geradas no registro **1011**, foi criada uma nova seção de campos no cadastro do Processo Referenciado (**MATA967**), de forma que será possível configurar o **CST**, **Alíquota** e **Valor** conforme determina o processo. Abaixo a nova seção criada:

![image2019-11-13_16-53-40.png](https://tdn.totvs.com/download/attachments/520675673/image2019-11-13_16-53-40.png?version=1&modificationDate=1573674820067&api=v2)

Esta seção somente será habilitada quando o campo **Ind. Nat. Judi (****CCF\_NATJU)**se tratar sem trânsito em julgado e com exigibilidade suspensa de contribuição, e o campo **Cod. Trib (CCF\_TRIB)**for **7=PIS** ou **8=COFINS,**caso contrário esta seção permanecerá desabilitada;

Abaixo detalhamento de cada campo que compõe a nova seção;

**CST -**Informe aqui o **CST** da Contribuição conforme a determinação do processo;

**% Redução -**Informe neste campo o percentual de redução de base de cálculo (se houver) conforme determinação do processo. Campo não obrigatório e somente será habilitado para os **CSTs 01** e **02;**

**ICMS -**Indique (se necessário) neste campo se o **ICMS** deverá ser deduzido da base de cálculo da contribuição, conforme determinação do processo. Campo não obrigatório e somente será habilitado para os **CST 01 e 02;**

**ISS -**Indique(se necessário) neste campo se o **ISS** deverá ser deduzido da base de cálculo da contribuição, conforme determinação do processo. Campo não obrigatório e somente será habilitado para os **CST 01** e **02;**

**Alíquota -**Indique neste campo a alíquota conforme determinação do processo. Este campo somente deverá ser preenchido se o processo determinar alguma alíquota diferenciada, caso contrário basta deixar este campo vazio, para rotina considerar alíquota utilizada na própria escrituração. Este campo somente será habilitado para os **CSTs 01** e **02;**

**Cod Rec. -**Informe neste campo o código de receita da **DCTF** conforme o tributo. Este campo deverá ser preenchido se houver **CST** informado neste seção;

Lembrando que esta seção deverá ser preenchida conforme determinação do processo, se o processo determina que deverá ser tributado à **alíquota zero**, então o **CST** deverá ser preenchido com **06** por exemplo, se o processo determina algum percentual de redução de base de cálculo, este percentual deverá ser preenchido neste seção, se o processo determina a exclusão do **ICMS** ou **ISS** da base de cálculo, também será possível configurar neste seção, e se ainda o processo determina tributação com um alíquota menor, também podemos configurar neste seção. Importante que o cadastro seja feito em um item de processo para o **PIS** e em outro item de processo para a **COFINS;**

A parcela com **exigibilidade suspensa** de **PIS** e **COFINS** será obtido por meio da diferença entre a contribuição escriturada e a contribuição calculada conforme determina o processo;

Para exemplificar a geração do registro **1011**, em um cenário hipotético que o contribuinte tenha um processo sem trânsito em julgado, que permita a exclusão do valor do **ICMS** (calculado no documento fiscal) da base de cálculo de **PIS** e **COFINS**, tributados com alíquota básica, devemos configurar esta nova seção da seguinte maneira;

![image2019-11-13_17-39-44.png](https://tdn.totvs.com/download/attachments/520675673/image2019-11-13_17-39-44.png?version=1&modificationDate=1573677584090&api=v2)

Uma operação com valor de receita de R$ 100,00 com **ICMS** de R$ 18,00, teremos os seguintes valores

Valores e informações conforme escrituração

**CST de PIS** = 01

**Base de Cálculo de PIS** = 100,00

**Alíquota de PIS** = 1,65

**Valor de PIS** = 1,65

**CST da COFINS** = 01

**Base de Cálculo da Cofins** = 100,00

**Alíquota da Cofins** = 7,6

**Valor da Cofins** = 7,6

Os valores e informações conforme decisão judicial ficariam da seguinte maneira

**CST de PIS** = 01

**Base de Cálculo de PIS** = 82,00

**Alíquota de PIS** = 1,65

**Valor de PIS** = 1,35

**CST da COFINS** = 01

**Base de Cálculo da Cofins** = 82,00

**Alíquota da Cofins** = 7,6

**Valor da Cofins** = 6,23

Neste exemplo, o valor de **PIS** com exigibilidade suspensa será de 0,30 ( 1,65 - 1,35), e da **Cofins** será de 1,37 (7,60 - 6,23);

Em outro exemplo, se o processo determinar tributação à **alíquota zero**, devemos configurar da seguinte maneira.

![image2019-11-13_17-42-4.png](https://tdn.totvs.com/download/attachments/520675673/image2019-11-13_17-42-4.png?version=1&modificationDate=1573677725077&api=v2)

Mantendo o mesmo valor de receita de R$ 100,00, teríamos os seguintes informações;

Valores e informações conforme escrituração;

**CST de PIS** = 01

**Base de Cálculo de PIS** = 100,00

**Alíquota de PIS** = 1,65

**Valor de PIS** = 1,65

**CST da COFINS** = 01

**Base de Cálculo da Cofins** = 100,00

**Alíquota da Cofins** = 7,6

**Valor da Cofins** = 7,60

Os valores e informações conforme decisão judicial ficariam da seguinte maneira:

**CST de PIS** = 06

**Base de Cálculo de PIS** = 100,00

**Alíquota de PIS** =0,00

**Valor de PIS** = 0,00

**CST da COFINS** = 06

**Base de Cálculo da Cofins** = 100,00

**Alíquota da Cofins** = 0,00

**Valor da Cofins** =0,00

Neste exemplo, o valor de **PIS** com exigibilidade suspensa será de 1,65 ( 1,65 - 0,00), e da **Cofins** será de 7,60 (7,60 - 0,00);

Lembrando que por se tratar de processo sem trânsito em julgado a nota deverá ser escriturada nos blocos de movimentação e no bloco de apuração da EFD Contribuições **como se não houvesse benefício do processo.** Os documentos fiscais que tiverem processos com trânsito em julgado não serão demonstrados no registro **1011**;

Uma vez cadastrado o processo, deverá ser vinculado com o documento fiscal por meio da rotina Nota Fiscal Manual de Saída → Outras Ações → **Complementos (MATA926)**, em **Informações Complementares** e no sub-menu **Processos referenciados.**Os processos deverão ser informados a nível de item do documento fiscal, vinculando os dois itens do processo, um para o **PIS** e outro para a **COFINS**;

![image2019-11-13_17-24-13.png](https://tdn.totvs.com/download/attachments/520675673/image2019-11-13_17-24-13.png?version=1&modificationDate=1573676653147&api=v2)

![image2019-11-13_17-24-24.png](https://tdn.totvs.com/download/attachments/520675673/image2019-11-13_17-24-24.png?version=1&modificationDate=1573676664673&api=v2)

Uma vez configurado desta maneira, ao processar a apuração e gerar o arquivo da **EFD Contribuições** a partir de janeiro de 2020, o detalhamento da exigibilidade suspensa será gerado no registro **1011**;

Os valores com exigibilidade suspensa serão totalizados e demonstrados no campo **06-DESC\_DEC\_JUD** do registro **1010** pai dos registros filhos **1011**, detalhados com o código de receita informado na nova seção do cadastro de Processo Referenciado. Lembrando que o valor da exigibilidade suspensa será a diferença entre o valor do tributo escriturado e o valor conforme determina o processo;

Para facilitar a conferência dos valores de exigibilidade suspensa, foram criadas novas seções no relatório de conferência, lá teremos a nível de item de documento fiscal e por processo os valores processados pela rotina.

Para mais informações acesse o *link*;

<https://tdn.totvs.com/pages/releaseview.action?pageId=520675673>
