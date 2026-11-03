---
content_hash: 9411d774f1cbfa8c3754ae34a1016bb09a6267d49263a30123342f2173e9db36
fetched_at: '2026-07-02T19:24:21.497827+00:00'
page_id: '267804722'
product: protheus
source: tdn-tec
title: Erro quando o nome da empresa possui apóstrofo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267804722
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Ao acessar a rotina SIGAFIN -> Atualizações -> Contas a Pagar -> Funções Contas a Pagar ocorre o erro:  **Error:** Unexpected identifier  $('<div></div>').tworkspace({id:4500, owner:3116, backgroundColor:'#ffffff', unfocusable:true, caption:'Funções Contas a Pagar [02.9.0006]', foregroundColor:'#000000', statusBar:{items: ['TOTVS 2011 Série T Varejo MSSQL P11\_sql', 'Administrador', '19/10/2016', 'Teste 'teste / Matriz']}, alignment:'CONTROL\_ALIGN\_ALLCLIENT', windowID:3000, font:{'color':'#000000', 'font-size':'8pt', 'font-family':'Arial'}}); |
| Correção | Corrigido para que seja permitido utilizar apóstrofo no nome da empresa. |
| Informações adicionais | * Referente ao chamado: TWDHQV * Referente à ocorrência: SSIM-1249 * Disponível a partir da build 7.00.131227A - 2.3.6 |
