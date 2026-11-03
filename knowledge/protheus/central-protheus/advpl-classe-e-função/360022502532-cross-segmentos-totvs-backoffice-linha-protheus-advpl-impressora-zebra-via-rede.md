---
article_id: 360022502532
category: ADVPL - Classe e Função
content_hash: 7d4ee7c30215b79a823fc89c31df5647d4b6628ee5d33519bbb41bbcc57ce1f1
fetched_at: '2026-06-28T22:40:20.442585+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Impressora Zebra
  via rede com endereço IP
type: support-article
updated_at: '2022-01-11T22:39:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022502532-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impressora-Zebra-via-rede-com-endere%C3%A7o-IP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**É possível imprimir via rede utilizando a Classe MSCBprinter ou apenas via LPT ou COM\* ?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Como as portas homologadas para impressão térmica são somente Serial(COM) e Paralela(LPT), temos como alternativa paliativa a emulação da porta, que neste exemplo seria via NET USE do Windows.  
Seguem as orientações para configuração:

1º) Instalar a impressora e seus drivers no servidor de impressão.  
2º) Compartilhar a impressora na rede.  
3º) Em cada máquina que enviará a impressão, instalar a impressora que foi compartilhada na rede.  
4º) Na máquina que enviará a impressão, via CMD.exe, mapear a impressora na porta LPT\* utilizando o comando:  
NET USE \* \\ IP \IMPRESSORA  
'\*' é a porta que irá mapear: LPT1, LPT2, COM1, COM2...) Posteriormente testar a impressão das etiquetas passando como porta o nome \* que foi mapeado (ex: LPT1)  
  
Exemplo de código:

```
#Include "Protheus.ch"  
#INCLUDE "TBICONN.CH"   
  
User Function Impressora()  
Local cPorta := "LPT1" // Mapeamento feito através de NET USE  
Local cModelo := "ZEBRA"  
  
MSCBPRINTER(cModelo, cPorta,,10,.F.,,,,,,.F.,)  
  
MSCBCHKSTATUS(.F.)  
  
MSCBBEGIN(1,6)  
MSCBSAY(10,10,"TESTE IMPRESSAO EM REDE", "N","A","040,030")  
MSCBEND()  
  
MSCBCLOSEPRINTER()  
  
Return
```

**Reforçamos que essa solução é paliativa, caso não funcione com determinado modelo de impressora, a equipe ADVPL somente realizará os testes na porta direta, conforme homologado.**
