---
article_id: 36609324575639
category: SIGAEST - MOVIMENTAÇÕES
content_hash: aa7bb08180bbdf45bacd59eab63173d0650e3c6323bd0ca78baf41c29261ec52
fetched_at: '2026-06-28T22:38:53.999662+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - É possível efetuar
  endereçamento automático no Armazém de Processo (MV_LOCPROC)?
type: support-article
updated_at: '2025-12-05T23:00:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36609324575639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-efetuar-endere%C3%A7amento-autom%C3%A1tico-no-Armaz%C3%A9m-de-Processo-MV-LOCPROC
---

No Protheus padrão, não há funcionalidade de endereçamento automático no Armazém de Processo (MV\_LOCPROC). Porém, especificamente para as funcionalidades do módulo Automação Coleta de Dados (SIGAACD), pode-se usar o parâmetro MV\_ENDPROC para definir um Endereço Padrão, que o sistema considera automaticamente nas movimentações do Armazém de Processo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36609319521303) Tempo aproximado para leitura: **00:03:20 min**  
  
**Dúvida**

É possível efetuar **endereçamento automático** no Armazém de Processo (MV\_LOCPROC)? Existe algum parâmetro para realizar esse procedimento?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Atualmente, para o Protheus padrão no **Armazém de Processo (MV\_LOCPROC)**, ***não existe essa funcionalidade***. Existe apenas para os processos do módulo Automação Coleta de Dados (SIGAACD). como indicado [nesse link](https://tdn.totvs.com/x/GCQEN) com o parâmetro MV\_ENDPROC. Para esse cenário pode se utilizar o parametro MV\_ENDPROC e definir o endereço padrão do armazém de processo.

Para o SIGAACD utilizar o parâmetro **MV\_ENDPROC**, que permite definir o **endereçamento padrão do Armazém de Processo**.

Ao habilitar o parâmetro e configurar o endereço desejado, o sistema passa a considerar essa informação automaticamente durante as movimentações do armazém de processo.

Exemplo passo a passo abaixo:

**MV\_LOCPROC =** **99**

**ENDEREÇO CADASTRADO NO ARMAZÉM 99 =** **PADRAO**

**MV\_ENDPROC =** **PADRAO****99** **<- Indicar o Endereço desejado e em seguida o Armazém de Processo**

![MV_LOCPROC.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36649289839767)![MV_LOCPROC 02.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36649289841431)![MV_LOCPROC 03.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36649289846039)

**Observações:** Como o processo não existe para o módulo padrão, recomendamos seguir com a abertura de uma Sugestão de Melhoria no produto através de nossa Central Colaborativa. Veja abaixo as instruções:

A sugestão de melhoria no produto deve ser incluída na [**Central Colaborativa TOTVS**,](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics) localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
   
Para conhecer mais sobre as suas **funcionalidades**clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS).  
Você pode acompanhar as suas **sugestões**e **comentários**clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**

***Saiba mais:***

[*Clique aqui e acesse mais artigos sobre Movimentação no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Como utilizar produto com apropriação indireta?](https://tdn.totvs.com/pages/viewpage.action?pageId=235592220)
