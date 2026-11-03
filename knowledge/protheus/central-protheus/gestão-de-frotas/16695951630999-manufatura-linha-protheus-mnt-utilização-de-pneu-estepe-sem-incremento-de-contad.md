---
article_id: 16695951630999
category: Gestão de Frotas
content_hash: c27c9a3403f7ffad30e14120194f48c9acb7d9a61ad7e4bf0aa7907a4c03c993
fetched_at: '2026-06-28T22:42:39.606109+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Utilização de Pneu Estepe Sem Incremento
  de Contador
type: support-article
updated_at: '2024-01-10T17:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16695951630999-Manufatura-Linha-Protheus-MNT-Utiliza%C3%A7%C3%A3o-de-Pneu-Estepe-Sem-Incremento-de-Contador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16695958346903) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Qual configuração é necessária para que o **Pneu de Estepe** não receba o incremento de **Contador**?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas (SIGAGFR) - Todas as versões  
  
**Solução**Para que o **Pneu de Estepe** não receba a informação de **Contador**, é necessário o cadastro da **Estrutura Padrão - MNTA095**, no caminho: **Atualizações / Controle de Oficina / Bens / Estrutura Padrão**.  
Neste cadastro será necessário informar a **Família** e **Modelo** do **Bem Pai da Estrutura**, em seguida informar a **Família** do **Pneu Estepe** e a **Localização** do Pneu Estepe, e selecionar a opção **Bem Ativo** igual a **Não**, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16695703770775)

**Saiba mais**  
Para informações a respeito da atualização de contador em abastecimento, veja o artigo do *link* [Manufatura - Linha Protheus - MNT - Atualização do contador de bens de uma estrutura no abastecimento do pai](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055864154)
