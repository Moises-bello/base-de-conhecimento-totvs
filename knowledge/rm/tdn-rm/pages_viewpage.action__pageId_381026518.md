---
content_hash: a28f71fc11bd9cb1236392c47dd29bb39b5bc06497fbeaa4b571c8355c49193b
fetched_at: '2026-06-29T00:09:02.562232+00:00'
page_id: '381026518'
product: rm
source: tdn-rm
title: 1573336 FISCAL01-2641 DT NFS-e - Regra de geração da TAG tipoTrib do layout
  único do TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381026518
version: 5
---

# Regra de geração da TAG tipoTrib do layout único do TSS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio - NFS-e |
| **Situação/Requisito:** | Documentar o funcionamento da TAG tipoTrib do layout único do TSS |
| **Solução/Implementação:** | A TAG tipoTrib é gerada com o código informado na coluna **Natureza de Operação da NFS-e** (TTRBITMMOV.NATOPERNFSE) da linha do ISS do Item. Caso a nota tenha mais de um item todos deverão ter o mesmo código.    Os códigos aceitos são definidos pelo TSS conforme documentação **<http://tdn.totvs.com.br/pages/releaseview.action?pageId=243641191>** verifique a tag tipotrib.  Exemplo:  • 1 – Isenta de ISS;  • 2 – Não incidência no município;  • 3 – Imune;  • 4 – Exigibilidade Susp. Dec. J.  • 5 – Não tributável;  • 6 – Tributável;  • 7 – Tributável fixo;  • 8 – Tributável S.N;  • 9 – Cancelado;  • 10 – Extraviado.  • 11 – Micro Empreendedor Individual (MEI)  • 12 - Exigibilidade Susp. Proc. A. • 13 – Sem recolhimento • 14 – Devido a outro município  Caso o campo não seja preenchido o processo de montagem do xml irá definir o tipoTrib conforme abaixo:  **Se** Não Existe ISS no nota  **Então** Não Tributável  **Senão** **Se** Tipo Recolhimento ISS **igual** a Isento  **Então** Isento  **Senão** **Se** Tipo Recolhimento ISS **igual** a Imune  **Então** Imune  **Senão** **Se** Tipo Recolhimento ISS **igual** a Deposito Judicial  **Então** Exigibilidade Suspensa por Deposito Judicial  **Senão** **Se** Tipo Recolhimento ISS **igual** a Devido **E** Município da Filial **igual** Vitoria-ES  **Então** Tributável  **Senão** **Se** Regime de ISS da Filial **igual** a Isento  **Então** Isento  **Senão** **Se** Regime de ISS da Filial **igual** a Imune  **Então** Imune  **Senão** **Se** Município de prestação **diferente** do município da Filial  **Então** Não Incidência no município  **Senão** **Se** Filial Optante pelo Simples  **Então** Tributável SN  **Senão** Tributável  Ainda existe a possibilidade do usuário configurar o sistema para que o campo Natureza de Operação do ISS seja preenchido de forma automática, porem utilizando códigos especificos definidos conforme a necessidade. Para isso basta utilizar o **[cadastro de Natureza de Operação do ISS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Opera%C3%A7%C3%A3o%20ISS.aspx)** que está no modulo Fiscal. |
