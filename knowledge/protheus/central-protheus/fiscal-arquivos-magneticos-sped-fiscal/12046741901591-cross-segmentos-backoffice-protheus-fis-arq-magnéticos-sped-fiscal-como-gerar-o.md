---
article_id: 12046741901591
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 995961d43ef93b79a7365564faa146a2feb6163004be891041fc32c83006cfb5
fetched_at: '2026-06-28T22:42:01.193115+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C173 via complementos fiscais no Sped Fiscal?
type: support-article
updated_at: '2023-02-01T16:49:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12046741901591-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C173-via-complementos-fiscais-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao gerar o Sped Fiscal, o registro **C173 - Operações com Medicamentos** não é apresentado.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**

**Solução**O registro em si é alimentado com as seguintes espécies e seguindo determinações ao pai C170, somente gerado para saídas:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”.
* Nota Fiscal Eletrônica, Modelo 55 – Espécie “SPED”.

Para gerar o registro, realize o seguinte procedimento:

1 - Acesse o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar.** Preencha o parâmetro **MV\_MEDICA** no configurador o parâmetro com o grupo de produto de **Medicamentos*****:***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12045407575703)***

2 - Preencha no cadastro de produto no campo **Grupo - B1\_GRUPO** informado no parâmetro **MV\_MEDICA.**

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12045554776855)***

3 - Acesse a rotina **de Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Saída > Complementos.**

4 - Preencha todos os campos da aba ***"*****Medicamentos*****".*** Dessa forma deverá ser preenchido os campos da tabela **CD7** de forma manual e o campo **CD7\_FABRIC** deverá ser preenchido com o seguinte conteúdo:

* Data de fabricação do medicamento no formato “ddmmaaaa” contido na alimentado na tabela SB8 campo **B8\_DFABRIC** que já é de seu conhecimento.
* Caso o campo **B8\_DFABRIC** esteja em branco deverá ser informado conteúdo dos campos das tabelas abaixo.
* Nota de Entrada Tabela **SD1 - D1\_DFABRIC**
* Nota de Saída Tabela **SD2 - D2\_DFABRIC**

**Atenção:**

Para preenchimento do campo **08\_VL\_TAB\_MAX** do registro C173 o campo **CD7\_PRECO**da tabela CD7 que considera o conteúdo do campo Preço MAX (**DA1\_PRCMAX**) da tabela **DA1** deverá ser preenchido.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12045706189079)

Após as configurações gere o arquivo Sped Fiscal.
