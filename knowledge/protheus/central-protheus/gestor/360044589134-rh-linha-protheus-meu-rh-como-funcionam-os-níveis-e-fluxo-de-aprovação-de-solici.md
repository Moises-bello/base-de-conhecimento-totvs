---
article_id: 360044589134
category: GESTOR
content_hash: b568d866c8684d2852cc3351afa455c22d099d0eac3067f5443202f22748a171
fetched_at: '2026-06-28T22:44:35.625954+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como funcionam os Níveis e Fluxo de aprovação
  de Solicitações Sem Visão
type: support-article
updated_at: '2026-06-22T18:13:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044589134-RH-Linha-Protheus-MEU-RH-Como-funcionam-os-N%C3%ADveis-e-Fluxo-de-aprova%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%B5es-Sem-Vis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19065409590295)Tempo aproximado para leitura: 00:03:00 min  
  
Dúvida**Como funcionam os Níveis e Fluxo de aprovação de Solicitações Sem Visão  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Conforme informado no artigo a seguir: "**[MP - MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058407953)**", uma das configuração de hierarquia é a **Sem Visão.**  
  
Na configuração **Sem Visão**, o parâmetro **MV\_ORGCFG** deve estar com conteúdo '**0**' (sem aspas).  
  
Desta forma, é obrigatório que sua configuração siga estritamente as orientações indicadas no Boletim Técnico: **[Workflow de solicitações (por estrutura de departamentos)](https://tdn.totvs.com/pages/releaseview.action?pageId=547861194)**Para configurar a hierarquia sem visão deve-se seguir as orientações do documento abaixo, nele é  apresentado uma hierarquia por departamento da seguinte forma:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19068280453655)  
Presidente      → 000000001  
Gerente          → 000000002  
Coordenador  → 000000003  
Líder               → 000000004  
Funcionários   → 000000005  
  
É mostrado também como deve ser preenchido os departamentos criados, **tendo como obrigatório a matricula responsável e o departamento superior** exceto o **ultimo nível da hierarquia que não possui departamento superior.**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19068242821527)  
  
Para mais detalhes segue a documentação abaixo:  
**[RH - Linha Protheus - MEU RH - Como configurar a hierarquia por departamentos (MV\_ORGCFG=0)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623-RH-Linha-Protheus-MEU-RH-Como-configurar-a-hierarquia-por-departamentos-MV-ORGCFG-0-?source=search)**  
  
**IMPORTANTE:**Qualquer configuração diferente do artigo acima, o Sistema perderá a referência no fluxo de aprovação. Abaixo separamos dois artigos com orientações para correção de casos já mapeados: **[MP - MEU RH - Mesmo zerando todas solicitações o sininho do Gestor permanece indicado solicitações pendentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045356294)  
[MP - MEU RH - O que fazer quando as Solicitações não seguem os Níveis ou Fluxo de aprovação desejado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058413613)****Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
