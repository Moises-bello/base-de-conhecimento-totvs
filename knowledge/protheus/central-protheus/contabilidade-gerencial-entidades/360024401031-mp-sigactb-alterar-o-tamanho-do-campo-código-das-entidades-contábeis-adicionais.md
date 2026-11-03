---
article_id: 360024401031
category: Contabilidade Gerencial - Entidades
content_hash: 565a337362ed056dbc96de699cf29adac75eff47e58ab8ba77fe044c96e25f5b
fetched_at: '2026-06-28T22:40:49.792249+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: MP - SIGACTB - Alterar o tamanho do campo código das entidades contábeis adicionais
type: support-article
updated_at: '2021-04-28T14:47:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais
---

**Dúvida**Como faço para alterar o **tamanho dos campos código das entidades contábeis adicionais**??

**Ambiente**Protheus - Contabilidade Gerencial - 12.1.17  
  
  
**Solução**

Para alterar o tamanho do código das entidades adicionais, deve-se utilizar o **grupo de campos da entidade adicional**, assim quando o cliente alterar através da tabela **SXG(grupo de campos)**, este irá replicar o tamanho desejado para os campos da entidade adicional em todas as tabelas que utilizam e possuem vinculo com o grupo.

1-Para alterar, acesse o **Módulo Configurador > Base de Dados > Dicionário > Base de Dados**, após acessar a rotina selecione o grupo de campos conforme imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022393571/mceclip0.png)

2-Selecione o grupo pertencente a entidade adicional desejada e altere:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022393731/mceclip1.png)

3-Será apresentada uma tela para alteração do tamanho das entidades, escolha o tamanho que esteja entre o máximo e mínimo estipulado e salve:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022400112/mceclip2.png)

4-Após confirmar a alteração, grave estas através da opção Salvar e Avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022394071/mceclip3.png)

5-Siga avançando nos próximos passos de confirmação da gravação, após a atualização os campos que utilizam essa entidade adicional estarão conforme o alterado.

**\*Sugerimos que realize um backup da sua base antes de realizar o procedimento.**

* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema  
    
  Ao realizar alteração dos campos
* altere para  20 as entidade ("Centro de Custo", "Item Contábil" e "Classe Valor") "Salvar "
* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
* altere para  50 a conta contabil  "Salvar "
* Veja se a alteração do tamanho de grupo de campos esta  [REFLETINDO PARA TODAS AS TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050034853-MP-SIGACTB-AO-REALIZAR-ALTERA%C3%87%C3%83O-NO-TAMANHO-DE-GRUPO-DE-CAMPOS-CONFIGURAR-N%C3%83O-ESTA-REFLETINDO-PARA-TODAS-AS-TABELAS?source=search)do sistema
