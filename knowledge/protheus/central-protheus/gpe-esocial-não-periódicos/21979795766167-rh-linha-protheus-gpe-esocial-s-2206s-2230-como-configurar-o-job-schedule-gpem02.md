---
article_id: 21979795766167
category: GPE - eSocial - Não Periódicos
content_hash: cf24f9c530dd9bc298fe7bcaf6aa928b13a2b6cef86fac81e812437e41d801e9
fetched_at: '2026-06-28T22:45:04.785674+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como configurar o job
  schedule GPEM026B na tela PO UI
type: support-article
updated_at: '2026-06-25T14:15:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21979795766167-RH-Linha-Protheus-GPE-eSocial-S-2206-S-2230-Como-configurar-o-job-schedule-GPEM026B-na-tela-PO-UI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21979849789975) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar o *job schedule* no Protheus?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões   
  
**Solução**  
Antes de realizar a configuração, é importante realizar as seguintes validações:  
  
- Para que o S-2206 gere com a tag <dtAlteracao> utilizando a data da alteração salarial (R3\_DATA), o parâmetro **MV\_DTALTSA** deve estar falso:  
[RH - Linha Protheus - GPE - eSocial - S-2206 - Como utilizar o parâmetro MV\_DTALTSA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9295167803287-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-utilizar-o-par%C3%A2metro-MV-DTALTSA?source=search)  
  
- Sempre que integrado com o TAF os eventos S-2206/S-2306 (Alteração de contrato ou salário) e S-2230 (Término de afastamento temporário com data futura), o campo de integração com o TAF será preenchida. Caso não haja informação de integração com o TAF no SIGAGPE, quando executado o *job schedule* irá integrar essas informações, mesmo que já tenha as informação no SIGATAF e/ou eSocial.   
Por exemplo: No histórico de salário o campo 'Campo Integ. TAF (R3\_INTGTAF)' está vazio, ao executar o *job shedule* será integrada a informação e o campo 'Campo Integ. TAF (R3\_INTGTAF)' será preenchido.  
  
Para realizar a configuração do *job schedule* realize os procedimentos abaixo:  
  
1.  O sistema irá verificar o conteúdo do parâmetro **MV\_DTCGINI** com a data oficial que indica quando a empresa iniciou a entrega dos eventos não periódicos (2ª fase). Em casos de duvidas sobre as datas oficias consulte: [**Cronograma de implantação**](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao).  
**Atenção:** O data do parâmetro pode ser diferente para cada grupo de empresas, ou seja, os eventos não periódicos serão enviados a partir da data informada no parâmetro.  
  
2. Abra o SIGACFG para configuração da rotina.  
Caminho: Ambiente > *Schedule* > *Schedule*.   
  
Verifique se o status do schedule encontra-se 'em execução' na *Home*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979849796503)  
  
3. Realize a configuração do Agente e verifique o seu *status*, eles são os reesposáveis por executar as funções  
Se não tiver um Agente cadastrado, poderá incluir um novo agente ou ou adicionar o agentes padrão  
![Incluir agente job.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795673751)  
  
Caso o IP\PORTA não estiver ativo\liberado, o *JOB* vai ser iniciado porém não levará o evento para o TAF. Lembrando que para descobrir se o *JOB* está funcionando corretamente, acesse o arquivo *CONSOLE.LOG* da pasta *appserver* e busque pelo seguinte texto: ***Starting Job*** ou ***Alert info***.  
[Como gerar o Console.log para análise do Suporte?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035487834)  
  
O status do Agente deve estar iniciado:  
![iniciar agentes.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795678743)

4. Realize a configuração do agendamento de acordo com a necessidade da empresa:  
  
Caso esta execução não deva integrar alguma informação, é possível desabilitar. Para isso, é preciso informar na parametrização como falso no cadastro do *Job*, seguindo a ordem dos campos:

* **lAltSal**  - Informa se deve ou não executar a rotina de alteração salarial
* **lAfast**  - Informa se deve ou não executar a rotina de afastamentos
* **lAltSindica** - Informa se deve ou não executar a rotina de alteração sindical
* **lConvoca** - Informa se deve ou não executar a rotina de locais de convocação
* **lAltDep**  - Informa se deve ou não executar a rotina de alteração de dependentes
* **lAltTurno**- Informa se deve ou não executar a rotina de troca de turno.
* **lFunCargo**- Informa se deve ou não executar a rotina de alteração contratual por atualização de função.
  + Para quem já utiliza o *job* **GPEM026B()**, esta nova execução vem desabilitada por padrão (False), sendo necessário habilitar a opção. Para isso, no cadastro do Schedule no módulo Configurador, é preciso informar o sétimo parâmetro como True (verdadeiro), dessa forma: **GPEM026B**(.F.,.F.,.F.,.F.,.F.,.F.,**.T.**)
  + [Como gerar S-2206 para alteração de CBO via job](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11277229779351-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-gerar-S-2206-para-altera%C3%A7%C3%A3o-de-CBO-via-job)

Exemplo: **GPEM026B(.T.,.F.,.F.,.F.,.F.,.F.,.F.)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795687575)**  
 ![agendamentos.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795680919)

No exemplo acima parametrizamos o primeiro campo como *True* para integrar somente as **alterações salariais** e as demais informações de alterações como *False* para que não sejam integradas.

Nos "Agendamentos" informe a recorrência que será iniciado esta rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795691159)  
Na "Parametrização" informe a empresa e quais filiais que farão parte este agendamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795694615)  
Ao concluir ele apresentará na listagem dos Agendamentos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795698327)  
  
5. No Monitor é possível visualizar algumas informações da execução da rotina:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21979795710103)  
  
**Consulte Também:** [Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais, fim de afastamento e trocas de turno com o TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)  
  
**Saiba mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Próximos Treinamentos  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
