---
article_id: 360036740393
category: RH - Cadastros
content_hash: 7e848720c6489ba06fcbb08e3e580d916466e5841971a61b4136561d8c4714ed
fetched_at: '2026-06-28T22:44:53.050396+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: 'RH - Linha Protheus - PON - O que avaliar quando apresenta mensagem: Arquivo
  do relógio não encontrado no servidor:\SYSTEM\(NOME DO ARQUIVO TXT).'
type: support-article
updated_at: '2026-01-15T13:55:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036740393-RH-Linha-Protheus-PON-O-que-avaliar-quando-apresenta-mensagem-Arquivo-do-rel%C3%B3gio-n%C3%A3o-encontrado-no-servidor-SYSTEM-NOME-DO-ARQUIVO-TXT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35189221617431) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
O que avaliar quando apresenta mensagem: **"Arquivo do relógio não encontrado no servidor:\SYSTEM\(NOME DO ARQUIVO TXT)"**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando é apresentado no cadastro de relógio a seguinte mensagem:  **"Arquivo do relógio não encontrado no servidor:\SYSTEM\(NOME DO ARQUIVO TXT)"**, será necessário verificar as seguintes informações:

**1.** No **Cadastro de Relógios (Atualizações>Cadastro do Ponto>Relógios),** veja se no campo **Nome Arquivo** o caminho do **arquivo txt** não contém a **extensão** preenchida. (Ex: MOVBAND.TXT - é necessário possuir a extensão .TXT)  
![2019-10-02_16_10_22-TOTVS_Educacional__Microsiga__02.9.0016.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047394114)  
  
**2.** Após **informar o nome da extensão**, o aruqivo será validado corretamente:  
![2019-10-02_16_11_21-TOTVS_Educacional__Microsiga__02.9.0016.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047394374)  
  
Para o cenário descrito acima o **arquivo txt** deve possuir a configuração abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32104159708695)  
  
Existem cenários, onde a **extensão do arquivo** já é identificada pelo *Windows*, dessa forma, não é necessário informar a extensão do arquivo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32104159710615)  
  
Se o arquivo estiver no cenário mencionado acima, ao validarmos no **cadastro de relógios**, a mensagem será apresentada, por conta do nome do arquivo estar incorreto.   
\*\*\*Com a **extensão txt** já presente e sendo informada novamente no final do nome).  
![2019-10-02_16_22_46-TOTVS_Educacional__Microsiga__02.9.0016.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048283233)  
  
Um **arquivo txt** nesse cenário abaixo, será validado somente se informarmos a **extensão** duas vezes no campo **Nome Arquivo**.  
![2019-10-02_16_23_52-TOTVS_Educacional__Microsiga__02.9.0016.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048283253)  
  
**Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)[RH - Linha Protheus - PON - Dica quando tiverem o log: Totalizador divergente com as marcações do arquivo txt](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052358173-RH-Linha-Protheus-PON-Dica-quando-tiverem-o-log-Totalizador-divergente-com-as-marca%C3%A7%C3%B5es-do-arquivo-txt?source=search)  
[RH - Linha Protheus - PON - Como efetuar o cadastro do Relógio de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-RH-Linha-Protheus-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-de-Ponto?source=search)  
[RH - Linha Protheus - PON - Descrição e funcionalidade dos campos do Cadastro de Relógio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000615241-RH-Linha-Protheus-PON-Descri%C3%A7%C3%A3o-e-funcionalidade-dos-campos-do-Cadastro-de-Rel%C3%B3gio?source=search)
