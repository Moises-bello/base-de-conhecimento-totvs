---
article_id: 9929757356567
category: MDT - PPP
content_hash: fdaef92090929a01c644f04e29338ec0b4fdea581668ef68976e4fdce93f9f2b
fetched_at: '2026-06-28T22:44:22.272425+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual a funcionalidade do parâmetro MV_PPPDTRI
type: support-article
updated_at: '2024-07-04T12:29:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9929757356567-RH-Linha-Protheus-MDT-Qual-a-funcionalidade-do-par%C3%A2metro-MV-PPPDTRI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24649903528343) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a funcionalidade do parâmetro MV\_PPPDTRI?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**O parâmetro **MV\_PPPDTRI** tem reflexo na impressão do PPP (MDTR700) no item **15** - **Exposição a Fatores de Riscos** com a impressão do item **15.1**. É através dele que define se o tempo de exposição ao fator de risco sem proteção será apresentada no PPP ou não.  
  
**Exemplo 1**- Apresentar no PPP apenas o período onde o funcionário estava exposto com proteção:  
  
   Data de Admissão do Funcionário:01/01/2001  
   Data da Avaliação do Risco:01/01/2019  
   Data da Entrega do EPI ao Funcionário:15/01/2019  
   Período informado no parâmetro: 30  
  
Analisando o cenário acima:

O funcionário iniciou a exposição ao risco no dia 01/01/2019 e recebeu a entrega do EPI apenas no dia 15/01/2019, ficando 14 dias exposto ao risco sem proteção. Porém, como o período do parâmetro estava como 30 dias, na impressão do PPP o sistema apresenta apenas o período no qual ele estava exposto e com proteção, e não o período no qual ele estava sem a proteção.

![](https://tdn.totvs.com/download/attachments/498446038/image2019-6-25_17-21-6.png?version=1&modificationDate=1561494384387&api=v2)  
  
**Exemplo 2**- Apresentar no PPP todo o período de exposição do funcionário ao risco:  
  
  Data de Admissão do Funcionário:01/01/2001  
  Data da Avaliação do Risco:01/01/2019  
  Data da Entrega do EPI ao Funcionário:15/01/2019  
  Período informado no parâmetro: 10  
  
Analisando o cenário acima:

O funcionário iniciou a exposição ao risco no dia 01/01/2019 e recebeu a entrega do EPI apenas no dia 15/01/2019, ficando 14 dias exposto ao risco sem proteção. O que mudou do Exemplo 1, é que o período informado não abrange o período da entrega do EPI, ou seja, o PPP apresentará duas datas de exposição, sendo a primeira, onde o funcionário estava exposto ao risco sem a proteção do EPI e a segunda data onde ele passou a fazer uso do EPI.

![](https://tdn.totvs.com/download/attachments/498446038/image2019-6-25_17-25-39.png?version=1&modificationDate=1561494384177&api=v2)  
  
Importante: **MV\_PPPDTRI** - Quantidade de dias de tolerância que o funcionário poderá ficar sem receber o EPI, a partir do inicio de exposição a um agente de risco. **Conteúdo padrão é 30**.  
  
**Saiba Mais**[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos sobre PPP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945654-MDT-PPP)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
