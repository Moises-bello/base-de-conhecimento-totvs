---
article_id: 16035305685399
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8aeb2dbcd402663c8deb8da036ed45f3e73b6708f8c28ab92b4dc9b30e5b9506
fetched_at: '2026-06-28T22:42:41.037434+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Classificar o excedente de produção
  no APP Minha Produção '
type: support-article
updated_at: '2023-07-18T12:28:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16035305685399-Manufatura-Linha-Protheus-SIGAPCP-Classificar-o-excedente-de-produ%C3%A7%C3%A3o-no-APP-Minha-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035291475223) Tempo aproximado para leitura: **00:01:27 min  
  
Dúvida**Como classificar o **excedente de produção**, como **ganho de produção** ou **produção a maior** através do app minha produção?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Quando é realizado o apontamento de produção maior que o saldo da **OP - Ordem de Produção** através do **app minha produção**, não é exibida a tela para classificação do excedente.  
  
Nesse caso é necessário configurar os parâmetros **MV\_GANHOPR** **- Utilizado para verificar se permite o conceito de Ganho de Produção na inclusão do apontamento de produção** e **MV\_PERCPRM - Percentual da quantidade das ordens de produção qual será permitido apontado a maior** para definir se será **ganho de produção** ou **produção a maior**.  
  
Quando o parâmetro **MV\_GANHOPR** estiver como **.T.**, realizará sempre ganho de produção, independente do conteúdo do parâmetro **MV\_PERCPRM.**Quando o parâmetro **MV\_GANHOPR** estiver como **.F.**, e o parâmetro **MV\_PERCPRM** maior que zero, realizará **produção a maior.  
  
Saiba mais**Para mais detalhes sobre o app minha produção, acesse: [Guia de Uso - Minha Produção.](https://tdn.totvs.com/pages/releaseview.action?pageId=606095034#tudo-sobre-funcionalidades-interfaces-Linha-Protheus)
