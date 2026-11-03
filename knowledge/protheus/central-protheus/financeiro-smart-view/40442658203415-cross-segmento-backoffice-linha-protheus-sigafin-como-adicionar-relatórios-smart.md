---
article_id: 40442658203415
category: Financeiro - Smart View
content_hash: d8c74de6a77010def3037a463b2de3f3ab0b0bf5d20cc75406fd2a3ad68bf197
fetched_at: '2026-06-28T22:37:44.614366+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFIN - Como adicionar relatórios
  SmartView do módulo SIGAFIN ao menu?
type: support-article
updated_at: '2026-05-14T18:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40442658203415-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-adicionar-relat%C3%B3rios-SmartView-do-m%C3%B3dulo-SIGAFIN-ao-menu
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40442669713047) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como posso adicionar novos relatórios SmartView padrão no menu do Financeiro, caso eles não estejam disponíveis de forma nativa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2310

**Solução**  
O boletim abaixo contem os relatórios SmartView do módulo Financeiro, e essa lista será atualizada caso exista novos relatórios a serem publicados.

[Lista de relatórios Smartview Financeiro](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

**Nesta documentação, usaremos o relatório** [Smart View - Retorno CNAB](https://tdn.totvs.com/display/PROT/Smart+View+-+Retorno+CNAB) (Fonte FINSV051) **como exemplo, e abordaremos o processo em etapas.**

Antes dos passos abaixo, valide se o ambiente esta atualizado, se possui o fonte em seu inspetor de Objetos e se possui em seu ambiente as configurações básicas para Smartview, pois isso é muito importante, para saber se você contem os últimos fontes dos relatórios atualizados no acumulado do Financeiro.

[Acumulado Financeiro de acordo sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=531017758)

[*Como efetuar as configurações basicas para Smartview*](https://tdn.totvs.com/x/8WTCMQ)

**1)** Acesso o modulo configurador SIGACFG, e navegue até:**Ambiente>Cadastros>Menu** e selecione o menu **Financeiro** apenas.

Clique ao lado esquerdo em **SIGAFIN** e depois clique em Adicionar, será criada a seleção do menu, maximize para **Consultas>SmarView** conforme print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442669713815)

**2)** Após isso, efetue o processo conforme print abaixo, passo a passo na numerações, colocando o nome do relatório e fontes, conforme boletim do mesmo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442669715479)

**3)** Efetuado as etapas acima, clique em **Gerar**, escreva **SIGAFIN** e depois clique em gerar, confirme a geração,**e salve o backup do menu.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442658188823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442669720087)

Depois clique em sair.

**4)** Após acesse a rotina via menu, efetue login no smartclient, e acesse o módulo 6 **SIGAFIN**, depois em: **Consultas > SmartView > Selecione o relatório recém adicionado**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442669720727)

**5)** Você também pode usar a barra de pesquisa para localizar rotinas/relatórios **através do nome**, ou até mesmo através do código fonte da rotina/relatório caso saiba, exemplo o **FINSV051**, assim ele vai abrir automaticamente o relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40442658194199)

**Pontos importantes:**

**Esse processo é o mesmo para relatórios de outros módulos?**

Podemos informar que o processo pode ser similar, mas pode existir particularidades, devido a cada módulo possuir uma regra de inclusões no menu, então o recomendado é que valide a documentação de inclusão do módulo.

**Mas e para adicionar relatórios customizados?**

O processo é quase o mesmo, onde a diferença seria no item **2)** da sessão, ao invés de selecionar "Tipo **Função Protheus**", você selecionaria "**SmartView**" e na sessão "**Programa**" ao clicar nos 3 pontinhos, será aberto uma lista dos relatórios adicionado no **SmartView**, para que você relacione no menu do Protheus.  
Caso tenha dificuldades com o processo de inclusão para relatórios customizados, ou apresente erros e demais, sugerimos contatar nosso time de **Protheus Framework** para melhores orientações do processo de relatórios customizados a serem incluídos no sistema.

Saiba mais:

[Smart View - Financeiro](https://tdn.totvs.com/display/public/PROT/Smart+View+-+Financeiro)

[Amarração Protheus x Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=708098869)

[É possível criar relatórios customizados no Smart View?](https://tdn.totvs.com/pages/releaseview.action?pageId=905612950)
