---
article_id: 360052702294
category: Encargos
content_hash: c50f72512893dc65ae131c55cc6a6c2e534680ffd6dee172ef6b24103e32952b
fetched_at: '2026-06-28T22:46:53.251983+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Como resolver a inconsistência "Alíquota  Fap inválida. O valor
  deve estar entre 0,5 e 2,00"
type: support-article
updated_at: '2025-03-12T10:07:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052702294-RH-RM-FOP-Como-resolver-a-inconsist%C3%AAncia-Al%C3%ADquota-Fap-inv%C3%A1lida-O-valor-deve-estar-entre-0-5-e-2-00
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:20 min**

**Dúvida**Ao acessar o aplicativo da SEFIP, é verificado que a Alíquota FAP não está parametrizada, gerando o erro "**Alíquota Fap inválida. O valor deve estar entre 0,5 e 2,00**". Como resolver?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que esta inconsistência não seja apresentada, é necessário informar a alíquota FAP diretamente no aplicativo da SEFIP, pois alíquota não é exportada, tendo em vista que no layout da SEFIP não possui campo para receber a informação e até o momento a Caixa não atualizou o seu programa para tal. Segue passo a passo para a conferência das informações que corroboram com a argumentação anterior e orienta o preenchimento.

**Passo 1**No manual de Erro Ação da próprio SEFIP, verificamos que no código 101177 não temos na coluna Registro/Posição nenhuma informação de qual linha e posição essa informação deveria constar, isso porque a mesma é somente digitada no aplicativo da Caixa:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086004474/mceclip0.png)  
  
**Passo 2**Na página 57 do manual da GFIP, é mencionado que esse campo deve ser preenchido, não mencionando a possibilidade de importa-lo:  
 **![](https://totvssuporte.zendesk.com/attachments/token/kazpYUEsJ2TcH76ztrFnWcwCx/?name=inline-767413703.png)****Passo 3**No manual Operacional da SEFIP, página 36, mostra que a informação FAP deve ser preenchida, conforme orientação da própria caixa:  
  
![](https://megasistemas.zendesk.com/hc/pt-br/article_attachments/210283428/Manual_Operacional.jpg)  
  
**Importante:** Em casos de dúvidas, será necessário entrar em contato com o help desk da Caixa Econômica Federal.
