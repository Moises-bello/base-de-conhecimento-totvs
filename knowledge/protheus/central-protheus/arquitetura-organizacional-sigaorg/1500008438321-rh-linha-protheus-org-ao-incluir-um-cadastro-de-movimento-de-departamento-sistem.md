---
article_id: 1500008438321
category: Arquitetura Organizacional (SIGAORG)
content_hash: e4542a7a56f167121ee0b416718e4dada0c176dc3edc7830e3ec481fe1c6e7fd
fetched_at: '2026-06-28T22:42:52.939965+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: 'RH - Linha Protheus - ORG - Ao incluir um Cadastro de Movimento de Departamento
  sistema apresenta a mensagem: Movimentação já foi manipulada'
type: support-article
updated_at: '2022-06-06T17:12:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008438321-RH-Linha-Protheus-ORG-Ao-incluir-um-Cadastro-de-Movimento-de-Departamento-sistema-apresenta-a-mensagem-Movimenta%C3%A7%C3%A3o-j%C3%A1-foi-manipulada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min****Dúvida**Ao incluir um Cadastro de Movimento de Departamento via rotina ORGM010 sistema apresenta a mensagem: Movimentação já foi manipulada.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012326522/mceclip0.png)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Arquitetura Organizacional – Todas as versões  
 **Solução**Existe um parâmetro que indica se a aprovação deve ser feita pela rotina de movimentação de departamento. Para conferir o parâmetro basta acessar o configurador e verificar o conteúdo do parâmetro **MV\_APRPOST,** seu conteúdo pode ser**S = Sim; N = Não.**

**![p1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360007943412/p1.jpg)**

Para ter acesso a alteração ou exclusão deve ser configurado o parâmetro MV\_APRPOST=S dessa forma a movimentação de departamentos que forem cadastrados depois poderão ser excluído caso desejado.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos sobre Arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/Artigos%20sobre%20Portal%20Gest%C3%A3o%20Capital%20Humano)
