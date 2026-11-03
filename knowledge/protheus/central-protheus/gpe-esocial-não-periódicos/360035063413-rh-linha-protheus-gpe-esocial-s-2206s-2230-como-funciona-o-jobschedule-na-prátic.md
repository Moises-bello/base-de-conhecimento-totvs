---
article_id: 360035063413
category: GPE - eSocial - Não Periódicos
content_hash: 2fa1527fc16ed66462188919bf020d1bfeef2a2aadb423368006f4f91e16e93f
fetched_at: '2026-06-28T22:45:04.808153+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule
  na prática referente a integração das Alterações Salariais, fim de afastamento,
  trocas de turno e alteração na função com o TAF
type: support-article
updated_at: '2026-06-16T13:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-funciona-o-Job-Schedule-na-pr%C3%A1tica-referente-a-integra%C3%A7%C3%A3o-das-Altera%C3%A7%C3%B5es-Salariais-fim-de-afastamento-trocas-de-turno-e-altera%C3%A7%C3%A3o-na-fun%C3%A7%C3%A3o-com-o-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25869706465943)** Tempo aproximado para leitura: **00:03:00min  
  
Dúvida**Como enviar alteração de salario para o eSocial?  
  
Como enviar data fim de afastamento para o eSocial?  
  
Como funciona o *Job/Schedule* na prática referente a integração das alterações salariais, fim de afastamento, trocas de turno e alteração de CBO da Função ou Cargo com o TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**O ***Job/Schedule*** integra informações de eventos não periódicos (S-2206 e S-2230)  em processos onde não é possível gerar o registro no momento da inclusão / alteração, para isso o sistema vai verificar a data informada no parâmetro **MV\_DTCGINI** (que deve conter a data do inicio dos eventos não periódicos de acordo com o cronograma oficial estabelecido pelo governo para a obrigação). Em casos de duvidas sobre as datas oficias consulte: [Cronograma de implantação.](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)  
  
As integrações com o TAF ocorrem nas seguintes situações:  
  
**1. Eventos S-2206 originados das alterações salariais realizadas através das rotinas de Reajuste, Dissidio Retroativo e do módulo de Cargos e Salários:**Independente de quando foi configurado o ***Job/Schedule***, após sua execução, o sistema vai verificar a data informada no parâmetro **MV\_DTCGINI**, e tentar integrar com o TAF todas as alterações salariais existentes no histórico de alterações salariais e de cargo do Trabalhador no GPE (tabelas SR3 e SR7) com a Data Aumento igual ou posterior a do parâmetro e com o campo "**Integra TAF**" vazio.  
  
Após a integração com o TAF o Sistema preenche a data de integração no campo "**Integra TAF**" e evita que essa informação seja lida novamente pelo *Job/Schedule* e envida em duplicidade ao TAF.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044820774)  
  
**2. Eventos S-2230 quando o fim do afastamento ocorre após 15 dias de data sua data de início.**O melhor exemplo para tratar sobre esse assunto é a Licença Maternidade, por exemplo, supondo que um Trabalhador iniciou a licença hoje (29/08/2019) e o período padrão de afastamento é de 120 dias, sendo assim ele retornaria em 26/12/2019, mas se eu tentar enviar o evento S-2230 **sem o parâmetro** **MV\_DTFIMA** habilitado, só haverá integração do início deste afastamento.   
  
Neste cenário você será obrigado a enviar o evento S-2230 com a data fim do afastamento, e isso só era aceito pelo governo se a data futura fosse dentro de um período de 15 dias da data do calendário.  
  
Nessa situação o ***Job/Schedule*** vai efetuar o envio da data Fim ao TAF para que você não tenha que deixar isso anotado e fazer manualmente quando a data fim obedecer o prazo previsto pelo leiaute do eSocial.  
  
**Importante**  
Com a chegada da **NT 15/2019** é permitido enviar o inicio e o fim do afastamento em um evento (S-2230) ajustando o parâmetro **MV\_DTFIMA** conforme boletim: <https://tdn.totvs.com/pages/viewpage.action?pageId=515671214>   
  
Exemplo de afastamentos licença maternidade (120 dias):  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045735993)**Toda vez que o *Job/Schedule* é realizado o Sistema registra as informações processadas no *Console.log* do Appserver conforme imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045735813)  
Em caso de duvidas consulte: [Como gerar o Console.log para análise do Suporte?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035487834)  
  
**3. Eventos S-2206 referente a trocas de turno em data futura.**

