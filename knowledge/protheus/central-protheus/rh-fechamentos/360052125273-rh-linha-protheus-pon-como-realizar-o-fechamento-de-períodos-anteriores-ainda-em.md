---
article_id: 360052125273
category: RH - Fechamentos
content_hash: fa99eb0c194e0dcb1d7d9a1b52e102f6c5fd59f1993b7f423d288aa95d76c13a
fetched_at: '2026-06-28T22:44:48.883604+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como realizar o fechamento de períodos anteriores
  ainda em aberto
type: support-article
updated_at: '2026-02-12T11:50:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052125273-RH-Linha-Protheus-PON-Como-realizar-o-fechamento-de-per%C3%ADodos-anteriores-ainda-em-aberto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31908747644311) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como realizar o fechamento de períodos anteriores que ainda constam em aberto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
No modulo do Ponto Eletrônico, existem dois parâmetros que controlam o período de apontamento em aberto, que são:  
- **MV\_PAPONTA** - deve ser preenchido com o dia inicial/final do período, por exemplo: 01/31, 26/25.  
- **MV\_PONMES** - deve ser preenchido com o período completo que está aberto, por exemplo 01/05/2025 á 31/05/2025.  
  
Sendo assim, é possível alterar os parâmetros para retroagir as datas para períodos anteriores que ainda estejam abertos. Acessar a rotina em **Atualizações >** **Cadastro de Ponto > Período de Apontamento**, e clicar **Outras Ações - Modificar Período - Dia Inicial/Final** deve ser inserida a informação dos dias início/fim do período que será utilizado para preenchimento do parâmetro **MV\_PAPONTA**.

Neste exemplo, supondo que os períodos são dos meses completos, deve ser informado 01/31 (mesmo nos casos onde o mês tenha 30, 29 ou 28 dias) e clique em Salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31908739762711)  
  
  
Na próxima tela, deve ser informado o **último dia** do período de apontamento que precisa ser retroagido para conseguir realizar o fechado. E nesse exemplo, supondo que o período seja o mês de Janeiro/2025, deve ser informado ultimo dia do período 31/01/2025:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31908739764887)  
  
  
  
Será exibido um help em tela informando que o período foi aberto, então basta clicar em Fechar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31908747651735)  
  
  
O próximo passo é **retroagir** a data base do sistema para o último dia do período de apontamento que está aberto e será fechado, executar a rotina de **Fechamento Mensal** em **Miscelânea > Fechamentos> Mensal.** Ao acessar a rotina será exibido quais filiais e seus respectivos períodos serão fechados.

Caso você trabalhe com o Fechamento exclusivo por filial, poderá selecionar apenas uma filial a ser fechada,  clicando em **Outras Ações > Parâmetros**, caso contrário, todas as filais demonstradas na tela serão fechadas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31908739766423)  
  
Ao concluir a operação, se não existirem marcações ímpares que precisem de tratamento, automaticamente o finalizar o processo do fechamento abrirá o próximo período, no caso do exemplo, de 01/02/2025 a 28/02/2025.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31908747655575)  
  
**Importante:** O próprio Sistema entenderá meses de 30, 29 ou 28 dias, não será necessário alterar os parâmetros, porém orientamos que confira as datas do período antes de efetuar a primeira Leitura/Apontamento.  
Os períodos que serão fechados não poderão estar cadastrados na rotina de Período de Apontamento com bolinha de cor verde, pois isso significa que indevidamente utilizou o botão de **"Incluir"** para criar o registro (mais detalhes podem ser acessados [nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)).   
Se existirem registros, será necessário deletá-los posicionando sobre o registro em questão e clicando em Outras Ações > Excluir, permanecendo apenas com o último período realmente fechado pelo Sistema, com bolinha de cor vermelha.  
  
**Saiba mais:**[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
