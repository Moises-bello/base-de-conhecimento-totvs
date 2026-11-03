---
article_id: 19437319784983
category: RH - Cadastros
content_hash: 38da43586d42fc7c3ec0aa8e4040b6051ab264c4f3fc15ff3f381979ddea863d
fetched_at: '2026-06-28T22:44:52.733000+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Ao cadastrar um novo relógio de ponto, é gerada
  mensagem de que o arquivo não foi encontrado na System
type: support-article
updated_at: '2026-02-03T17:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19437319784983-RH-Linha-Protheus-PON-Ao-cadastrar-um-novo-rel%C3%B3gio-de-ponto-%C3%A9-gerada-mensagem-de-que-o-arquivo-n%C3%A3o-foi-encontrado-na-System
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19437286535191) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao cadastrar um novo relógio de ponto, é gerada mensagem de que o arquivo não foi encontrado na *System:*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19437302998423)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando são utilizadas as rotinas **Cadastro de Relógios** e **Leitura/Apontamento** que necessitam ler os arquivos de relógios, o sistema automaticamente faz uma cópia temporária destes arquivos para a pasta definida na variável *StartPath* no arquivo .INI do server.  
Algumas customizações gravam esses arquivos diretamente neste diretório *StartPath,* e neste caso, não é necessária a cópia temporária. Para inibir uma nova cópia destes arquivos foi criado o parâmetro **MV\_POARQ**.  
  
Para inibir uma nova cópia dos arquivos de relógio, deve-se criar o parâmetro **MV\_POARQ**. Caso o conteúdo do parâmetro seja configurado como **1,** indica que os arquivos do relógio **já estão** na pasta configurada no *StartPath* no arquivo .INI do server, ou seja, esses arquivos não sofrerão cópia.  
  
Caso o conteúdo do parâmetro seja configurado como **2**, indica que os arquivos do relógio **não estão** na pasta configurada no *StartPath* no arquivo .INI do server, indicando que os arquivos serão copiados de forma temporária para esta pasta, enquanto são utilizados pelo sistema.  
  
Para criação do parâmetro, acesse o **Configurador - Ambientes - Cadastros - Parâmetros,** e crie o parâmetro conforme instruções abaixo:

|  |  |
| --- | --- |
| **Nome:** | MV\_POARQ |
| **Tipo:** | 1 |
| **Conteúdo Padrão:** | 1 |
| **Descrição:** | Define se os arquivos de relógio estão no diretório |
| **Cont. Descr.** | do StartPath (1 ou 2). |

**Importante:**  
Para utilização do Smartclient via WEBAPP que faça a validação dos arquivos tem como premissa a instalação do WebAgent, veja mais na documentação: <https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent>  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[SIGAPON - Cadastro de Relógios](https://tdn.totvs.com/pages/releaseview.action?pageId=630848642)  
[Como utilizar o parâmetro MV\_POARQ](https://tdn.totvs.com/pages/releaseview.action?pageId=510506068)
