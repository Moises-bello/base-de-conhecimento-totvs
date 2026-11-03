---
content_hash: 839ca2e56ffd84b9d7837af46dba696e663b7efc6c4e9aa1a9e69c87f5782b64
fetched_at: '2026-06-29T00:11:56.759451+00:00'
page_id: '871517255'
product: rm
source: tdn-rm
title: FIN - Contabilizar lançamentos financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=871517255
version: 8
---

Esse processo realiza a contabilização de lançamentos financeiros com:

* Status: Em aberto
* Tipo contábil: A contabilizar
* Tipo baixa pendente: Livre

O usuário deve informar um filtro para os registros a serem processados e indicar se a data de contabilização buscará o default configurado no módulo TOTVS Gestão Financeira ou a data de competência do lançamento (quando informada).

A partir da release 12.1.2506.139, o processo passa a contemplar também os lançamentos com os status "Baixado", "Baixado parcialmente" e "Baixado por acordo", desde que estejam com o tipo contábil "A contabilizar". Isso permite que a contabilização de lançamentos seja realizada mesmo após a baixa, caso não tenha ocorrido previamente.

#### Envio de e-mail

Enviar e-mail para: quando informado, ao final da execução será enviado um e-mail contendo os principais dados da execução.

#### Geração de log

Ao término do processo, será gerado um arquivo de log com as informações da execução, salvo no diretório do servidor configurado no FileServerPath, na subpasta *ContabilizacaoInclusaoLancamento*.

O arquivo terá no final do seu nome o número do job executado.

falseFracionamento de jobs

Para melhorar a performance em cenários com grandes volumes de dados, é possível fracionar a execução em múltiplos jobs. No cadastro do registro de fracionamento, utilize a classe de job *FinContabilidadeLanInclusaoProcess*.

Para mais detalhes a respeito de fracionamento, consulte a documentação .
