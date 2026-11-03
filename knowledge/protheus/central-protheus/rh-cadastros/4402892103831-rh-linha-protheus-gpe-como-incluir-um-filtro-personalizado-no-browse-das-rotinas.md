---
article_id: 4402892103831
category: RH - Cadastros
content_hash: 23fef7f7fb3369fb9e543918459d1c607e6562b6e1e3b4a74f31adef7838c2ff
fetched_at: '2026-06-28T22:43:25.894462+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir um filtro personalizado no browse
  das rotinas do Gestão de Pessoal pelo Controle de Acesso de Usuários
type: support-article
updated_at: '2026-06-25T10:55:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402892103831-RH-Linha-Protheus-GPE-Como-incluir-um-filtro-personalizado-no-browse-das-rotinas-do-Gest%C3%A3o-de-Pessoal-pelo-Controle-de-Acesso-de-Usu%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41477825157015) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como realizar a inclusão de **Filtros Personalizados nos*****browse*** das rotinas do Gestão de Pessoal?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
As rotinas do Gestão de Pessoal não são todas desenvolvidas no modelo de dados MVC e nem possuem Pontos de Entrada disponíveis na montagem dos filtros do ***browse***, portanto existe a rotina **GPEA270**, **Controle de Acesso de Usuários**, onde é possível incluir filtros customizados para cada usuário ou Grupo de Usuários especificamente.  
  
Exemplo:  
**1.**O filtro pode ser incluído para um Grupo ou para um Usuário específico, preenchendo os campos "**Grupo Usuari**" ou "**ID Usuario**":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34523268155031)  
  
**2.**O campo **"Arquivo"** é referente à qual tabela o filtro irá ser efetuado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34523268156823)  
  
**3.** O campo "**Filtro Brows**" permite a inclusão de fórmulas para realizar o Filtro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34523268160023)

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action;jsessionid=B53643127B4E2F7BEFBF2A2D359DEA4B?pageId=235569727)
