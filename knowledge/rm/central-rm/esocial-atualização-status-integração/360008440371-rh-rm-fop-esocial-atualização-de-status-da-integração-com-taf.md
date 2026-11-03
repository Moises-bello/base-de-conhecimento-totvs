---
article_id: 360008440371
category: esocial - Atualização Status Integração
content_hash: fcadf379a0f60e0e580d91bd851ad6e0f1466d4b5b0d7ad00f7b28decad9207f
fetched_at: '2026-06-28T22:47:11.178088+00:00'
product: rm
section_id: 1500000860962
source: central-rm
title: RH - RM - FOP - eSocial - Atualização de status da integração com TAF
type: support-article
updated_at: '2026-01-09T12:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008440371-RH-RM-FOP-eSocial-Atualiza%C3%A7%C3%A3o-de-status-da-integra%C3%A7%C3%A3o-com-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23761933521431)**Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
No TOTVS Folha e Pagamento ao executar o processo **Atualização de Status da Integração com o TAF**, o sistema apresenta erros de integração ou não apresenta erro porém não atualiza o status dos eventos na fila.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial- - Todas as versões  
  
**Causa**  
Esta situação pode ocorrer devido a algumas situações como ambiente desatualizado, parametrização incorreta ou perda de referência entre as tabelas **PESOCIALEVENTOS** e **TAFXERP**.  
  
**Solução**  
Para solucionar o erro de integração deverá validar os passos abaixo:  
1. O ambiente deve ser mantido sempre atualizado. Verifique se o seu ambiente está atualizado com os últimos pacotes liberados **RM** e **TAF**pois ocorreram várias correções nos processos e é extremamente importante que o usuário mantenha os ambientes atualizados [TOTVS S/A - Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=1029447).  
2. Acesse **Folha de Pagamento | Configurações | Parametrizador | eSocial | Integração com TAF** e verifique se os campos de **Servidor** e **Porta** estão corretamente preenchidos de acordo com o web service parametrizado no TAF e execute o teste de conexão com o banco conforme indicado abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23761933523351)

2.2. Verifique se a URL está conectando quando digitado o endereço no *browser* (Navegador), conforme exemplo abaixo ao qual retornou que o web service está operando com sucesso, se baseando na imagem no tópico 2.1 a url ficaria como 192.168.0:8090/rest.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062021733)

**Importante**  
A perda de referência entre o XML do RM e TAF pode influenciar em não atualização do status da forma correta. As tabelas utilizadas são **PESOCIALEVENTOS**  no RM e **TAFXERP** no TAF. Para os casos em que ocorre a perda de referência consulte a documentação a seguir: [RM - eSocial - Status do evento no RM divergente do status do evento no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015722272-RM-eSocial-Status-do-evento-no-RM-divergente-do-status-do-evento-no-TAF?source=search)
