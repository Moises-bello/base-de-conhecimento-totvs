---
article_id: 360004209412
category: RH - Cadastros
content_hash: 2fa8c62310782ae46a383c3727792c22cb73e44318c5c360078c779f0f92bd44
fetched_at: '2026-06-28T22:44:52.671125+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Como efetuar o cadastro do Relógio de Ponto
type: support-article
updated_at: '2026-05-12T18:38:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-RH-Linha-Protheus-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40419583768343) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como efetuar o cadastro do Relógio de Ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O Protheus permite o cadastro de dois tipos de Relógio de Ponto, sendo:  
**1.** - **AFD** - relógios REP homologados pela portaria **1510/671** do MTE ou 373 do Inmetro. Os arquivos gerados por este tipo de relógio contem o número de **PIS ou CPF dos funcionários**, portanto, o *layout* proposto pelo MTE deve ser obedecido;  
  
**2 -** **Não AFD** - relógios que **não são AFD** tem arquivos com número de **crachá**. Neste caso, não existe um *layout* determinado, pois cada fabricante pode trabalhar com o seu. Cabe ao fabricante informar exatamente o *layout* ao cliente, para que seja possível cadastrar o equipamento.  
  
Qualquer relógio é compatível com o Protheus desde que gere arquivo TXT dentro de uma das opções citadas acima.  
  
Para criar o cadastro de um relógio, basta acessar **Atualizações>Cadastro do Ponto>Relógios.**  
Para os dois tipos de Relógio mencionados acima, o cadastro de alguns campos devem estar conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19287219965079)  
  
Conheça os **principais campos**:  
  
**1. Pasta Geral**  
**-** No campo **Nro. Relógio** (P0\_RELOGIO) - Deve ser informado o **código** do relógio, que obrigatoriamente deve possuir **3 dígitos**, por exemplo: 001;  
 - No campo Descrição (P0\_DESC) - Deve ser informado o nome do relógio;  
**-** No campo **Controle** (P0\_CONTROL) - Deve ser informado o **tipo** de controle para qual este relógio foi destinado, onde: **P** - Relógio para controle de ponto; **R** - Relógio para controle de refeitório; **A** - Relógio/Catraca para Controle de Visitantes;  
**-** No campo **Tipo Arquivo** (P0\_TIPOARQ) - Deve ser informado o tipo do arquivo para este relógio, onde: **D** - Para arquivos padrão xBase; **T** - Para Arquivo Texto ou **R**- Para integração com Carol Clock In ou Suricato;  
**-** No campo **Nome Arquivo** (P0\_ARQUIVO) -Deve ser informado o caminho  para pasta local ou de rede onde o arquivo TXT está salvo, mas nunca a pasta System (exceção apenas para uso de *Schedule*), por exemplo: C:PROTHEUS10/PONTO/CD.TXT. Vale ressaltar que o nome do arquivo de marcações deve ser exclusivo para cada relógio e não pode repetir para relógios diferentes.  
Nos casos de uso das integrações com Carol Clock In ou Suricato, este campo será automaticamente preenchido com a palavra REP e **não deve ser alterado.**  
**-** No campo **Incremental** (P0\_INC) **-** Deve ser informado **1- SIM,** se o relógio é incremental, ou seja, a**cumula** as marcações no arquivo txt ou **2 - NÃO,** se o relógio não é incremental, ou seja, **não acumula** as marcações no arquivo txt;  
**-** No campo **REP** (P0\_REP): Dever ser informado conforme o tipo do REP:  
**>** número de fabricação nos casos de REP homologado pelas antigas portarias 1510/373 ou nos casos de REP C homologado pela portaria 671 em vigência;  
**>** número do processo do último acordo ou convenção coletiva no caso de REP-A, e caso não haja, informar 99999999999999999;  
**>** número de registro no INPI, no caso de REP-P  
Nos casos de relógios que fazem o controle através do **Crachá** do funcionário, este campo deve **ficar vazio.**  
  
Caso o formato do arquivo de marcações seja **AFD – Arquivo Fonte de Dados,** o sistema seguirá os *layouts* definidos pelo MTP de forma automática, não sendo necessário o preenchimento das demais abas do cadastro, salvo exceção dos cadastros para integração com o Suricato, onde deve ser informado na aba Outros - Campo Novo Relógio = SIM.  
  
