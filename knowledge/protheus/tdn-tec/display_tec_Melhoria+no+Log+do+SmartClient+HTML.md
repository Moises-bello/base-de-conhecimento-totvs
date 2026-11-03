---
content_hash: 2717b2d03944114a21520346e6fb14f5542341cb51cb70136fd701baf05bf63e
fetched_at: '2026-07-02T19:24:18.882040+00:00'
page_id: '221552108'
product: protheus
source: tdn-tec
title: Melhoria no Log do SmartClient HTML
type: documentation
url: https://tdn.totvs.com/display/tec/Melhoria+no+Log+do+SmartClient+HTML
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Log nao salva tudo que é exibido na saida do console. |
| Ocorrência | Quando é utilizada a funcao System.out.println para imprimir algo no console, ele nao salva no arquvo de log. |
| Melhoria | Troca de System.out.println por LoggerClass.log para salvar no arquivo de log do tomcat |
| Informações adicionais | * Referente ao chamado: Não há chamado associado. * Referente à ocorrência: BAS-611 * Disponível em builds superiores a 7.00.131227A - 2.2.22 |
