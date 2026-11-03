---
article_id: 28957522132247
category: Financeiro - Conciliador Backoffice
content_hash: 3e792141f29ba0664874efc5c70c090b74b62bcd5a85bf38e4f4170e0dcbdf5a
fetched_at: '2026-06-28T22:37:47.226285+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Registros
  conciliados não aparecem no novo conciliador
type: support-article
updated_at: '2026-01-07T17:45:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28957522132247-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Registros-conciliados-n%C3%A3o-aparecem-no-novo-conciliador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491194903) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Registros conciliados não aparecem no novo conciliador  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2210  
  
**Importante**

O que foi conciliado não precisa ser incorporado à nova rotina, já que, conforme a documentação, é necessário estabelecer um prazo máximo para iniciar a conciliação na nova rotina.

O saldo referente a antiga rotina não será exibido no novo conciliador, também não é possível incorporar o saldo anterior por envolver novas tabelas, porém no **extrato bancário (FINSV014)** é possível visualizar o que foi incorporado à antiga rotina.

**Saiba mais**

[Conciliadores Bancários Manual e Automático (FINA380 e FINA473)](https://tdn.totvs.com/pages/releaseview.action?pageId=754946735)

**Solução**

Para exibir os registros antigos no novo conciliador, é necessário executar o wizard WIZARDUUID para criar os IDs dos registros antigos.

Ao executar o Wizard, deve informar o usuário e senha

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491199255)

Selecionar o grupo de empresa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491201047)

Selecionar a opção **"Popular os campos de ID"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957522083223)

Informar o período que deseja popular os IDs para os antigos registros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491203735)

Selecionar todas as tabelas para criação do campo ID

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491205143)

Após concluir o processo será exibido a mensagem que o processo foi atualizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28957491207575)

Após o processo executar o UPDDISTR.

**Importante**

O que foi conciliado na rotina anterior não aparecerá como conciliado após o procedimento acima, será preciso conciliar novamente na nova rotina para alimentar as novas tabelas.

**Saiba mais**

[Conciliador Backoffice - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)
