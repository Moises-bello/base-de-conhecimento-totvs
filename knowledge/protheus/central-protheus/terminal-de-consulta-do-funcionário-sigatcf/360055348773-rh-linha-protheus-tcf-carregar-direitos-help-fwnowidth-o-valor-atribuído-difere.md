---
article_id: 360055348773
category: Terminal de Consulta do Funcionário (SIGATCF)
content_hash: 7021863d8a201422c3a36848e2f3c6958b308879aa3f707c33c80c3c619f082c
fetched_at: '2026-06-28T22:43:01.521089+00:00'
product: protheus
section_id: 206971507
source: central-protheus
title: 'RH - Linha Protheus -  TCF - Carregar Direitos Help: FWNOWIDTH: O valor atribuído
  difere do tamanho do campo Descrição'
type: support-article
updated_at: '2023-05-12T18:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055348773-RH-Linha-Protheus-TCF-Carregar-Direitos-Help-FWNOWIDTH-O-valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Descri%C3%A7%C3%A3o
---

**Dúvida**O que verificar, no módulo 18 **(SIGATCF)** **Terminal de Consulta do Funcionário**, ao carregar Direitos na rotina **Atualizações > Configurações > Usuários > Genéricos**, ocorre erro: Help: FWNOWIDTH: O valor atribuído difere do tamanho do campo (Descrição).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089484954/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Terminal de Consulta do Funcionário – Todas as versões  
  
**Solução**Divergência de tamanho nos campos **AI6\_CODUSU (Código Usuário)**, **AI6\_WEBSRV (Código Web Service)** e **AI6\_NOMEWS (Descrição do Web Service)**.  
Os campos citados (**AI6\_CODUSU, AI6\_WEBSRV e AI6\_NOMEWS**) cada um tem um tamanho e devem seguir o padrão do sistema.   
  
É necessário atualizar o ambiente e executar UPDDISTR com o ultimo acumulado do RH. Para realizar o download consulte o artigo abaixo.  
  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
  
**Saiba Mais**  
[Artigos Terminal de Consulta do Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971507-RH-Terminal-de-Consulta-do-Funcion%C3%A1rio-)  
[Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
