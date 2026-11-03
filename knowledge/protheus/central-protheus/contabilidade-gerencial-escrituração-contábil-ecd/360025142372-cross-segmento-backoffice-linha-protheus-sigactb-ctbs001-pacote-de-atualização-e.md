---
article_id: 360025142372
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 3c83467667e6ceb2de563eded6f2982a92c710c1fd95cc96feca98ed4cf3ed11
fetched_at: '2026-06-28T22:40:44.271967+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Pacote de
  atualização e como realizar a atualização da ECD 2026 (leiaute 9)
type: support-article
updated_at: '2026-03-16T13:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECD-2026-leiaute-9
---

Para atualizar a ECD (leiaute 9) no Protheus 12, mantenha o sistema com as últimas atualizações do portal, baixe os artefatos do pacote backoffice, crie a pasta leiaute9 em System e descompacte os arquivos XML nela. Aplique as procedures de atualização, copie arquivos para Systemload e execute o UPDDISTR. A entrega para 2026 terá atualização do manual, mas sem impacto para entregas de 2025.

**Dúvida:**  
Como realizar a atualização da ECD? (leiaute 9)

**Ambiente:**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial- CTBS001 - A partir da versão 12

**Solução:**

Para a entrega da ECD em 2026, haverá uma atualização do Manual. Contudo, não haverá impactos para aqueles que já realizaram ou estão em processo de preparação para a entrega da escrituração referente ao ano-calendário de 2025, permitindo que os clientes continuem a gerar o arquivo utilizando o leiaute adotado nas entregas a partir de 2021 (leiaute 9).  
<http://sped.rfb.gov.br/arquivo/show/7990>

Com isso, uma vez que esteja com as últimas atualizações liberadas no portal, já está preparado para gerar o arquivo da ECD

**Passo 1** - Recomendamos efetuar a atualização com as últimas liberações do portal. Para efetuar o procedimento, consulte os passos de atualização em [Atualização básica do Protheus 12.](https://tdn.totvs.com/pages/viewpage.action?pageId=271651871)  
  
Atualizações Pacote acumulado e artefatos:

* [Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
* [Pacote LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)
* [Pacote DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)
* [Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)
* [Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)

**Passo 2** - Baixar os artefatos de atualização disponíveis no pacote backoffice: [**Pacote Backoffice expedição continua**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777#issues-17).   
Este pacote contém:

Arquivo "**Config.ZIP**" contem os arquivos abaixo:

* Criar dentro da pasta ***System***a pasta **leiaute 9**, conforme a documentação: [Pasta do leiaute para geração do arquivo texto](https://tdn.totvs.com/pages/releaseview.action?pageId=536725577)
* Baixar os arquivos **XML** e descompactar na pasta leiaute9: [Arquivos XML](https://tdn.totvs.com/pages/releaseview.action?pageId=235331339)
* Aplicar Procedure responsáveis pela atualização de saldos (Ex: **p12\_01.sps**) Para mais detalhes veja [Atualização de Proceduras](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)
* Os arquivo **ECD.CH** e **ECF.CH** são de uso interno do sistema e não precisam ser copiado para seu ambiente.

**Passo 3** - Copiar os arquivos abaixo para a pasta ***Systemload*** (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e cópia do arquivo novo)

**hlpdfeng.txt**

**hlpdfpor.txt**

**hlpdfspa.txt**

**sdfbra.txt**

**Passo 4** - Realizar a execução do [**UPDDISTR**](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)em seu ambiente  
  
Atenção: A não atualização do ambiente conforme procedimentos descritos acarretará erros na execução do processo.

**Saiba Mais**

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD/ECF - Relatório de Checklist para geração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008351187)
* [Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - ECD Pré-requisitos para entrega](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291)
* [Pagina Centralizadora ECD (Documentações e Atualizações centralizadas)?](https://tdn.totvs.com/display/public/PROT/ECD)
* [Videos How To ECD](https://tdn.totvs.com/pages/releaseview.action?pageId=758499600)
