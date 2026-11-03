---
article_id: 10092401547415
category: RH - Integração de Titulo
content_hash: 4cc369c053fe87d113d507c9aea685b6fa40fb22f9fbfde2db44d65d756c1b51
fetched_at: '2026-06-28T22:43:36.169846+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como bloquear ou liberar a visualização de determinados
  títulos na rotina Manutenção de Títulos
type: support-article
updated_at: '2025-07-15T19:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10092401547415-RH-Linha-Protheus-GPE-Como-bloquear-ou-liberar-a-visualiza%C3%A7%C3%A3o-de-determinados-t%C3%ADtulos-na-rotina-Manuten%C3%A7%C3%A3o-de-T%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33490594772119) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como bloquear ou liberar a visualização de determinados títulos na rotina Manutenção de Títulos?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12..1.25  
  
**Solução**Para liberar ou bloquear acessos na rotina Manutenção de títulos, deve ser feita a parametrização na rotina Controle de Acessos de Usuários.  
  
Para isso, siga o passo a passo abaixo:

1. Entre na rotina **Controle de Acessos de Usuários** pelo caminho **>Atualizações >Cadastros >Controle de Acessos de Usuários**;  
  
2. Clique em **Incluir**;  
  
3. Informe o **usuário** ou **grupo** que deseja parametrizar, no exemplo abaixo farei por usuário:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091225883287)  
  
4. No campo **Arquivo**, selecione a tabela **RC1-Movimentação de títulos** e clique em **Salvar**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091309434263)  
  
5. No campo **Filtro Brows**, crie um filtro para liberação ou bloqueio de visualização, no exemplo abaixo irei liberar a visualização apenas dos títulos de código 004:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091472757783)  
  
6. Clique em **Adicionar** e **OK:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091529372951)  
  
7. Clique em **Salvar**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091799542295)  
  
8. Na rotina de Manutenção de títulos o usuário parametrizado só consegue visualizar os títulos 004:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10091915832599)

**Saiba Mais:**

[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
