---
article_id: 19222215435927
category: RH - Cadastros
content_hash: 133a2ae83ce42175fc69389793d99ac71c86413aa85f28f437e46a7d5c3376dd
fetched_at: '2026-06-28T22:44:52.944851+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como cadastrar um relógio para leitura e gravação
  das refeições contidas no arquivo TXT de Ponto
type: support-article
updated_at: '2026-02-06T18:55:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19222215435927-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-leitura-e-grava%C3%A7%C3%A3o-das-refei%C3%A7%C3%B5es-contidas-no-arquivo-TXT-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276529815)****Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como realizar o cadastro de um relógio para leitura e gravação das refeições contidas no arquivo TXT de Ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** Acessar em **Atualizações> Cadastro do Ponto> Relógios** (PONA030), clicar em **Incluir;**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224292962071)**  
  
  
**2.** Na aba**Geral** preencher os campos de acordo com o exemplo abaixo:  
- **Nro. Relógio** deve ser preenchido o código disponível que consta em seu ambiente   
- **Descrição** pode ser definido pelo usuário que estiver realizando o cadastro  
- **Controle** seleciona a opção**'R'**  
**- REP** e **Tipo do** **REP** deixar em **branco**  
**- Nome Arquivo** certificar o caminho informado neste campo se está correto comparando com o local/pasta que está salvo o arquivo TXT e que esteja no diretório local da máquina do usuário, exemplo: 'C:\':  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276532631)  
  
  
**3.** Como o arquivo não segue o **layout único da Portaria 1510 ou 671**, ou seja, não é um arquivo de relógio **REP**, o layout é customizável e configurado através das **demais abas do cadastro de relógio.**  
  
Exemplo como deve ser preenchido as demais abas:   
\***Importante:** O controle de batidas de relógios **NÃO** **REP** e de **REFEIÇÃO** é realizado pelo crachá, será validado no cadastro de funcionário no campo RA\_CRACHA, nesse campo deve ser informado a numeração do crachá do funcionário que deverá consta no arquivo TXT  
  
Exemplo de layout do Arquivo TXT:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19222253390231)  
  
**Posição de 01 à 05** - Crachá (Aba **Código** do cadastro de Relógio)  
**Posição de 06 à 08** - Código do Relógio (Aba **Relógio** do cadastro de Relógio)  
**Posição de 09 à 10** - Dia da Marcação (Aba **Dia** do cadastro de Relógio)  
**Posição de 11 à 12** - Mês da Marcação (Aba **Mês** do cadastro de Relógio)   
**Posição de 13 à 16** - Ano da Marcação (Aba **Ano** do cadastro de Relógio)   
**Posição de 17 à 18** - Hora da Marcação (Aba **Horas** do Cadastro de Relógio)   
**Posição de 19 à 20** - Minuto da Marcação (Aba **Minutos** do Cadastro de Relógio)  
  
Desta forma, as abas devem ser configuradas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276535191)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224292967831)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276538519)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276540311)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276540951)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224276541975)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224292975895)  
  
  
As demais abas não necessitam de preenchimento.  
  
**OBS.:** Este é apenas um exemplo de arquivo TXT.   
Para saber sobre as **posições do arquivo TXT** gerado pelo relógio/catraca de refeitório, **ao que se refere cada dado do arquivo**, entre em contato com o **Fornecedor do relógio/catraca** e solicite o **layout** para que possa configurar no **Protheus** de acordo com o **layout** recebido, pois a definição do **layout** é do **fabricante.**  
  
  
**4.** Após preencher todos os campos, clique em **Salvar;**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38224292979991)**  
  
  
**5.** Para verificar se o Sistema está reconhecendo o TXT configurado, posicione no relógio cadastrado e utilize a tecla **F4** do teclado, assim o sistema fará uma pré-leitura do arquivo e mostrará na tela os dados:   
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19222244026775)  
  
  
**6.** Após estes procedimentos, o **relógio está apto a ser lido** através da rotina **Miscelânea > Cálculos> Leitura e Apontamento** (PONM010).  
  
\*Lembrando que se faz necessário ter toda a **configuração do cadastro de refeição** em seu ambiente para obter os registros de forma correta.   
Para mais detalhes sobre essa configuração [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Como-efetuar-os-cadastros-das-refei%C3%A7%C3%B5es-para-Leitura-no-Ponto-Eletr%C3%B4nico)  
  
  
  
**Saiba Mais**  
[RH - Linha Protheus - PON - Cadastros e Controle de Refeições no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Cadastros-e-Controle-de-Refei%C3%A7%C3%B5es-no-Ponto-Eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - PON - Descrição e funcionalidade dos campos do Cadastro de Relógio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000615241-RH-Linha-Protheus-PON-Descri%C3%A7%C3%A3o-e-funcionalidade-dos-campos-do-Cadastro-de-Rel%C3%B3gio?source=search)  
[RH - Linha Protheus - PON - Relatório de Refeições - PONR070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050364213-RH-Linha-Protheus-PON-Relat%C3%B3rio-de-Refei%C3%A7%C3%B5es-PONR070?source=search)  
[MP - PON - Como funciona a Leitura/Apontamento das marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-MP-PON-Como-funciona-a-Leitura-Apontamento-das-marca%C3%A7%C3%B5es)
