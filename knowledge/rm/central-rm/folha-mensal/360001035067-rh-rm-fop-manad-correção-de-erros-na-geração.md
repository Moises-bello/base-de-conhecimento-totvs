---
article_id: 360001035067
category: Folha Mensal
content_hash: e3abbe340aa6779df0a812ef64f421e29d670aa0bc2610f6337fe43784529845
fetched_at: '2026-06-28T22:47:00.344329+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - MANAD: Correção de erros na geração'
type: support-article
updated_at: '2024-10-18T15:31:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001035067-RH-RM-FOP-MANAD-Corre%C3%A7%C3%A3o-de-erros-na-gera%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:20 min  
  
Ocorrência**Na geração do MANAD há três parâmetros que deverão seguir as orientação de parametrização, com pena de ocorrerem erros na validação do arquivo via SVA. Os erros são retornados conforme abaixo:  
  
-Base de Cálculo da Prev. Social está divergente da soma das rubricas classificadas como como 1, 2;  
-Rubrica informada (PROV\_DESC='0') não pode ser classificada com IND\_BASE\_PS=1,2,3;  
-Não foi localizado registro de remuneração (K250) do trabalhador na competência;  
-Base de Cálculo do IRRF está divergente da soma das rubricas classificadas como 1 e 2.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Estes erros ocorrem, pois a parametrização na geração do MANAD está incorreta ou existem inconsistências no cadastro do evento e/ou envelope do funcionário.  
  
**Solução**Para solucionar esta ocorrência acesse a rotina do MANAD em **"Folha Mensal | MANAD"**, e marque os parâmetros conforme abaixo:  
  
1. O parâmetro **"Zerar valor de bases negativas no registro K250"** deverá ser DESMARCADO na aba "Parâmetros Globais".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004095092/mceclip3.png)  
  
2. Na segunda aba, Opções de Exportação, em "Eventos tipo base (Indicação de Provento/Desconto)", deverá MARCAR a opção **"Exportar como Provento/Desconto"**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004101891/mceclip1.png)  
  
3. Nas aba de Seleção de Coligadas, edite a coligada que deverá ser gerada e MARQUE o parâmetro **"Considera como 1 os indices de base 9 no registro K300"**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360004094692/mceclip2.png)  
  
Após aplicação da orientação acima, caso ainda retorne os erros na validação do SVA, deverá ser avaliado a linha do erro juntamente com o Layout do MANAD para análise. Provavelmente existem eventos com incidências incorretas ou inconsistência no envelope do funcionário. Caso ainda assim não se obtenha sucesso, favor abrir um ticket para Folha de Pagamento.
