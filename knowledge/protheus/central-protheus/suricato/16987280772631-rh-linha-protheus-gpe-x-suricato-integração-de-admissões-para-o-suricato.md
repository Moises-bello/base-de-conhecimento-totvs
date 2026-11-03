---
article_id: 16987280772631
category: Suricato
content_hash: a8b3018047a839ee1638046addfd2e7e0c68840e216dc28e3f82688114848e2b
fetched_at: '2026-06-28T22:44:57.357992+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - GPE x Suricato - Integração de Admissões para o Suricato
type: support-article
updated_at: '2023-12-20T12:25:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16987280772631-RH-Linha-Protheus-GPE-x-Suricato-Integra%C3%A7%C3%A3o-de-Admiss%C3%B5es-para-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16987258265879) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona a integração de admissões do Protheus para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir da versão 12.1.23  
  
**Solução**A integração de **admissões** feitas do **Protheus** para o **Suricato**, ocorrem de forma **automática** no momento em que o usuário **salva o registro**.  
  
Existe um **campo não visual** dentro da rotina de **Cadastro de Funcionários** que controla se aquele registro foi integrado ou não, e se sim, em qual dia/mês/ano. O campo citado é o **RA\_RHEXP,** da tabela **SRA.**  
  
Para análise dos dados integrados e geração do arquivo **XML**, é necessário que o conteúdo do parâmetro **MV\_TSATLOG** esteja como **5**, desta forma, quando a admissão for feito no **Protheus**, serão gerados os **XMLs** dentro da pasta ***System*** do ambiente.  
Essa opção é útil para **analisar erros**, porém, existe uma queda de **performance**. Neste caso orientamos que o cliente gere os arquivos desta forma apenas para análises pontuais.  
  
Quando os arquivos **XML** são gerados dentro da pasta ***System***, eles podem ser de envio ou retorno. Entende-se por **XML** de **envio**:  
**- Numero Sequencial\_SND.XML** → XML enviado ao Suricato. Exemplo: 12345678\_SND  
Entende-se por **XML** de **retorno**:  
**- Numero Sequencial\_RCV.XML** → XML recebido do Suricato como retorno do XML SND. Exemplo: 12345678\_RCV.  
  
Com a **admissão** feita, serão gerados os arquivos **XML** dentro da pasta ***System***:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987009699991)  
  
  
O **Protheus** gera **XMLs** contendo:  
  
**- dados de pessoa física:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987037631127)  
  
  
**- dados do funcionário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987051093399)  
  
  
**- dados do Turno de Trabalho/Tabela de Horário Padrão.** Caso o Turno tenha **mais de uma Sequência**, será gerado um **XML** para **cada Sequência:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987089071511)  
  
  
**- dados do Turno vinculado ao funcionário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987126538135)  
OBS: a tag **initialScaleBaseDate** vai demonstrar como data a **Segunda-Feira da semana de admissão** do funcionário. Por exemplo: para um funcionário admitido no dia 01.08.2023 (Terça-Feira), será demonstrada a data de 31.07.2023. Isso ocorre por validações feitas no **Suricato** relacionadas à liberação de acesso da pessoa na empresa.  
  
O conteúdo do campo **RA\_RHEXP** ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987189530263)  
  
E no **Suricato**, o registro ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16987238527255)  
  
  
Nos casos que ocorrerem **falhas** na integração, para **forçar o reenvio dos dados** devem ser feitos os trâmites abaixo:  
- **limpeza** do conteúdo do campo **RA\_RHEXP** do cadastro do funcionário;  
- **para integração de um único registro:** acessar o **cadastro do funcionário** e fazer alguma **alteração** de dados que constem no XML, como exemplo, o **crachá**. Pode ser adicionado um número, ou retirado um número;  
- **salvar** o registro no **Protheus**. Isso fará com que os **XMLs** sejam gerados novamente dentro da pasta ***System***, ou seja, o **Protheus** enviará os dados novamente ao **Suricato**.  
**OBS:** depois você pode retornar no cadastro do funcionário e retornar o número original do crachá e salvar, o dado será atualizado no Suricato imediatamente. Esta ação de alteração se faz necessária apenas em casos de falha da integração.  
**- para integração de vários registros:** recomendamos que o reenvio seja feito através da rotina de **Carga Inicial** (PONM430), selecionando apenas a opção **08 - Funcionários**. Serão gerados **XMLs** para **todos** os funcionários do ambiente, portanto, pode ocorrer queda de performance.  
  
**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
