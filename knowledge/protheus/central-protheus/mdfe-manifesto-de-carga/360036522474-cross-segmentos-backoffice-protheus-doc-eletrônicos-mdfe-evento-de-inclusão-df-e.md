---
article_id: 360036522474
category: MDFe - Manifesto de Carga
content_hash: 538855fb5cd6c813ccc489732d6486379ecca9635e9fedeb3fe95aa0c4ad109d
fetched_at: '2026-06-28T22:40:08.283296+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Evento de
  Inclusão DF-e para envio da tag Carrega Posterior
type: support-article
updated_at: '2025-06-10T18:48:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036522474-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Evento-de-Inclus%C3%A3o-DF-e-para-envio-da-tag-Carrega-Posterior
---

**Dúvida**Como gerar Evento de Inclusão DF-e para envio da tag Carrega Posterior ?

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

* **IMPORTANTE:**

Os fontes devem estar atualizados conforme o link abaixo:

[MP - MDFE - Manifesto Eletrônico MOC versão 3.00A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026589553)

1- Ao acessar a rotina de MDF-e, será apresentado no filtro as novas opções referente a **tag de Carrega Posterior:**

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-4_9-35-32.png?version=1&modificationDate=1567600532857&api=v2)

2- Caso necessário refazer o filtro, selecione a opção é no botão de **Outras Ações / Filtro**, que mostra a tela principal para um novo filtro.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-4_9-41-7.png?version=1&modificationDate=1567600867480&api=v2)

3- Na inclusão do Manifesto, seleciona no campo **Carrega Posterior igual a 1**. Esta opção permitirá que o veículo com tipo próprio poderá ser gerado sem a seleção do documento eletrônico.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-4-21.png?version=1&modificationDate=1567443861853&api=v2)

4- Antes de encerrar a inclusão do MDF-e, lembre-se de informar na aba de Carregamento/Percurso, o **Município de Carregamento**.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-5-31.png?version=1&modificationDate=1567443931360&api=v2)

5- Ao clicar na opção Salvar, deverá informar o Município Descarregamento

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-6-48.png?version=1&modificationDate=1567444008103&api=v2)

6- Ao confirmar a inclusão do MDF-e, deve seguir o processo para transmissão do documento que é efetuado atualmente.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-7-27.png?version=1&modificationDate=1567444047657&api=v2)

7- Foi incluído campo de **Legenda** para este evento, conforme descrição abaixo:

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-7-47.png?version=1&modificationDate=1567444067280&api=v2)

**Observação:** Caso não seja utilizado a opção Carrega Posterior, o processo de inclusão de MDF-e segue o que é efetuado atualmente.

8- Após transmitir e autorizar a MDF-e, acesse a opção "**Gerenciar MDFe**",  opção  **Eventos**

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-9-33.png?version=1&modificationDate=1567444173963&api=v2)

9- Para esta rotina é possível a inclusão do vínculo da NF-e, referente a situação posterior ao MDF-e.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-10-4.png?version=1&modificationDate=1567444204920&api=v2)

10- Na opção de **Seleção de Eventos** estarão disponibilizados os eventos de Incluir DF-e e Inclusão Condutor, os campos da rotina serão adaptados de acordo com a opção selecionada.

 Os campos de **Número MDF-e**, **Série MDF-e**, **UF Carregamento**, **UF Descarregamento**, **Veículo**, **Status** e **Carrega Posterior**são informações detalhadas do MDF-e selecionado.

Na seção **Parâmetro do Evento** estarão os campos disponíveis para seleção das NF-es para o vínculo ao MDF-e:

**Dt. Inicial** e **Dt. Final**: Informar o período onde foram emitidos os documentos eletrônicos. Ex.: 01/03/2019 a 31/08/2019.

**Nota Inicial** e **Nota Final**: Informa a numeração da nota inicial e final dos documento eletrônicos. Ex.: 000000255 a 00000289 ou branco a ZZZZZZZZZ.

**Série**: Informar a série dos documentos eletrônicos. Ex.: 001;241 ou 562 (Poderá utilizar qualquer tipo de separador **- / \* ; ,**).

Após colocar os dados acima para busca, clique no botão **Buscar NF-e**.

Na opção **Replica Município** é possível informar o município de Descarregamento para os documentos eletrônicos (NF-e) selecionados. Caso este campo seja preenchidos assim que o campo **Cod. Município Descarregamento** for informado e pressionado o batão **Add Município**, os documentos eletrônicos selecionados utilizaram este código.

**Incluir Condutor**

Nesta opção também sera possível a transmissão do evento de '**Inclusão de Condutor** "

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-11-9.png?version=1&modificationDate=1567444269213&api=v2)

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-11-29.png?version=1&modificationDate=1567444289447&api=v2)

Na opção de **Seleção de Eventos** estarão disponibilizados os eventos de Incluir DF-e e Inclusão Condutor, os campos da rotina serão adaptados de acordo com a opção selecionada.

Os campos de **Número MDF-e**, **Série MDF-e**, **UF Carregamento**, **UF Descarregamento**, **Veículo**, **Status** e **Carrega Posterior** são informações detalhadas do MDF-e selecionado.

Na seção **Parâmetro do Evento** estarão os campos para**Inclusão do Condutor**:

**Código**: Informar o código do condutor  (Cadastrado Rotina de Motorista - tabela DA4 através do Cadastro de Veículo - tabela DA3).

**Nome do Condutor** e **CPF** serão mostrados de acordo com o código selecionado.

**Importante: O processo efetuado para o transmitir o evento de Inclusão do Condutor não foi alterado nesta nova rotina.**

**Observação:**

A tela de  Inclusão de condutor  antiga sera descontinuada, porém ainda esta válida.

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-11-55.png?version=1&modificationDate=1567444315843&api=v2)

![](https://tdn.totvs.com/download/attachments/513430091/image2019-9-2_14-12-18.png?version=1&modificationDate=1567444338307&api=v2)
