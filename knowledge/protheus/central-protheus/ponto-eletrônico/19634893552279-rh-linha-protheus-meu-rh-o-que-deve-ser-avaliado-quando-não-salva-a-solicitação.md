---
article_id: 19634893552279
category: PONTO ELETRÔNICO
content_hash: 0d94ebae1a710fd258bb539742318f1292a5cc82521751043c0b125c8e8cdf69
fetched_at: '2026-06-28T22:44:36.530077+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que deve ser avaliado quando não salva a solicitação
  de abono
type: support-article
updated_at: '2026-06-22T18:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19634893552279-RH-Linha-Protheus-Meu-RH-O-que-deve-ser-avaliado-quando-n%C3%A3o-salva-a-solicita%C3%A7%C3%A3o-de-abono
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19634877668119) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que deve ser avaliado quando não salva a solicitação de abono  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
No App Meu RH, existe uma rotina onde é possível a **inclusão de uma Solicitação de Abono de Horas ou dias**, para justificar um evento de desconto que foi apontado pelo Ponto Eletrônico.  
  
Nesta solicitação, é possível a **inclusão de um anexo** para justificar o abono das horas ou dia(s).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19634922312727)  
  
Os anexos dos abonos serão registrados na **tabela ACB - Banco de Conhecimento.**  
Esta tabela foi criada pelo *Framework* e, possui um c**ontrole de numeração pelo Configurador**.  
  
Por vezes, o abono com o anexo não é salvo, **pois o Controle de Numeração está incorreto**, gerando uma chave duplicada na tabela ACB, mediante registro no [***console.log*** **do Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751).  
  
Para verificação, sugerimos que analise inicialmente, **o compartilhamento da tabela ACB em seu banco de dados**, para isso, acessar o **módulo Configurador, em Base de Dados > Dicionário > Base Dados**, localizar a tabela ACB e verificar o compartilhamento, **que sugerimos sempre estar como totalmente compartilhada.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19634893527447)  
  
Após, verifique qual o **último registro que a tabela ACB** recebeu a inclusão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19634918017559)  
  
No exemplo acima, o **objeto 00022 foi o último a ser inserido**.  
Com isso, acessar o **Configurador** novamente, e na rotina **Ambiente > Cadastros > Controle de Numeração**, localizar no quadrante superior a tabela ACB:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19634922317719)  
  
Veja que, nesse caso, **o próximo número a ser incluído será o 00023.**  
Neste cenário, temos **o controle de numeração correto**, porém, em casos que o número está inconsistente, **será necessária a intervenção a fim de editar o número próximo a ser incluído.**  
  
Importante frisar que, **o App Meu RH precisará estar sempre atualizado**, tanto o RPO com a expedição contínua semanal do GPE, **quanto os arquivos de Portal Meu RH**, que são expedidos mensalmente, ou no máximo de 20 em 20 dias.  
  
Cabe ressaltar que, a inclusão de um abono pelo Meu RH, será permitida com data início igual ou maior, ao primeiro dia do período de apontamento aberto naquele momento pelo parâmetro MV\_PONMES.  
  
**Importante:**  
[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA), para ter acesso ao pacote de expedição contínua do GPE.  
[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059194334), para saber como coletar os arquivos de portal Meu RH, e como atualizá-los.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
