---
content_hash: fc0785456354cf71a598f359c010f6efdb33090fed813c6206d050f589063c80
fetched_at: '2026-06-29T00:10:20.081320+00:00'
page_id: '485860484'
product: rm
source: tdn-rm
title: FIN - Novidades da Versão 12.1.25
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485860484
version: 8
---

**12.1.25 - O sistema foi evoluído para realizar a conciliação DDA com o Valor Líquido.**

Na conciliação DDA foi criado o parâmetro 'Utilizar valor líquido na conciliação DDA'  que possibilita que seja utilizado o Valor Líquido no processo.

**12.1.25 - Melhoria no processo de acordo.**  
Implementado parâmetro no Template de Acordo " Permitir acordo para lançamentos gerados por acordo" . Esse parâmetro define se será permitido ou não gerar acordo para lançamento gerados por acordo.

**12.1.25 - Inserido no Retorno de Débito automático o Status "Pendente Autorização".**

O *Status Pendente de Autorização* foi implementado para corresponder a um novo status retornado por alguns bancos. Este significa que o correntista ainda não autorizou o débito, porém ainda pode autorizar por ainda não ter chegado a data do vencimento do título. As posições 68 a 69 do arquivo se referem aos códigos de ocorrências do banco, sendo o valor **PE** referente a "Débito Pendente de Autorização".