Nos casos de equipamentos que não são AFD, ou seja, tem o controle através do Crachá do funcionário, se faz obrigatório o cadastro das posições do arquivo, informação que deve ser requisitada ao fabricante para o correto cadastro no Protheus conforme orientações abaixo:  
  
**Aba Código:**  
**- Ini. Código** (P0\_CODINI) e **Fim. Código** (P0\_CODFIM) - Deve ser informada a posição inicial e final do **crachá do funcionário** conforme arquivo txt. A quantidade de dígitos deve ser exatamente igual a quantidade de dígitos informado no campo crachá no cadastro do funcionário.  
  
**Aba Relógio:**  
**- Ini. Relógio** (P0\_RELOINI) e **Fim. Relógio** (P0\_RELOFIM) - Deve ser informada a posição inicial e final do **relógio** conforme arquivo txt. O código do txt deve ser igual ao código do cadastro do relógio. Caso o arquivo txt não possua o código do relógio, deve ser utilizado o campo **Form Relogio** preenchendo com um valor fixo, por exemplo "001".  
  
**Aba Dia:**  
**- Ini. Dia** (P0\_DIAINI) e **Fim. Dia** (P0\_DIAFIM) -Deve ser informada a posição inicial e final do dia conforme arquivo txt.  
  
**Aba Mês:**  
- **Ini. Mes** (P0\_MESINI) e **Fim Mes** (P0\_MESFIM) - Deve ser informada a posição inicial e final do mês conforme arquivo txt.  
  
**Aba Ano:**  
**- Ini. Ano** (P0\_ANOINI) e **Fim Ano** (P0\_ANOFIM) - Deve ser informada a posição inicial e final do ano conforme arquivo txt.  
  
**Aba Horas:**  
**- Ini. Hora** (P0\_HORAINI) e **Fim Hora** (P0\_HORAFIM) - Deve ser informada a posição inicial e final da hora conforme arquivo txt.  
  
**Aba Minutos:**  
**- Ini. Minutos** (P0\_MINUINI) e **Fim Minutos** (P0\_MINUFIM) - Deve ser informada a posição inicial e final dos minutos conforme arquivo txt.  
  
  
**IMPORTANTE**  
- Um relógio associado a um número de REP **não pode ser eliminado** e nem pode ter o **número alterado** caso tenha marcações registradas pela leitura de marcações.  
- A tabela **SP0** que trata sobre o cadastro de relógios pode ser totalmente Compartilhada ou totalmente Exclusiva.  
**Compartilhamento Totalmente Exclusivo** - é importante saber que os funcionários devem obrigatoriamente registrar o ponto apenas nos relógios cadastrados na mesma filial dele, ou seja, se o funcionário pertence a filial 01, poderá registrar o ponto apenas nesta filial, caso contrário, quando for realizada a leitura das marcações, esses dados não serão gravados na tabela SP8 - Marcações.  
  
Nos casos onde as integrações com Suricato ou Carol Clock In forem utilizadas em mais de uma Filial do mesmo Grupo de Empresas, se torna **obrigatório** que a SP0 seja totalmente compartilhada.  
  
Se o campo Centro de Custo for preenchido, só serão lidas as marcações dos funcionários que estão atrelados ao mesmo código de Centro de Custo informado do cadastro do Relógio.  
  
**Saiba mais**  
[RH - Linha Protheus - PON x Suricato - Como cadastrar um relógio que integra com o Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057418593-RH-Linha-Protheus-PON-Como-cadastrar-no-Protheus-um-rel%C3%B3gio-que-integra-com-o-Suricato)  
[RH - Linha Protheus - PON - Como cadastrar um relógio para integração do Clock In com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083354-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-integra%C3%A7%C3%A3o-do-Clock-In-com-o-Ponto-Eletr%C3%B4nico)  
[RH - Linha Protheus - PON - Após o cadastro do relógio, como podemos ter uma prévia se o arquivo será lido pelo Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016519452-RH-Linha-Protheus-PON-Ap%C3%B3s-o-cadastro-do-rel%C3%B3gio-como-podemos-ter-uma-pr%C3%A9via-se-o-arquivo-ser%C3%A1-lido-pelo-Sistema)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
