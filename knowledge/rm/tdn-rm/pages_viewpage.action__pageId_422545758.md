---
content_hash: 7d20935656b95cf225830b53efbb413113488fed570b74305c3c48dea57e3cf8
fetched_at: '2026-06-29T00:09:20.982479+00:00'
page_id: '422545758'
product: rm
source: tdn-rm
title: Pré-requisitos para o uso da NFC-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545758
version: 11
---

Para o correto funcionamento do processo da NFC-e no RM alguns pré-requisitos devem ser atendidos.

* Versão atualizada da Biblioteca RM.
* TOPConnector Monitor e TSS instalados e configurados;

***Observação:*** A configuração do JOB da NFCe no arquivo .ini do servidor do TSS deve ser feita manualmente da seguinte forma:   
Seção do JOB   
\*\_\[NFCE\_WF\]\_\*   
main=NFCEWF

Environment=Nome do Environment Ativação do JOB da NFCe   
\*\_\[ONSTART\]\_\*   
JOBS=NFCE\_WF

* Certificado digital A1 quando for utilizada da integração via TSS;
* Conexão com a Internet;
* TOTVS Gestão de Compras e TOTVS Gestão Fiscal parametrizados.

Como Fazer

* [Instalação e Configuração do TSS](http://tdn.totvs.com.br/pages/releaseview.action?pageId=64652506)
* [Parametrização da Filial (Integração do RM com o TSS)](http://tdn.totvs.com.br/pages/releaseview.action?pageId=66126229)
