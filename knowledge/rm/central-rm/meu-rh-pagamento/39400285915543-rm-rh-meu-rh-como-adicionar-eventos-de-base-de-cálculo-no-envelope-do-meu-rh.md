---
article_id: 39400285915543
category: Meu RH - Pagamento
content_hash: 400bcb89300297ba59a334aeb43019a5bdfc24e53bc2d11ae4942eafd229822f
fetched_at: '2026-06-28T22:47:33.823900+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RM - RH - Meu RH - Como adicionar eventos de Base de Cálculo no Envelope do
  Meu RH?
type: support-article
updated_at: '2026-04-06T10:50:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39400285915543-RM-RH-Meu-RH-Como-adicionar-eventos-de-Base-de-C%C3%A1lculo-no-Envelope-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39400285877527) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possível disponibilizar a exibição dos eventos de base de cálculo no envelope do Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
No Meu RH, os eventos de base de cálculo são ocultados por padrão. No entanto, é possível customizar o relatório de download do envelope de pagamento para que esses eventos também sejam exibidos.

A seguir, exemplificamos o passo a passo para realizar essa configuração:  
  
1. Realize o download do relatório **"Envelope Pgto Portal Personalizado"** através do [**TOTVS Compartilhamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento), selecionando a versão compatível com o seu banco de dados (SQL Server ou Oracle).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39417580666903)

2. Acesse o Menu **Gestão** > **RM Reports** e localize o relatório importado. Selecione, e clique em **Processos** > **Editar Estrutura**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39417555037079)

3. Na tela de edição da estrutura do relatório, em **Início** selecione a opção **"Editar Sentença".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39417580672919)

Localize a consulta SQL com o código  "**RELPPFFINANC**" e clique em **Editar**. Remova a linha abaixo que contém o filtro de eventos de base e clique em salvar.

`AND PEVENTO.PROVDESCBASE <> 'B'`

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39400255431319)

4. Na **Grade de Propriedades** do relatório, selecione a *"**Expressão4**"*. No ícone de **dados**, clique no editor da expressão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39400255432471)

Atualize a expressão lógica alterando a condição `PROVDESC = 'P'`para`PROVDESC <> 'D'`

* Antes: `String(If(Relatório.PROVDESC = 'P', Relatório.VALOR, ''))`
* Depois:  `String(If(Relatório.PROVDESC <> 'D', Relatório.VALOR, ''))`

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39400285884311)

Após realizar estas alterações na estrutura do relatório, clique na opção **Inicio** e em seguida em **Salvar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39417886200343)

5. Acesse na **Folha de pagamento** > **Configurações** > **Parametrizador** > **RM Portal**. Edite o Quiosque dos colaboradores e na etapa **Demonstrativo de Pagamento**, marque a flag **"Relatório RM Reports"** e vincule o relatório customizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39417555041559)

Após a configuração, ao realizar o download do envelope de pagamento no Meu RH, os eventos de base de cálculo também serão exibidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39400285885975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39400285888919)

**Importante:**A estrutura exemplo deste relatório customizado está disponível nos itens anexados e deve ser utilizada apenas como guia.

Se durante o processo de customização surgirem dificuldades, como erros ou resultados diferentes do esperado, recomendamos acionar a **consultoria** especializada da TOTVS (serviço tarifado) para apoio, pois o **suporte padrão não contempla a análise de estruturas customizadas.**
