---
article_id: 360058207014
category: GPE - eSocial - Não Periódicos
content_hash: 74b285c2ecf0ff9b6a4f68da2e408e1684243c9a034c905083eb47430faa3534
fetched_at: '2026-06-28T22:45:05.748916+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2230 - Esse afastamento já foi integrado
  ao TAF e transmitido ao governo
type: support-article
updated_at: '2026-06-16T11:27:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058207014-RH-Linha-Protheus-GPE-eSocial-S-2230-Esse-afastamento-j%C3%A1-foi-integrado-ao-TAF-e-transmitido-ao-governo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23219349744407) Tempo aproximado para leitura: 00:02:00 min**  
  
**Ocorrência**  
Esse afastamento já foi integrado ao TAF e transmitido ao governo. Caso deseje retificá-lo, favor enviar TAG de retificação igual a 2  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098611054)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esta mensagem pode ocorrer em algumas situações:  
  
1. Quando há um afastamento integrado ao TAF e transmitido ao RET com os campos R8\_INTGTAF, R8\_TAFKI e R8\_TAFKF em branco. Após aplicado o pacote mencionado, deverá ser utilizado o rdmake **RHTAFKEY** para correção do incidente.   
  
2. Conforme necessidade de realizar a alteração de um afastamento já transmitido ao governo.  
  
3. Alterar o motivo de afastamento onde evento é enviado como Afastamento Sem relação com o Trabalho (Auxilio Doença) e é alterado para Afastamento por Doença/Acidente de Trabalho relacionado ao trabalho.  
  
**Solução**  
Para correção seguir as orientações de cada item abaixo conforme o número da causa.   
  
1. Executar o rdmake **RHTAFKEY**, para mais detalhes verifique o link abaixo:   
[Como utilizar o rdmake RHTAFKEY?](https://tdn.totvs.com/display/public/PROT/DRHESOCP-19610+DT+RDMAKE+Com+ajuste+dos+campos+R8_TAFKI+e+R8_TAFKF)  
  
2. Alteração do registro para informar o término do afastamento, caso ele tenha sido incluído sem uma data final. Devem ser informados os campos: "**Numero de Dias**" e "**Data Fim Afastamento**", campos: R8\_DURACAO, e R8\_DATAFIM, respectivamente.  
  
3. Alteração para retificar o afastamento enviado inicialmente. Nesse caso é necessário preencher o campo "**Origem da Alteração**" (R8\_ORIGALT) e informar o motivo pelo qual o registro está sendo retificado, escolhendo uma das opções: 1 = Iniciativa do Empregador; 2 = Revisão Administrativa; 3 = Determinação Judicial.  
  
Observação: Para todos os cenários é necessário estar com as atualizações abaixo aplicadas no ambiente  
[Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)   
[Pacote e Dicionário Correções Expedição Continua TAF](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP)

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
