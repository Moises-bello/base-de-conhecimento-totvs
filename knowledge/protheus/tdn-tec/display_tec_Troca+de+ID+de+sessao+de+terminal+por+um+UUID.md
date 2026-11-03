---
content_hash: 5237210d0177bab2fdc1da00eac3111b14a6c9ca968af36bcf83726ee85b69ef
fetched_at: '2026-07-02T19:24:18.888626+00:00'
page_id: '221552141'
product: protheus
source: tdn-tec
title: Troca de ID de sessao de terminal por um UUID
type: documentation
url: https://tdn.totvs.com/display/tec/Troca+de+ID+de+sessao+de+terminal+por+um+UUID
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Troca de ID de sessao de terminal por um UUID |
| Ocorrência | Em ambientes com balanceamento de carga, caso esteja configurado para cachear requisições, havia a possibilidade de um cliente receber uma mensagem que nao deveria receber. |
| Melhoria | O SmartClient HTML passa a gerar um UUID fortemente seguro para cada nova conexão, mitigando a possibilidade de um cliente receber uma mensagem cacheada para outro cliente que possuía o mesmo ID.  Agora também é realizada a verificação desse UUID nas duas pontas, abortando a execução do programa caso recebe uma mensagem com UUID que nao seja o seu. |
| Informações adicionais | * Referente ao chamado: Não há chamado associado. * Referente à ocorrência: BAS-1002 * Disponível em builds superiores a 7.00.131227A - 2.2.22 |
