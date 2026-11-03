---
article_id: 360055966693
category: RH - Períodos de Apontamento
content_hash: 5a9ac6155d62a52524ec2a2ba866f4db4d40fb829bf4f8a50cb275f20f25d47f
fetched_at: '2026-06-28T22:44:45.118677+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Conteúdo correto dos campos Responsável Fechamento
  - PO_RESPONS e Flag Fechamento - PO_FLAGFEC
type: support-article
updated_at: '2025-07-29T18:39:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055966693-RH-Linha-Protheus-PON-Conte%C3%BAdo-correto-dos-campos-Respons%C3%A1vel-Fechamento-PO-RESPONS-e-Flag-Fechamento-PO-FLAGFEC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33800654785175) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Conteúdo correto dos campos Responsáveis pelo Fechamento Mensal - **PO\_RESPONS** e **PO\_FLAGFEC**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O conteúdo correto gravado nesses campos, contidos na tabela SPO são:  
- **PO\_RESPONS**: deve estar preenchido com **S** **(SISTEMA)**, quando ocorre o Fechamento Mensal.  
Se este campo estiver como **U (USUÁRIO)**, indica que a linha foi criada pelo usuário de forma manual. O **botão de Incluir** foi criado destinado para clientes que estão migrando seu ambiente de outro sistema e deseja subir os períodos retroativos a implantação do PROTHEUS, para se manter um histórico. Por este motivo o **botão de Incluir deve ser utilizado com cautela**, pois uma vez este período na SPO o sistema validará as tabelas de acumulados/históricos de períodos fechados;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30088410133399)  
- **PO\_FLAGFEC**: será sempre preenchido com **0 (Fechado)**, visto que nessa tabela só deve existir registros de períodos já fechados.   
  
  
**Saiba Mais**  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