Para que seja possível efetuar o cadastro de troca de turno em data futura, foram criados os campos **PF\_INTGTAF** (que irá possuir a data que o registro foi integrado) e **PF\_TAFKEY** (que irá possuir uma chave de integração com o TAF para relacionamento na tabela TAFST2), que possuem a estrutura abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5067591957783)

Como não é possível determinar quais registros da tabela SPF já foram integrados, foi necessário a criação do o parâmetro **MV\_DTCGTNO**, do tipo **Data**, que será utilizado no *job***GPEM026B()** para definir a partir de qual data será considerado os registros de trocas de turno para integração do evento S-2206. Ou seja, se o parâmetro estiver preenchido com 01/06/2020, apenas os registros da tabela SPF com o campo PF\_DATA igual ou superior a 01/06/2020 serão considerados.  
  
Através da data configurada no parâmetro **MV\_DTCGTNO**, o sistema irá efetuar filtro nos registros da tabela SPF (Troca de Turno) para considerar os que ainda não tenham sido integrados, isto é, que estejam com o campo PF\_INTGTAF vazio. Além disso, no filtro será considerado apenas os registros com data até a data de execução que o job está sendo executado, Ou seja, caso o parâmetro **MV\_DTCGTNO**tenha sido configurado com a data de 01/06/2020 e o job **GPEM026B()**foi executado na data de 19/05/2020, não seria processado nenhum registro, uma vez que somente consideraria um registro na tabela SPF com o campo PF\_DATA igual o superior a 01/06/2020 mas que fosse menor ou igual a 19/05/2020, o que nunca será verdadeiro.  
Consulte: [Documentação MV\_DTCGTNO](https://tdn.totvs.com/display/PROT/5028023+DRHESOCP-10981+DT+Melhoria+para+troca+de+turno+em+data+futura)  
  
**4. Evento S-2230 referente a cálculo de férias programadas.**Ao efetuar o cálculo de férias programadas, o evento S-2230 não é integrado ao TAF, apresentando a mensagem de envio por *Job*. Porém, conforme manual do eSocial versão 2.5 e S-1.0, não é possível registrar início de afastamento em data futura, exceto se o motivo de afastamento for férias cuja data de início não ultrapasse 60 dias do envio do evento.  
  
Como solução foi criado o parâmetro **MV\_INTFEPR** para indicar se o evento S-2230 deve ser integrado ao TAF no momento do cálculo da programação de férias, ou se deve ser enviada via job (schedule).  
 **Observação:** Mesmo com parâmetro habilitado, caso a data de início ultrapasse 60 dias do envio do evento S-2230, será enviado pelo *Job* na data de início das férias.  
Consulte: [Documentação MV\_INTFEPR](https://tdn.totvs.com/pages/releaseview.action?pageId=513433334)  
  
**5. Eventos S-2206/S-2306 referente a alteração de função.**No leiaute simplificado, não há envio do evento de tabela S-1030, sendo assim, ao alterar o CBO de uma função ou a descrição, deve ser disponibilizada opção de geração do evento S-2206 sem necessidade de alterar o campo função na SRA.  
  
Como solução, ao alterar as informações de CBO ou descrição de uma função, o registro será levado para o controle de *Job* (tabela RJB), que executará o disparo dos eventos S-2206/S-2306 filtrando os trabalhadores vinculados à função atualizada (tabela RJC).  
  
Para quem utiliza o *job* **GPEM026B()**, esta nova execução vem desabilitada por padrão (False), sendo necessário habilitar a opção. Para isso, no cadastro do Schedule no módulo Configurador, é preciso informar o sétimo parâmetro como True (verdadeiro), dessa forma: **GPEM026B**(.F.,.F.,.F.,.F.,.F.,.F.,**.T.**)  
 **Observação:**Para saber como parametrizar o *Job/Schedule* acesse:

* [Como configurar o job schedule GPEM026B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5220215589527)
* [Como configurar o job schedule GPEM026B na tela PO UI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI?source=search)
* [Como gerar S-2206 para alteração de CBO via job](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11277229779351-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-gerar-S-2206-para-altera%C3%A7%C3%A3o-de-CBO-via-job)

**Saiba mais**Para saber mais consulte os *links* abaixo:   
[Artigo relacionados ao evento S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854-RH-Linha-Protheus-GPE-eSocial-S-2206-Quais-s%C3%A3o-os-artigos-e-documenta%C3%A7%C3%B5es-relacionados-ao-evento-S-2206-Altera%C3%A7%C3%A3o-de-Contrato-de-Trabalho)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
