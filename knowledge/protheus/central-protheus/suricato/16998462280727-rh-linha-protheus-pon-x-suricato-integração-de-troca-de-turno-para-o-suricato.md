---
article_id: 16998462280727
category: Suricato
content_hash: c5fe27013fee1562e4f580c9226840eb1b398fed295815e0e1384e722e834457
fetched_at: '2026-06-28T22:44:57.411393+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Integração de Troca de Turno para o
  Suricato
type: support-article
updated_at: '2023-12-20T13:04:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16998462280727-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-de-Troca-de-Turno-para-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16998456675735) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona a integração de Troca de Turno do Protheus para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**A integração de **Trocas de Turno** feitas no **Protheus**, ocorrem de forma **automática** no momento em que o usuário **salva o registro**.  
  
Existe um **campo não visual** dentro da rotina de **Troca de Turno** que controla se aquele registro foi integrado ou não, e se sim, em qual dia/mês/ano. O campo citado é o **PF\_RHEXP,** da tabela **SPF.**Para análise dos dados integrados e geração do arquivo **XML**, é necessário que o conteúdo do parâmetro **MV\_TSATLOG** esteja como **5**, desta forma, quando a Troca de Turno for feita no **Protheus**, serão gerados os **XMLs** dentro da pasta ***System*** do ambiente.  
Essa opção é útil para **analisar erros**, porém, existe uma queda de **performance**. Neste caso orientamos que o cliente gere os arquivos desta forma apenas para análises pontuais.  
  
Quando os arquivos **XML** são gerados dentro da pasta ***System***, eles podem ser de envio ou retorno. Entende-se por **XML** de **envio**:  
**- Numero Sequencial\_SND.XML** → XML enviado ao Suricato. Exemplo: 12345678\_SND  
Entende-se por **XML** de **retorno**:  
**- Numero Sequencial\_RCV.XML** → XML recebido do Suricato como retorno do XML SND. Exemplo: 12345678\_RCV.  
  
O comportamento da integração é de **retirar o vínculo** entre o **turno antigo** e o **funcionário** no **Suricato**, e enviar os **novos dados,** portanto, serão gerados **XMLs** contendo os dados do novo turno, a retirada do vínculo com o turno antigo, e o vínculo com o novo turno.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16996065611159)  
  
  
O **Protheus** gera **XMLs** contendo:  
  
- **os dados do novo Turno de Trabalho/Sequência da Tabela de Horário Padrão** (caso exista mais de uma Sequência, será gerado um XML para cada uma dela):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998445060247)  
  
  
**- a remoção do vinculo do funcionário com o Turno antigo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998484809111)  
  
  
**- o vínculo do funcionário com o novo Turno:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998470449047)  
OBS: a tag **initialScaleBaseDate** vai demonstrar como data a **Segunda-Feira da semana da Troca de Turno** do funcionário. Por exemplo: para um funcionário que teve troca de turno no dia 01.08.2023 (Terça-Feira), será demonstrada a data de 31.07.2023. Isso ocorre por validações feitas no **Suricato** relacionadas à liberação de acesso da pessoa na empresa.  
  
O conteúdo do campo **PF\_RHEXP** ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998445388567)  
  
No Suricato, acessando **Registro - Perfil de Acesso**, será possível verificar os horários atualizados e que o funcionário poderá acessar a empresa ou refeitório:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998462117015)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16998477718807)  
  
  
Nos casos em que ocorrerem **falhas** na integração, para **forçar o reenvio dos dados** devem ser feitos os trâmites abaixo:  
- **limpeza** do conteúdo do campo **RA\_RHEXP** do cadastro do funcionário;  
- **para integração de um único registro:** acessar o **cadastro do funcionário** e fazer alguma **alteração** de dados que constem no XML, como exemplo, o **crachá**. Pode ser adicionado um número, ou retirado um número;  
- **salvar** o registro no **Protheus**. Isso fará com que os **XMLs** sejam gerados novamente dentro da pasta ***System***, ou seja, o **Protheus** enviará os dados novamente ao **Suricato**.  
**OBS:** depois você pode retornar no cadastro do funcionário e retornar o número original do crachá e salvar, o dado será atualizado no Suricato imediatamente. Esta ação de alteração se faz necessária apenas em casos de falha da integração.  
**- para integração de vários registros:** recomendamos que o reenvio seja feito através da rotina de **Carga Inicial** (PONM430), selecionando apenas a opção **08 - Funcionários**. Serão gerados **XMLs** para **todos** os funcionários do ambiente, portanto, pode ocorrer queda de performance.  
  
**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
