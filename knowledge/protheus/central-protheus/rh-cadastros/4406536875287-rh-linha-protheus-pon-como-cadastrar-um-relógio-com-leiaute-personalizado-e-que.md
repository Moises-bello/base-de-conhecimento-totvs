---
article_id: 4406536875287
category: RH - Cadastros
content_hash: eb8cdb0ebfc9b815561c95aac5ea9d0b4f361e0c15775a87a28e3b1b528ea06d
fetched_at: '2026-06-28T22:44:52.815202+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como cadastrar um relógio com leiaute personalizado
  e que não seja homologado pela portaria 671 ou 1510
type: support-article
updated_at: '2026-02-04T19:30:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406536875287-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-com-leiaute-personalizado-e-que-n%C3%A3o-seja-homologado-pela-portaria-671-ou-1510
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38169701964183)****Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como **cadastrar um relógio com leiaute personalizado** e que não seja homologado pelas **portarias 671 ou 1510?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse **Atualizações > Cadastro do Ponto > Relógios** e clique em **Incluir:**  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406529226391)**  
  
  
2. Preencha a aba **Geral** e deixe o campo **REP em branco.** Observe se o caminho informado no campo **Nome Arquivo** está correto comparando com o **local que está o TXT;**  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406529289495)**  
  
  
3. Como o arquivo não segue o layout único da Portaria 1510, ou seja, não é um arquivo de relógio REP, o layout deve ser configurado através das demais abas do cadastro do relógio, conforme exemplo abaixo.

**IMPORTANTE:**  
O controle de batidas de relógios **NÃO REP** e de **REFEIÇÃO** é realizado pelo **crachá**, que será validado no cadastro do funcionário no campo **RA\_CRACHA**.  
A posição do crachá deve ser validada na aba **“Código”** do cadastro do relógio.  
Valide também as demais posições e configure-as de acordo com o seu leiaute personalizado.  
  
Arquivo TXT, onde:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537298967)  
  
**Posição de 01 à 05** - Crachá (Aba **Código** do cadastro de Relógio)  
**Posição de 06 à 08** - Código do Relógio (Aba **Relógio** do cadastro de Relógio)  
**Posição de 09 à 10** - Dia da Marcação (Aba **Dia** do cadastro de Relógio)  
**Posição de 11 à 12** - Mês da Marcação (Aba **Mês** do cadastro de Relógio)   
**Posição de 13 à 16** - Ano da Marcação (Aba **Ano** do cadastro de Relógio)   
**Posição de 17 à 18** - Hora da Marcação (Aba **Horas** do Cadastro de Relógio)   
**Posição de 19 à 20** - Minuto da Marcação (Aba **Minutos** do Cadastro de Relógio)  
  
Desta forma, as abas devem ser configuradas:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537438743)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537446039)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406529440151)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537465495)  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406529449623)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406529455895)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537494807)  
  
As demais abas não necessitam de preenchimento.  
  
OBS: Este é apenas um exemplo de arquivo TXT. Para saber sobre as **posições do arquivo TXT** gerado pelo relógio, **ao que se refere cada dado do arquivo**, entre em contato com o **Fornecedor do relógio** e solicite o **layout** para que possa **configurar no Protheus de acordo com o layout recebido.**  
  
4. Após preencher todos os campos, clique em **Salvar:**  
**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537530007)**  
  
  
5. Para verificar se o Sistema está **reconhecendo o TXT configurado**, posicione no relógio cadastrado e utilize a tecla **F4** do teclado, assim o Sistema fará uma pré leitura do arquivo e mostrará na tela os dados:   
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406537622935)  
  
  
6. Após estes procedimentos, o **relógio está apto a ser lido** através da rotina **Miscelânea - Cálculos - Leitura e Apontamento - PONM010.**  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como funciona a Leitura e Apontamento das marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-MP-PON-Como-funciona-a-Leitura-Apontamento-das-marca%C3%A7%C3%B5es)
