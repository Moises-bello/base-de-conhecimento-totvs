---
article_id: 360034004133
category: eSocial - Gerar XML/ Integração Evento
content_hash: d31c7fd2f7e509f7abafc3d773735d0255be048d2f19068d214b15ba08e2e6ac
fetched_at: '2026-06-28T22:47:12.175769+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 933 na integração com governo: O somatório
  dos Proventos deve ser maior ou igual ao somatório dos Descontos'
type: support-article
updated_at: '2026-06-01T16:06:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034004133-RH-RM-FOP-eSocial-Erro-933-na-integra%C3%A7%C3%A3o-com-governo-O-somat%C3%B3rio-dos-Proventos-deve-ser-maior-ou-igual-ao-somat%C3%B3rio-dos-Descontos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20974668413847) Tempo aproximado para leitura: 00:02:00 min**  
  
**Ocorrência**  
Ao transmitir o evento S-1200 para o governo é retornado a inconsistência **Código de Ocorrência: 933 - Descrição: O somatório dos Proventos deve ser maior ou igual ao somatório dos Descontos no Demonstrativo de Pagamento X. Valor encontrado: -XXX**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043853773)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Conforme mensagem apresentada, a inconsistência é apresentada quando o somatório dos proventos está maior que o somatório de descontos. Isso pode ocorrer por motivos diversos como: falta de distribuição do SEFIP para um determinado evento de provento; líquido do envelope de pagamento negativo; ou tipo de rubrica incorreta no eSocial Web.  
  
**Solução**  
Para correção da ocorrência favor realizar as validações abaixo:  
• Falta de **distribuição do SEFIP**  
Para empresas que utilizam tomadores de serviço, o sistema irá buscar as verbas para montagem do XML na distribuição do SEFIP realizada. Caso exista eventos de provento faltantes na distribuição, o somatório total de descontos poderá ser superior ao somatório dos proventos, apresentando o erro supracitado. Desta forma, verifique em **Encargos | SEFIP | Distribuir SEFIP** a distribuição realizada para o mês/ano correspondente ao período de apuração.  
  
• **Líquido** do envelope **negativo**  
Conforme Layout do eSocial, não é permitido informar um líquido negativo. Desta forma, caso o envelope do funcionário apresente valor líquido negativo, deve-se zerar o líquido com um evento de insuficiência de saldo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043855293)  
Tag vrLiq do evento S-1210

• Tipo de **rubrica incorreta** no eSocial Web  
1. Para corrigir o tipo de rubrica, no módulo Folha de Pagamento acesse **Administração de Pessoal | Eventos** e altere a parametrização conforme a sua necessidade.   
2. Em seguida, acesse **eSocial | Fila de Eventos** e inclua um novo registro manualmente com o **Tipo de Operação** como **Alteração** e informe a **Competência** conforme o S-1010 que foi enviado na carga inicial.

**Importante**  
Para facilitar a validação do XML, execute o processo **Validar S-1200 com Envelope** presente em **eSocial | Eventos Periódicos**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043018974)

**Saiba mais**  
Para mais informações acesse: 

* [S-1010 - Tabela de Rubricas](http://tdninterno.totvs.com/display/public/LRM/S-1010+-+Tabela+de+Rubricas)
