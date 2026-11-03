---
article_id: 39227892417559
category: Meu RH - Gestão de Comunicados e Push Notification
content_hash: 8315b427fd2e2173e5e337fe21d2fd9214dd9e1bf9b7bb722bd7f60aac42e151
fetched_at: '2026-06-28T22:47:26.562658+00:00'
product: rm
section_id: 37779496229783
source: central-rm
title: RH - RM - Meu RH - Gestão de comunicados não envia, fica somente no status
  "Aguardando"
type: support-article
updated_at: '2026-03-24T17:10:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39227892417559-RH-RM-Meu-RH-Gest%C3%A3o-de-comunicados-n%C3%A3o-envia-fica-somente-no-status-Aguardando
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39227892410263) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Após realizar o envio de um comunicado para o Meu RH, o status fica somente "Aguardando" e não atualiza para "Enviado".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227864543895)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2310.123  
  
**Causa**  
Este erro ocorre quando há alguma falha durante a execução do Job de envio do comunicado.  
  
**Solução**  
Para realizar o reenvio deste comunicado, siga os passos abaixo:

1. Acesse no RM a aba **Ambiente**>**Gerenciamento de Jobs**. Crie um filtro com a classe do processo = 'FopPushCommunicateRhProcess'

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227892412695)

2. Localize na coluna '**Iniciado Em**' a execução que ainda não foi finalizada e verifique qual é o nome do servidor que está responsável pela execução.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227892412951)

3. Acesse o **Cockpit** através do menu **ambiente**, localize o servidor que assumiu a execução do envio do comunicado e expanda a janela **Informações de Processamento e memória.** Na opção "Executar processos", clique na opção Stop, e depois clique na opção start para inicia-lo novamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227864544791)

4. Em **Gerenciamento de Jobs**, selecione o Job do comunicado que não foi enviado, e clique na opção Reiniciar Job:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227864545943)

Realizando este processo, será recriado uma nova execução do job deste comunicado com o mesmo ID Job. Aguarde o processo finalizar e assim que concluir, atualize a tela gestão de comunicados para validar a atualização do status para "Enviado".  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39227864546199)

**Importante:** Após a execução do job, caso o status apresente mensagem de erro, acesse o detalhamento da execução para verificar a descrição do erro retornado. Alguns exemplos de erros comuns:

* “Um ou mais erros”
* “O processo não pode acessar o arquivo”
* “Cadeia de caracteres não foi reconhecida como um booleano válido”

Para tratativa dessas ocorrências, consulte o TDN, onde estão disponíveis os principais erros mapeados e suas respectivas orientações de correção: [TDN - Comunicados para o RH](https://tdn.totvs.com/display/NPR/33.0+Comunicados+para+o+RH#id-33.0ComunicadosparaoRH-13.PRINCIPAISD%C3%9AVIDASEERROSCONHECIDOS)

**Saiba mais**

[RH - RM - Meu RH - Como disponibilizar comunicados no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18788237258135-RH-RM-Meu-RH-Como-disponibilizar-comunicados-no-Meu-RH)
