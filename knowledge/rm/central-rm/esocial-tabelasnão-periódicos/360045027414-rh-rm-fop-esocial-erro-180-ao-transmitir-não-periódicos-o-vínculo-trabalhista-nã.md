---
article_id: 360045027414
category: eSocial - Tabelas/Não Periódicos
content_hash: 59f6fe27889b805b61848ccf25d50ff827bd489b7c9d714f7d6529c007c42019
fetched_at: '2026-06-28T22:47:10.317609+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 180 ao transmitir não periódicos: O Vínculo
  Trabalhista não foi localizado'
type: support-article
updated_at: '2024-12-30T13:04:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045027414-RH-RM-FOP-eSocial-Erro-180-ao-transmitir-n%C3%A3o-peri%C3%B3dicos-O-V%C3%ADnculo-Trabalhista-n%C3%A3o-foi-localizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24349735700247)** Tempo aproximado para leitura:**00:01:00 min  
  
Ocorrência**Ao transmitir eventos não periódicos para o governo é retornada a mensagem de erro **Código da Ocorrência: 180 - Descrição: O Vínculo Trabalhista não foi localizado. Ação Sugerida: Utilize o evento de admissão para cadastramento do vinculo trabalhista.**

![ok.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062280694)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões   
  
 **Causa**Conforme mensagem supracitada, a inconsistência é apresentada quando está tentando transmitir eventos não periódicos (**S-2205, S-2206**, etc) e o Governo não localiza o vínculo trabalhista (**S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador**) registrado no Portal do eSocial.

Em alguns casos, o vínculo trabalhista **existe** no Portal do eSocial e mesmo assim a inconsistência é retornada. Possivelmente, o registro de alteração está com alguma informação divergente como, por exemplo, a **Matricula eSocial** ou **CPF** do trabalhador.  
  
 **Solução**  
 Para solucionar essa ocorrência, realize as seguintes validações:

• Registro de cadastramento inicial **não consta** no **Portal do eSocial**  
Para os casos que não foi localizado o registro no eSocial será necessário enviar o evento de registro de admissão (S-2206) para o efetivo vínculo, para, em seguida, prosseguir com o envio da alteração cadastral ou contratual.

• Registro de cadastramento inicial**consta** no **Portal do eSocial**O eSocial valida a data de alteração contratual para realizar a vinculação ao cadastro do trabalhador, mas se essa data for anterior a data que o funcionário inciou o vínculo, o eSocial não localizará as informações cadastrais. Dessa forma, será necessário ajustar a data de alteração para ser enviado ao eSocial. Para isso, no módulo **TOTVS Folha de Pagamento** acesse **Administração de Pessoal | Funcionários | Anexos | Históricos** e ajuste o histórico que gerou essa mudança.

• Dados **divergentes** no XML  
Caso exista no XML um dado divergente do arquivo de admissão, como **CPF** ou **Matricula**,por exemplo, o eSocial não identificará o trabalhador pois essas informações são chaves primárias de identificação dos dados cadastrais. Sendo assim, confira os dados preenchidos no cadastro do funcionário em **Identificação |** **Matricula eSocial** e em **Documentação | CPF**, realizando os ajustes necessários. Em seguida, gere o XML novamente e integre com o TAF para transmissão ao Governo.  
  
**Saiba mais**  
Para mais informações acesse:   
      • [Alteração de Matricula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021481212-RM-eSocial-Altera%C3%A7%C3%A3o-da-matr%C3%ADcula-eSocial?source=search)
