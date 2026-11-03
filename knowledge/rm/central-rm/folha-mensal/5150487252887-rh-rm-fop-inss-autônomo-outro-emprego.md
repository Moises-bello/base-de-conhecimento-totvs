---
article_id: 5150487252887
category: Folha Mensal
content_hash: 7c7ecfa52cb7862b2b1b296c886a38162521dcb76b9e314394aeeec22b58d286
fetched_at: '2026-06-28T22:46:59.219339+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - INSS Autônomo Outro Emprego
type: support-article
updated_at: '2025-01-22T19:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5150487252887-RH-RM-FOP-INSS-Aut%C3%B4nomo-Outro-Emprego
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29427686775191)Tempo aproximado para leitura: **00:07:00 min  
  
D****úvida**Como parametrizar o sistema para calcular INSS Autônomo Outro Emprego?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O produto padrão não contempla o cálculo de INSS para autônomos e diretores de forma automática, tendo em vista que, o cálculo é muito abrangente e não há uma legislação clara e objetiva para tal. O dificulta a implementação no produto padrão e também a montagem de uma fórmula que atenda todos os casos.  
  
Conforme entendimentos, segue uma sugestão de fórmula mais simples para o cálculo de INSS como desejado. É importante ressaltar que esse é um exemplo básico para quem for informar a Base de INSS do Autônomo do Outro emprego ou informar o INSS do Autônomo descontado do outro emprego. Para isso sugerimos que sejam seguidos os seguintes passos de preferência em uma ambiente de homologação e após validado replicar em ambiente de produção.  
  
Segue abaixo passo a passo exemplificativo:  
  
1. Em primeiro momento, será necessário criar a tabela de cálculo em: **Cálculos | Tabelas de Cálculos.**  
  
**--> Código da Tabela:** 0003  
  
![](https://totvssuporte.zendesk.com/attachments/token/sPllh3F1KBt5BnIRJXfv69jOO/?name=inline-648215021.png)  
  
2. Logo, cadastre os valores da Tabela de INSS. É importante ressaltar que, os valores informados na imagem abaixo são fictícios e devem ser alterados conforme tabela e valores disponíveis nas plataformas legais.  
  
![](https://totvssuporte.zendesk.com/attachments/token/ikBymKIJT3MUo5tIGHBaLFSGz/?name=inline-1868253288.png)  
  
**Importante**  
- O escopo do produto é voltado para o regime CLT, e o autônomo não é regido pela CLT, [art. 7º, CLT,](http://www.sato.adm.br/guiadp/BcoCLT/banco_de_dados_clt_art_007.htm), mas por uma legislação especial. Assim, os direitos são específicos e limitados.  
  
- O sistema permite o cadastro pelo sistema, fazendo todo o tratamento através de fórmulas. Caso a fórmula disponibilizada não atenda a necessidade da empresa, você poderá realizar as alterações necessárias. Nas categorias 721, 722 e 723, o cálculo não deve ser realizado pelo Código de Cálculo 3 – I.N.S.S, o cálculo deve ser feito através de fórmula, devido ao uso da tabela de INSS.  
  
- A fórmula demonstrada como exemplo neste artigo é apenas um modelo e caso haja necessidade de adaptações a TOTVS dispõe do serviço de consultoria via telefone ou in loco. Trata-se de atendimento personalizado capaz de atender o cliente de forma diferenciada, além de contar com um escopo mais amplo. Os analistas atuam diretamente no seu ambiente via acesso remoto.  
  
**CÓDIGO: EVT0260**

1. Criar a seguinte fórmula:

DECL TOTAL;  
SETVAR (TOTAL, C('0046') + C('9022'));  
T('0003' , TOTAL) - C('9021')  
  
0046 – Evento da remuneração do autônomo na empresa  
9022 – Evento da remuneração do autônomo outro emprego  
9021 – Evento de INSS descontado no outro emprego  
0003 – Tabela utilizada para cálculo  
TOTAL será a soma da remuneração na empresa e no outro emprego  
Joga-se este TOTAL na tabela criada no item 1  
  
Esta fórmula deve ser informada no evento que tenha o CC85- INSS Calculado pelo Usuário e com uma prioridade maior.  
  
Informar na movimentação do autônomo a Base de INSS Outro Emprego ou o INSS descontado no outro emprego. A fórmula acima irá calcular 11% de toda a base, limitando-se o desconto ao teto.   
  
![](https://totvssuporte.zendesk.com/attachments/token/YhkbHqP8jmNYDhgcth2wVh5NE/?name=inline-1333562350.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/qaKgX2HPFlYEJh1KWhVT2PS5T/?name=inline1767778961.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/TYlgKXzkfSNKJnhQ31Ut8vbgF/?name=inline-279283112.png)  
  
**Saiba Mais**  
[RH - RM - FOP - Cálculo INSS e IRRF para Autônomos e Diretores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412995898519-RH-RM-FOP-C%C3%A1lculo-INSS-e-IRRF-para-Aut%C3%B4nomos-e-Diretores)  
[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RM-FOP-Fun%C3%A7%C3%B5es-de-Formula-de-calculo-Folha-de-Pagamento-RM-Labore-?source=search)
