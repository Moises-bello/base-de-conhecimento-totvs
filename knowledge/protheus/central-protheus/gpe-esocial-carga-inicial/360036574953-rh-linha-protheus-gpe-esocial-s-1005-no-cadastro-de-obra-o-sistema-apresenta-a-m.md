---
article_id: 360036574953
category: GPE - eSocial - Carga Inicial
content_hash: ba45157c13d9d873899df713d36fed473cfc27be028a4792bcc05e5b00390a1b
fetched_at: '2026-06-28T22:45:03.206893+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1005 - No cadastro de Obra o Sistema
  apresenta a mensagem: A Obra não está cadastrada no Complemento de Empresa (F0F).
  Verifique o cadastro antes de realizar a integração'
type: support-article
updated_at: '2026-06-23T18:35:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036574953-RH-Linha-Protheus-GPE-eSocial-S-1005-No-cadastro-de-Obra-o-Sistema-apresenta-a-mensagem-A-Obra-n%C3%A3o-est%C3%A1-cadastrada-no-Complemento-de-Empresa-F0F-Verifique-o-cadastro-antes-de-realizar-a-integra%C3%A7%C3%A3o
---

**Ocorrência**  
No cadastro de Obra o Sistema apresenta a mensagem: A Obra não está cadastrada no Complemento de Empresa (F0F). Verifique o cadastro antes de realizar a integração.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Essa mensagem é apresentada no momento que grava um cadastro de estabelecimento ou centro de custo com os parâmetros do eSocial ativos ou quando tenta realizar a carga de um evento S-1005 e sua causa é falta de preenchimento do Cadastro de complementos de estabelecimentos (F0F).  
  
**Solução**  
Para solucionar a inconsistência você deverá preencher o Cadastro de complementos de estabelecimentos (**FISA137** {**F0F**}), para mais informações [**clique aqui**](https://tdn.totvs.com/pages/viewpage.action?pageId=330137845), nos casos de obras próprias essa informação é obrigatória.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29554889753495)  
  
Para que seja possivel selecionar o codigo de **CNO**, é necessário preencher a rotina **MATA322**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41435501585559)

Se já estiver com os parâmetros do eSocial ativos o Sistema vai enviar o evento ao TAF ao finalizar os cadastros, caso contrário, você pode utilizar a rotina de Carga Inicial do módulo de Gestão de Pessoal (SIGAGPE).  
  
**Artigos relacionados**  
[MP - GPE - eSocial - S-1005/S-1020 - Como enviar informações de Obra cadastrada no SIGAMAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036071454)  
[MP - GPE - eSocial - S-1005/S-1020 - Como Realizar Cadastro de Obras para envio ao eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036072094)  
[MP - GPE - eSocial - S-1005/S-1020 - Como enviar informações de Obra cadastrada no Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036573933)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-1005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822873)  
[Artigos S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051258534)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
