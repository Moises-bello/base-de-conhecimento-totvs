---
article_id: 4410280168983
category: RH - Cálculos
content_hash: 678c7744ef15bf72f79d8543bc086a5027c8565744f1ec2c5e9ada2fbcdef8c1
fetched_at: '2026-06-28T22:44:51.642940+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON - Faltam códigos de Identificadores de Ponto na Tabela
  20 do Configurador
type: support-article
updated_at: '2026-02-11T14:12:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410280168983-RH-Linha-Protheus-PON-Faltam-c%C3%B3digos-de-Identificadores-de-Ponto-na-Tabela-20-do-Configurador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35380677741079) Tempo aproximado para leitura: 00:01:00 min**  
  
**Ocorrência**  
Ao realizar a leitura/apontamento, o sistema emite no *log* a mensagem "**Faltam códigos de Identificadores de Ponto na Tabela 20 do Configurador".**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Ao realizar o processo de [**Leitura e Apontamento das marcações**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-RH-Linha-Protheus-PON-Como-funciona-a-Leitura-e-Apontamento-das-marca%C3%A7%C3%B5es) ou[**Cálculo Mensal**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal), o sistema gera a mensagem abaixo no *log* de ocorrências:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410268952471)

Para resolver esta mensagem, será necessário **atualizar a base com a última Expedição do RH e executar o UPDDISTR** para criação dos novos ID's de Ponto.

Saiba mais sobre o processo de UPDDISTR:  
[Upgrade de Release do Protheus 12](https://tdn.totvs.com/display/public/framework/Upgrade+de+Release+do+Protheus+12)

Após a atualização, acesse a rotina de **Eventos do SIGAPON** para criar os novos eventos e vincular os novos identificadores.

Link para acesso ao pacote RH Expedição:    
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
