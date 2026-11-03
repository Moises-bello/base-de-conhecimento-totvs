---
article_id: 13232008158231
category: eSocial - Parametrizador
content_hash: c63cc32ef964b78480aa08b72f9bf02eef8c46abc0a280b756f5c6ed648fef37
fetched_at: '2026-06-28T22:47:06.289831+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na geração XML: A seção ''xxxx'' está relacionado
  nos parâmetros do eSocial Seções a desconsiderar e/ou Registros Inativos a Desconsiderar
  não podendo ser utilizada'
type: support-article
updated_at: '2024-12-18T15:56:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13232008158231-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-XML-A-se%C3%A7%C3%A3o-xxxx-est%C3%A1-relacionado-nos-par%C3%A2metros-do-eSocial-Se%C3%A7%C3%B5es-a-desconsiderar-e-ou-Registros-Inativos-a-Desconsiderar-n%C3%A3o-podendo-ser-utilizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24160800041879) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML apresenta a mensagem **Erro na validação do campo 'nrInsc': A seção 'xxxx' está relacionado nos parâmetros do eSocial (Seções a desconsiderar e/ou Registros Inativos a Desconsiderar) não podendo ser utilizada.**  
**Avalie a necessidade da utilização desta seção e ajuste a parametrização.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro é devido a seção constar incluída como desconsideradas nos parâmetros do eSocial (Seções a desconsiderar e/ou Registros Inativos a Desconsiderar) ou a Seção encontra-se desativada.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse, **Configurações | Parametrizador | eSocial | Seção a Desconsiderar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13231560894487)

1.2. Veja se consta alguma **seção** e **avalie a necessidade da permanência** na aba e se enquadra nas **regras**.

1.3. Após a exclusão da **seção** no parametrizador, regere o XML.  
  
2. **Verifique se a seção está inativa**. Selecione a seção e clique em **Editar;**

2.1. Acesse a aba **Identificação**, e desmarque a flag de **Desativada.** Abaixo um exemplo da parametrização:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13231941327383)

2.2. Após, regere o XML.

**Saiba mais**  
Para mais informações sobre as regras acesse:

* [Seções a Desconsiderar](https://tdn.totvs.com/pages/viewpage.action?pageId=452719499)
