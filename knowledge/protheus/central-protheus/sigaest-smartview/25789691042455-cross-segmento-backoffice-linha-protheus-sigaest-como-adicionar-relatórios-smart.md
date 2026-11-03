---
article_id: 25789691042455
category: SIGAEST - SMARTVIEW
content_hash: 69346e0a32d1f02617a71676cd0106b0ec747bf6beff275217bceb3dcf5faec2
fetched_at: '2026-06-28T22:38:47.240624+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como adicionar relatórios
  SmartView do módulo SIGAEST ao menu?
type: support-article
updated_at: '2025-12-22T15:27:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25789691042455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-adicionar-relat%C3%B3rios-SmartView-do-m%C3%B3dulo-SIGAEST-ao-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25789679653399) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como posso adicionar novos relatórios SmartView padrão no menu de Estoque/Custos, caso eles não estejam disponíveis de forma nativa?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2310

**Solução**

O boletim abaixo contem os relatórios SmartView do módulo de Estoque/Custos, e essa lista será atualizada caso exista novos relatórios a serem publicados.

[Lista de relatórios SmartView Estoque Custos](https://tdn.totvs.com/x/M8LrL)

**Nesta documentação, usaremos o relatório SmartView – Termo de Retirada (ESTSV026) como exemplo, e abordaremos o processo em 11 etapas.**

Antes dos passos abaixo, valide se o ambiente esta atualizado, se possui o fonte em seu inspetor de Objetos e se possui em seu ambiente as configurações basicas para Smartview, pois isso é muito importante, para saber se voce contem os ultimos fontes dos relatórios atualizados no acumulado do estoque.

[Acumulado estoque custos de acordo sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=522000602)

[*Como efetuar as configurações basicas para Smartview*](https://tdn.totvs.com/x/8WTCMQ)  
  
**Caso deseje, Disponibilizamos um vídeo que demonstra esse passo a passo explicado nesta documentação:**

**1)** Acesso o modulo configurador SIGACFG, e navegue até: **Ambiente>Cadastros>Menu** e selecione o menu **SIGAEST** apenas.

Clique ao lado esquerdo em **SIGAEST** e depois clique em Adicionar, será criada a seleção do menu, maximize para **Consultas>SmarView** conforme print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791168317719)

**2)** Após isso, efetue o processo conforme print abaixo, passo a passo na numerações, colocando o nome do relatório e fontes, conforme boletim do mesmo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791204223383)

**3)** Efetuado as etapas acima, clique em **Gerar**, escreva **SIGAEST** e depois clique em gerar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791204226071)

**4)** Confirme a geração, **e salve o backup do menu:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791168322327)

**5)** Depois clique em sair:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936274199)

**Sugerimos sempre reiniciar os serviços após essa tarefa.**

**6)** Após acesse a rotina via menu, efetue login no smartclient, e acesse o módulo **4 SIGAEST**, depois em: **Consultas > SmartView > Selecione o relatório recém-adicionado**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791872641943)

**7)** Voce também pode usar a barra de pesquisa para localizar rotinas/relatórios **através do nome**, ou até mesmo através do codigo fonte da rotina/relatório caso saiba, **ESTSV026**, assim ele vai abrir automaticamente o relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936277271)

**8)** Ao abrir o relatório selecione a visão desejada, e filtre de acordo orientações do boletim do mesmo, aqui vamos usar o exemplo em tela, clique em **imprimir**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936277783)

**9)** Filtre os dados desejados e basta clicar em **Enviar**, que será exibido as informações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936278807)

**10)** A visão é responsiva, ou seja voce pode reconfigurar com outros dados e clicar em **enviar**, **que sera refeito o relatório com as novas parametrizações, sem a necessidade de sair e entrar novamente.**

Voce já terá disponível a opção de **imprimir** ou baixar o relatório em **pdf**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936280471)

**11)** Caso desejar em outro formato, basta clicar no **filtro**, e selecionar o formato disponível e após clicar em exportar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25791936281623)

Pronto, assim voce concluir o processo de como incluir um relatório SmartView padrão na rotina.

**Esse processo é o mesmo para relatórios de outros módulos?**

Podemos informar que o processo pode ser o mesmo, mas pode existir particularidades, devido a cada módulo possuir uma regra de inclusões no menu, então o recomendado é que valide a documentação de inclusão do módulo.

**Mas e para adicionar relatórios customizados?**

O processo é quase o mesmo, onde a diferença seria no item **2)** da sessão, ao invés de selecionar "Tipo **Função Protheus**", você selecionaria "**SmartView**" e na sessão "**Programa**" ao clicar nos 3 pontinhos, será aberto uma lista dos relatórios adicionado no **SmartView**, para que você relacione no menu do Protheus.  
Caso tenha dificuldades com o processo de inclusão para relatórios customizados, ou apresente erros e demais, sugerimos contatar nosso time de **Protheus Framework** para melhores orientações do processo de relatórios customizados a serem incluídos no sistema.

**Saiba mais:**

*[Relação de SmartViews do Estoque (TDN)](https://tdn.totvs.com/x/pwKQLg)*

[*Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/16108365627287-SIGAEST-SMARTVIEW)
