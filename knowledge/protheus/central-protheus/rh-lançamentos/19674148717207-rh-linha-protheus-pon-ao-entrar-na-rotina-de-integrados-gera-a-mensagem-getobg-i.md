---
article_id: 19674148717207
category: RH - Lançamentos
content_hash: b2caa2a4f83b87f150c5260e719fc90828709062855173e069b53bf8ecdc304f
fetched_at: '2026-06-28T22:44:46.771003+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: 'RH - Linha Protheus - PON - Ao entrar na rotina de integrados gera a mensagem:
  GETOBG "Informe o campo Detalhe CENTRO CUSTO"'
type: support-article
updated_at: '2025-10-27T14:46:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19674148717207-RH-Linha-Protheus-PON-Ao-entrar-na-rotina-de-integrados-gera-a-mensagem-GETOBG-Informe-o-campo-Detalhe-CENTRO-CUSTO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19674117987479) Tempo aproximado para leitura: **00:01:00 min******Dúvida****Ao entrar na rotina de **Integrados (PONA280),em Atualizações>Lançamentos>Integrados,** é gerada a mensagem: **GETOBG "Informe o campo Detalhe CENTRO CUSTO"  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947692055)  
  
Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**A mensagem ocorre quando alguma informação das propriedades dos campos **P8\_CC, PC\_CC e PK\_CC** estão incorretas**.**  
 **Solução**Para correção, será necessário verificar as propriedades dos campos no padrão, conforme abaixo:  
No **Configurador (SIGACFG)**, acesse o dicionário de dados em **Base de Dados > Dicionário > Base de Dados**, abra o dicionário da empresa e filtre as tabelas **SP8, SPC e SPK**.  
Garanta que os campos estejam conforme o padrão abaixo:

**P8\_CC**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908288279)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947698839)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908292631)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947704343)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908296855)  
  
**PC\_CC  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908300311)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947709335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947711767)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947714199)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947717271)**  
**PK\_CC:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908310423)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908314007)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908908317463)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947727383)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35908947728919)  
  
**Saiba mais**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
