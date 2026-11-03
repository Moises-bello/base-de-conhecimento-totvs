---
article_id: 360037061574
category: RH - Lançamentos
content_hash: 3550b9d3983db0c84ceb8c426d07f4d69dae02f6528b297b2e3dd2bbed33d825
fetched_at: '2026-06-28T22:43:31.188709+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Como excluir verbas em lote que constam nos Lançamentos
  por Funcionários
type: support-article
updated_at: '2025-07-23T17:39:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037061574-RH-Linha-Protheus-GPE-Como-excluir-verbas-em-lote-que-constam-nos-Lan%C3%A7amentos-por-Funcion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521313815) Tempo aproximado para leitura: **00:02:50 min  
  
Dúvida**Como realizar a exclusão de verbas em lote nos Lançamentos por funcionários (tabela RGB) ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**A opção poderá ser executada apenas após a **criação** do grupo de perguntas **(GPEA580).**Para confirmar a existência do grupo de perguntas, acesse o **Configurador** com senha de **administrador** em **Base de Dados > Dicionário > Base de Dados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521320727)**Clique em **Perguntas**, busque pela rotina **GPEA580** e depois clique em **editar**. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238513952279)  
  
As configurações devem estar da seguinte forma:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521329815)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238513957783)**Caso existam divergência, será necessário **atualizar** o **Dicionário de Dados.** Veja sessão **Saiba Mais** para material de apoio, caso necessário.  
  
Após verificar o Grupo de Perguntas, a exclusão em lote poderá ser realizada. Veja exemplo abaixo.Duas matriculas com algumas verbas lançadas e nas duas matriculas as mesmas verbas, nesse exemplos as verbas  151,160 e 285 estão nas duas matriculas, conforme imagem abaixo:

Matrícula **00001**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238513963159)

Matricula **000002**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521350679)  
  
Para realizar a exclusão em lote, ainda na rotina de **Lançamentos Por Funcionário,** clique em **Outras Ações > Excluir em Lote**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521354263)  
  
Preencha os parâmetros de exclusão conforme necessidade da empresa.  
Seguindo o exemplo acima, vamos excluir as verbas **informadas** no Processo **00001,** período **202408** da folha (roteiro **FOL**) referente ao pagamento **01** de **todos os funcionários** que as possuir**.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521356951)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238513987223)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238513989783)  
  
**Importante:** Caso queira excluir apenas algum (uns) código (s) de verba (s) apenas, o campo **Informe as Verbas** deve ser preenchido com seus respectivos códigos, limitando-se a **10** por processo de exclusão.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521364247)

Após o preenchimento dos parâmetros, clique em ok. e ok novamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521366295)

No termino do processo, o Sistema apresentará uma mensagem informando que as verbas foram excluídas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521371159)

Ao selecionar as matrículas que tinham as verbas lançadas e clicar em **Visualizar/ Alterar / Incluir**, podemos ver que os lançamentos existentes antes foram excluídos com êxito.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238514004631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26238521374743)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como atualizar o dicionário de dados (arquivo SXSBRA.TXT) do Protheus 12](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXLby0QxM6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzIxMTgxNTE1OTY3ODk1LVJILUxpbmhhLVByb3RoZXVzLUdQRS1Db21vLWF0dWFsaXphci1vLWRpY2lvbiVDMyVBMXJpby1kZS1kYWRvcy1hcnF1aXZvLVNYU0JSQS1UWFQtZG8tUHJvdGhldXMtMTIGOwhUOg5zZWFyY2hfaWRJIik5YWM0MWYxNC0yYWJjLTQ2NDctYjFhMy00MTA3OTlkNGM0YjEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiNhdHVhbGl6YXIgZGljaW9uw6FyaW8gZGUgZGFkb3MGOwhUOhJyZXN1bHRzX2NvdW50aQI%2BBA%3D%3D--c16abafbde48835a4371bbf3f2f791a35024a9b0)

[RH - Linha Protheus - GPE - Lançamentos por Funcionário Nenhum Roteiro foi definido como Ordinário](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwibmbHRUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBsWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAwMDM2MjkwNy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTGFuJUMzJUE3YW1lbnRvcy1wb3ItRnVuY2lvbiVDMyVBMXJpby1OZW5odW0tUm90ZWlyby1mb2ktZGVmaW5pZG8tY29tby1PcmRpbiVDMyVBMXJpbwY7CFQ6DnNlYXJjaF9pZEkiKWU4MWQ2MjI3LTcxMGMtNGIzZi1hYzk5LTIwYTA3NWFmYzNiZAY7CEY6CXJhbmtpBzoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiImxhbsOnYW1lbnRvcyBwb3IgZnVuY2lvbsOhcmlvBjsIVDoScmVzdWx0c19jb3VudGkC7gM%3D--4493a2a014b1610524d423d799f3ea756099a9ef)

[RH - Linha Protheus - GPE - No lançamento por funcionário é apresentada a mensagem: Não permitida a inclusão de lançamentos para esta verba](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg5PGrUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB6Gh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NjAxNzU5My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtTm8tbGFuJUMzJUE3YW1lbnRvLXBvci1mdW5jaW9uJUMzJUExcmlvLSVDMyVBOS1hcHJlc2VudGFkYS1hLW1lbnNhZ2VtLU4lQzMlQTNvLXBlcm1pdGlkYS1hLWluY2x1cyVDMyVBM28tZGUtbGFuJUMzJUE3YW1lbnRvcy1wYXJhLWVzdGEtdmVyYmEGOwhUOg5zZWFyY2hfaWRJIillODFkNjIyNy03MTBjLTRiM2YtYWM5OS0yMGEwNzVhZmMzYmQGOwhGOglyYW5raQg6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIiJsYW7Dp2FtZW50b3MgcG9yIGZ1bmNpb27DoXJpbwY7CFQ6EnJlc3VsdHNfY291bnRpAu4D--c516346c1a9a2b3748a6d7da5994886f5c1859aa)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
