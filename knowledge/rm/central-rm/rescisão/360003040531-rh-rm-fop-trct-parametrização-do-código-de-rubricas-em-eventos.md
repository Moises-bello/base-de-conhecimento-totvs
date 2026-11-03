---
article_id: 360003040531
category: Rescisão
content_hash: f8468282c362681a390cc15c8d83dcd4a187ec1d3a410a8acc444ded04c3409c
fetched_at: '2026-06-28T22:46:55.445211+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - TRCT: parametrização do código de rubricas em eventos'
type: support-article
updated_at: '2024-06-17T15:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003040531-RH-RM-FOP-TRCT-parametriza%C3%A7%C3%A3o-do-c%C3%B3digo-de-rubricas-em-eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24103638869527)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como parametrizar o sistema para pagamento nas rubricas do Termo de Rescisão de Contrato de Trabalho e definir quais códigos de rubrica utilizar dentro do evento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para realizar a parametrização das rubricas no TRCT, três passos deverão ser realizados, conforme abaixo:  
  
1. Cadastro das rubricas na tabela dinâmica **Homologrub.** Para isso, acesse: **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas** e procure pela tabela ***Homologrub***. Nesta tabela serão cadastradas todas rubricas necessárias para geração do TRCT.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014458669335)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014541188247)  
  
2. Associação das rubricas aos eventos do sistema. Para isso, acesse: **Administração de Pessoal | Eventos | Eventos**, aplique o filtro desejado e edite o evento que deseja parametrizar. Na aba **Identificação**, campo **Código Rubrica**, informe a rubrica desejada, conforme criado no passo 1. Importante ressaltar que os códigos de rubrica associados aos eventos são uma definição que partirá do usuário.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014505630231)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014561990295)  
  
3. Associação das rubricas aos campos do TRCT. Logo, acesse: **Rescisão | TRCT | Portaria 1621/2010,** marque o parâmetro **Alterar Rubricas** e avance.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014565389719)  
  
Na tela a seguir será demonstrada a lista com todos os campos disponíveis no TRCT. Informe a mesma rubrica informada no cadastrado do evento, no campo específico onde deseja que a rubrica seja gerada no TRCT. Ou seja, a mesma rubrica deverá ser informada no cadastro de evento e no campo especifico do TRCT. Veja no print abaixo a rubrica 001- Salário Fixo, que foi informada no campo 70 do TRCT.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014617758231)  
  
Avance e continue a geração normal do TRCT. Lembrando que, caso queira informar as rubricas nos campos de desconto do TRCT, você deverá fazer na tela seguinte, conforme abaixo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9014618846615)  
  
**Importante**  
Essa documentação é orientativa no sentido de dar dicas sobre o processos de cadastramento e  os tipos de rubricas, porém não define quais deverão ser usadas, pois tal tratativa  é de responsabilidade de cada empresa determinar quais as rubricas utilizar.  
  
**Saiba mais**  
Para maiores informações sobre quais rubricas utilizar em quais campos ou para maiores informações sobre o TRCT, [CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=42042615#:~:text=Na%20gera%C3%A7%C3%A3o%20do%20TRCT%2C%20para,ter%20relacionada%20sua%20respectiva%20rubrica.).
