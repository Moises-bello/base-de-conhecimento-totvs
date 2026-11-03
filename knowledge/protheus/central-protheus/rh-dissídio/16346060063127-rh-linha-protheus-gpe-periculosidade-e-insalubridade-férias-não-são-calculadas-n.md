---
article_id: 16346060063127
category: RH - Dissídio
content_hash: 6d1489b48f17097218a846fec402ef39a353e4b8feabd405c31082fbd3229460
fetched_at: '2026-06-28T22:43:43.416263+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Periculosidade e insalubridade férias não são calculadas
  no dissídio retroativo
type: support-article
updated_at: '2025-11-04T12:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16346060063127-RH-Linha-Protheus-GPE-Periculosidade-e-insalubridade-f%C3%A9rias-n%C3%A3o-s%C3%A3o-calculadas-no-diss%C3%ADdio-retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16346051083287) Tempo aproximado para leitura: **00:01:30 min** **Ocorrência**Periculosidade e insalubridade férias não são calculadas no dissídio retroativo.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões.  
  
**Causa**  
Falta de informação no histórico cadastro funcionário.  
  
**Solução**

1) Verifique na rotina de Histórico alterações cadastrais (tabela SR9), se consta alterações gravadas indevidamente ou fora da ordem cronológica:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16345077612951)  
  
Para conseguir inserir a informação, retorne a data base do sistema para a data exata da alteração, e ajuste as informações para adicional de periculosidade e salve a informação:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16345917654935)

2. Caso os dados do funcionário estejam corretos ou já tenham sido corrigidos , sugerimos verificar também se o sindicato vinculado a esse funcionário tem a aba de adicional configurada, nesse exemplo estamos utilizando o adicional de insalubridade:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19993818662423)

Para este cadastro também existe a gravação do histórico de alterações (tabela RG4) , que será o preponderante no processamento da rotina de dissídio.  
  
Acesse Atualizações -> Cadastros -> Sindicatos -> Visualizar -> Outras Ações -> Histórico

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19993623173015)

**Saiba Mais:**  
[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
