---
article_id: 360047331074
category: GESTOR
content_hash: 87010e8cd702cb9993ab1da2d18c09aa14e5a766b8a8b5989d8711313b84de68
fetched_at: '2026-06-28T22:44:35.612536+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como funcionam os Níveis e Fluxo de aprovação
  de Solicitações Com Visão
type: support-article
updated_at: '2026-06-22T19:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047331074-RH-Linha-Protheus-MEU-RH-Como-funcionam-os-N%C3%ADveis-e-Fluxo-de-aprova%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%B5es-Com-Vis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24765253912343) Tempo aproximado para leitura: 00:08:00 min  
  
Dúvida**Como funcionam os Níveis e Fluxo de aprovação de Solicitações Com Visão?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Conforme informado no artigo a seguir "**[Como funcionam os Níveis e Fluxo de aprovação de Solicitações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058407953)**", uma das configuração de hierarquia é a **Com Visão Organizacional.**Na configuração **Com Visão**, o parâmetro **MV\_ORGCFG** deve estar com conteúdo '**1**' ou '**2**' (sem aspas).  
  
Para acessar o parâmetro **MV\_ORGCFG**é necessário seguir o seguinte caminho no Configurador - (**SIGACFG**).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24788706861975)  
Parâmetro:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24788706871703)  
  
**MV\_ORGCFG** = Configura o modo de uso do modulo Arquitetura Organizacional.   
**0**=Não utiliza;  
**1**=Utiliza com controle de Postos;  
**2**=Utiliza sem controle de Postos;  
  
Caso seja utilizado como '**1**' (sem aspas), o sistema valida a necessidade de vincular a todos os funcionários um **Departamento** e **Posto de trabalho**conforme o Boletim técnico:  
**[RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV\_ORGCFG=1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062313494-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-1?source=search)**  
Caso seja utilizado como '**2**' (sem aspas), o sistema valida somente a necessidade de amarrar um departamento, não obrigando o preenchido de um posto.  
  
Exemplo de estrutura utilizando o valor **2**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24788692930327)  
  
Desta forma, é obrigatório que sua configuração siga estritamente as orientações indicadas no Boletim Técnico: **[Hierarquias - Níveis de fluxo de aprovação de Solicitações](https://tdn.totvs.com/pages/viewpage.action?pageId=500300689)** e a documentação sobre o Cadastro de Visão: **[RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV\_ORGCFG=2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051101414-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-2?source=search)** (elas foram criadas para o **Portal GCH**, mas funciona da mesma forma para o **MEU RH**).  
  
**IMPORTANTE:** Qualquer configuração diferente do artigo acima vai fazer o Sistema se perder no fluxo de aprovação. Abaixo separamos dois artigos com orientações para correção de casos mapeados: **-> [Mesmo zerando todas solicitações o sininho do Gestor permanece indicado solicitações pendentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045356294)  
-> [O que fazer quando as Solicitações não seguem os Níveis ou Fluxo de aprovação desejado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058413613)**Abaixo há um vídeo de um evento "Tira Dúvidas", em que é demonstrado como realizar o cadastro de uma hierarquia com estas configurações:  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
