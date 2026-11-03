---
content_hash: b7f81b8b3e3a7fd5ea1cc31ba9ad0d7af36a920c501d8b89f31f9bf78bad2bbc
fetched_at: '2026-06-29T00:11:22.352215+00:00'
page_id: '701680326'
product: rm
source: tdn-rm
title: Planilhas.Net
type: documentation
url: https://tdn.totvs.com/display/LRM/Planilhas.Net
version: 1
---

# Limitações da Planilha Excel

---

     A Planilha.Net Excel é um recurso do RM que utiliza a planilha do Microsoft Office Excel para que o usuário possa trabalhar com os dados do sistema integrados com essa planilha. A disponibilidade do seu uso requer que o usuário tenha uma licença do pacote Office. Por se tratar de uma integração com um recurso de terceiros, o uso dessa planilha pode apresentar algumas limitações conforme informado abaixo. Ressalta-se que a planilha RM está disponível para ser utilizada pelo usuário em vez da Planilha.Net Excel e assim evitar essas limitações.

false

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

Click e conheça as lmitações...falseConsulta SQL em Célula Mesclada

Evite adicionar consultas SQL em células mescladas, pois é uma operação conflitante por causa da manipulação de dados feita pelo Excel. Caso adicione, muito provavelmente o Excel começará a mostrar o seguinte erro nas aberturas de arquivos e durante o uso da planilha:

O que acontece é que o Excel não consegue manipular de forma efetiva dados contidos em células mescladas, e como a **Consulta SQL** se trata exatamente de uma manipulação de dados, acontece estes conflitos.

Este **NÃO** se trata de um erro do **RM**, mas sim do **Excel**, por causa dos conflitos de dados em células mescladas. Dessa forma, a recomendação da fabricante do Excel (Microsoft) é desfazer a mesclagem das células que possuem manipulação de dados. Logo, desfazer a mesclagem de células que contém **Consultas SQL**embutidas.

Por conta das inconsistências geradas pela manipulação de dados em células mescladas, **NÃO** recomendamos que se utilize mesclagem de células.

falsePincel de Formatação

          Para cada instância da Planilha.Net Excel é criado um processo isolado. Portanto, alguns recursos próprios do Excel como o pincel de formatação funcionará apenas para planilha corrente. Desse modo, não é possível copiar a formatação de uma planilha e colar em outra.

falseProgramas com Versões Distintas do Office

         Conforme documentado pela Microsoft a utilização de aplicativos, em versões distintas do Office, podem causam problemas de funcionamento e integrações no SharePoint, Interop, Vsto entre outras. Qualquer aplicativo do pacote office como; Lync, OneNote, OneDrive, Skype, etc. pode originar o problema caso esteja em versões distintas do pacote Office instalado.

Por exemplo; em um ambiente temos instalado o Office 2013 e o Skype for Bussiness 2016. Desta forma as funcionalidades do sistema ficarão comprometidas e poderão deixar de funcionar corretamente.

Para solucionar o problema, desinstale o aplicativo com versão diferente do Office. Se o aplicativo for de uso necessário instale-o novamente, porém na mesma versão do pacote do Office instalado na máquina.

Referência:  
<https://docs.microsoft.com/en-us/deployoffice/install-different-office-visio-and-project-versions-on-the-same-computer>

<https://support.office.com/en-us/article/Install-and-use-different-versions-of-Office-on-the-same-PC-6ebb44ce-18a3-43f9-a187-b78c513788bf>

false

**Bloqueio de célula ou planilha**

         Informamos que planilha ou células bloqueadas ***impedem recálculos*** de suas células. Respeitando assim o processo padrão do funcionamento da planilha de excel.

false

**Exportação da Planilha por dentro do Excel**

A planilha **.Net Excel** utiliza toda infraestrutura do **Excel** onde, o RM não faz nenhuma **alteração/modificação** na forma que o Excel exporta o seus objetos, mesmo após abrir a planilha através do RM.

Caso a planilha seja exportada para outros tipos de arquivos como **CSV e TXT.** e não for possível visualizar os dados pelo fato deles estarem serializados, recomentamos exportar para um XLSX ou CSV e abrir o arquivo **direto no Excel e exporta-lo novamente.**

Ex:  Arquivo exportado para TXT onde o **Excel serializou** as informações.

 ***Veja os principais conteúdos::***
