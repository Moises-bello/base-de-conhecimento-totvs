---
article_id: 28456340302999
category: Financeiro
content_hash: 82a98f1c5b94553932e7d40888969f5900b5b4c1978d22d302c6bc794c655aaf
fetched_at: '2026-06-28T22:38:03.141087+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - PDF grava
  com zero KB de tamanho ou não abre o PDF ao utilizar a user Function BaixaBoleto()
  para download de boletos utilizando a classe BankBillsService
type: support-article
updated_at: '2024-12-11T20:05:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28456340302999-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-PDF-grava-com-zero-KB-de-tamanho-ou-n%C3%A3o-abre-o-PDF-ao-utilizar-a-user-Function-BaixaBoleto-para-download-de-boletos-utilizando-a-classe-BankBillsService
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28456340230935) Tempo aproximado para leitura: **00:15:00 min****Dúvida**FINA713 - PDF grava com zero KB de tamanho ou não abre o PDF ao utilizar a user Function BaixaBoleto() para download de boletos utilizando a classe BankBillsService  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - A partir da 12.1.2210  
  
**Solução:**

Ao utilizar o ponto de entrada que está na documentação abaixo:

[Download de boletos utilizando a classe BankBillsService](https://tdn.totvs.com/display/public/PROT/Download+de+boletos+utilizando+a+classe+BankBillsService)

Deveria criar um arquivo com a extensão \*.PDF no diretório \protheus\_data\spool\boletos\01\\*.pdf

E esse arquivo deve ter um tamanho superior a 1kb e abrir

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28456340232855)

Caso esse arquivo esteja sendo criado menor que 1kb logo esse arquivo não vai abrir e apresentar erro ou no ponto de entrada a variável

cBase64

 esteja sendo criada vazia

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28456340250007)

Será necessário fazer download do arquivo **printer.exe** e atualizar esse arquivo tanto no smartclient do servidor como da estação que esteja sendo executado o smartclient local.

Não esqueça de efetuar um backup do arquivo antes da atualização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28456279981591)

Sempre faça primeiramente em uma base de teste

[**Para Linux:**](https://tdn.totvs.com/display/tec/TOTVS+Printer)

No Linux a interface gráfica deve ser baseada em X11 (Xorg). Sistemas Operacionais mais recentes por padrão podem ser baseados em Wayland e, neste caso, o agente TOTVSPrinter não funcionará.

Por exemplo, o Red Hat Enterprise Linux 8 e Ubuntu 17.10 usam Wayland por padrão, mas permitem que seja alterado para X11 de uma maneira bem simples, bastando na tela de login clicar no ícone de engrenagem e selecionar Ubuntu on Xorg no Ubuntu 17.10 ou Standard (X11 display server) on Xorg ou Classic (X11 display server) no RHEL8. Para maiores informações consulte a documentação do Sistema Operacional utilizado.

**Saiba mais:**

[TOTVS Printer](https://tdn.totvs.com/display/tec/TOTVS+Printer)

[Download PDF dos boletos - FINA710](https://tdn.totvs.com/display/public/PROT/Download+PDF+dos+boletos+-+FINA710)

[Como é gerado o nome do Boleto enviado via API - FINA713 - Boleto Online ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20836978162839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Nome-do-Boleto-Gerado-ao-efetuar-o-download-pelo-Novo-Gestor-Financeiro)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28456279988375)
