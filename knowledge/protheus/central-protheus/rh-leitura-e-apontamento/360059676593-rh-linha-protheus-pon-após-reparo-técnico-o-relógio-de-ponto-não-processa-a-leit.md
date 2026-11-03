---
article_id: 360059676593
category: RH - Leitura e Apontamento
content_hash: 26bdace0ba4ae5e41c12f71c3fe4c40da03c96fd70c214431e4fefe56b15fefb
fetched_at: '2026-06-28T22:44:45.906413+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Após reparo técnico, o Relógio de Ponto não processa
  a leitura das marcações
type: support-article
updated_at: '2025-12-08T19:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059676593-RH-Linha-Protheus-PON-Ap%C3%B3s-reparo-t%C3%A9cnico-o-Rel%C3%B3gio-de-Ponto-n%C3%A3o-processa-a-leitura-das-marca%C3%A7%C3%B5es
---

**Ocorrência**  
Após reparo técnico, o Relógio de Ponto não processa a leitura das marcações.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
Quando um REP passa por manutenção, o controle de **NSR é reiniciado,** o que faz com que o **SIGAPON** não realize a leitura das marcações e as mesmas não não gravadas, pois todos os NSRs lidos no passado para aquele relógio, são gravados em tabelas do módulo.  
  
**Solução**  
Para solucionar esta situação, foi adicionada a opção **Reiniciar NSR** no menu **Outras Ações** ao alterar o cadastro de um relógio.  
  
Para isto, acesse o **módulo 16-Ponto Eletrônico: atualizações>cadastro do ponto>relógios**,   
filtre o código do relógio, após alterar, clique em **Outras Ações>Reiniciar NSR.**  
Esta opção estará disponível somente para relógios com **Tipo de Arquivo T (TArquivos ASCII)** e que sejam **Incrementais.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35468499801879)  
  
Após clicar nesta opção, o sistema irá criar um novo registro na **tabela de Cabeçalho de Pré-leitura - RFB**, indicando que o NSR lido deste relógio foi reiniciado e deixando o campo de controle **RFB\_IDORG=000000000**.  
  
**IMPORTANTE!**

**Essa opção somente deve ser utilizada em casos específicos, onde o controle de NSR do REP foi reinicializado.**

**Saiba Mais:**  
[Reiniciar NSR de relógios REP](https://tdn.totvs.com/pages/releaseview.action?pageId=754961213)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
