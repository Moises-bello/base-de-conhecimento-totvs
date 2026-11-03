---
article_id: 360004052211
category: RH - Leitura e Apontamento
content_hash: 2c9aaec9fb3bb00d3ac4a4fdd786e040404f7ee230c23b6fcef0b9367844f685
fetched_at: '2026-06-28T22:44:45.920062+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona a Leitura e Apontamento das marcações
type: support-article
updated_at: '2026-06-17T12:44:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-RH-Linha-Protheus-PON-Como-funciona-a-Leitura-e-Apontamento-das-marca%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35432790498839) Tempo aproximado para leitura: 00:01:30 min**  
  
**Dúvida**  
Como funciona a Leitura e Apontamento das marcações do ponto?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Ao realizar a leitura das marcações a partir da rotina **Leitura/Apontamento (PONM010): Miscelânea > Cálculos > Leitura/Apontamento**, o sistema faz algumas verificações, como:  
**1.** Verifica se o **intervalo de datas** informado nos parâmetros está de acordo com a **data base e** [**período em aberto do sistema;**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)  
**2.** Verifica através do [**cadastro de Relógios**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-RH-Linha-Protheus-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-de-Ponto) **(Atualizações>Cadastro de Ponto>Relógios** o arquivo TXT que contém as marcações de ponto;  
**3.** Verifica se existe registro de [**Troca de Turno**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios) **(Atualizações>Cadastro de**  
**Funcionários>Troca de Turno** para o primeiro dia do período de apontamento vigente.  
  
Quando a leitura é processada, os dados são armazenados nas seguintes tabelas:  
**- SP8 (Marcações do Período em aberto)**: nesta tabela, são armazenadas todos os tipos de **marcações de ponto** de períodos em aberto, ou seja: marcações eletrônicas vindas do TXT, automáticas, integradas por outros sistemas, como: **MEU RH, CLOCKIN e SURICATO**;  
**- SPC (Apontamentos do Período em aberto)**: nesta tabela, são armazenados todos os **apontamentos** de períodos em aberto, ou seja, os eventos que foram gerados: **(faltas, atrasos, horas extras, entre outros);**  
**-** **RFB (Cabeçalho de Pré-Leitura)**: esta tabela é responsável por verificar cada TXT lido e armazenar o último NSR de cada um deles. Quando um dia de marcação foi lido e o dado gravado na tabela,  não é possível processar uma leitura para o mesmo dia, com isso, não existe risco de algum dado ser sobreposto.  
**- RFE (Tabela de Pré-leitura)**: esta tabela armazena apenas as marcações originais vindas de arquivos TXT.  
  
No momento em que a leitura é processada, existe uma ordem de gravação dos dados nas tabelas citadas, que são:  
**1.** **RFB:** primeiro o sistema verifica se o dado, com base no NSR gravado no campo RFB\_IDORG, que o usuário está tentando ler é maior que este código, se for igual ou menor não lê, só irá ler marcações com NSR maiores. Esta validação só é válida para arquivos TXT/AFD;  
**2.** **RFE:** grava as marcações vindas do TXT ou da integração do SURICATO ou CLOCKIN;  
**3. SP8:** As marcações da RFE serão gravadas para a SP8, sendo possível a visualização pela rotina;  
**4. SPC:** Após toda a leitura ser feita, o apontamento do período será processado;  
  
**Saiba Mais:**  
[**Manual do Ponto Eletrônico**](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
