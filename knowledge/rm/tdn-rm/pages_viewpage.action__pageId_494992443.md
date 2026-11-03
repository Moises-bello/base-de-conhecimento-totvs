---
content_hash: 21c0ce91058e28bed8ccf06034c2f1f279abec90481e09400617264e7cc1160c
fetched_at: '2026-06-29T00:10:21.969020+00:00'
page_id: '494992443'
product: rm
source: tdn-rm
title: Registro 10 - Identificação do Estabelecimento Informante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494992443
version: 3
---

Este registro será preenchido com os dados contidos no cadastro da Filial selecionada.

***Campos a serem observados:***

* Campo 06 - Unidade Federada (ST)
* Campo 07 - Inscrição Estadual (ST)

Estes campos serão preenchidos pelos registros presentes no Cadastro de Inscrição Estadual S.T. disponível no Anexos do cadastro da Filial

BLOCO0left00000000

**Abertura do Arquivo Digital e Identificação da Pessoa Jurídica**

Este registros é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Tributação do cadastro de Filiais.

00010001

**Abertura do Bloco 0**

Este é um registro de controle gerado automaticamente pelo processo da rotina que informa se existe ou não movimentação no bloco 0.

00100010

**Parâmetros de Tributação**

Este registro é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Tributação do cadastro de Filiais. A informação da Forma de Apuração é carregada com base nos períodos de apuração criados para os tributos CSLL e IRPJ incluídos para as filiais. A informação da Forma de Tributação é carregada com base nos eventos tributários incluídos para estes mesmos Tributos. Portando deve-se dar uma atenção especial a estes dois cadastros para que não sejam apresentados erros na validação do arquivo texto da rotina.

00200020

**Parâmetros Complementares**

Este registro é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Complementares do cadastro de Filiais.

00300030

**Dados Cadastrais**

Este registro é gerado com base nas informações do cadastro da Filial Matriz dos estabelecimentos ou da Filial SCP quando a declaração pertencer a uma Filial do tipo SCP.

00350035

**Identificação das SCP**

Neste registro será gerada uma linha para cada filial do tipo SCP que existir no cadastro de Filais na Coligada corrente.

09300930

**Identificação dos Signatários da ECF**

Para que este registro seja corretamente gerado as informações do anexo Dados Fiscais | Contador e Dados Fiscais |  Representante deverão estar rigorosamente preenchidos. Estes dados são obrigatórios para a validação do arquivo no PVA da ECF.

09900990

**Encerramento do Bloco 0**

Este é um registro de controle gerado automaticamente pelo processo da rotina.
